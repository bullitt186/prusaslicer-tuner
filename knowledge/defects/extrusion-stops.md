---
type: defect
title: Extrusion stops mid-print
description: The print continues moving but no plastic comes out.
altLabel: [stops extruding mid print, Extrusion stoppt]
facets: {phase: [extrusion]}
caused_by:
  - {cause: causes/out-of-filament, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/partial-clog, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/extruder-gear-backlash-or-wear, rank: 3, evidence: B, source: tsg-s3d}
  - {cause: causes/stepper-driver-or-wiring, rank: 4, evidence: B, source: tsg-s3d}
  - {cause: causes/brittle-filament, rank: 5, evidence: C, source: tsg-all3dp}
  - {cause: causes/filament-tension-or-drag, rank: 6, evidence: C, source: tsg-all3dp}
related: [defects/extruder-skipping, defects/no-extrusion-at-start]
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
# Extrusion stops mid-print

The print continues moving but no plastic comes out.

Check the spool first. If the extruder motor turns but the filament does not move, the filament is ground. If the motor stops while X/Y keep moving, the extruder driver may have overheated and cut out.[^tsg-s3d] Snapped, brittle filament hides inside Bowden tubes.[^tsg-all3dp]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Caused by:** [Out of filament](../causes/out-of-filament.md) (#1; B) · [Partial clog](../causes/partial-clog.md) (#2; B) · [Extruder gear backlash, play or wear](../causes/extruder-gear-backlash-or-wear.md) (#3; B) · [Stepper driver or wiring fault](../causes/stepper-driver-or-wiring.md) (#4; B) · [Brittle filament snaps](../causes/brittle-filament.md) (#5; C) · [Filament tension or path drag](../causes/filament-tension-or-drag.md) (#6; C)
- **Related:** [Extruder skipping / clicking](extruder-skipping.md) · [No extrusion at print start](no-extrusion-at-start.md)
<!-- /generated:relations -->
