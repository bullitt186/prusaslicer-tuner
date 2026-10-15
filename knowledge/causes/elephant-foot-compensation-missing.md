---
type: cause
title: "No elephant-foot compensation"
description: "Some first-layer flare is inherent; without compensation the bottom stays wider than the wall."
altLabel: [Elefantenfuß-Kompensation fehlt]
facets: {phase: [first-layer]}
check: "Bottom edge wider than the wall even with correct squish."
fixed_by:
  - {action: "set elephant-foot compensation (or chamfer the model)", sets: [{key: elefant_foot_compensation, direction: up}]}
sources:
  - id: tsg-all3dp
    title: "All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)"
    resource: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - id: tsg-dataset
    title: "Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb"
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:55:00Z
status: stable
---
# No elephant-foot compensation

Some first-layer flare is inherent; without compensation the bottom stays wider than the wall.[^tsg-all3dp]

**Check:** Bottom edge wider than the wall even with correct squish.

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (set elephant-foot compensation (or chamfer the model)) `elefant_foot_compensation` ↑
- **Causes:** [Elephant foot](../defects/elephant-foot.md) (#3; C)
<!-- /generated:relations -->
