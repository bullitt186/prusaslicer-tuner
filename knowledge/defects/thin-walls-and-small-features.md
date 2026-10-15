---
type: defect
title: Thin walls and small features missing
description: Thin walls get gaps in the middle or small features do not print.
altLabel: [gaps in thin walls, small features not printed, fine detail not printing, dünne Wände fehlen]
facets: {phase: [walls-seams]}
caused_by:
  - {cause: causes/wall-thinner-than-line-width, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/nozzle-too-large-for-detail, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/print-speed-too-high, rank: 3, evidence: C, source: tsg-all3dp}
related: [defects/dimensional-inaccuracy]
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
# Thin walls and small features missing

Thin walls get gaps in the middle or small features do not print.

A wall a few line widths thick (e.g. 1.0 mm with 0.4 mm lines) needs thin-wall handling or a line width that divides it; features below the nozzle size need a smaller nozzle or thicker geometry.[^tsg-s3d]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Related:** [Dimensional inaccuracy](dimensional-inaccuracy.md) · [Nozzle selection](../hardware/nozzle-selection.md)
- **Caused by:** [Wall thinner than the extrusion width](../causes/wall-thinner-than-line-width.md) (#1; B) · [Nozzle too large for the detail](../causes/nozzle-too-large-for-detail.md) (#2; B) · [Print speed too high](../causes/print-speed-too-high.md) (#3; C)
<!-- /generated:relations -->
