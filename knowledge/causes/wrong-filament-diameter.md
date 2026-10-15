---
type: cause
title: "Wrong filament diameter setting"
description: "The slicer computes volume from the configured diameter; a mismatch scales all extrusion."
altLabel: [filament diameter mismatch, falscher Filamentdurchmesser]
facets: {phase: [extrusion]}
check: "Measure the filament with calipers at several points and compare with the profile."
fixed_by:
  - {action: "set the measured diameter", sets: [{key: filament_diameter, direction: set}]}
sources:
  - id: tsg-s3d
    title: "Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)"
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-all3dp
    title: "All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)"
    resource: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - id: tsg-dataset
    title: "Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb"
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:55:00Z
status: stable
---
# Wrong filament diameter setting

The slicer computes volume from the configured diameter; a mismatch scales all extrusion.[^tsg-s3d]

**Check:** Measure the filament with calipers at several points and compare with the profile.[^tsg-all3dp]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (set the measured diameter) `filament_diameter` =
- **Causes:** [Over-extrusion](../defects/over-extrusion.md) (#4; B) · [Under-extrusion](../defects/under-extrusion.md) (#3; B)
<!-- /generated:relations -->
