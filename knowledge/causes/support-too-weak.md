---
type: cause
title: Supports too weak
description: Sparse or tall supports wobble, crack or detach mid-print.
altLabel: [support density too low, Support zu schwach]
facets: {phase: [supports-bridges]}
check: Supports look uneven or stringy before the overhang reaches them.
fixed_by:
  - {action: 'denser or stronger supports, brim, shorter supports', sets: [{key: support_material_spacing, direction: down}, {key: brim_width, direction: up}]}
sources:
  - id: tsg-all3dp
    title: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-migration
  at: '2026-10-13T23:30:00Z'
status: stable
---
# Supports too weak

Sparse or tall supports wobble, crack or detach mid-print. [^tsg-all3dp]

**Check:** Supports look uneven or stringy before the overhang reaches them.

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (denser or stronger supports, brim, shorter supports) `support_material_spacing` ↓ `brim_width` ↑
- **Causes:** [Supports fail during the print](../defects/supports-fail.md) (#1; C)
<!-- /generated:relations -->
