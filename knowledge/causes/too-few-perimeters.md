---
type: cause
title: Too few perimeters
description: Thin shells let infill show through and give step-downs a weak foundation.
altLabel: [walls too thin, zu wenige Wände]
facets: {phase: [walls-seams]}
check: Defect disappears with more perimeters (e.g. 2 → 4).
fixed_by:
  - {action: add perimeters, sets: [{key: perimeters, direction: up}]}
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
# Too few perimeters

Thin shells let infill show through and give step-downs a weak foundation. [^tsg-s3d] [^tsg-all3dp]

**Check:** Defect disappears with more perimeters (e.g. 2 → 4).

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (add perimeters) `perimeters` ↑
- **Causes:** [Infill visible through walls](../defects/infill-visible-through-walls.md) (#1; C) · [Gaps or pillowing in top layers](../defects/top-surface-gaps.md) (#5; B)
<!-- /generated:relations -->
