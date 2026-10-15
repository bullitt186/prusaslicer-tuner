---
type: defect
title: Poor bridges & overhangs
description: Sagging bridges, curled/droopy overhangs.
timestamp: 2026-10-13
altLabel: [sagging bridges, droopy overhangs, Brücken hängen durch, Überhänge, poor bridging, messy bridges, messy overhangs]
facets: {phase: [supports-bridges]}
caused_by:
  - {cause: causes/insufficient-cooling, rank: 1, evidence: B, source: [tsg-s3d, tsg-all3dp]}
  - {cause: causes/bridge-flow-or-speed-wrong, rank: 2, evidence: B, source: [tsg-s3d, tsg-all3dp]}
  - {cause: causes/overhang-too-fast, rank: 3, evidence: C}
  - {cause: causes/nozzle-temp-too-high, rank: 4, evidence: C}
  - {cause: causes/missing-supports, rank: 5, evidence: B, source: [tsg-s3d, tsg-all3dp]}
sources:
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-all3dp
    title: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-migration
  at: '2026-10-13T23:30:00Z'
---
# Bridges and overhangs
General knowledge.
- More cooling: `bridge_fan_speed`, `overhang_fan_speed_0..3` (with `enable_dynamic_fan_speeds = 1`).
- Bridges: `bridge_speed` (slower), `bridge_flow_ratio` ≤ 1, `thick_bridges`.
- Overhangs: `enable_dynamic_overhang_speeds` and the `overhang_speed_0..3` keys, `overhangs` (detect), lower `temperature`, `external_perimeters_first` (can hurt extreme overhangs).
- Curling overhangs in PETG or ABS: also see [overheating](overheating.md).

<!-- generated:relations -->
## Relations
- **Caused by:** [Insufficient part cooling](../causes/insufficient-cooling.md) (#1; B) · [Bridge flow or speed wrong](../causes/bridge-flow-or-speed-wrong.md) (#2; B) · [Overhangs printed too fast](../causes/overhang-too-fast.md) (#3; C) · [Nozzle temperature too high](../causes/nozzle-temp-too-high.md) (#4; C) · [Unsupported overhang or bridge](../causes/missing-supports.md) (#5; B)
- **Related:** [Poor surface above or below supports](support-surface-quality.md)
- **Linked from:** [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md)
<!-- /generated:relations -->
