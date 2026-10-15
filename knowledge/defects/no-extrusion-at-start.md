---
type: defect
title: No extrusion at print start
description: Nothing or too little comes out during the first moves or layers.
altLabel: [not extruding at start of print, extrudiert nicht am Anfang]
facets: {phase: [first-layer]}
caused_by:
  - {cause: causes/extruder-not-primed, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/z-offset-too-low, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/extruder-gear-backlash-or-wear, rank: 3, evidence: B, source: tsg-s3d}
  - {cause: causes/partial-clog, rank: 4, evidence: B, source: tsg-s3d}
related: [defects/extruder-skipping, defects/extrusion-stops]
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
# No extrusion at print start

Nothing or too little comes out during the first moves or layers.

If extrusion only recovers around the 3rd–4th layer, the nozzle started too close to the bed and blocked the outlet; otherwise it oozed empty during heat-up and needs a skirt or purge line.[^tsg-s3d] Plastic shavings point to filament ground at the drive gear ([extruder skipping](extruder-skipping.md)).

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Related:** [Extrusion stops mid-print](extrusion-stops.md) · [Extruder skipping / clicking](extruder-skipping.md)
- **Caused by:** [Extruder not primed](../causes/extruder-not-primed.md) (#1; B) · [Nozzle too close to the bed](../causes/z-offset-too-low.md) (#2; B) · [Extruder gear backlash, play or wear](../causes/extruder-gear-backlash-or-wear.md) (#3; B) · [Partial clog](../causes/partial-clog.md) (#4; B)
<!-- /generated:relations -->
