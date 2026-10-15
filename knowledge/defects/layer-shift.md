---
type: defect
title: Layer shifting
description: Horizontal offset between layers — belts, nozzle strikes on curled parts, current, drivers, too much accel.
timestamp: 2026-10-13
altLabel: [layer shifting, shifted layers, Schichtversatz, verschobene Schichten, layers don't line up, print leans, print offset in some places]
facets: {phase: [motion]}
caused_by:
  - {cause: causes/loose-mechanics, rank: 1, evidence: B, source: [ellis-layer-shifting, tsg-s3d, tsg-prusa, tsg-all3dp]}
  - {cause: causes/worn-or-binding-motion-parts, rank: 2, evidence: B, source: [ellis-layer-shifting, tsg-prusa, tsg-all3dp]}
  - {cause: causes/nozzle-strike-on-curled-part, rank: 3, evidence: B, source: [ellis-layer-shifting, tsg-prusa, tsg-all3dp]}
  - {cause: causes/stepper-driver-or-wiring, rank: 4, evidence: B, source: [ellis-layer-shifting, tsg-s3d]}
  - {cause: causes/acceleration-too-high, rank: 5, evidence: B, source: [ellis-layer-shifting, tsg-s3d]}
  - {cause: causes/print-speed-too-high, rank: 6, evidence: C, source: tsg-all3dp}
sources:
  - id: ellis-layer-shifting
    title: Ellis Print Tuning Guide — Layer shifting
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/layer_shifting.html
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-prusa
    title: Prusa Knowledge Base, print quality troubleshooting (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://help.prusa3d.com/category/print-quality-troubleshooting_225
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
# Layer shifting
- CoreXY: the shift direction identifies the A or B motor (seen from the front, B is left and A is right).
- Mechanical (most common): belt tension (X/Y about 120 Hz over 15 cm), belt routing and rubbing, binding bearings, poor motors, **nozzle hitting curled parts** (see [warping](warping.md) and [cooling](../tuning/cooling-layer-times.md)).
- Electrical: `run_current`, crimps, broken wire strands in drag chains, overheating drivers.
- Motion: accel or speed too high, so lower `max_accel`, use input shaper, and test with `TEST_SPEED`.
- Slicer: keep z-hop at 0.2–0.3 mm. `retract_lift` helps against nozzle strikes. Lower `travel_speed` and `travel_acceleration` (or `machine_max_acceleration_travel`).

<!-- generated:relations -->
## Relations
- **Caused by:** [Loose belts, pulleys or toolhead parts](../causes/loose-mechanics.md) (#1; B) · [Binding or worn bearings, rails or motors](../causes/worn-or-binding-motion-parts.md) (#2; B) · [Nozzle hits curled print](../causes/nozzle-strike-on-curled-part.md) (#3; B) · [Stepper driver or wiring fault](../causes/stepper-driver-or-wiring.md) (#4; B) · [Acceleration or corner velocity too high](../causes/acceleration-too-high.md) (#5; B) · [Print speed too high](../causes/print-speed-too-high.md) (#6; C)
- **Linked from:** [Warping / corner lifting](warping.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md)
<!-- /generated:relations -->
