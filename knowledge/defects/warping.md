---
type: defect
title: Warping / corner lifting
description: Corners curl up during print, mainly ABS/ASA/PC/nylon; shrinkage stress beats adhesion.
timestamp: 2026-10-13
altLabel: [corner lifting, curling corners, Verzug, Ecken heben sich, print edges bending]
facets: {phase: [adhesion-warping]}
caused_by:
  - {cause: causes/chamber-too-cold, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/excessive-cooling, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/material-shrinkage, rank: 3, evidence: C}
  - {cause: causes/bed-temp-too-low, rank: 4, evidence: B, source: [tsg-s3d, tsg-all3dp]}
  - {cause: causes/small-contact-area, rank: 5, evidence: B, source: [tsg-s3d, tsg-all3dp]}
  - {cause: causes/unsuitable-build-surface, rank: 6, evidence: C, source: tsg-all3dp}
  - {cause: causes/bed-not-level-or-unmeshed, rank: 7, evidence: C, source: tsg-all3dp}
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
# Warping
Ellis covers this indirectly (see [cooling](../tuning/cooling-layer-times.md) and [adhesion](poor-bed-adhesion.md)). The rest is general knowledge.
- Adhesion first: [poor bed adhesion](poor-bed-adhesion.md).
- Enclosure and chamber: preheat or heat soak (`chamber_temperature`, `chamber_minimal_temperature` in the filament profile drive this in PrusaSlicer ≥ 2.8 when the printer supports it). Close the doors for ABS/ASA/PC.
- Less part cooling: lower `max_fan_speed` / `min_fan_speed`, and raise `disable_fan_first_layers`.
- `brim_width` 5–10 mm, or a mouse-ear brim. Rounded corners in the model.
- Higher `first_layer_bed_temperature` / `bed_temperature`.
- Curling can also cause nozzle strikes and [layer shifts](layer-shift.md).

## Related
- [ABS / ASA](../materials/asa-abs.md)
- [Nylon (PA)](../materials/nylon.md)
- [Engineering materials](../materials/engineering-materials.md)
- [Voron thermal and motion mechanics](../hardware/voron-thermal-mechanics.md)

<!-- generated:relations -->
## Relations
- **Caused by:** [Chamber too cold for the material](../causes/chamber-too-cold.md) (#1; B) · [Too much part cooling](../causes/excessive-cooling.md) (#2; B) · [Material shrinkage stress](../causes/material-shrinkage.md) (#3; C) · [Bed temperature too low](../causes/bed-temp-too-low.md) (#4; B) · [Small contact area](../causes/small-contact-area.md) (#5; B) · [Unsuitable build surface](../causes/unsuitable-build-surface.md) (#6; C) · [Bed not level or mesh missing](../causes/bed-not-level-or-unmeshed.md) (#7; C)
- **Materials prone to this:** [ABS / ASA](../materials/asa-abs.md) (B) · [Nylon (PA)](../materials/nylon.md) (C) · [PC / PC-CF](../materials/pc-cf.md) (C)
- **Linked from:** [Layer shifting](layer-shift.md) · [Poor bed adhesion](poor-bed-adhesion.md) · [FDM print defect diagnostic matrix](../troubleshooting/diagnostic-matrix.md) · [Cooling and layer times](../tuning/cooling-layer-times.md)
<!-- /generated:relations -->
