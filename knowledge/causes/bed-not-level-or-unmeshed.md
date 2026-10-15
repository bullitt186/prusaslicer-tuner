---
type: cause
title: "Bed not level or mesh missing"
description: "Nozzle height varies across the bed when the gantry is racked or no heat-soaked mesh is used."
altLabel: [no bed mesh, gantry out of square, Bett nicht gelevelt, kein Bed Mesh]
facets: {phase: [first-layer]}
check: "Squish patches across the bed differ; PROBE_ACCURACY and mesh range show it."
fixed_by:
  - {action: "heat-soaked mesh before each print, square the gantry, tighten hardware", sets: [{key: klipper/bed_mesh, direction: set}]}
sources:
  - id: ellis-first-layer-inconsistency
    title: "Ellis Print Tuning Guide — First layer inconsistency"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/first_layer_squish_consistency_issues/first_layer_inconsistency.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Bed not level or mesh missing

Nozzle height varies across the bed when the gantry is racked or no heat-soaked mesh is used.

**Check:** Squish patches across the bed differ; PROBE_ACCURACY and mesh range show it.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (heat-soaked mesh before each print, square the gantry, tighten hardware) `bed_mesh` =
- **Causes:** [First layer inconsistency](../defects/first-layer-inconsistency.md) (#1; B) · [Poor bed adhesion](../defects/poor-bed-adhesion.md) (#7; B) · [Warping / corner lifting](../defects/warping.md) (#7; C)
<!-- /generated:relations -->
