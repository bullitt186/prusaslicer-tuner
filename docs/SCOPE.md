# Scope

What this project is for, so contributions go in the same direction. Changing this file is a
maintainer decision, recorded as an ADR.

## Purpose

prusaslicer-tuner lets an AI agent read, explain, diff and, with the user's approval, edit
PrusaSlicer printer, print and filament profiles, and diagnose FDM print defects from photos or
descriptions using a curated knowledge graph mapped to PrusaSlicer keys and Klipper / Prusa
firmware parameters. It is for people who tune their own printers with an agent (MCP server or
Claude Code skill).

## In scope

- Reading, resolving (vendor `inherits` chains, built-in defaults), diffing and editing
  PrusaSlicer user profiles (`profiles.py`, MCP tools).
- The FDM knowledge library in `knowledge/` (fundamentals, defects, causes, tuning procedures,
  materials, hardware, firmware, mechanical behaviour) and its graph compiler `kg.py`.
- Source research and provenance in `research/`.
- Calibration test prints, fetched from their sources (`test_prints/fetch.sh`).
- Agent workflows for diagnosis and filament calibration (`SKILL.md`).

## Out of scope

- Facts about one user's printers (hardware, hosts, own calibration values): they belong in the
  user's own skill or notes (ADR-0003).
- Access to printers or firmware configuration (`printer.cfg`, Moonraker, SSH): the tool has
  none; the agent uses what the environment provides (`SKILL.md`).
- Writing vendor preset files: vendor presets are only copied, never written.
- Redistributing the test print STLs: their licences do not allow it (`README.md`).
- Other slicers than PrusaSlicer: Open: to be decided by the maintainer.

## Direction

Open: to be decided by the maintainer. There is no roadmap file or open issue yet.

## Principles

- Every claim in the knowledge library maps to a source or is labelled a hypothesis or
  starting value; numbers come with their context (`knowledge/maintenance.md`).
- Frontmatter is the single source of truth; generated output comes from `kg.py fix` only
  (ADR-0002).
- Profiles are changed only on request, one change at a time, with a backup first (`SKILL.md`).
- `profiles.py` stays standard library only.
