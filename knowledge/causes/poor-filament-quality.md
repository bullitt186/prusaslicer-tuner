---
type: cause
title: Poor or degraded filament
description: Diameter variation, additives or aged material change the extruded volume from layer to layer.
altLabel: [cheap filament, diameter variation, schlechtes Filament, Filament-Toleranz]
facets: {phase: [material-handling]}
check: Measure diameter along the spool; compare with a fresh high-quality spool.
fixed_by:
  - {action: 'swap to a fresh, tightly toleranced spool; store filament dry'}
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
# Poor or degraded filament

Diameter variation, additives or aged material change the extruded volume from layer to layer. [^tsg-s3d]

**Check:** Measure diameter along the spool; compare with a fresh high-quality spool.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (swap to a fresh, tightly toleranced spool; store filament dry)
- **Causes:** [Inconsistent extrusion](../defects/inconsistent-extrusion.md) (#4; B) · [Under-extrusion](../defects/under-extrusion.md) (#12; B) · [Lines or ridges on the sides (Z banding)](../defects/z-banding.md) (#1; B)
<!-- /generated:relations -->
