---
type: defect
title: Model errors (non-manifold geometry)
description: Sections are missing or the print differs from the model although the printer works.
altLabel: [print looks wrong, Modellfehler]
facets: {phase: [model]}
caused_by:
  - {cause: causes/non-manifold-mesh, rank: 1, evidence: C, source: tsg-all3dp}
related: [defects/dimensional-inaccuracy]
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
# Model errors (non-manifold geometry)

Sections are missing or the print differs from the model although the printer works.

Check the slicer's repair warnings and layer preview; repair or boolean-merge overlapping bodies before slicing.[^tsg-all3dp]

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Caused by:** [Broken (non-manifold) model](../causes/non-manifold-mesh.md) (#1; C)
- **Related:** [Dimensional inaccuracy](dimensional-inaccuracy.md)
<!-- /generated:relations -->
