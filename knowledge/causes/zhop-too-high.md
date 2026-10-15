---
type: cause
title: "Z-hop too high"
description: "A high lift gives the nozzle time and height to drag a string on every travel."
altLabel: [excessive z hop, retract lift too high, Z-Hop zu hoch]
facets: {phase: [retraction-travel]}
check: "Strings appear mainly at travel starts; they shrink with z-hop at 0.2–0.3 mm or off."
fixed_by:
  - {action: "reduce lift", sets: [{key: filament_retract_lift, direction: down}, {key: retract_lift, direction: down}]}
sources:
  - id: ellis-retraction
    title: "Ellis Print Tuning Guide — Retraction"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Z-hop too high

A high lift gives the nozzle time and height to drag a string on every travel.

**Check:** Strings appear mainly at travel starts; they shrink with z-hop at 0.2–0.3 mm or off.[^ellis-retraction]

[^ellis-retraction]: Ellis Print Tuning Guide — Retraction

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (reduce lift) `filament_retract_lift` ↓ `retract_lift` ↓
- **Causes:** [Stringing / oozing](../defects/stringing.md) (#5; B)
<!-- /generated:relations -->
