---
type: cause
title: Unsupported overhang or bridge
description: Overhangs and long bridges beyond the printer's ability need support or redesign.
altLabel: [no supports, fehlender Support]
facets: {phase: [supports-bridges]}
check: Failure only on steep overhangs or long spans.
fixed_by:
  - {action: enable supports or redesign/orient the part, sets: [{key: support_material, direction: enable}]}
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
# Unsupported overhang or bridge

Overhangs and long bridges beyond the printer's ability need support or redesign. [^tsg-s3d] [^tsg-all3dp]

**Check:** Failure only on steep overhangs or long spans.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (enable supports or redesign/orient the part) `support_material` on
- **Causes:** [Poor bridges & overhangs](../defects/bridging-overhangs.md) (#5; B)
<!-- /generated:relations -->
