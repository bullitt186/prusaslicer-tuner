---
type: defect
title: Gaps between infill and walls
description: Infill does not fuse to the innermost perimeter.
altLabel: [gaps between infill and outline, gaps between infill and outer wall, Lücken zwischen Infill und Wand]
facets: {phase: [walls-seams]}
caused_by:
  - {cause: causes/infill-overlap-wrong, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/print-speed-too-high, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/nozzle-temp-too-low, rank: 3, evidence: C, source: tsg-all3dp}
related: [defects/weak-infill, defects/infill-visible-through-walls]
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
# Gaps between infill and walls

Infill does not fuse to the innermost perimeter.

Raise overlap first (e.g. 20 % → 30 % as a starting point), then slow down.[^tsg-s3d] See [infill/perimeter overlap](../tuning/infill-perimeter-overlap.md).

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Related:** [Infill visible through walls](infill-visible-through-walls.md) · [Weak or messy infill](weak-infill.md)
- **Caused by:** [Infill/perimeter overlap wrong](../causes/infill-overlap-wrong.md) (#1; B) · [Print speed too high](../causes/print-speed-too-high.md) (#2; B) · [Nozzle temperature too low](../causes/nozzle-temp-too-low.md) (#3; C)
<!-- /generated:relations -->
