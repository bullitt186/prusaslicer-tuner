---
type: cause
title: Layer height too large for the nozzle
description: Each layer must be pressed onto the one below; above about 80 % of the nozzle diameter it is not.
altLabel: [layer too thick, Schichthöhe zu groß]
facets: {phase: [extrusion]}
check: Layer separation disappears with layer height ≤ ~80 % of nozzle diameter.
fixed_by:
  - {procedure: fundamentals/layer-height-extrusion-width, action: reduce layer height relative to the nozzle, sets: [{key: layer_height, direction: down}]}
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
# Layer height too large for the nozzle

Each layer must be pressed onto the one below; above about 80 % of the nozzle diameter it is not. [^tsg-s3d]

**Check:** Layer separation disappears with layer height ≤ ~80 % of nozzle diameter.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** [Layer height and extrusion width](../fundamentals/layer-height-extrusion-width.md) (reduce layer height relative to the nozzle) `layer_height` ↓
- **Causes:** [Poor layer adhesion](../defects/poor-layer-adhesion.md) (#7; B) · [Poor surface above or below supports](../defects/support-surface-quality.md) (#2; B)
<!-- /generated:relations -->
