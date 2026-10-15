---
type: defect
title: Extruder skipping / clicking
description: Wide periodic gaps, clicking extruder; clogs, heat creep, tension, flow above limit, current.
timestamp: 2026-10-13
altLabel: [extruder clicking, grinding filament, Extruder klickt, Extruder rutscht durch, stripped filament]
facets: {phase: [extrusion]}
caused_by:
  - {cause: causes/partial-clog, rank: 1, evidence: B, source: [ellis-extruder-skipping, tsg-s3d]}
  - {cause: causes/heat-creep, rank: 2, evidence: B, source: ellis-extruder-skipping}
  - {cause: causes/filament-tension-or-drag, rank: 3, evidence: B, source: [ellis-extruder-skipping, tsg-all3dp]}
  - {cause: causes/retraction-excessive, rank: 4, evidence: B, source: [ellis-extruder-skipping, tsg-s3d]}
  - {cause: causes/extruder-motor-current, rank: 5, evidence: B, source: ellis-extruder-skipping}
  - {cause: causes/volumetric-flow-exceeded, rank: 6, evidence: B, source: [ellis-extruder-skipping, tsg-s3d]}
  - {cause: causes/nozzle-temp-too-low, rank: 7, evidence: B, source: [ellis-extruder-skipping, tsg-s3d, tsg-all3dp]}
  - {cause: causes/stepper-driver-or-wiring, rank: 8, evidence: B, source: ellis-extruder-skipping}
  - {cause: causes/z-offset-too-low, rank: 9, evidence: B, source: ellis-extruder-skipping}
sources:
  - id: ellis-extruder-skipping
    title: Ellis Print Tuning Guide — Extruder skipping
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
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
  at: 2026-10-13 23:00:00+00:00
---
# Extruder skipping
Mark the motor shaft: shuddering points to wiring or resistance, no movement to electrical or driver heat, normal rotation to a grip problem or loose grub screw.
In order of likelihood: partial clog (nozzle or heatbreak); enclosure heat with PLA; filament tension; too much retraction (direct drive ≤ about 1 mm); motor current (≤ 50–60% of rated); **volumetric flow above the hotend limit** (`filament_max_volumetric_speed`; see [max volumetric flow](../tuning/max-volumetric-flow.md)); spool or PTFE drag; hotend fan not at 100%; thermistor type or temperature too low; wiring; driver settings; skipping only on the first layer means too much squish.[^ellis-extruder-skipping]

[^ellis-extruder-skipping]: Ellis Print Tuning Guide — Extruder skipping

<!-- generated:relations -->
## Relations
- **Caused by:** [Partial clog](../causes/partial-clog.md) (#1; B) · [Heat creep](../causes/heat-creep.md) (#2; B) · [Filament tension or path drag](../causes/filament-tension-or-drag.md) (#3; B) · [Retraction too long or too fast](../causes/retraction-excessive.md) (#4; B) · [Extruder motor current wrong](../causes/extruder-motor-current.md) (#5; B) · [Volumetric flow above the hotend limit](../causes/volumetric-flow-exceeded.md) (#6; B) · [Nozzle temperature too low](../causes/nozzle-temp-too-low.md) (#7; B) · [Stepper driver or wiring fault](../causes/stepper-driver-or-wiring.md) (#8; B) · [Nozzle too close to the bed](../causes/z-offset-too-low.md) (#9; B)
- **Related:** [Extrusion stops mid-print](extrusion-stops.md) · [No extrusion at print start](no-extrusion-at-start.md)
- **Materials prone to this:** [PLA](../materials/pla.md) (B) · [TPU (flexible)](../materials/tpu.md) (C)
- **Linked from:** [Overheating (esp. PLA in enclosures)](overheating.md) · [Under-extrusion](under-extrusion.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Extruder calibration (rotation_distance / e-steps)](../tuning/extruder-calibration.md) · [Max volumetric flow](../tuning/max-volumetric-flow.md)
<!-- /generated:relations -->
