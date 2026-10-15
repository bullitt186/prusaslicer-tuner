---
type: cause
title: Travel moves too slow
description: Slow travel gives the nozzle more time to ooze over open space.
altLabel: [slow travel, Leerfahrt zu langsam]
facets: {phase: [retraction-travel]}
check: Stringing drops when travel speed rises (if the machine can handle it).
fixed_by:
  - {action: raise travel speed, sets: [{key: travel_speed, direction: up}]}
sources:
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-migration
  at: '2026-10-13T23:30:00Z'
status: stable
---
# Travel moves too slow

Slow travel gives the nozzle more time to ooze over open space. [^tsg-s3d]

**Check:** Stringing drops when travel speed rises (if the machine can handle it).

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (raise travel speed) `travel_speed` ↑
- **Causes:** [Stringing / oozing](../defects/stringing.md) (#10; B)
<!-- /generated:relations -->
