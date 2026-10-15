---
type: cause
title: "Nozzle too far from the bed"
description: "First-layer lines are round and barely touch: poor adhesion, gaps in the second layer, separated bottom perimeters."
altLabel: [too little squish, z offset too high, zu wenig gequetscht, Düse zu hoch]
facets: {phase: [first-layer]}
check: "Inspect first-layer patches: gaps between lines, rounded tops."
fixed_by:
  - {procedure: tuning/first-layer-squish, action: "lower Z in 0.01 mm babysteps", sets: [{key: klipper/z_offset, direction: set}, {key: prusa-fw/z_offset, direction: set}]}
sources:
  - id: ellis-build-surface-adhesion
    title: "Ellis Print Tuning Guide — Build surface adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/build_surface_adhesion.html
  - id: ellis-perimeter-separation
    title: "Ellis Print Tuning Guide — Perimeter separation"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/perimeter_separation.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Nozzle too far from the bed

First-layer lines are round and barely touch: poor adhesion, gaps in the second layer, separated bottom perimeters.

**Check:** Inspect first-layer patches: gaps between lines, rounded tops.

<!-- generated:relations -->
## Relations
- **Fixed by:** [First layer squish (Z offset)](../tuning/first-layer-squish.md) (lower Z in 0.01 mm babysteps) `z_offset` = `z_offset` =
- **Causes:** [Perimeter separation](../defects/perimeter-separation.md) (#1; B) · [Poor bed adhesion](../defects/poor-bed-adhesion.md) (#3; B) · [Under-extrusion](../defects/under-extrusion.md) (#7; C)
<!-- /generated:relations -->
