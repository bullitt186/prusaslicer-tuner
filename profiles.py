#!/usr/bin/env python3
"""Read, resolve, diff and edit PrusaSlicer profiles (stdlib only).

  profiles.py list
  profiles.py show <type> <name> [--grep REGEX] [--overrides]
  profiles.py diff <type> <a> <b> [--grep REGEX]
  profiles.py set  <type> <name> key=value ... [--copy NEW_NAME]

<type>: print | filament | printer | physical_printer | sla_print | sla_material
<name>: user profile (file stem) or vendor preset name.
Config dir: $PRUSASLICER_DIR, else PrusaSlicer's default data dir for this OS
(macOS ~/Library/Application Support/PrusaSlicer, Linux ~/.config/PrusaSlicer, Windows %APPDATA%/PrusaSlicer).
"""
import argparse, os, re, shutil, subprocess, sys, time
from pathlib import Path

def _default_root():
    if sys.platform == "darwin":
        return Path.home() / "Library/Application Support/PrusaSlicer"
    if sys.platform == "win32":
        return Path(os.environ.get("APPDATA", Path.home())) / "PrusaSlicer"
    return Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "PrusaSlicer"


ROOT = Path(os.environ.get("PRUSASLICER_DIR") or _default_root())
BACKUPS = Path(os.environ.get("PROFILES_BACKUP_DIR", Path(__file__).resolve().parent / "backups"))
META_KEYS = {"renamed_from", "alias", "inherits"}  # vendor bookkeeping, not settings
# Built-in defaults (vendor presets only list what differs from them). Regenerate after a
# PrusaSlicer upgrade: /Applications/PrusaSlicer.app/Contents/MacOS/PrusaSlicer --save prusaslicer_defaults.ini
DEFAULTS = Path(__file__).resolve().parent / "prusaslicer_defaults.ini"


def parse_kv(text):
    out = {}
    for line in text.splitlines():
        if line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        out[k.strip()] = v.strip()
    return out


def load_vendors(root=None):
    """{vendor: {(type, name): dict}}. Abstract parents (*common* ...) are only unique per vendor."""
    vendors = {}
    for f in sorted(((root or ROOT) / "vendor").glob("*.ini")):
        secs, cur = vendors.setdefault(f.stem, {}), None
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^\[(\w+):(.+)\]\s*$", line)
            if m:
                cur = secs.setdefault((m[1], m[2]), {})
            elif line.startswith("["):
                cur = None
            elif cur is not None and "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                cur[k.strip()] = v.strip()
    return vendors


def user_file(typ, name, root=None):
    return (root or ROOT) / typ / f"{name}.ini"


def _defaults(typ, root=None):
    """Bottom layer: built-in defaults for keys that belong to `typ` (= appear in a user file of that type)."""
    if not DEFAULTS.exists():
        return {}
    # ponytail: type membership learned from user files; a type with no user files gets no defaults
    keys = set()
    for f in ((root or ROOT) / typ).glob("*.ini"):
        keys |= parse_kv(f.read_text(encoding="utf-8")).keys()
    return {k: (v, "default") for k, v in parse_kv(DEFAULTS.read_text(encoding="utf-8")).items() if k in keys}


def _vendor_eff(vendors, vendor, typ, name, depth=0):
    if depth > 20:
        raise SystemExit(f"inherits loop at {vendor}:{name}")
    own, eff = vendors[vendor][(typ, name)], {}
    for parent in filter(None, (p.strip() for p in own.get("inherits", "").split(";"))):
        if (typ, parent) not in vendors[vendor]:
            raise SystemExit(f"{vendor}:{name} inherits missing '{parent}'")
        eff.update(_vendor_eff(vendors, vendor, typ, parent, depth + 1))
    eff.update({k: (v, f"{vendor}:{name}") for k, v in own.items()})
    return eff


def resolve_vendor(typ, name, vendors, hint=None, root=None):
    """Resolve a vendor preset by name. Same name in several vendors (e.g. Generic PETG in
    PrusaResearch/Creality/Templates): pick the one whose compatible_printers_condition matches
    `hint` (the user file's), else PrusaResearch > others > Templates."""
    if name.endswith(" @Template"):
        name, cands = name[: -len(" @Template")], ["Templates"]
    else:
        cands = sorted((v for v in vendors if (typ, name) in vendors[v]),
                       key=lambda v: (v == "Templates", v != "PrusaResearch", v))
    cands = [v for v in cands if (typ, name) in vendors.get(v, {})]
    if not cands:
        raise SystemExit(f"not found: {typ} '{name}' (no user file, no vendor section)")
    base = _defaults(typ, root)
    effs = [{**base, **_vendor_eff(vendors, v, typ, name)} for v in cands]
    for eff in effs:  # ponytail: condition-string match only; evaluate conditions if this guesses wrong
        if hint is not None and eff.get("compatible_printers_condition", ("",))[0] == hint:
            return eff
    return effs[0]


def resolve(typ, name, vendors, root=None):
    """-> {key: (value, source)}; source 'user' only where the user file differs from its parent."""
    f = user_file(typ, name, root)
    if not f.exists():
        return resolve_vendor(typ, name, vendors, root=root)
    own, eff = parse_kv(f.read_text(encoding="utf-8")), _defaults(typ, root)
    for parent in filter(None, (p.strip() for p in own.get("inherits", "").split(";"))):
        eff.update(resolve(typ, parent, vendors, root) if user_file(typ, parent, root).exists()
                   else resolve_vendor(typ, parent, vendors, own.get("compatible_printers_condition"), root))
    for k, v in own.items():
        if k not in eff or eff[k][0] != v:
            eff[k] = (v, "user")
    return eff


def cmd_list(_):
    for typ in ("printer", "physical_printer", "print", "filament", "sla_print", "sla_material"):
        names = sorted(p.stem for p in (ROOT / typ).glob("*.ini"))
        if names:
            print(f"## {typ}\n" + "\n".join(f"  {n}" for n in names))
    ini = ROOT / "PrusaSlicer.ini"
    if ini.exists():
        m = re.search(r"^\[presets\]\n(.*?)(?:\n\[|\Z)", ini.read_text(encoding="utf-8"), re.S | re.M)
        print("## active presets\n" + (m[1].strip() if m else "  (none)"))


def _filter(eff, pattern):
    rx = re.compile(pattern, re.I) if pattern else None
    return {k: v for k, v in sorted(eff.items()) if not rx or rx.search(k)}


def cmd_show(a):
    eff = resolve(a.type, a.name, load_vendors())
    for k, (v, src) in _filter(eff, a.grep).items():
        if a.overrides and src != "user":
            continue
        print(f"{k} = {v}    [{src}]")


def cmd_diff(a):
    vendors = load_vendors()
    x, y = resolve(a.type, a.a, vendors), resolve(a.type, a.b, vendors)
    for k in _filter(dict.fromkeys(x.keys() | y.keys(), 0), a.grep):
        vx, vy = x.get(k, ("<unset>",))[0], y.get(k, ("<unset>",))[0]
        if vx != vy:
            print(f"{k}:\n  A {vx}\n  B {vy}")


def write_profile(path, values):
    header = f"# edited by profiles.py on {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    path.write_text(header + "".join(f"{k} = {v}\n" for k, v in sorted(values.items())), encoding="utf-8")


def apply_set(typ, name, changes, copy=None, root=None):
    """Edit a user profile in place (after backup) or write a tuned copy. Returns written path."""
    root = root or ROOT
    src = user_file(typ, name, root)
    if src.exists():
        values = parse_kv(src.read_text(encoding="utf-8"))
    elif copy:  # vendor preset -> new user preset: full config like PrusaSlicer writes it
        values = {k: v for k, (v, _) in resolve(typ, name, load_vendors(root), root).items() if k not in META_KEYS}
        values["inherits"] = name
    else:
        raise SystemExit(f"'{name}' is a vendor preset; use --copy NEW_NAME (vendor files are never edited)")
    unknown = [k for k in changes if k not in values]
    if unknown:
        raise SystemExit(f"unknown keys for {typ} '{name}': {', '.join(unknown)}")
    values.update(changes)
    dst = user_file(typ, copy, root) if copy else src
    if dst.exists():
        bdir = BACKUPS / time.strftime("%Y%m%d-%H%M%S") / typ
        bdir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(dst, bdir / dst.name)
        print(f"backup: {bdir / dst.name}")
    write_profile(dst, values)
    return dst


def cmd_set(a):
    changes = {}
    for kv in a.changes:
        k, sep, v = kv.partition("=")
        if not sep:
            raise SystemExit(f"expected key=value, got '{kv}'")
        changes[k.strip()] = v.strip()
    dst = apply_set(a.type, a.name, changes, a.copy)
    print(f"wrote: {dst}")
    if subprocess.run(["pgrep", "-if", "PrusaSlicer"], capture_output=True).returncode == 0:
        print("NOTE: PrusaSlicer is running - restart it to load the change; saving that preset in the GUI would overwrite it.")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(f=cmd_list)
    s = sub.add_parser("show"); s.add_argument("type"); s.add_argument("name")
    s.add_argument("--grep"); s.add_argument("--overrides", action="store_true", help="only keys differing from parent")
    s.set_defaults(f=cmd_show)
    d = sub.add_parser("diff"); d.add_argument("type"); d.add_argument("a"); d.add_argument("b"); d.add_argument("--grep")
    d.set_defaults(f=cmd_diff)
    e = sub.add_parser("set"); e.add_argument("type"); e.add_argument("name"); e.add_argument("changes", nargs="+")
    e.add_argument("--copy", metavar="NEW_NAME"); e.set_defaults(f=cmd_set)
    a = p.parse_args(argv)
    a.f(a)


if __name__ == "__main__":
    main()
