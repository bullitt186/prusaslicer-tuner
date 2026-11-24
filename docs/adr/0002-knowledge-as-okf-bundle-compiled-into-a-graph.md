# ADR-0002: Knowledge as an OKF bundle compiled into a graph

- **Status:** Accepted
- **Date:** 2026-11-24

## Context

The agent diagnoses print defects from a knowledge library that grows from many
sources (Ellis' Print Tuning Guide, the Troubleshooting Guide dataset, Prusa,
Klipper and Voron documentation, community reports). Agents need ranked causes
and the exact profile keys behind a fix, not whole articles. This ADR records the
decision as it stands in `knowledge/maintenance.md` and `kg.py`; it was made
before ADRs existed.

## Decision

The knowledge lives in `knowledge/` as an OKF v0.2 bundle: one Markdown file per
technical concept with YAML frontmatter and `sources` provenance, organised by
concept, not by source. The frontmatter is the single source of truth.
`knowledge/schema.yaml` defines concept types, a fixed predicate list with
domain, range and qualifiers, and closed vocabularies. `kg.py` validates the
bundle and generates everything else: `index.md`, the `## Relations` blocks, the
views, `knowledge/graph.json` for the MCP tools `lookup` and `card`, and the
viewer. `kg.py fix` writes nothing while any error exists.

## Consequences

Generated blocks and `graph.json` are never edited by hand. A knowledge change
must pass `kg.py check` and leave `kg.py fix` without a diff; hooks and CI
enforce this. Every topic must be reachable (no orphans). The checks do not prove
technical correctness; evidence levels A–D on edges state how strong a claim is.

## Alternatives considered

Not recorded.
