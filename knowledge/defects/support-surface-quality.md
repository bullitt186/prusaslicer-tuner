---
type: defect
title: Poor surface above or below supports
description: Surfaces resting on supports droop, or supports leave scars when removed.
altLabel: [poor surface above supports, rough surface beneath supports, Support-Oberfläche rau]
facets: {phase: [supports-bridges]}
caused_by:
  - {cause: causes/support-interface-settings, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/layer-height-too-large, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/nozzle-temp-too-high, rank: 3, evidence: C, source: tsg-all3dp}
related: [defects/supports-fail, defects/bridging-overhangs]
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
# Poor surface above or below supports

Surfaces resting on supports droop, or supports leave scars when removed.

Lower layer heights improve overhangs; support density around 20–40 % is a common starting range; 1–2 empty layers and an XY offset around 0.2–0.4 mm are typical starting values for same-material supports, less with a soluble interface.[^tsg-s3d]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Caused by:** [Support interface or gap wrong](../causes/support-interface-settings.md) (#1; B) · [Layer height too large for the nozzle](../causes/layer-height-too-large.md) (#2; B) · [Nozzle temperature too high](../causes/nozzle-temp-too-high.md) (#3; C)
- **Related:** [Poor bridges & overhangs](bridging-overhangs.md) · [Supports fail during the print](supports-fail.md)
<!-- /generated:relations -->
