---
type: cause
title: "Bed temperature too high"
description: "Lower layers stay soft and sag under the weight of the part."
altLabel: [Bett zu heiß, Druckbett zu heiß]
facets: {phase: [first-layer]}
check: "Bottom flare shrinks with a cooler bed (5 °C steps as a starting value)."
fixed_by:
  - {action: "lower bed temperature by 5 °C steps", sets: [{key: first_layer_bed_temperature, direction: down}, {key: bed_temperature, direction: down}]}
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
# Bed temperature too high

Lower layers stay soft and sag under the weight of the part.[^tsg-all3dp]

**Check:** Bottom flare shrinks with a cooler bed (5 °C steps as a starting value).

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (lower bed temperature by 5 °C steps) `first_layer_bed_temperature` ↓ `bed_temperature` ↓
- **Causes:** [Elephant foot](../defects/elephant-foot.md) (#2; C) · [First layer inconsistency](../defects/first-layer-inconsistency.md) (#4; C)
<!-- /generated:relations -->
