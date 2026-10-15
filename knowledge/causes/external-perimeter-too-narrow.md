---
type: cause
title: "External perimeter too narrow"
description: "With layer heights above about half the nozzle size, a narrow outer line cannot reach the neighbouring perimeter."
altLabel: [outer wall too thin, Außenwand zu schmal]
facets: {phase: [walls-seams]}
check: "Gaps between outer and inner wall everywhere; layer height > 50 % of the nozzle."
fixed_by:
  - {procedure: fundamentals/layer-height-extrusion-width, action: "widen the external perimeter", sets: [{key: external_perimeter_extrusion_width, direction: up}]}
sources:
  - id: ellis-perimeter-separation
    title: "Ellis Print Tuning Guide — Perimeter separation"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/perimeter_separation.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# External perimeter too narrow

With layer heights above about half the nozzle size, a narrow outer line cannot reach the neighbouring perimeter.

**Check:** Gaps between outer and inner wall everywhere; layer height > 50 % of the nozzle.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Layer height and extrusion width](../fundamentals/layer-height-extrusion-width.md) (widen the external perimeter) `external_perimeter_extrusion_width` ↑
- **Causes:** [Perimeter separation](../defects/perimeter-separation.md) (#3; B)
<!-- /generated:relations -->
