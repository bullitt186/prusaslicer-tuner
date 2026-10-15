---
type: cause
title: "Volumetric flow above the hotend limit"
description: "Speed asks for more mm³/s than the hotend can melt: under-extrusion on fast sections, skipping and weak layers."
altLabel: [max flow exceeded, "hotend can't keep up", Volumenstrom zu hoch, Hotend zu langsam]
facets: {phase: [extrusion]}
check: "Defect only on fast sections or high line widths; disappears when slowed down."
fixed_by:
  - {procedure: tuning/max-volumetric-flow, action: "measure the limit and cap flow per filament", sets: [{key: filament_max_volumetric_speed, direction: down}]}
sources:
  - id: ellis-extruder-skipping
    title: "Ellis Print Tuning Guide — Extruder skipping"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
  - id: ellis-layer-adhesion
    title: "Ellis Print Tuning Guide — Poor layer adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/poor_layer_adhesion.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Volumetric flow above the hotend limit

Speed asks for more mm³/s than the hotend can melt: under-extrusion on fast sections, skipping and weak layers.

**Check:** Defect only on fast sections or high line widths; disappears when slowed down.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Max volumetric flow](../tuning/max-volumetric-flow.md) (measure the limit and cap flow per filament) `filament_max_volumetric_speed` ↓
- **Causes:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (#6; B) · [Poor layer adhesion](../defects/poor-layer-adhesion.md) (#2; B) · [Under-extrusion](../defects/under-extrusion.md) (#5; C)
<!-- /generated:relations -->
