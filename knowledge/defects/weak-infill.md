---
type: defect
title: Weak or messy infill
description: Infill is stringy, incomplete or fails to support the surfaces above.
altLabel: [infill messy and incomplete, stringy infill, schwaches Infill]
facets: {phase: [infill]}
caused_by:
  - {cause: causes/infill-too-fast, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/infill-line-too-thin, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/infill-too-sparse, rank: 3, evidence: C, source: tsg-all3dp}
  - {cause: causes/partial-clog, rank: 4, evidence: C, source: tsg-all3dp}
related: [defects/under-extrusion, defects/infill-wall-gaps]
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
# Weak or messy infill

Infill is stringy, incomplete or fails to support the surfaces above.

Infill runs fastest and under-extrudes first; slow it down or widen infill lines (a wider line at the same density is stronger), and choose a stronger pattern.[^tsg-s3d]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Related:** [Gaps between infill and walls](infill-wall-gaps.md) · [Under-extrusion](under-extrusion.md)
- **Caused by:** [Infill printed too fast](../causes/infill-too-fast.md) (#1; B) · [Infill lines too thin](../causes/infill-line-too-thin.md) (#2; B) · [Infill too sparse](../causes/infill-too-sparse.md) (#3; C) · [Partial clog](../causes/partial-clog.md) (#4; C)
<!-- /generated:relations -->
