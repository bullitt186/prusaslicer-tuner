---
type: defect
title: Gaps or pillowing in top layers
description: Top surfaces show holes, bumps or gaps where solid layers sag into the infill.
altLabel: [gaps in top layers, pillowing, pits in top layer, gaps in floor corners, Löcher in der Deckschicht, Kissenbildung]
facets: {phase: [top-bottom]}
caused_by:
  - {cause: causes/top-layers-insufficient, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/infill-too-sparse, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/em-too-low, rank: 3, evidence: B, source: tsg-s3d}
  - {cause: causes/insufficient-cooling, rank: 4, evidence: C, source: tsg-all3dp}
  - {cause: causes/too-few-perimeters, rank: 5, evidence: B, source: tsg-s3d}
related: [defects/under-extrusion, defects/small-infill-overextruded]
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
# Gaps or pillowing in top layers

Top surfaces show holes, bumps or gaps where solid layers sag into the infill.

Solid top layers must bridge the infill. As a starting point the top shell should be at least ~0.5 mm thick, i.e. more layers at small layer heights; raise infill density if gaps persist; only then suspect under-extrusion.[^tsg-s3d] Pillowing also responds to stronger cooling on the top layers.[^tsg-all3dp] Gaps at floor corners where a part steps in need more perimeters.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Caused by:** [Too few top solid layers](../causes/top-layers-insufficient.md) (#1; B) · [Infill too sparse](../causes/infill-too-sparse.md) (#2; B) · [Extrusion multiplier too low](../causes/em-too-low.md) (#3; B) · [Insufficient part cooling](../causes/insufficient-cooling.md) (#4; C) · [Too few perimeters](../causes/too-few-perimeters.md) (#5; B)
- **Related:** [Small infill areas look overextruded](small-infill-overextruded.md) · [Under-extrusion](under-extrusion.md)
<!-- /generated:relations -->
