---
type: cause
title: Layer height too small
description: A tiny gap under the nozzle restricts flow and makes extrusion uneven.
altLabel: [very low layer height, Schichthöhe zu klein]
facets: {phase: [extrusion]}
check: Extrusion evens out at a more typical layer height.
fixed_by:
  - {procedure: fundamentals/layer-height-extrusion-width, action: use a layer height suited to the nozzle, sets: [{key: layer_height, direction: up}]}
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
# Layer height too small

A tiny gap under the nozzle restricts flow and makes extrusion uneven. [^tsg-s3d]

**Check:** Extrusion evens out at a more typical layer height.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** [Layer height and extrusion width](../fundamentals/layer-height-extrusion-width.md) (use a layer height suited to the nozzle) `layer_height` ↑
- **Causes:** [Inconsistent extrusion](../defects/inconsistent-extrusion.md) (#3; B)
<!-- /generated:relations -->
