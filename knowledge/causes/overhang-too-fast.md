---
type: cause
title: "Overhangs printed too fast"
description: "Fast overhangs do not get enough time to cool."
altLabel: [overhang speed, Überhang zu schnell]
facets: {phase: [supports-bridges]}
check: "Overhang quality improves with dynamic overhang speeds."
fixed_by:
  - {action: "enable dynamic overhang speeds", sets: [{key: enable_dynamic_overhang_speeds, direction: enable}]}
sources:
  - id: tsg-all3dp
    title: "All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)"
    resource: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - id: orca-source
    title: "OrcaSlicer source (overhang speed settings), commit 869e450"
    resource: https://github.com/SoftFever/OrcaSlicer/commit/869e450981bb8bece1622ef3fd55381962af11b3
  - id: tsg-dataset
    title: "Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb"
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:55:00Z
status: stable
---
# Overhangs printed too fast

Fast overhangs do not get enough time to cool.[^tsg-all3dp]

**Check:** Overhang quality improves with dynamic overhang speeds.[^orca-source]

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)
[^orca-source]: OrcaSlicer source (overhang speed settings), commit 869e450

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (enable dynamic overhang speeds) `enable_dynamic_overhang_speeds` on
- **Causes:** [Poor bridges & overhangs](../defects/bridging-overhangs.md) (#3; C)
<!-- /generated:relations -->
