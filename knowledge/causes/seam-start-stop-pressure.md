---
type: cause
title: "Seam start/stop pressure"
description: "Pressure at loop starts and ends leaves a zit; extra restart or no wipe makes it worse."
altLabel: [seam blob, restart extra, Naht-Blob]
facets: {phase: [walls-seams]}
check: "Observe one perimeter: the blob is at the start or the end of the loop."
fixed_by:
  - {procedure: tuning/pressure-advance, action: "tune PA first, then restart/wipe", sets: [{key: retract_restart_extra, direction: down}, {key: wipe, direction: enable}, {key: filament_wipe, direction: enable}]}
sources:
  - id: tsg-s3d
    title: "Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)"
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-dataset
    title: "Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb"
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:55:00Z
status: stable
---
# Seam start/stop pressure

Pressure at loop starts and ends leaves a zit; extra restart or no wipe makes it worse.[^tsg-s3d]

**Check:** Observe one perimeter: the blob is at the start or the end of the loop.[^tsg-s3d]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** [Pressure advance / Linear advance](../tuning/pressure-advance.md) (tune PA first, then restart/wipe) `retract_restart_extra` ↓ `wipe` on `filament_wipe` on
- **Causes:** [Zits, blobs & visible seam](../defects/zits-blobs.md) (#2; B)
<!-- /generated:relations -->
