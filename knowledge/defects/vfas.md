---
type: defect
title: VFAs (vertical fine artifacts)
description: Fine vertical lines on walls — belts/pulleys/idlers (2 mm spacing) or bearings/rails/motor drivers.
timestamp: 2026-10-13
altLabel: [vertical fine artifacts, vertical lines on walls, vertikale Linien]
facets: {phase: [mechanics]}
caused_by:
  - {cause: causes/belt-or-pulley-artifacts, rank: 1, evidence: B, source: ellis-vfas}
  - {cause: causes/worn-or-binding-motion-parts, rank: 2, evidence: B, source: ellis-vfas}
  - {cause: causes/stepper-driver-tuning, rank: 3, evidence: D, source: ellis-vfas}
sources:
  - id: ellis-vfas
    title: "Ellis Print Tuning Guide — VFAs"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/vfas.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# VFAs
- **~2 mm spacing:** belt, pulley or idler teeth. Tension A/B belts to about 110 Hz over 150 mm, fix belt rubbing and pulley height, clean the teeth, use genuine Gates parts.
- **Other spacing:** bearings, rails, motors. Print one square axis-aligned and one at 45° to isolate the axis (A/B vs X/Y).
- X/Y-only artifacts: motor driver tuning in Klipper (community TMC2209 values, e.g. `microsteps: 32`, `interpolate: false`, stealthChop off, `driver_TBL/TOFF/HEND/HSTRT`). Experimental.
- Slicer-side mitigations (general knowledge): change `external_perimeter_speed` to move the artifact frequency, and keep the outer wall speed constant.
Not a profile problem. Hand off to printer-side mechanical checks and firmware tooling.

<!-- generated:relations -->
## Relations
- **Caused by:** [Belt or pulley tooth artifacts](../causes/belt-or-pulley-artifacts.md) (#1; B) · [Binding or worn bearings, rails or motors](../causes/worn-or-binding-motion-parts.md) (#2; B) · [Stepper driver tuning artifacts](../causes/stepper-driver-tuning.md) (#3; D)
- **Related:** [Lines or ridges on the sides (Z banding)](z-banding.md)
- **Linked from:** [Extrusion patterns ("wood grain")](extrusion-patterns.md) · [Ringing / ghosting](ringing.md)
<!-- /generated:relations -->
