---
type: defect
title: Infill visible through walls
description: The infill pattern shows through the outer walls.
altLabel: [infill visible from outside, infill ghosting, Infill scheint durch]
facets: {phase: [walls-seams]}
caused_by:
  - {cause: causes/too-few-perimeters, rank: 1, evidence: C, source: tsg-all3dp}
  - {cause: causes/perimeter-order, rank: 2, evidence: C, source: tsg-all3dp}
related: [defects/infill-wall-gaps]
sources:
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
# Infill visible through walls

The infill pattern shows through the outer walls.

Infill overlapping the perimeter imprints the wall, mostly with thin shells. Thicker shells or printing infill after perimeters hide it.[^tsg-all3dp]

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Caused by:** [Too few perimeters](../causes/too-few-perimeters.md) (#1; C) · [Perimeter order pushes walls out](../causes/perimeter-order.md) (#2; C)
- **Related:** [Gaps between infill and walls](infill-wall-gaps.md)
<!-- /generated:relations -->
