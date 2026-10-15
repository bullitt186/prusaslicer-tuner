---
type: defect
title: Scars on top surfaces
description: Travel moves leave marks across top layers.
altLabel: [diagonal scars, nozzle drag marks, Kratzer auf der Oberfläche]
facets: {phase: [top-bottom]}
caused_by:
  - {cause: causes/em-too-high, rank: 1, evidence: B, source: tsg-s3d}
  - {cause: causes/no-z-hop, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/travel-over-open-space, rank: 3, evidence: C, source: tsg-all3dp}
  - {cause: causes/nozzle-temp-too-high, rank: 4, evidence: C, source: tsg-all3dp}
related: [defects/over-extrusion, defects/stringing]
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
# Scars on top surfaces

Travel moves leave marks across top layers.

Check for over-extrusion first; then use a small z-hop. Retraction-triggered lifts only happen when a retraction happens.[^tsg-s3d]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Caused by:** [Extrusion multiplier too high](../causes/em-too-high.md) (#1; B) · [No z-hop over printed surfaces](../causes/no-z-hop.md) (#2; B) · [Travel crosses open air](../causes/travel-over-open-space.md) (#3; C) · [Nozzle temperature too high](../causes/nozzle-temp-too-high.md) (#4; C)
- **Related:** [Over-extrusion](over-extrusion.md) · [Stringing / oozing](stringing.md)
<!-- /generated:relations -->
