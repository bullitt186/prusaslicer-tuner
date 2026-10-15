---
type: cause
title: Nozzle too close to the bed
description: 'Over-squished first layer: flare, rough surface, the extruder struggles on the first layer.'
altLabel: [too much squish, z offset too low, zu stark gequetscht, Düse zu tief, nozzle too close to print bed]
facets: {phase: [first-layer]}
check: First-layer patches are translucent or ridged; skipping only on the first layer.
fixed_by:
  - {procedure: tuning/first-layer-squish, action: raise Z in 0.01 mm babysteps, sets: [{key: klipper/z_offset, direction: set}, {key: prusa-fw/z_offset, direction: set}]}
sources:
  - id: ellis-extruder-skipping
    title: Ellis Print Tuning Guide — Extruder skipping
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
generated:
  by: process:kg-migration
  at: 2026-10-13 23:00:00+00:00
status: stable
---
# Nozzle too close to the bed

Over-squished first layer: flare, rough surface, the extruder struggles on the first layer.

**Check:** First-layer patches are translucent or ridged; skipping only on the first layer.

<!-- generated:relations -->
## Relations
- **Fixed by:** [First layer squish (Z offset)](../tuning/first-layer-squish.md) (raise Z in 0.01 mm babysteps) `z_offset` = `z_offset` =
- **Causes:** [Dimensional inaccuracy](../defects/dimensional-inaccuracy.md) (#1; B) · [Elephant foot](../defects/elephant-foot.md) (#1; C) · [Extruder skipping / clicking](../defects/extruder-skipping.md) (#9; B) · [No extrusion at print start](../defects/no-extrusion-at-start.md) (#2; B) · [Over-extrusion](../defects/over-extrusion.md) (#2; C) · [Under-extrusion](../defects/under-extrusion.md) (#8; B)
<!-- /generated:relations -->
