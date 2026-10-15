---
type: cause
title: "Bed temperature too low"
description: "The first layer does not stay soft enough to bond and contracts early."
altLabel: [Bett zu kalt, Druckbett zu kalt]
facets: {phase: [first-layer]}
check: "Adhesion improves with a hotter bed (5–10 °C steps as a starting value, within the material window)."
fixed_by:
  - {action: "raise bed temperature within the material window", sets: [{key: first_layer_bed_temperature, direction: up}, {key: bed_temperature, direction: up}]}
sources:
  - id: ellis-build-surface-adhesion
    title: "Ellis Print Tuning Guide — Build surface adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/build_surface_adhesion.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Bed temperature too low

The first layer does not stay soft enough to bond and contracts early.

**Check:** Adhesion improves with a hotter bed (5–10 °C steps as a starting value, within the material window).

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (raise bed temperature within the material window) `first_layer_bed_temperature` ↑ `bed_temperature` ↑
- **Causes:** [Poor bed adhesion](../defects/poor-bed-adhesion.md) (#2; B) · [Warping / corner lifting](../defects/warping.md) (#4; B)
<!-- /generated:relations -->
