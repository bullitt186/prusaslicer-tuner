---
type: cause
title: "Material shrinkage stress"
description: "Cooling plastic contracts; in high-shrink materials the stress beats bed adhesion at sharp corners."
altLabel: [thermal contraction, Schrumpfung]
facets: {phase: [adhesion-warping]}
check: "Lifting starts at sharp corners and grows with part size."
fixed_by:
  - {action: "brim or mouse ears, rounded corners in the model", sets: [{key: brim_width, direction: up}]}
sources:
  - id: tsg-s3d
    title: "Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)"
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: prusa-warping
    title: "Prusa Knowledge Base — Warping"
    resource: https://help.prusa3d.com/article/warping_2011
  - id: tsg-dataset
    title: "Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb"
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:55:00Z
status: stable
---
# Material shrinkage stress

Cooling plastic contracts; in high-shrink materials the stress beats bed adhesion at sharp corners.[^tsg-s3d]

**Check:** Lifting starts at sharp corners and grows with part size.[^prusa-warping]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^prusa-warping]: Prusa Knowledge Base — Warping

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (brim or mouse ears, rounded corners in the model) `brim_width` ↑
- **Causes:** [Warping / corner lifting](../defects/warping.md) (#3; C)
<!-- /generated:relations -->
