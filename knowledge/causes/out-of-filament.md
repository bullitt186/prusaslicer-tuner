---
type: cause
title: Out of filament
description: The spool ran out or the filament end left the extruder.
altLabel: [empty spool, Filament leer, Spule leer]
facets: {phase: [material-handling]}
check: Check the spool and the filament path to the nozzle.
fixed_by:
  - {action: load a new spool; use a runout sensor if available}
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
# Out of filament

The spool ran out or the filament end left the extruder. [^tsg-s3d] [^tsg-all3dp]

**Check:** Check the spool and the filament path to the nozzle.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (load a new spool; use a runout sensor if available)
- **Causes:** [Extrusion stops mid-print](../defects/extrusion-stops.md) (#1; B)
<!-- /generated:relations -->
