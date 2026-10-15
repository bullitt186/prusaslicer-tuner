---
type: cause
title: Shrinkage not compensated
description: Constant errors need an XY offset; errors that grow with part size are shrinkage and need scaling.
altLabel: [scaling error, Schrumpfung nicht kompensiert]
facets: {phase: [model]}
check: 'Measure a small and a large part: same error = offset, proportional error = shrinkage.'
fixed_by:
  - {action: compensate shrinkage (scale) or a constant XY offset, sets: [{key: filament_shrinkage_compensation_xy, direction: set}, {key: xy_size_compensation, direction: set}]}
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
# Shrinkage not compensated

Constant errors need an XY offset; errors that grow with part size are shrinkage and need scaling. [^tsg-s3d] [^tsg-all3dp]

**Check:** Measure a small and a large part: same error = offset, proportional error = shrinkage.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (compensate shrinkage (scale) or a constant XY offset) `filament_shrinkage_compensation_xy` = `xy_size_compensation` =
- **Causes:** [Dimensional inaccuracy](../defects/dimensional-inaccuracy.md) (#4; B)
<!-- /generated:relations -->
