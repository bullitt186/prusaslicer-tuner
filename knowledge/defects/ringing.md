---
type: defect
title: Ringing / ghosting
description: Echo ripples after sharp corners or features on walls.
timestamp: 2026-10-13
altLabel: [ghosting, echoes, rippling, Geisterbilder, Ringing, vibrations]
facets: {phase: [motion]}
caused_by:
  - {cause: causes/resonance-uncompensated, rank: 1, evidence: C}
  - {cause: causes/loose-mechanics, rank: 2, evidence: B, source: [tsg-s3d, tsg-all3dp]}
  - {cause: causes/acceleration-too-high, rank: 3, evidence: B, source: [tsg-s3d, tsg-all3dp]}
  - {cause: causes/print-speed-too-high, rank: 4, evidence: B, source: tsg-s3d}
  - {cause: causes/worn-or-binding-motion-parts, rank: 5, evidence: C, source: tsg-all3dp}
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
# Ringing / ghosting
General knowledge; Ellis has no dedicated article.
- Klipper printers: run input shaper calibration (`SHAPER_CALIBRATE` with an ADXL; both Vorons have one), check belt tension, and look for loose parts on the toolhead.
- Slicer: lower `external_perimeter_acceleration` / `perimeter_acceleration` and `external_perimeter_speed`. Check `machine_max_acceleration_extruding` (only enforced when `machine_limits_usage` emits it).
- Different from [VFAs](vfas.md), which have fixed spacing and no decay.

<!-- generated:relations -->
## Relations
- **Caused by:** [Resonance not compensated](../causes/resonance-uncompensated.md) (#1; C) · [Loose belts, pulleys or toolhead parts](../causes/loose-mechanics.md) (#2; B) · [Acceleration or corner velocity too high](../causes/acceleration-too-high.md) (#3; B) · [Print speed too high](../causes/print-speed-too-high.md) (#4; B) · [Binding or worn bearings, rails or motors](../causes/worn-or-binding-motion-parts.md) (#5; C)
- **Linked from:** [Lines or ridges on the sides (Z banding)](z-banding.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [FDM print defect diagnostic matrix](../troubleshooting/diagnostic-matrix.md)
<!-- /generated:relations -->
