---
type: cause
title: Nozzle too large for the detail
description: Features smaller than the nozzle cannot be reproduced in XY.
altLabel: [nozzle diameter too big, Düse zu groß]
facets: {phase: [model]}
check: Missing features are thinner than the nozzle diameter.
fixed_by:
  - {procedure: hardware/nozzle-selection, action: use a smaller nozzle or thicken the features in CAD}
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
# Nozzle too large for the detail

Features smaller than the nozzle cannot be reproduced in XY. [^tsg-s3d] [^tsg-all3dp]

**Check:** Missing features are thinner than the nozzle diameter.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** [Nozzle selection](../hardware/nozzle-selection.md) (use a smaller nozzle or thicken the features in CAD)
- **Causes:** [Thin walls and small features missing](../defects/thin-walls-and-small-features.md) (#2; B)
<!-- /generated:relations -->
