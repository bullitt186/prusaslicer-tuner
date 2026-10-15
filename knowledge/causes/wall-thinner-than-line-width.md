---
type: cause
title: Wall thinner than the extrusion width
description: Walls only a few line widths thick leave gaps, or vanish below one line width.
altLabel: [thin wall, Wand dünner als Linienbreite]
facets: {phase: [walls-seams]}
check: Preview shows gaps or missing thin features.
fixed_by:
  - {procedure: fundamentals/layer-height-extrusion-width, action: enable thin-wall handling or adjust line width to fit the wall, sets: [{key: thin_walls, direction: enable}, {key: extrusion_width, direction: set}]}
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
# Wall thinner than the extrusion width

Walls only a few line widths thick leave gaps, or vanish below one line width. [^tsg-s3d]

**Check:** Preview shows gaps or missing thin features.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** [Layer height and extrusion width](../fundamentals/layer-height-extrusion-width.md) (enable thin-wall handling or adjust line width to fit the wall) `thin_walls` on `extrusion_width` =
- **Causes:** [Thin walls and small features missing](../defects/thin-walls-and-small-features.md) (#1; B)
<!-- /generated:relations -->
