---
type: process
title: Knowledge maintenance
description: Repository rules for evidence, provenance, context, cross-links and validation of the FDM/FFF knowledge bundle.
tags: [maintenance, provenance, validation, okf, mcp]
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: okf-spec
    title: Google Open Knowledge Format specification
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
---
# Knowledge maintenance

This repository follows OKF v0.2: Markdown files with YAML frontmatter, stable path identity, and `sources` provenance. OKF deliberately does not prescribe a fixed FDM taxonomy or a mandatory validator; this repository's evidence labels and QA checks are documented conventions layered on top of the official format. [^okf-spec]

## Authoring rules

- Organize by technical concept, not by source. Merge overlapping evidence into one topic and preserve disagreements with their operating conditions.
- Every substantive number, recommendation or empirical claim must map to an inspected source ID or be explicitly labeled as a hypothesis/starting value.
- A number without material, hardware, software and process context is incomplete. If context is unknown, say so rather than inventing a universal setting.
- Use relative Markdown links for cross-topic relationships. Keep explanations in one canonical topic and link to it from defects, materials and procedures.
- Prefer an update to an existing topic over a duplicate file. Use stable filenames and deterministic index ordering.

## Knowledge graph model

The bundle compiles into a knowledge graph. Frontmatter is the single source of truth, and `uv run kg.py fix` derives everything else: the `index.md` catalog, a `## Relations` block per doc, the ranked cause map in the [diagnostic matrix](troubleshooting/diagnostic-matrix.md), the setting index in the [profile knowledge map](slicer/profile-knowledge-map.md), and `graph.json` for the MCP tools `lookup`/`card` and the viewer. `knowledge/schema.yaml` defines concept types (by folder), the fixed predicate list with domain/range and qualifiers, closed facet vocabularies and completeness rules.

- **Concept ID** = path without `.md`. Labels use SKOS names: `title` (prefLabel), `altLabel` (English *and* German user wording), `description` (definition), `broader`, `related`. Labels are one namespace: two concepts may not share a normalized label.
- **Causal chain:** problem `caused_by` cause (`rank`, `evidence`, optional `when`, `source`) → cause `fixed_by` procedure/material/component and/or `sets: [{key, direction}]`, or a physical `action` → procedure `calibrates` key. Material `prone_to` problem (`via` cause). Inverses (`causes`, `fixes`, `affects`, `calibrated_by`, `narrower`) and `overrides` / `set_in` are generated; never write them.
- **Ranking:** `rank` orders causes cheapest and most likely first. When a new source adds an existing cause to a problem, add or extend the edge's `source` instead of creating a second cause.
- **Evidence on edges:** A = specification or reproducible measurement; B = vendor/firmware documentation and documented procedures (Klipper, Prusa KB, Simplify3D, Ellis guide); C = editorial guides or unsourced general practice; D = single anecdote or experimental community value.
- **Keys:** `sets`/`calibrates` accept PrusaSlicer keys from `prusaslicer_keys.json` (regenerate with `uv run kg.py keys` after regenerating `prusaslicer_defaults.ini`) and firmware parameters from `schema.yaml`.
- **Integration:** every topic must be reachable: linked from another topic's body or connected by a typed edge (orphans are errors). Prefer an edge or an `altLabel` on an existing concept over a new file.
- Exempt infrastructure: `index.md`, `log.md`, this file.

## Validation and enforcement

`uv run kg.py check` validates the schema rules (types, predicates, domain/range, existing targets and keys, evidence values, source IDs, unique ranks, label collisions, completeness), plus provenance, footnotes, links and orphans. It fails on stale generated output. `kg.py fix` (which also rebuilds the viewer `build/graph.html`) **writes nothing while any error exists**, so an invalid edit never reaches `graph.json` or the MCP server. Two ratchet rules (`schema.yaml` `require`) keep cleaned-up warning classes from returning: `v02_provenance` makes a doc without `sources` + `generated` an error, and `no_dead_ends` makes a topic without any outgoing link or typed edge an error. The numeric-context heuristic stays a warning because it has false positives; keep it at zero by citing the source or naming a value as a starting value with its conditions, never by adding filler words. `test_kg.py` covers the rules.

Enforcement: `.githooks/pre-commit` (check + tests on knowledge changes), `.githooks/pre-push` (full check), `.githooks/post-commit`, `post-merge` and `post-checkout` (rebuild `build/graph.html` after commits, pulls and branch switches); enable per clone with `git config core.hooksPath .githooks`. GitHub Actions (`.github/workflows/knowledge.yml`) re-runs everything on push/PR and mails on failure; branch protection is unavailable on this private free-plan repo, so never use `--no-verify` for knowledge commits. These checks do not prove technical correctness, source availability or experimental validity.

The MCP server reads `graph.json` (`lookup`, `card`) and the docs (`read_knowledge`); it does not transform or rank claims beyond the authored `rank`.

[^okf-spec]: Google Open Knowledge Format specification
