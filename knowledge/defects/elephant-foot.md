---
type: defect
title: Elephant foot
description: Bottom layers flare outward beyond the wall line.
timestamp: 2026-10-13
altLabel: [elephants foot, bottom flare, Elefantenfuß, print bows out at bottom]
facets: {phase: [first-layer]}
caused_by:
  - {cause: causes/z-offset-too-low, rank: 1, evidence: C, source: tsg-all3dp}
  - {cause: causes/bed-temp-too-high, rank: 2, evidence: C, source: tsg-all3dp}
  - {cause: causes/elephant-foot-compensation-missing, rank: 3, evidence: C, source: tsg-all3dp}
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
---
# Elephant foot
- Cause: too much first-layer squish, a bed that's too hot (the lower layers sag), or a wide first-layer line.
- Fix: check [squish](../tuning/first-layer-squish.md), lower `first_layer_bed_temperature` / `bed_temperature` by 5 °C, and set `elefant_foot_compensation` (print, typically 0.1–0.2 mm). Too much compensation causes [perimeter separation](perimeter-separation.md) in the bottom layers. A chamfer in the model is the clean alternative.

<!-- generated:relations -->
## Relations
- **Related:** [Dimensional inaccuracy](dimensional-inaccuracy.md)
- **Caused by:** [Nozzle too close to the bed](../causes/z-offset-too-low.md) (#1; C) · [Bed temperature too high](../causes/bed-temp-too-high.md) (#2; C) · [No elephant-foot compensation](../causes/elephant-foot-compensation-missing.md) (#3; C)
- **Linked from:** [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [First layer squish (Z offset)](../tuning/first-layer-squish.md)
<!-- /generated:relations -->
