---
type: defect
title: Over-extrusion
description: Rough/ridged top surfaces, blobby small areas, dimensional oversize, nozzle dragging through top layers.
timestamp: 2026-10-13
altLabel: [overextrusion, Überextrusion, zu viel Material, stringy and droopy]
facets: {phase: [extrusion]}
caused_by:
  - {cause: causes/em-too-high, rank: 1, evidence: B, source: [tsg-s3d, tsg-all3dp]}
  - {cause: causes/z-offset-too-low, rank: 2, evidence: C}
  - {cause: causes/pa-too-low, rank: 3, evidence: C}
  - {cause: causes/wrong-filament-diameter, rank: 4, evidence: B, source: tsg-s3d}
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
# Over-extrusion

- Check `extrusion_multiplier` first, following the [EM procedure](../tuning/extrusion-multiplier.md). Small top islands always look a little overextruded (see [small infill areas](small-infill-overextruded.md)), so judge the widest areas.
- A first layer squished too much carries up through the solid layers.
- Bulges at corners only point to PA too low (see [pressure advance](../tuning/pressure-advance.md)), not to EM.
- Oversize holes and walls: tune EM first, then `filament_shrinkage_compensation_xy`. Use `xy_size_compensation` only for holes.
Related: [bulging](bulging.md).

<!-- generated:relations -->
## Relations
- **Caused by:** [Extrusion multiplier too high](../causes/em-too-high.md) (#1; B) · [Nozzle too close to the bed](../causes/z-offset-too-low.md) (#2; C) · [Pressure advance too low](../causes/pa-too-low.md) (#3; C) · [Wrong filament diameter setting](../causes/wrong-filament-diameter.md) (#4; B)
- **Related:** [Scars on top surfaces](top-surface-scars.md)
- **Linked from:** [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Extrusion multiplier (flow)](../tuning/extrusion-multiplier.md)
<!-- /generated:relations -->
