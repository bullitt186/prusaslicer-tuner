---
type: defect
title: Lines or ridges on the sides (Z banding)
description: Individual layers stand out as lines, often in a repeating pattern.
altLabel: [lines on the side of print, horizontal lines, Z-Banding, Querrillen]
facets: {phase: [extrusion]}
caused_by:
  - {cause: causes/poor-filament-quality, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/temperature-fluctuation, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/worn-or-binding-motion-parts, rank: 3, evidence: B, source: tsg-s3d}
  - {cause: causes/filament-tension-or-drag, rank: 4, evidence: B, source: tsg-s3d}
related: [defects/vfas, defects/inconsistent-extrusion]
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
# Lines or ridges on the sides (Z banding)

Individual layers stand out as lines, often in a repeating pattern.

A 5 % diameter variation can change line width by up to about 0.05 mm; a cyclic temperature swing beyond about ±2 °C or Z-axis wobble/backlash also prints as periodic ridges.[^tsg-s3d] Different from [VFAs](vfas.md) (vertical) and [ringing](ringing.md).

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Related:** [Inconsistent extrusion](inconsistent-extrusion.md) · [VFAs (vertical fine artifacts)](vfas.md)
- **Caused by:** [Poor or degraded filament](../causes/poor-filament-quality.md) (#1; B) · [Hotend temperature fluctuation](../causes/temperature-fluctuation.md) (#2; B) · [Binding or worn bearings, rails or motors](../causes/worn-or-binding-motion-parts.md) (#3; B) · [Filament tension or path drag](../causes/filament-tension-or-drag.md) (#4; B)
<!-- /generated:relations -->
