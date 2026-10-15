---
type: cause
title: "Chamber too cold for the material"
description: "Shrinking materials (ABS, ASA, PC, PA) build stress against a cool chamber and lift or crack."
altLabel: [no heat soak, Bauraum zu kalt, kein Heat Soak]
facets: {phase: [adhesion-warping]}
check: "Warping drops with an enclosed, heat-soaked chamber."
fixed_by:
  - {procedure: hardware/voron-thermal-mechanics, action: "enclose and heat soak", sets: [{key: chamber_temperature, direction: up}]}
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
# Chamber too cold for the material

Shrinking materials (ABS, ASA, PC, PA) build stress against a cool chamber and lift or crack.[^prusa-warping]

**Check:** Warping drops with an enclosed, heat-soaked chamber.[^tsg-s3d]

[^prusa-warping]: Prusa Knowledge Base — Warping
[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** [Voron thermal and motion mechanics](../hardware/voron-thermal-mechanics.md) (enclose and heat soak) `chamber_temperature` ↑
- **Causes:** [Warping / corner lifting](../defects/warping.md) (#1; B)
<!-- /generated:relations -->
