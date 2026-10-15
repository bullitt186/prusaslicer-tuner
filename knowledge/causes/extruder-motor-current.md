---
type: cause
title: "Extruder motor current wrong"
description: "Too little current loses steps under load; too much overheats the motor and softens the filament."
altLabel: [extruder stepper current, Extruder-Motorstrom]
facets: {phase: [firmware]}
check: "Compare configured run_current with the motor rating (Klipper: keep ≤ 50–60 % of rated as a starting point)."
fixed_by:
  - {action: "adjust extruder run_current", sets: [{key: klipper/run_current, direction: set}]}
sources:
  - id: ellis-extruder-skipping
    title: "Ellis Print Tuning Guide — Extruder skipping"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Extruder motor current wrong

Too little current loses steps under load; too much overheats the motor and softens the filament.

**Check:** Compare configured run_current with the motor rating (Klipper: keep ≤ 50–60 % of rated as a starting point).

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (adjust extruder run_current) `run_current` =
- **Causes:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (#5; B)
<!-- /generated:relations -->
