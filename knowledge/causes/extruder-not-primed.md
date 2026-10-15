---
type: cause
title: Extruder not primed
description: During heat-up the nozzle oozes empty, so the first moves extrude nothing until pressure rebuilds.
altLabel: [nozzle not primed, Düse nicht vorgefüllt]
facets: {phase: [first-layer]}
check: Extrusion starts a few seconds late or only after the skirt.
fixed_by:
  - {action: print a skirt or purge line before the part; add skirt loops if needed, sets: [{key: skirts, direction: up}]}
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
# Extruder not primed

During heat-up the nozzle oozes empty, so the first moves extrude nothing until pressure rebuilds. [^tsg-s3d]

**Check:** Extrusion starts a few seconds late or only after the skirt.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (print a skirt or purge line before the part; add skirt loops if needed) `skirts` ↑
- **Causes:** [No extrusion at print start](../defects/no-extrusion-at-start.md) (#1; B)
<!-- /generated:relations -->
