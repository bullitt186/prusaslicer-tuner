# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""Run: uv run test_kg.py — schema rules, generated inverses, alias collisions, idempotence, no output on invalid input."""
import json, shutil, tempfile
from pathlib import Path
import kg

root = Path(tempfile.mkdtemp()).resolve()
kg.ROOT = root
shutil.copy(Path(__file__).parent / "knowledge/schema.yaml", root / "schema.yaml")
for f in ("defects", "causes", "tuning", "materials"):
    (root / f).mkdir()

SRC = "sources:\n  - id: s1\n    title: Src\n    resource: https://example.com\ngenerated:\n  by: test\n  at: 2026-01-01\n"


def doc(path, title, extra="", body="body"):
    (root / path).write_text(f"---\ntype: concept\ntitle: {title}\ndescription: about {title}\n{SRC}{extra}---\n{body}\n")


def run(write=False):
    errors, warnings, graph, docs = kg.compile_bundle(root, write=write)
    return errors, graph


(root / "index.md").write_text("---\ntype: index\ntitle: Index\ndescription: idx\n---\n<!-- generated:catalog -->\n<!-- /generated:catalog -->\n\n## Tail\n")
doc("defects/stringing.md", "Stringing", "altLabel: [oozing, Fädenziehen]\ncaused_by:\n  - {cause: causes/wet, rank: 1, evidence: B, when: {material: [petg]}, source: s1}\n  - {cause: causes/hot, rank: 2, evidence: C}\n")
doc("causes/wet.md", "Wet filament", "altLabel: [nasses Filament]\ncheck: popping\nfixed_by:\n  - {procedure: tuning/retraction, action: dry first, sets: [{key: filament_retract_length, direction: up}]}\n")
doc("causes/hot.md", "Temperature too high", "altLabel: [too hot]\ncheck: temp tower\nfixed_by:\n  - {action: lower temp, sets: [{key: temperature, direction: down}, {key: klipper/pressure_advance, direction: up}]}\n")
doc("tuning/retraction.md", "Retraction", "calibrates: [retract_length, filament_retract_length]\n")
doc("materials/petg.md", "PETG", "prone_to:\n  - {problem: defects/stringing, via: wet, evidence: B}\n")

errs, _ = run(write=True)
assert errs == [], errs
g = json.loads((root / "graph.json").read_text())
assert g["aliases"]["faedenziehen"] == ["defects/stringing"], g["aliases"].get("faedenziehen")
assert {"s": "key/filament_retract_length", "p": "overrides", "o": "key/retract_length", "note": "unless nil"} in g["edges"]
assert g["nodes"]["klipper/pressure_advance"]["set_in"] == "klipper"
assert any(e["p"] == "caused_by" and e["when"] == {"material": ["materials/petg"]} for e in g["edges"])
wet = (root / "causes/wet.md").read_text()
assert "- **Causes:** [Stringing](../defects/stringing.md) (#1; B; when petg)" in wet, wet
assert "- **Prone to:** [Stringing](../defects/stringing.md)" in (root / "materials/petg.md").read_text()
assert "- [Stringing](defects/stringing.md): about Stringing" in (root / "index.md").read_text()
assert run()[0] == [], "fix must be idempotent"

# Each invalid edit must fail AND leave graph.json untouched.
before = (root / "graph.json").read_text()
cases = {
    "defects/stringing.md": ("caused_by:\n  - {cause: causes/nope, rank: 1, evidence: B}\n", "target does not exist"),
    "causes/hot.md": ("fixed_by:\n  - {action: x, sets: [{key: not_a_key, direction: up}]}\n", "unknown setting"),
    "tuning/retraction.md": ("caused_by:\n  - {cause: causes/wet, rank: 1, evidence: B}\n", "not allowed on a procedure"),
    "materials/petg.md": ("prone_to:\n  - {problem: causes/wet, evidence: B}\n", "expected problem"),
    "causes/wet.md": ("altLabel: [oozing]\nfixed_by:\n  - {action: x}\n", "label collision"),
}
for path, (extra, needle) in cases.items():
    original = (root / path).read_text()
    title = original.split("title: ")[1].split("\n")[0]
    doc(path, title, extra)
    errs, _ = run(write=True)
    assert any(needle in e for e in errs), (path, needle, errs)
    assert (root / "graph.json").read_text() == before, f"graph.json written despite error ({needle})"
    (root / path).write_text(original)

doc("defects/stringing.md", "Stringing", "caused_by:\n  - {cause: causes/wet, rank: 1, evidence: E}\n  - {cause: causes/hot, rank: 1, evidence: B, source: nope}\n")
original = (root / "causes/hot.md").read_text()
(root / "causes/hot.md").write_text(original.replace("check: temp tower\n", ""))
assert any("cause has no check" in e for e in run()[0]), "completeness rule must fire"
(root / "causes/hot.md").write_text(original)

errs, _ = run()
assert any("evidence must be" in e for e in errs) and any("duplicate rank" in e for e in errs) and any("source 'nope'" in e for e in errs), errs
# Ratchet rules (schema require.v02_provenance / no_dead_ends): both must block and leave graph.json untouched.
doc("defects/stringing.md", "Stringing", "altLabel: [oozing]\ncaused_by:\n  - {cause: causes/wet, rank: 1, evidence: B}\n  - {cause: causes/hot, rank: 2, evidence: C}\n")
assert run(write=True)[0] == []
before = (root / "graph.json").read_text()
original = (root / "materials/petg.md").read_text()
(root / "materials/petg.md").write_text(original.replace("generated:\n  by: test\n  at: 2026-01-01\n", ""))
errs, _ = run(write=True)
assert any("missing v0.2 provenance" in e for e in errs), errs
assert (root / "graph.json").read_text() == before
(root / "materials/petg.md").write_text(original)
(root / "materials/pla.md").write_text("---\ntype: material\ntitle: PLA\ndescription: about PLA\n" + SRC + "---\nsee nothing\n")
doc("defects/stringing.md", "Stringing", "altLabel: [oozing]\ncaused_by:\n  - {cause: causes/wet, rank: 1, evidence: B}\n  - {cause: causes/hot, rank: 2, evidence: C}\n", "see [pla](../materials/pla.md)")
errs, _ = run(write=True)
assert any("materials/pla.md: dead end" in e for e in errs), errs
assert (root / "graph.json").read_text() == before
print("ok")
