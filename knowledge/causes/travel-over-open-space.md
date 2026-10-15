---
type: cause
title: "Travel crosses open air"
description: "Every travel over empty space is a chance to ooze. Avoiding it only works inside one island; between separate islands the nozzle must cross air."
altLabel: [travel over gaps, Leerfahrten über Lücken]
facets: {phase: [retraction-travel]}
check: "Strings only where travel crosses holes or gaps; compare a preview with avoid crossing perimeters on."
fixed_by:
  - {action: "route travel inside perimeters and wipe before travel", sets: [{key: avoid_crossing_perimeters, direction: enable}, {key: filament_wipe, direction: enable}]}
sources:
  - id: ellis-retraction
    title: "Ellis Print Tuning Guide — Retraction"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Travel crosses open air

Every travel over empty space is a chance to ooze. Avoiding it only works inside one island; between separate islands the nozzle must cross air.

**Check:** Strings only where travel crosses holes or gaps; compare a preview with avoid crossing perimeters on.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (route travel inside perimeters and wipe before travel) `avoid_crossing_perimeters` on `filament_wipe` on
- **Causes:** [Stringing / oozing](../defects/stringing.md) (#7; B) · [Scars on top surfaces](../defects/top-surface-scars.md) (#3; C)
<!-- /generated:relations -->
