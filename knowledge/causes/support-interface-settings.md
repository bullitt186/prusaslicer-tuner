---
type: cause
title: Support interface or gap wrong
description: Too little gap welds supports to the part; too much or too sparse a top lets the surface droop.
altLabel: [support contact distance, Support-Abstand]
facets: {phase: [supports-bridges]}
check: The underside is either torn on removal or droopy; vary one support setting at a time.
fixed_by:
  - {action: 'tune support Z gap, XY offset and interface layers', sets: [{key: support_material_contact_distance, direction: set}, {key: support_material_xy_spacing, direction: set}, {key: support_material_interface_layers, direction: up}]}
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
# Support interface or gap wrong

Too little gap welds supports to the part; too much or too sparse a top lets the surface droop. [^tsg-s3d] [^tsg-all3dp]

**Check:** The underside is either torn on removal or droopy; vary one support setting at a time.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (tune support Z gap, XY offset and interface layers) `support_material_contact_distance` = `support_material_xy_spacing` = `support_material_interface_layers` ↑
- **Causes:** [Poor surface above or below supports](../defects/support-surface-quality.md) (#1; B)
<!-- /generated:relations -->
