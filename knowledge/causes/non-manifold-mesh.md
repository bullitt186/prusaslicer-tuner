---
type: cause
title: Broken (non-manifold) model
description: Intersecting or open meshes slice into missing or wrong regions.
altLabel: [non-manifold edges, defektes Modell, kaputtes STL]
facets: {phase: [model]}
check: The slicer warns about errors, or the layer preview differs from the model.
fixed_by:
  - {action: 'repair the mesh (slicer repair, Meshmixer, Blender) or merge bodies with a boolean'}
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
# Broken (non-manifold) model

Intersecting or open meshes slice into missing or wrong regions. [^tsg-all3dp]

**Check:** The slicer warns about errors, or the layer preview differs from the model.

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (repair the mesh (slicer repair, Meshmixer, Blender) or merge bodies with a boolean)
- **Causes:** [Model errors (non-manifold geometry)](../defects/model-errors.md) (#1; C)
<!-- /generated:relations -->
