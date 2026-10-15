---
type: defect
title: Inconsistent extrusion
description: Line width varies along a single straight extrusion.
altLabel: [uneven extrusion, bumpy lines, ungleichmäßige Extrusion]
facets: {phase: [extrusion]}
caused_by:
  - {cause: causes/filament-tension-or-drag, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/partial-clog, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/layer-height-too-small, rank: 3, evidence: B, source: tsg-s3d}
  - {cause: causes/poor-filament-quality, rank: 4, evidence: B, source: tsg-s3d}
  - {cause: causes/extruder-gear-backlash-or-wear, rank: 5, evidence: B, source: tsg-s3d}
related: [defects/under-extrusion, defects/extrusion-patterns, defects/z-banding]
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
# Inconsistent extrusion

Line width varies along a single straight extrusion.

Watch a straight line being printed. Keep extrusion width within roughly 100–150 % of the nozzle as a rule of thumb; far below it the extruder cannot push a steady flow.[^tsg-s3d]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Caused by:** [Filament tension or path drag](../causes/filament-tension-or-drag.md) (#1; B) · [Partial clog](../causes/partial-clog.md) (#2; B) · [Layer height too small](../causes/layer-height-too-small.md) (#3; B) · [Poor or degraded filament](../causes/poor-filament-quality.md) (#4; B) · [Extruder gear backlash, play or wear](../causes/extruder-gear-backlash-or-wear.md) (#5; B)
- **Related:** [Extrusion patterns ("wood grain")](extrusion-patterns.md) · [Under-extrusion](under-extrusion.md) · [Lines or ridges on the sides (Z banding)](z-banding.md)
<!-- /generated:relations -->
