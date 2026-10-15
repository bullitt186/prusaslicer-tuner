---
type: cause
title: "Pressure advance too high"
description: "Pressure is pulled too early: gaps at line starts, thin corners and under-extruded starts."
altLabel: [linear advance too high, PA zu hoch, Pressure Advance zu hoch]
facets: {phase: [extrusion]}
check: "PA tower: line starts recover at a lower value."
fixed_by:
  - {procedure: tuning/pressure-advance, action: "lower PA per filament", sets: [{key: klipper/pressure_advance, direction: down}, {key: prusa-fw/linear_advance, direction: down}]}
sources:
  - id: klipper-pa
    title: "Klipper — Pressure advance"
    resource: https://www.klipper3d.org/Pressure_Advance.html
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:55:00Z
status: stable
---
# Pressure advance too high

Pressure is pulled too early: gaps at line starts, thin corners and under-extruded starts.[^klipper-pa]

**Check:** PA tower: line starts recover at a lower value.[^klipper-pa]

[^klipper-pa]: Klipper — Pressure advance

<!-- generated:relations -->
## Relations
- **Fixed by:** [Pressure advance / Linear advance](../tuning/pressure-advance.md) (lower PA per filament) `pressure_advance` ↓ `linear_advance` ↓
- **Causes:** [Under-extrusion](../defects/under-extrusion.md) (#6; C)
<!-- /generated:relations -->
