---
type: cause
title: "Pressure advance too low"
description: "Nozzle pressure lags the toolhead: corners bulge, line ends blob and residual pressure oozes on travel."
altLabel: [linear advance too low, PA zu niedrig, Pressure Advance zu niedrig]
facets: {phase: [extrusion]}
check: "Print a PA tower or pattern; sharper corners at a higher value confirm it."
fixed_by:
  - {procedure: tuning/pressure-advance, action: "raise PA per filament", sets: [{key: klipper/pressure_advance, direction: up}, {key: prusa-fw/linear_advance, direction: up}]}
sources:
  - id: ellis-retraction
    title: "Ellis Print Tuning Guide — Retraction"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Pressure advance too low

Nozzle pressure lags the toolhead: corners bulge, line ends blob and residual pressure oozes on travel.

**Check:** Print a PA tower or pattern; sharper corners at a higher value confirm it.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Pressure advance / Linear advance](../tuning/pressure-advance.md) (raise PA per filament) `pressure_advance` ↑ `linear_advance` ↑
- **Causes:** [Over-extrusion](../defects/over-extrusion.md) (#3; C) · [Stringing / oozing](../defects/stringing.md) (#3; B) · [Zits, blobs & visible seam](../defects/zits-blobs.md) (#1; C)
<!-- /generated:relations -->
