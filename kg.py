# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""Knowledge graph compiler for the OKF bundle in knowledge/.

  uv run kg.py check      validate; exit 1 on errors or stale generated output
  uv run kg.py fix        regenerate index catalog, Relations blocks, views, graph.json and build/graph.html (only if valid)
  uv run kg.py build      same as fix (kept for hooks and habits)
  uv run kg.py keys       regenerate prusaslicer_keys.json (after regenerating prusaslicer_defaults.ini)
  -q                      hide warnings

Frontmatter is authored; everything between <!-- generated:NAME --> markers, graph.json and
build/ is generated. Rules and vocabularies live in knowledge/schema.yaml.
"""
from __future__ import annotations

import datetime
import json
import posixpath
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE / "knowledge"
KEYS_FILE = HERE / "prusaslicer_keys.json"
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
NUMERIC_RE = re.compile(r"\b\d+(?:[.,]\d+)?\s*(?:°C|mm/s|mm³/s|mm|%)\b")
GEN_RE = re.compile(r"\n*<!-- generated:(\w+) -->.*?<!-- /generated:\1 -->\n?", re.DOTALL)
META = {"index.md", "log.md", "maintenance.md"}  # bundle infrastructure, exempt from graph rules
VIEWS = ("matrix", "keymap")  # opt-in generated views: a doc containing the marker gets it filled


# ---------- loading ----------

def _plain(v):
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.isoformat()
    if isinstance(v, dict):
        return {str(k): _plain(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_plain(x) for x in v]
    return v


def frontmatter(text: str):
    """(meta dict, body, error)."""
    if not text.startswith("---\n"):
        return {}, text, None
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text, "unterminated frontmatter"
    try:
        meta = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as e:
        return {}, text[end + 5:], f"invalid YAML frontmatter: {str(e).splitlines()[0]}"
    if not isinstance(meta, dict):
        return {}, text[end + 5:], "frontmatter is not a mapping"
    return _plain(meta), text[end + 5:], None


def norm(label: str) -> str:
    """Alias normalization: case, umlauts/accents, punctuation."""
    s = label.lower().replace("ß", "ss").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"['’]", "", s)
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def rel_link(src: str, dst: str) -> str:
    return posixpath.relpath(dst, posixpath.dirname(src) or ".")


def topic_links(path: Path, body: str) -> set[str]:
    """Authored internal links (generated sections excluded), as paths relative to ROOT."""
    out = set()
    for target in LINK_RE.findall(GEN_RE.sub("", body)):
        target = target.split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        try:
            out.add((path.parent / target).resolve().relative_to(ROOT.resolve()).as_posix())
        except ValueError:
            out.add("../" + target)
    return out


def load(root: Path | None = None):
    root = root or ROOT
    schema: dict = yaml.safe_load((root / "schema.yaml").read_text(encoding="utf-8"))
    docs, errors = {}, []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if rel.startswith("_") or "/_" in rel:
            continue
        text = path.read_text(encoding="utf-8")
        meta, body, err = frontmatter(text)
        if err:
            errors.append(f"{rel}: {err}")
        folder = rel.split("/")[0] if "/" in rel else ""
        docs[rel] = {"path": path, "text": text, "meta": meta, "body": body, "folder": folder,
                     "id": rel[:-3], "type": schema["folders"].get(folder) if folder else "meta",
                     "links": topic_links(path, body)}
        if folder and folder not in schema["folders"]:
            errors.append(f"{rel}: folder '{folder}' is not declared in schema.yaml folders")
    return schema, docs, errors


def load_keys() -> dict[str, str]:
    return json.loads(KEYS_FILE.read_text(encoding="utf-8")) if KEYS_FILE.exists() else {}


# ---------- graph ----------

def build_graph(schema, docs, keys):
    """Return (graph dict, errors, warnings). Pure: no file writes."""
    errors, warnings = [], []
    nodes, edges = {}, []
    by_id = {d["id"]: d for d in docs.values() if d["type"] not in (None, "meta")}
    preds = schema["predicates"]
    fw = {f"{ns}/{p}" for ns, ps in schema["firmware_params"].items() for p in ps}
    facets = schema["facets"]

    for d in by_id.values():
        m = d["meta"]
        nodes[d["id"]] = {"type": d["type"], "label": m.get("title", d["id"]),
                          "altLabel": list(m.get("altLabel") or []),
                          "description": m.get("description", ""), "path": d["id"] + ".md"}
        for k in ("facets", "check"):
            if m.get(k):
                nodes[d["id"]][k] = m[k]

    def node_type(i):
        if i in by_id:
            return by_id[i]["type"]
        if i.startswith("key/"):
            return "key" if i[4:] in keys else None
        return "firmware_param" if i in fw else None

    def resolve_ref(raw, default_prefix=None):
        if not isinstance(raw, str):
            return None
        raw = raw.strip()
        if raw.endswith(".md"):
            raw = raw[:-3]
        if "/" not in raw and default_prefix:
            raw = f"{default_prefix}/{raw}"
        return raw

    used_keys = set()
    for d in by_id.values():
        src, m, rel = d["id"], d["meta"], d["id"] + ".md"
        for field in m:
            if field in ("causes", "fixes", "affects", "calibrated_by", "narrower", "overrides", "set_in"):
                errors.append(f"{rel}: '{field}' is generated (inverse); remove it from frontmatter")
        if m.get("altLabel") is not None and not (isinstance(m["altLabel"], list) and all(isinstance(x, str) for x in m["altLabel"])):
            errors.append(f"{rel}: altLabel must be a list of strings")
        if "check" in m and d["type"] != "cause":
            errors.append(f"{rel}: 'check' is only allowed on causes")
        for fk, fv in (m.get("facets") or {}).items():
            if fk not in facets:
                errors.append(f"{rel}: unknown facet '{fk}' (allowed: {', '.join(facets)})")
                continue
            for v in fv if isinstance(fv, list) else [fv]:
                if v not in facets[fk]:
                    errors.append(f"{rel}: facet {fk}={v} not in schema vocabulary")
        source_ids = {s.get("id") for s in m.get("sources") or [] if isinstance(s, dict)}
        for pname, spec in preds.items():
            items = m.get(pname)
            if items is None:
                continue
            if not isinstance(items, list):
                errors.append(f"{rel}: {pname} must be a list")
                continue
            if d["type"] not in spec["domain"]:
                errors.append(f"{rel}: {pname} not allowed on a {d['type']} (domain: {', '.join(spec['domain'])})")
                continue
            ranks = set()
            for item in items:
                tgt_key = spec.get("target")
                if tgt_key is None:
                    q, target = {}, resolve_ref(item, "key" if "key" in spec["range"] else None)
                    if target is None:
                        errors.append(f"{rel}: {pname} items must be IDs")
                        continue
                else:
                    if not isinstance(item, dict):
                        errors.append(f"{rel}: {pname} items must be mappings like {{{tgt_key}: ..., ...}}")
                        continue
                    unknown = set(item) - {tgt_key} - set(spec["qualifiers"])
                    if unknown:
                        errors.append(f"{rel}: {pname}: unknown qualifier(s) {', '.join(sorted(unknown))}")
                    for r in spec.get("required", []):
                        if item.get(r) in (None, "", []):
                            errors.append(f"{rel}: {pname} -> {item.get(tgt_key)}: missing required '{r}'")
                    q = {k: v for k, v in item.items() if k != tgt_key}
                    target = resolve_ref(item.get(tgt_key))
                    if target is None and not (pname == "fixed_by" and (item.get("sets") or item.get("action"))):
                        errors.append(f"{rel}: {pname} item needs '{tgt_key}'")
                        continue
                # qualifiers
                if "evidence" in q and q["evidence"] not in schema["evidence"]:
                    errors.append(f"{rel}: {pname} -> {target}: evidence must be one of {schema['evidence']}")
                if "rank" in q:
                    if not isinstance(q["rank"], int) or q["rank"] < 1:
                        errors.append(f"{rel}: {pname} -> {target}: rank must be a positive integer")
                    elif q["rank"] in ranks:
                        errors.append(f"{rel}: {pname}: duplicate rank {q['rank']}")
                    ranks.add(q["rank"])
                if "source" in q:
                    for s in q["source"] if isinstance(q["source"], list) else [q["source"]]:
                        if s not in source_ids:
                            errors.append(f"{rel}: {pname} -> {target}: source '{s}' is not a sources[].id of this doc")
                if "via" in q:
                    via = resolve_ref(q["via"], "causes")
                    if node_type(via) != "cause":
                        errors.append(f"{rel}: {pname} -> {target}: via '{q['via']}' is not a cause")
                    q["via"] = via
                if "when" in q:
                    if not isinstance(q["when"], dict):
                        errors.append(f"{rel}: {pname} -> {target}: when must be a mapping")
                    else:
                        for wk, wv in q["when"].items():
                            vals = wv if isinstance(wv, list) else [wv]
                            if wk == "material":
                                ids = [resolve_ref(v, "materials") for v in vals]
                                for v, i in zip(vals, ids):
                                    if node_type(i) != "material":
                                        errors.append(f"{rel}: {pname} -> {target}: when.material '{v}' is not a material concept")
                                q["when"]["material"] = ids
                            elif wk in facets:
                                for v in vals:
                                    if v not in facets[wk]:
                                        errors.append(f"{rel}: {pname} -> {target}: when.{wk}={v} not in schema vocabulary")
                            else:
                                errors.append(f"{rel}: {pname} -> {target}: unknown when-key '{wk}'")
                if "sets" in q:
                    sets = q["sets"] if isinstance(q["sets"], list) else []
                    if not sets:
                        errors.append(f"{rel}: {pname} -> {target}: sets must be a non-empty list")
                    norm_sets = []
                    for s in sets:
                        if not isinstance(s, dict) or "key" not in s:
                            errors.append(f"{rel}: {pname} -> {target}: sets items need {{key, direction}}")
                            continue
                        kid = resolve_ref(s["key"], "key")
                        if node_type(kid) not in ("key", "firmware_param"):
                            errors.append(f"{rel}: {pname} -> {target}: unknown setting '{s['key']}' (not a PrusaSlicer key or schema firmware_param)")
                        if s.get("direction") not in schema["directions"]:
                            errors.append(f"{rel}: {pname} -> {target}: {s['key']} direction must be one of {schema['directions']}")
                        used_keys.add(kid)
                        norm_sets.append({"key": kid, **{k: v for k, v in s.items() if k != "key"}})
                    q["sets"] = norm_sets
                # target
                if target is not None:
                    tt = node_type(target)
                    if tt is None:
                        errors.append(f"{rel}: {pname} -> {target}: target does not exist")
                        continue
                    if tt not in spec["range"]:
                        errors.append(f"{rel}: {pname} -> {target}: target is a {tt}, expected {', '.join(spec['range'])}")
                        continue
                    if tt in ("key", "firmware_param"):
                        used_keys.add(target)
                edges.append({"s": src, "p": pname, "o": target, **q})

    # generated key/param nodes and relations
    for kid in sorted(used_keys):
        if kid.startswith("key/"):
            name = kid[4:]
            nodes[kid] = {"type": "key", "label": name, "altLabel": [], "scope": keys.get(name, "?"), "set_in": "slicer"}
            if name.startswith("filament_") and name[9:] in keys:
                base = "key/" + name[9:]
                nodes.setdefault(base, {"type": "key", "label": name[9:], "altLabel": [], "scope": keys[name[9:]], "set_in": "slicer"})
                edges.append({"s": kid, "p": "overrides", "o": base, "note": "unless nil"})
        else:
            ns, name = kid.split("/", 1)
            nodes[kid] = {"type": "firmware_param", "label": name, "altLabel": [], "set_in": ns}

    # completeness rules
    req = schema.get("require", {})
    out_by = {}
    for e in edges:
        out_by.setdefault((e["s"], e["p"]), []).append(e)
    for d in by_id.values():
        i, t, rel = d["id"], d["type"], d["id"] + ".md"
        if t == "problem" and req.get("problem_has_cause") and not out_by.get((i, "caused_by")):
            errors.append(f"{rel}: problem has no caused_by (schema require.problem_has_cause)")
        if t == "cause" and req.get("cause_has_fix") and not out_by.get((i, "fixed_by")):
            errors.append(f"{rel}: cause has no fixed_by (schema require.cause_has_fix)")
        if t == "cause" and req.get("cause_has_check") and not d["meta"].get("check"):
            errors.append(f"{rel}: cause has no check (schema require.cause_has_check)")
        if t == "material" and req.get("material_has_prone_to") and not out_by.get((i, "prone_to")):
            errors.append(f"{rel}: material has no prone_to (schema require.material_has_prone_to)")
        if t in ("problem", "cause") and req.get("altlabel_on_new_types") and not d["meta"].get("altLabel"):
            errors.append(f"{rel}: {t} needs at least one altLabel (schema require.altlabel_on_new_types)")

    # alias index + collisions (prefLabel and altLabel share one namespace)
    aliases: dict[str, set] = {}
    for i, n in nodes.items():
        for lab in [n["label"], *n["altLabel"]]:
            k = norm(lab)
            if k:
                aliases.setdefault(k, set()).add(i)
    for k, ids in sorted(aliases.items()):
        concept_ids = {i for i in ids if i in by_id}
        if len(concept_ids) > 1:
            errors.append(f"label collision: '{k}' is used by {', '.join(sorted(concept_ids))}")

    edges.sort(key=lambda e: (e["s"], e["p"], e.get("rank", 0), e["o"] or ""))
    graph = {"version": 1, "base_iri": schema.get("base_iri"),
             "nodes": dict(sorted(nodes.items())), "edges": edges,
             "aliases": {k: sorted(v) for k, v in sorted(aliases.items())}}
    return graph, errors, warnings


def graph_json(graph) -> str:
    return json.dumps(graph, ensure_ascii=False, indent=1, sort_keys=False) + "\n"


# ---------- rendering ----------

def set_block(text: str, name: str, content: str, at_end: bool = True) -> str:
    block = f"<!-- generated:{name} -->\n{content}<!-- /generated:{name} -->\n"
    pattern = re.compile(rf"\n*<!-- generated:{name} -->.*?<!-- /generated:{name} -->\n?", re.DOTALL)
    if not at_end and pattern.search(text):
        return pattern.sub(lambda _: "\n\n" + block, text, count=1)
    return pattern.sub("\n", text).rstrip("\n") + "\n\n" + block


def _qual(e) -> str:
    bits = []
    if "rank" in e:
        bits.append(f"#{e['rank']}")
    if "evidence" in e:
        bits.append(e["evidence"])
    for k, v in (e.get("when") or {}).items():
        bits.append("when " + ", ".join(x.split("/")[-1] for x in (v if isinstance(v, list) else [v])))
    if e.get("action"):
        bits.append(e["action"])
    return f" ({'; '.join(bits)})" if bits else ""


ARROW = {"up": "↑", "down": "↓", "set": "=", "enable": "on", "disable": "off", "check": "?"}


def _sets(e) -> str:
    return "".join(f" `{s['key'].split('/', 1)[1]}` {ARROW.get(s.get('direction'), '')}".rstrip() for s in e.get("sets", []))


def relations_block(rel, doc, docs_by_id, graph, schema, linked_from) -> str:
    i = doc["id"]
    labels = {**{p: s["label"] for p, s in schema["predicates"].items()},
              **{p: s["label"] for p, s in schema["generated_predicates"].items()}}
    inv = {p: s["inverse_label"] for p, s in schema["predicates"].items()}
    nodes = graph["nodes"]

    def link(t):
        if t is None:
            return "(settings only)"
        if t in docs_by_id:
            return f"[{nodes[t]['label']}]({rel_link(rel, t + '.md')})"
        return f"`{t}`"

    lines = []
    groups = {}
    for e in graph["edges"]:
        if e["s"] == i:
            groups.setdefault(labels[e["p"]], []).append(f"{link(e['o'])}{_qual(e)}{_sets(e)}")
        elif e["o"] == i and e["p"] in inv:
            lab = inv[e["p"]] if e["p"] != "related" else "Related"
            groups.setdefault(lab, []).append(f"{link(e['s'])}{_qual(e)}")
    for lab, items in groups.items():
        lines.append(f"- **{lab}:** " + " · ".join(dict.fromkeys(items)))
    typed = {e["o"] for e in graph["edges"] if e["s"] == i} | {e["s"] for e in graph["edges"] if e["o"] == i}
    lf = [r for r in linked_from if r[:-3] not in typed]
    if lf:
        lines.append("- **Linked from:** " + " · ".join(f"[{docs_by_id[r[:-3]]['meta'].get('title')}]({rel_link(rel, r)})" for r in lf))
    return "## Relations\n" + ("\n".join(lines) + "\n" if lines else "- (none yet)\n")


def view_matrix(rel, graph, docs_by_id) -> str:
    nodes, out = graph["nodes"], ["| Problem | Ranked causes | Settings touched by fixes |", "|---|---|---|"]
    fixes = {}
    for e in graph["edges"]:
        if e["p"] == "fixed_by":
            fixes.setdefault(e["s"], []).extend(s["key"].split("/", 1)[1] for s in e.get("sets", []))
    for pid in sorted((i for i, n in nodes.items() if n["type"] == "problem"), key=lambda i: nodes[i]["label"].lower()):
        cs = sorted((e for e in graph["edges"] if e["s"] == pid and e["p"] == "caused_by"), key=lambda e: e["rank"])
        causes = "; ".join(f"{e['rank']}. [{nodes[e['o']]['label']}]({rel_link(rel, e['o'] + '.md')})" for e in cs) or "—"
        keys = sorted({k for e in cs for k in fixes.get(e["o"], [])})
        out.append(f"| [{nodes[pid]['label']}]({rel_link(rel, pid + '.md')}) | {causes} | {', '.join(f'`{k}`' for k in keys) or '—'} |")
    return "\n".join(out) + "\n"


def view_keymap(rel, graph, docs_by_id) -> str:
    nodes, out = graph["nodes"], ["| Setting | Scope / set in | Changed by fixes for | Calibrated by | Overrides |", "|---|---|---|---|---|"]
    for kid in sorted(i for i, n in nodes.items() if n["type"] in ("key", "firmware_param")):
        n = nodes[kid]
        fixes = sorted({f"[{nodes[e['s']]['label']}]({rel_link(rel, e['s'] + '.md')}) {ARROW.get(s.get('direction'), '')}"
                        for e in graph["edges"] if e["p"] == "fixed_by" for s in e.get("sets", []) if s["key"] == kid})
        cal = sorted({f"[{nodes[e['s']]['label']}]({rel_link(rel, e['s'] + '.md')})" for e in graph["edges"] if e["p"] == "calibrates" and e["o"] == kid})
        ov = [f"`{e['o'].split('/', 1)[1]}`" for e in graph["edges"] if e["p"] == "overrides" and e["s"] == kid]
        where = f"{n.get('scope', '')} ({n['set_in']})" if n["type"] == "key" else n["set_in"]
        out.append(f"| `{n['label']}` | {where} | {'; '.join(fixes) or '—'} | {', '.join(cal) or '—'} | {', '.join(ov) or '—'} |")
    return "\n".join(out) + "\n"


def render(schema, docs, graph) -> dict[str, str]:
    docs_by_id = {d["id"]: d for d in docs.values()}
    linked_from = {rel: [] for rel in docs}
    for rel, d in docs.items():
        if rel in META:
            continue
        for t in sorted(d["links"]):
            if t in linked_from and t != rel:
                linked_from[t].append(rel)
    sections = schema["sections"]
    groups: dict[str, list[str]] = {}
    for rel, d in docs.items():
        if rel in ("index.md", "log.md"):
            continue
        groups.setdefault(d["folder"], []).append(rel)
    order = [k for k in sections if k in groups] + sorted(k for k in groups if k not in sections)
    catalog = ""
    for key in order:
        catalog += f"\n## {sections.get(key, key.replace('-', ' ').capitalize())}\n"
        for rel in sorted(groups[key], key=lambda r: str(docs[r]["meta"].get("title", r)).lower()):
            m = docs[rel]["meta"]
            catalog += f"- [{m.get('title')}]({rel}): {m.get('description')}\n"
    expected = {}
    for rel, d in docs.items():
        text = d["text"]
        if rel == "index.md":
            text = set_block(text, "catalog", catalog.lstrip("\n"), at_end=False)
        elif rel not in META:
            for v in VIEWS:
                if f"<!-- generated:{v} -->" in text:
                    fn = view_matrix if v == "matrix" else view_keymap
                    text = set_block(text, v, fn(rel, graph, docs_by_id), at_end=False)
            text = GEN_RE.sub(lambda m: m.group(0) if m.group(1) != "backlinks" else "\n", text)  # migrate old block
            text = set_block(text, "relations", relations_block(rel, d, docs_by_id, graph, schema, linked_from[rel]))
        expected[rel] = text
    return expected


# ---------- legacy content checks (provenance, links, footnotes) ----------

def content_checks(docs, graph, require=None):
    errors, warnings = [], []
    require = require or {}
    # ratchet: once a warning class reaches zero, schema.yaml `require` turns it into an error
    dead_end = errors if require.get("no_dead_ends") else warnings
    legacy = errors if require.get("v02_provenance") else warnings
    known = set(docs)
    titles = {}
    inbound = {rel: 0 for rel in docs}
    for rel, d in docs.items():
        if rel not in META:
            for t in d["links"] - {rel}:
                if t in inbound:
                    inbound[t] += 1
    for e in graph["edges"]:
        for end in (e["s"], e["o"]):
            if end and end + ".md" in inbound:
                inbound[end + ".md"] += 1
    for rel, d in docs.items():
        if rel == "log.md":
            continue
        meta, body, path = d["meta"], GEN_RE.sub("", d["body"]), d["path"]
        if rel not in META:
            if not inbound[rel]:
                errors.append(f"{rel}: orphan; no other topic links or relates to it")
            typed_out = any(e["s"] == d["id"] for e in graph["edges"])
            if not (d["links"] - META - {rel}) and not typed_out:
                dead_end.append(f"{rel}: dead end; links/relates to no other topic (add `related:` or a typed edge)")
        for key in ("type", "title", "description"):
            if not meta.get(key):
                errors.append(f"{rel}: missing required frontmatter key {key}")
        title = meta.get("title")
        if title in titles:
            errors.append(f"{rel}: duplicate title also used by {titles[title]}")
        elif title:
            titles[title] = rel
        sources = meta.get("sources") or []
        if rel != "index.md" and not meta.get("generated"):
            legacy.append(f"{rel}: missing v0.2 provenance (`sources` + `generated`)")
        if meta.get("generated") and not sources:
            errors.append(f"{rel}: v0.2 document has generated but no sources")
        ids = set()
        for source in sources:
            if not isinstance(source, dict):
                errors.append(f"{rel}: sources items must be mappings")
                continue
            sid, resource = str(source.get("id", "")), str(source.get("resource", ""))
            if not sid or sid in ids:
                errors.append(f"{rel}: source IDs must be present and unique")
            ids.add(sid)
            parsed = urlparse(resource)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                errors.append(f"{rel}: invalid source URL for {sid or '<missing id>'}")
            if not source.get("title"):
                errors.append(f"{rel}: source {sid or '<missing id>'} has no title")
        used = set(re.findall(r"\[\^([A-Za-z0-9_-]+)\]", body))
        defs = set(re.findall(r"^\[\^([A-Za-z0-9_-]+)\]:", body, re.MULTILINE))
        for fn in sorted(used):
            if fn not in defs:
                errors.append(f"{rel}: footnote {fn} has no definition")
            if fn not in ids:
                errors.append(f"{rel}: footnote {fn} has no matching sources.id")
        for target in LINK_RE.findall(body):
            target = target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            try:
                target_rel = (path.parent / target).resolve().relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                errors.append(f"{rel}: link escapes knowledge/: {target}")
                continue
            if target_rel not in known:
                errors.append(f"{rel}: broken internal link {target}")
        for line_no, line in enumerate(body.splitlines(), 1):
            if NUMERIC_RE.search(line) and not line.lstrip().startswith(("-", "|", "`")):
                context = ("starting", "typical", "example", "depends", "unknown", "range", "validate", "record")
                if not any(t in line.lower() for t in context) and "[^" not in line:
                    warnings.append(f"{rel}:{line_no}: numeric setting may need context or citation")
    return errors, warnings


# ---------- commands ----------

def compile_bundle(root: Path | None = None, write: bool = False):
    """Validate; if valid and write=True, write generated blocks and graph.json. Returns (errors, warnings, graph, docs)."""
    root = root or ROOT
    schema, docs, errors = load(root)
    if errors:
        return errors, [], None, docs
    graph, errors, warnings = build_graph(schema, docs, load_keys())
    for rel, d in docs.items():
        if rel not in ("log.md",) and not (d["meta"].get("title") and d["meta"].get("description")):
            errors.append(f"{rel}: missing title/description; cannot be catalogued")
    if errors:
        return errors, warnings, None, docs
    e2, w2 = content_checks(docs, graph, schema.get("require"))
    errors, warnings = errors + e2, warnings + w2
    if errors:  # never emit generated output from an invalid bundle
        return errors, warnings, None, docs
    expected = render(schema, docs, graph)
    gj = graph_json(graph)
    gpath = root / "graph.json"
    stale = [rel for rel, t in expected.items() if t != docs[rel]["text"]]
    graph_stale = not gpath.exists() or gpath.read_text(encoding="utf-8") != gj
    if write:
        for rel in stale:
            docs[rel]["path"].write_text(expected[rel], encoding="utf-8")
            docs[rel]["text"] = expected[rel]
            print(f"FIXED {rel}")
        if graph_stale:
            gpath.write_text(gj, encoding="utf-8")
            print("FIXED graph.json")
    else:
        errors += [f"{rel}: generated sections are stale; run `uv run kg.py fix`" for rel in stale]
        if graph_stale:
            errors.append("graph.json is stale; run `uv run kg.py fix`")
    return errors, warnings, graph, docs


def build_html(graph, docs, out: Path, verbose: bool = True):
    bodies = {d["id"]: GEN_RE.sub("", d["body"]).strip() for d in docs.values() if d["id"] in graph["nodes"]}
    data = json.dumps({"graph": graph, "bodies": bodies}, ensure_ascii=False).replace("</", "<\\/")
    tpl = (HERE / "kg_viewer.html").read_text(encoding="utf-8")
    out.parent.mkdir(exist_ok=True)
    out.write_text(tpl.replace("/*__DATA__*/null", data), encoding="utf-8")
    if verbose:
        print(f"wrote {out}")


def cmd_keys():
    import profiles
    scope = {}
    types = ("print", "filament", "printer")
    # Keys seen in user profiles and vendor presets (filament_retract_* etc. are absent from the defaults file).
    for typ in types:
        for f in (profiles.ROOT / typ).glob("*.ini"):
            for k in profiles.parse_kv(f.read_text(encoding="utf-8")):
                scope.setdefault(k, typ)
    for secs in profiles.load_vendors().values():
        for (typ, _), kv in secs.items():
            if typ in types:
                for k in kv:
                    if k not in profiles.META_KEYS:
                        scope.setdefault(k, typ)
    for k in profiles.parse_kv(profiles.DEFAULTS.read_text(encoding="utf-8")):
        scope.setdefault(k, "unknown")
    KEYS_FILE.write_text(json.dumps(dict(sorted(scope.items())), indent=1) + "\n", encoding="utf-8")
    print(f"wrote {KEYS_FILE.name}: {len(scope)} keys")
    return 0


def report(errors, warnings) -> int:
    if "-q" not in sys.argv:
        for w in warnings:
            print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"knowledge graph: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


def main(argv=None) -> int:
    args = [a for a in (argv if argv is not None else sys.argv[1:]) if not a.startswith("-")]
    cmd = args[0] if args else "check"
    if cmd == "keys":
        return cmd_keys()
    if cmd not in ("check", "fix", "build"):
        print(__doc__)
        return 2
    errors, warnings, graph, docs = compile_bundle(write=cmd in ("fix", "build"))
    rc = report(errors, warnings)
    if not errors and cmd in ("fix", "build"):  # viewer always matches graph.json
        build_html(graph, docs, HERE / "build" / "graph.html", verbose=cmd == "build")
    return rc


if __name__ == "__main__":
    sys.exit(main())
