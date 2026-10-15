---
type: defect
title: Dimensional inaccuracy
description: Printed parts are larger or smaller than designed.
altLabel: [dimensional accuracy, wrong size, Maßhaltigkeit, Maße stimmen nicht]
facets: {phase: [model]}
caused_by:
  - {cause: causes/z-offset-too-low, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/em-too-high, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/em-too-low, rank: 3, evidence: B, source: tsg-s3d}
  - {cause: causes/shrinkage-uncompensated, rank: 4, evidence: B, source: tsg-s3d}
  - {cause: causes/loose-mechanics, rank: 5, evidence: C, source: tsg-all3dp}
related: [defects/thin-walls-and-small-features, defects/elephant-foot]
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
# Dimensional inaccuracy

Printed parts are larger or smaller than designed.

Measure away from the first 10–20 layers, which first-layer squish distorts. Then fix EM. A constant error is an XY offset; an error growing with size is shrinkage (e.g. 0.1 mm over 20 mm = 0.5 %).[^tsg-s3d]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Caused by:** [Nozzle too close to the bed](../causes/z-offset-too-low.md) (#1; B) · [Extrusion multiplier too high](../causes/em-too-high.md) (#2; B) · [Extrusion multiplier too low](../causes/em-too-low.md) (#3; B) · [Shrinkage not compensated](../causes/shrinkage-uncompensated.md) (#4; B) · [Loose belts, pulleys or toolhead parts](../causes/loose-mechanics.md) (#5; C)
- **Related:** [Elephant foot](elephant-foot.md) · [Thin walls and small features missing](thin-walls-and-small-features.md) · [Model errors (non-manifold geometry)](model-errors.md)
- **Linked from:** [ABS / ASA](../materials/asa-abs.md)
<!-- /generated:relations -->
