---
type: defect
title: Print stuck to the bed
description: The finished part will not release from the build plate.
altLabel: [print welded to bed, PETG sticks too well, Druck klebt am Bett]
facets: {phase: [first-layer]}
caused_by:
  - {cause: causes/adhesion-too-strong, rank: 1, evidence: C, source: tsg-all3dp}
related: [defects/poor-bed-adhesion]
sources:
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
# Print stuck to the bed

The finished part will not release from the build plate.

Let the plate cool fully first; clean old glue build-up; for PETG on smooth PEI use a release agent or a textured sheet. Holes in large flat bases reduce suction.[^tsg-all3dp]

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Caused by:** [Adhesion too strong](../causes/adhesion-too-strong.md) (#1; C)
- **Related:** [Poor bed adhesion](poor-bed-adhesion.md)
- **Materials prone to this:** [PETG](../materials/petg.md) (B)
<!-- /generated:relations -->
