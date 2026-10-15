---
type: cause
title: "Stepper driver or wiring fault"
description: "Intermittent wiring, poor crimps or overheating drivers lose steps on motion axes or the extruder."
altLabel: [overheating driver, broken wire, bad crimp, Treiber überhitzt, Kabelbruch]
facets: {phase: [mechanics]}
check: "Mark the motor shaft: shuddering points to wiring, no movement to electrics or driver heat."
fixed_by:
  - {action: "repair wiring/crimps, cool drivers, check run_current", sets: [{key: klipper/run_current, direction: check}]}
sources:
  - id: ellis-extruder-skipping
    title: "Ellis Print Tuning Guide — Extruder skipping"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
  - id: ellis-layer-shifting
    title: "Ellis Print Tuning Guide — Layer shifting"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/layer_shifting.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Stepper driver or wiring fault

Intermittent wiring, poor crimps or overheating drivers lose steps on motion axes or the extruder.

**Check:** Mark the motor shaft: shuddering points to wiring, no movement to electrics or driver heat.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (repair wiring/crimps, cool drivers, check run_current) `run_current` ?
- **Causes:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (#8; B) · [Extrusion stops mid-print](../defects/extrusion-stops.md) (#4; B) · [Layer shifting](../defects/layer-shift.md) (#4; B)
<!-- /generated:relations -->
