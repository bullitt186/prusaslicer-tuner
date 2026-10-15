---
type: cause
title: "Extruder not calibrated"
description: "The extruder moves a different length than commanded, so every flow value is scaled wrong."
altLabel: [wrong rotation distance, wrong e-steps, Extruder nicht kalibriert]
facets: {phase: [extrusion]}
check: "Mark and extrude 100 mm slowly; measure the actual length."
fixed_by:
  - {procedure: tuning/extruder-calibration, action: "calibrate rotation distance / e-steps", sets: [{key: klipper/rotation_distance, direction: set}, {key: prusa-fw/e_steps, direction: set}]}
sources:
  - id: klipper-rotation-distance
    title: "Klipper — Rotation distance"
    resource: https://www.klipper3d.org/Rotation_Distance.html
  - id: ellis-extruder-calibration
    title: "Ellis Print Tuning Guide — Extruder calibration"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/extruder_calibration.html
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:55:00Z
status: stable
---
# Extruder not calibrated

The extruder moves a different length than commanded, so every flow value is scaled wrong.[^klipper-rotation-distance]

**Check:** Mark and extrude 100 mm slowly; measure the actual length.[^ellis-extruder-calibration]

[^klipper-rotation-distance]: Klipper — Rotation distance
[^ellis-extruder-calibration]: Ellis Print Tuning Guide — Extruder calibration

<!-- generated:relations -->
## Relations
- **Fixed by:** [Extruder calibration (rotation_distance / e-steps)](../tuning/extruder-calibration.md) (calibrate rotation distance / e-steps) `rotation_distance` = `e_steps` =
- **Causes:** [Under-extrusion](../defects/under-extrusion.md) (#2; C)
<!-- /generated:relations -->
