---
type: defect
title: Supports fail during the print
description: Support structures crack, wobble or detach before the overhang is printed.
altLabel: [supports fell apart, Support bricht ab]
facets: {phase: [supports-bridges]}
caused_by:
  - {cause: causes/support-too-weak, rank: 1, evidence: C, source: tsg-all3dp}
  - {cause: causes/small-contact-area, rank: 2, evidence: C, source: tsg-all3dp}
  - {cause: causes/brittle-filament, rank: 3, evidence: C, source: tsg-all3dp}
  - {cause: causes/loose-mechanics, rank: 4, evidence: C, source: tsg-all3dp}
related: [defects/support-surface-quality]
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
# Supports fail during the print

Support structures crack, wobble or detach before the overhang is printed.

Choose a sturdier support pattern for tall or low-contact supports, add a brim, and raise density only as a last resort because it makes removal harder.[^tsg-all3dp]

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Related:** [Poor surface above or below supports](support-surface-quality.md)
- **Caused by:** [Supports too weak](../causes/support-too-weak.md) (#1; C) · [Small contact area](../causes/small-contact-area.md) (#2; C) · [Brittle filament snaps](../causes/brittle-filament.md) (#3; C) · [Loose belts, pulleys or toolhead parts](../causes/loose-mechanics.md) (#4; C)
<!-- /generated:relations -->
