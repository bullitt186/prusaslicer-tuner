---
type: cause
title: Adhesion too strong
description: Large contact areas, glue build-up or materials like PETG on smooth PEI bond too well.
altLabel: [print stuck to bed, Druck klebt fest]
facets: {phase: [first-layer]}
check: The part releases only after full cooling or with a release agent.
fixed_by:
  - {procedure: tuning/build-surface, action: 'let it cool, use a release agent or textured sheet, clean old glue'}
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
# Adhesion too strong

Large contact areas, glue build-up or materials like PETG on smooth PEI bond too well. [^tsg-all3dp]

**Check:** The part releases only after full cooling or with a release agent.

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** [Build surface prep & handling](../tuning/build-surface.md) (let it cool, use a release agent or textured sheet, clean old glue)
- **Causes:** [Print stuck to the bed](../defects/part-stuck-to-bed.md) (#1; C)
<!-- /generated:relations -->
