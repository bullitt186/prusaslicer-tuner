# /// script
# requires-python = ">=3.10"
# dependencies = ["mcp>=1.2,<2"]  # ponytail: v1 FastMCP API; port to mcp 2.x MCPServer when v1 stops getting fixes
# ///
"""MCP server exposing profiles.py + the knowledge library. Run: uv run server.py"""
import contextlib, io, json, re, unicodedata
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
import profiles

HERE = Path(__file__).resolve().parent
KNOWLEDGE = HERE / "knowledge"
# SKILL.md body (minus frontmatter) doubles as the server's instructions: one source of truth
INSTRUCTIONS = (
    "Via MCP: `profiles.py list/show/diff/set` = tools list_profiles/show_profile/diff_profiles/set_profile; "
    "`knowledge/<path>` = read_knowledge(path). Firmware config (Klipper printer.cfg, Marlin/Prusa settings) isn't "
    "accessible via this server; obtain it with the user's own tools or ask the user what to check.\n" + (HERE / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[2])

mcp = FastMCP("prusaslicer-tuner", instructions=INSTRUCTIONS)


def _cli(*argv):
    """Run a profiles.py command, return its output; errors come back as text, not exceptions."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        try:
            profiles.main(list(argv))
        except SystemExit as e:
            if e.code not in (None, 0):
                print(e.code if isinstance(e.code, str) else f"error (exit {e.code})")
    return out.getvalue().strip() or "(no output)"


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def list_profiles() -> str:
    """List user profiles by type plus the currently active presets."""
    return _cli("list")


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def show_profile(type: str, name: str, grep: str = "", overrides_only: bool = False) -> str:
    """Effective values of a profile (user or vendor preset) after resolving inheritance.
    Each line: key = value [source], source = user | Vendor:Section | default.
    type: print | filament | printer | physical_printer | sla_print | sla_material. grep: regex on key names, e.g. "retract|^temperature". Always grep; full profiles are ~300 keys."""
    argv = ["show", type, name] + (["--grep", grep] if grep else []) + (["--overrides"] if overrides_only else [])
    return _cli(*argv)


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def diff_profiles(type: str, a: str, b: str, grep: str = "") -> str:
    """Keys whose effective values differ between two profiles of the same type."""
    return _cli("diff", type, a, b, *(["--grep", grep] if grep else []))


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=True))
def set_profile(type: str, name: str, changes: dict[str, str], copy_as: str = "") -> str:
    """Change profile keys. ONLY call after the user explicitly approved the exact changes
    and chose in-place vs copy. In place: original is backed up first. copy_as: write a new
    user profile instead (required for vendor presets). Unknown keys are refused."""
    argv = ["set", type, name, *(f"{k}={v}" for k, v in changes.items())]
    return _cli(*argv, *(["--copy", copy_as] if copy_as else []))


_graph: dict = {"mtime": None, "g": None}


def _g():
    """graph.json is written by `kg.py fix` only when the bundle validates; reload when it changes."""
    f = KNOWLEDGE / "graph.json"
    m = f.stat().st_mtime
    if _graph["mtime"] != m:
        _graph.update(mtime=m, g=json.loads(f.read_text(encoding="utf-8")))
    return _graph["g"]


def _norm(s):
    s = s.lower().replace("ß", "ss").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().replace("'", "").replace("’", "")
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def lookup(term: str) -> str:
    """Find knowledge-graph concepts by name or synonym (English or German, e.g. "Fädenziehen",
    "ghosting", "elephant foot", "retract_length"). Returns `id [type] label`. Next: card(id)."""
    g, q = _g(), _norm(term)
    if not q:
        return "empty term"
    hits = {}
    for lab, ids in g["aliases"].items():
        score = 3 if lab == q else 2 if lab.startswith(q) or q.startswith(lab) else 1 if q in lab or lab in q else 0
        if not score and set(q.split()) & set(lab.split()) - {"of", "the", "and", "to", "on", "in"}:
            score = 0.5
        for i in ids if score else []:
            if score > hits.get(i, (0,))[0]:
                hits[i] = (score, lab)
    if not hits:
        return f"no concept matches '{term}'. Try a shorter term or read_knowledge('index.md')."
    ranked = sorted(hits.items(), key=lambda kv: (-kv[1][0], g["nodes"][kv[0]]["type"] in ("key", "firmware_param"), len(kv[1][1])))[:12]
    n = g["nodes"]
    return "\n".join(f"{i} [{n[i]['type']}] {n[i]['label']}" + (f"  (matched: {lab})" if lab != _norm(n[i]["label"]) else "")
                     for i, (_, lab) in ranked)


_ARROW = {"up": "↑", "down": "↓", "set": "=", "enable": "on", "disable": "off", "check": "?"}


def _q(e):
    b = [f"#{e['rank']}"] if "rank" in e else []
    b += [e["evidence"]] if "evidence" in e else []
    b += [f"when {k}=" + ",".join(x.split("/")[-1] for x in (v if isinstance(v, list) else [v])) for k, v in (e.get("when") or {}).items()]
    b += [f"via {e['via']}"] if "via" in e else []
    b += [e["action"]] if e.get("action") else []
    b += ["src " + ",".join(e["source"] if isinstance(e["source"], list) else [e["source"]])] if e.get("source") else []
    s = f" ({'; '.join(b)})" if b else ""
    return s + "".join(f" {x['key']}{_ARROW.get(x.get('direction'), '')}" for x in e.get("sets", []))


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def card(id: str) -> str:
    """Compact concept card from the knowledge graph: labels, definition, check, and typed relations
    with qualifiers (rank, evidence A-D, when, sets key↑/↓) in both directions — without the article body.
    Walk problem → caused_by (ranked) → cause → fixed_by → procedure/sets keys. Use read_knowledge(path) only for detail.
    id examples: defects/stringing, causes/wet-filament, key/filament_retract_length, klipper/pressure_advance."""
    g = _g()
    id = id.strip().removesuffix(".md")
    n = g["nodes"].get(id)
    if not n:
        return f"unknown id '{id}'. Use lookup(term)."
    lab = lambda i: f"{i} \"{g['nodes'][i]['label']}\"" if i in g["nodes"] else str(i)
    out = [f"{id} [{n['type']}] {n['label']}"]
    if n.get("altLabel"):
        out.append("also: " + ", ".join(n["altLabel"]))
    for k in ("description", "check", "scope", "set_in"):
        if n.get(k):
            out.append(f"{k}: {n[k]}")
    inv = {"caused_by": "causes", "fixed_by": "fixes", "prone_to": "affects", "calibrates": "calibrated_by",
           "broader": "narrower", "related": "related", "overrides": "overridden_by"}
    rel = {}
    for e in g["edges"]:
        if e["s"] == id:
            rel.setdefault(e["p"], []).append((e.get("rank", 99), (lab(e["o"]) if e["o"] else "(settings)") + _q(e)))
        elif e["o"] == id:
            rel.setdefault(inv.get(e["p"], e["p"] + "^-1"), []).append((e.get("rank", 99), lab(e["s"]) + _q(e)))
        elif n["type"] in ("key", "firmware_param") and any(x["key"] == id for x in e.get("sets", [])):
            d = next(x["direction"] for x in e["sets"] if x["key"] == id)
            rel.setdefault("changed_by_fix_of", []).append((99, f"{lab(e['s'])} {_ARROW.get(d, d)}"))
    for p, items in rel.items():
        out.append(f"{p}:")
        out += [f"  - {t}" for _, t in sorted(items)]
    if n.get("path"):
        out.append(f"article: read_knowledge(\"{n['path']}\")")
    return "\n".join(out)


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def read_knowledge(path: str = "index.md") -> str:
    """Read a doc from the 3D-printing knowledge library (OKF). Start with index.md,
    then e.g. defects/stringing.md, tuning/retraction.md, materials/petg.md."""
    f = (KNOWLEDGE / path).resolve()
    if not f.is_relative_to(KNOWLEDGE) or f.suffix != ".md" or not f.is_file():
        return f"not found: {path}. Docs: " + json.dumps(sorted(str(p.relative_to(KNOWLEDGE)) for p in KNOWLEDGE.rglob("*.md")))
    return f.read_text(encoding="utf-8")


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def test_prints(match: str = "") -> str:
    """List calibration test-print files (STL) with absolute paths, filtered by a substring of the path,
    e.g. "First_Layer_Patch-0.25", "EM_Cube-0.95", "square_tower". When and how to use them: the
    "Test prints" section of tuning/first-layer-squish.md, tuning/extrusion-multiplier.md, tuning/pressure-advance.md."""
    files = sorted(p for p in (HERE / "test_prints").rglob("*.stl") if match.lower() in str(p.relative_to(HERE)).lower())
    if not files:
        return f"no test prints matching {match!r}. If the folder is empty, run {HERE / 'test_prints/fetch.sh'}"
    return "\n".join(map(str, files))


if __name__ == "__main__":
    mcp.run()  # ponytail: stdio only; remote (phone) needs streamable-http + auth in front
