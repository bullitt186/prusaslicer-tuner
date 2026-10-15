---
type: cause
title: No z-hop over printed surfaces
description: Without a small lift the nozzle drags across finished top layers during travel.
altLabel: [nozzle drags on top, kein Z-Hop]
facets: {phase: [retraction-travel]}
check: Scars follow travel paths over top surfaces.
fixed_by:
  - {action: enable a small lift on retraction, sets: [{key: retract_lift, direction: up}, {key: filament_retract_lift, direction: up}]}
sources:
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
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
# No z-hop over printed surfaces

Without a small lift the nozzle drags across finished top layers during travel. [^tsg-s3d] [^tsg-all3dp]

**Check:** Scars follow travel paths over top surfaces.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (enable a small lift on retraction) `retract_lift` ↑ `filament_retract_lift` ↑
- **Causes:** [Scars on top surfaces](../defects/top-surface-scars.md) (#2; B)
<!-- /generated:relations -->
