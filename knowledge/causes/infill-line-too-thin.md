---
type: cause
title: Infill lines too thin
description: Thin infill lines make weak infill walls; wider lines are stronger at the same density.
altLabel: [infill extrusion width, Infill-Linien zu dünn]
facets: {phase: [infill]}
check: Infill strength improves with a wider infill extrusion width.
fixed_by:
  - {action: widen infill lines, sets: [{key: infill_extrusion_width, direction: up}]}
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
# Infill lines too thin

Thin infill lines make weak infill walls; wider lines are stronger at the same density. [^tsg-s3d]

**Check:** Infill strength improves with a wider infill extrusion width.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (widen infill lines) `infill_extrusion_width` ↑
- **Causes:** [Weak or messy infill](../defects/weak-infill.md) (#2; B)
<!-- /generated:relations -->
