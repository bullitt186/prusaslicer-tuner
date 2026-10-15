---
type: defect
title: Poor bed adhesion
description: Prints don't stick, corners lift, parts pop off mid-print.
timestamp: 2026-10-13
altLabel: [not sticking to the bed, first layer not sticking, haftet nicht, Betthaftung, print doesn't stick to bed]
facets: {phase: [first-layer]}
caused_by:
  - {cause: causes/contaminated-build-surface, rank: 1, evidence: B, source: [ellis-build-surface-adhesion, tsg-prusa, tsg-all3dp]}
  - {cause: causes/bed-temp-too-low, rank: 2, evidence: B, source: [ellis-build-surface-adhesion, tsg-s3d]}
  - {cause: causes/z-offset-too-high, rank: 3, evidence: B, source: [ellis-build-surface-adhesion, tsg-s3d, tsg-prusa, tsg-all3dp]}
  - {cause: causes/first-layer-lines-too-thin, rank: 4, evidence: B, source: ellis-build-surface-adhesion}
  - {cause: causes/unsuitable-build-surface, rank: 5, evidence: B, source: [ellis-build-surface-adhesion, tsg-s3d, tsg-prusa]}
  - {cause: causes/small-contact-area, rank: 6, evidence: B, source: [ellis-build-surface-adhesion, tsg-s3d]}
  - {cause: causes/bed-not-level-or-unmeshed, rank: 7, evidence: B, source: [tsg-s3d, tsg-prusa, tsg-all3dp]}
  - {cause: causes/first-layer-too-fast, rank: 8, evidence: B, source: tsg-s3d}
  - {cause: causes/excessive-cooling, rank: 9, evidence: B, source: tsg-s3d}
sources:
  - id: ellis-build-surface-adhesion
    title: Ellis Print Tuning Guide — Build surface adhesion
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/build_surface_adhesion.html
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
# Poor bed adhesion
1. Contaminated plate: wash it with dish soap (see [build surface](../tuning/build-surface.md)).
2. Bed temperature: PLA about 60, PETG about 80, ABS 90–100 °C (Voron 2.4 ABS about 110 because of the thick bed). Keys: `first_layer_bed_temperature`, `bed_temperature`.[^ellis-build-surface-adhesion]
3. Squish: see [first layer squish](../tuning/first-layer-squish.md).
4. Thin first-layer lines: `first_layer_extrusion_width` ≥ 120%.
5. Fake PEI or the wrong side of the plate.
6. Adhesives (Magigoo, Vision Miner Nano Polymer), `brim_width`, mouse ears.
7. PETG sticks **too** well to smooth PEI. Use a release agent (glue stick or textured plate).
Lifting over time is [warping](warping.md).

[^ellis-build-surface-adhesion]: Ellis Print Tuning Guide — Build surface adhesion

<!-- generated:relations -->
## Relations
- **Related:** [Print stuck to the bed](part-stuck-to-bed.md)
- **Caused by:** [Contaminated build surface](../causes/contaminated-build-surface.md) (#1; B) · [Bed temperature too low](../causes/bed-temp-too-low.md) (#2; B) · [Nozzle too far from the bed](../causes/z-offset-too-high.md) (#3; B) · [First-layer lines too thin](../causes/first-layer-lines-too-thin.md) (#4; B) · [Unsuitable build surface](../causes/unsuitable-build-surface.md) (#5; B) · [Small contact area](../causes/small-contact-area.md) (#6; B) · [Bed not level or mesh missing](../causes/bed-not-level-or-unmeshed.md) (#7; B) · [First layer printed too fast](../causes/first-layer-too-fast.md) (#8; B) · [Too much part cooling](../causes/excessive-cooling.md) (#9; B)
- **Linked from:** [Bulging](bulging.md) · [Warping / corner lifting](warping.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Build surface prep & handling](../tuning/build-surface.md) · [Cooling and layer times](../tuning/cooling-layer-times.md) · [First layer squish (Z offset)](../tuning/first-layer-squish.md)
<!-- /generated:relations -->
