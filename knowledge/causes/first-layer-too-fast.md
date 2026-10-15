---
type: cause
title: First layer printed too fast
description: A fast first layer gets too little time to bond to the build surface.
altLabel: [erste Schicht zu schnell]
facets: {phase: [first-layer]}
check: Adhesion improves when the first layer runs at about half speed.
fixed_by:
  - {action: slow the first layer, sets: [{key: first_layer_speed, direction: down}]}
sources:
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-migration
  at: '2026-10-13T23:30:00Z'
status: stable
---
# First layer printed too fast

A fast first layer gets too little time to bond to the build surface. [^tsg-s3d]

**Check:** Adhesion improves when the first layer runs at about half speed.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (slow the first layer) `first_layer_speed` ↓
- **Causes:** [Poor bed adhesion](../defects/poor-bed-adhesion.md) (#8; B)
<!-- /generated:relations -->
