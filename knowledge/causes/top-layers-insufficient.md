---
type: cause
title: Too few top solid layers
description: Top solid layers must bridge the infill gaps; a thin top sags into them.
altLabel: [top layers too thin, zu wenige Deckschichten]
facets: {phase: [top-bottom]}
check: Gaps disappear with more top layers (aim for a top shell of at least ~0.5 mm as a starting point).
fixed_by:
  - {action: increase top solid layers / minimum top thickness, sets: [{key: top_solid_layers, direction: up}, {key: top_solid_min_thickness, direction: up}]}
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
status: stable
---
# Too few top solid layers

Top solid layers must bridge the infill gaps; a thin top sags into them. [^tsg-s3d] [^tsg-all3dp]

**Check:** Gaps disappear with more top layers (aim for a top shell of at least ~0.5 mm as a starting point).

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (increase top solid layers / minimum top thickness) `top_solid_layers` ↑ `top_solid_min_thickness` ↑
- **Causes:** [Gaps or pillowing in top layers](../defects/top-surface-gaps.md) (#1; B)
<!-- /generated:relations -->
