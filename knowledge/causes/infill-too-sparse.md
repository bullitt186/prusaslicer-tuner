---
type: cause
title: Infill too sparse
description: Low infill density leaves wide air gaps for top layers and corners to span.
altLabel: [infill percentage too low, zu wenig Infill]
facets: {phase: [infill]}
check: Top gaps shrink when infill density rises (e.g. 30 % → 50 %).
fixed_by:
  - {action: raise infill density, sets: [{key: fill_density, direction: up}]}
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
# Infill too sparse

Low infill density leaves wide air gaps for top layers and corners to span. [^tsg-s3d] [^tsg-all3dp]

**Check:** Top gaps shrink when infill density rises (e.g. 30 % → 50 %).

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (raise infill density) `fill_density` ↑
- **Causes:** [Gaps or pillowing in top layers](../defects/top-surface-gaps.md) (#2; B) · [Weak or messy infill](../defects/weak-infill.md) (#3; C)
<!-- /generated:relations -->
