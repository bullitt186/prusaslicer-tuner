---
type: defect
title: Under-extrusion
description: Gaps between lines, thin/weak walls, missing layers, holes in top surfaces.
timestamp: 2026-10-13
altLabel: [underextrusion, gaps between lines, Unterextrusion, zu wenig Material, some layers missing, uniformly thin layers]
facets: {phase: [extrusion]}
caused_by:
  - {cause: causes/em-too-low, rank: 1, evidence: B, source: [tsg-s3d, tsg-all3dp]}
  - {cause: causes/extruder-not-calibrated, rank: 2, evidence: C}
  - {cause: causes/wrong-filament-diameter, rank: 3, evidence: B, source: [tsg-s3d, tsg-all3dp]}
  - {cause: causes/partial-clog, rank: 4, evidence: C, source: tsg-all3dp}
  - {cause: causes/volumetric-flow-exceeded, rank: 5, evidence: C}
  - {cause: causes/pa-too-high, rank: 6, evidence: C}
  - {cause: causes/z-offset-too-high, rank: 7, evidence: C}
  - {cause: causes/z-offset-too-low, rank: 8, evidence: B, source: tsg-s3d}
  - {cause: causes/nozzle-worn-or-leaking, rank: 9, evidence: B, source: tsg-s3d}
  - {cause: causes/extruder-gear-backlash-or-wear, rank: 10, evidence: B, source: tsg-s3d}
  - {cause: causes/heat-creep, rank: 11, evidence: B, source: tsg-s3d}
  - {cause: causes/poor-filament-quality, rank: 12, evidence: B, source: tsg-s3d}
  - {cause: causes/worn-or-binding-motion-parts, rank: 13, evidence: C, source: tsg-all3dp}
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
---
# Under-extrusion

Compiled from the related Ellis articles linked below, plus general knowledge.

## Distinguish the pattern
- **Everywhere, at all speeds:** EM too low, extruder not calibrated, wrong filament diameter, partial clog. See [EM](../tuning/extrusion-multiplier.md) and [extruder calibration](../tuning/extruder-calibration.md).
- **Only on fast sections or perimeters:** flow dropoff or the volumetric limit. See [max volumetric flow](../tuning/max-volumetric-flow.md). Lower `filament_max_volumetric_speed`, raise `temperature` by 5–10 °C, or slow down.
- **At line starts and corners:** PA too high, or retraction/deretract imbalance. See [pressure advance](../tuning/pressure-advance.md). Raise `retract_restart_extra` only as a last resort.
- **Clicking extruder or periodic gaps:** [extruder skipping](extruder-skipping.md).
- **Second layer gappy:** too little first-layer squish. See [first layer squish](../tuning/first-layer-squish.md).
- **Perimeters not bonding:** [perimeter separation](perimeter-separation.md).

## Keys
filament: `extrusion_multiplier`, `filament_diameter`, `temperature`, `filament_max_volumetric_speed` · print: `max_volumetric_speed`, `perimeter_speed`, `external_perimeter_speed`, `infill_speed`, `solid_infill_speed`

<!-- generated:relations -->
## Relations
- **Related:** [Inconsistent extrusion](inconsistent-extrusion.md) · [Gaps or pillowing in top layers](top-surface-gaps.md) · [Weak or messy infill](weak-infill.md)
- **Caused by:** [Extrusion multiplier too low](../causes/em-too-low.md) (#1; B) · [Extruder not calibrated](../causes/extruder-not-calibrated.md) (#2; C) · [Wrong filament diameter setting](../causes/wrong-filament-diameter.md) (#3; B) · [Partial clog](../causes/partial-clog.md) (#4; C) · [Volumetric flow above the hotend limit](../causes/volumetric-flow-exceeded.md) (#5; C) · [Pressure advance too high](../causes/pa-too-high.md) (#6; C) · [Nozzle too far from the bed](../causes/z-offset-too-high.md) (#7; C) · [Nozzle too close to the bed](../causes/z-offset-too-low.md) (#8; B) · [Worn, dirty or leaking nozzle](../causes/nozzle-worn-or-leaking.md) (#9; B) · [Extruder gear backlash, play or wear](../causes/extruder-gear-backlash-or-wear.md) (#10; B) · [Heat creep](../causes/heat-creep.md) (#11; B) · [Poor or degraded filament](../causes/poor-filament-quality.md) (#12; B) · [Binding or worn bearings, rails or motors](../causes/worn-or-binding-motion-parts.md) (#13; C)
- **Linked from:** [Poor layer adhesion](poor-layer-adhesion.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [FDM print defect diagnostic matrix](../troubleshooting/diagnostic-matrix.md) · [Extrusion multiplier (flow)](../tuning/extrusion-multiplier.md) · [Max volumetric flow](../tuning/max-volumetric-flow.md)
<!-- /generated:relations -->
