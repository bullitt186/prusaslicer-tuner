---
type: cause
title: Infill printed too fast
description: Infill usually runs fastest; when the extruder cannot keep up it under-extrudes and fails to bond.
altLabel: [infill speed too high, Infill zu schnell]
facets: {phase: [infill]}
check: Infill becomes solid at about half the speed.
fixed_by:
  - {action: lower infill speed, sets: [{key: infill_speed, direction: down}]}
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
# Infill printed too fast

Infill usually runs fastest; when the extruder cannot keep up it under-extrudes and fails to bond. [^tsg-s3d] [^tsg-all3dp]

**Check:** Infill becomes solid at about half the speed.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (lower infill speed) `infill_speed` ↓
- **Causes:** [Weak or messy infill](../defects/weak-infill.md) (#1; B)
<!-- /generated:relations -->
