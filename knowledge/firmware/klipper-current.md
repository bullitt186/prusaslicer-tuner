---
type: firmware
title: Current Klipper calibration and compatibility notes
description: Klipper firmware state is versioned and authoritative for pressure advance, input shaping, extrusion calibration, retraction and motion limits.
tags: [klipper, firmware, pressure-advance, input-shaping, rotation-distance, retraction, compatibility]
generated:
  by: process:source-consolidation-2026-10-13
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: klipper-docs
    title: Klipper official documentation
    resource: https://www.klipper3d.org/
  - id: klipper-github
    title: Klipper source repository
    resource: https://github.com/Klipper3d/klipper
  - id: klipper-discourse
    title: Klipper Discourse representative corpus
    resource: https://klipper.discourse.group/
  - id: prusaslicer-source
    title: PrusaSlicer G-code writer
    resource: https://github.com/prusa3d/PrusaSlicer
related: [tuning/pressure-advance, tuning/input-shaping, tuning/retraction, firmware/klipper-operating-boundaries]
---
# Current Klipper calibration and compatibility notes

The inspected Klipper repository was `master` at commit `c7d572441f7d6d6d7f887df5c0fa8cec69d14980`, after release `v0.13.0`. Findings tied to `master` must not be assumed available in every installed release. [^klipper-github]

## Firmware-owned state

- `rotation_distance` calibrates extruder mechanics; it is not an Extrusion Multiplier.
- `pressure_advance` and `pressure_advance_smooth_time` are extruder/filament/nozzle/process dependent.
- `[input_shaper]` and resonance measurement control ringing compensation; `max_accel` remains a separate machine decision.
- `[firmware_retraction]` controls `G10/G11` when enabled.
- `[printer]` limits such as `max_velocity`, `max_accel`, `minimum_cruise_ratio` and `square_corner_velocity` constrain requested slicer motion.

## Pressure Advance

Klipper's official square-tower procedure uses `SQUARE_CORNER_VELOCITY=1`, `ACCEL=500`, a high-flow test and different starting factors for direct drive (`.005`) and long Bowden (`.020`). The value depends on extruder, nozzle, filament, temperature and flow. Klipper notes that high PA with high acceleration can cause extruder skips; these are starting factors, not universal settings. [^klipper-docs]

## Input Shaping

Measure with shaping and PA disabled, then select a shaper based on residual vibration versus smoothing. Current `master` adds parameterized shapers and independent Z-axis shaping; those features are version-sensitive. The current source also records calibration constraints such as maximum smoothing and residual vibration. [^klipper-github]

## Compatibility hazards

- `max_accel_to_decel` was removed in favor of `minimum_cruise_ratio`; old macros/configs require review.
- Klipper's current source contains a documented `SHAPER_FREQ_Y`/Z typo in one G-Code document while implementation/config reference use Z correctly; verify the installed version and actual config keys.
- Eddy-current `tap_threshold` changed units from Hz to Hz/mm in current development history and requires recalibration, not arithmetic conversion.
- PrusaSlicer may emit different PA and retraction commands based on firmware flavor; inspect generated G-code and avoid duplicate firmware/slicer retraction. [^prusaslicer-source]

## Safe diagnostic sequence

1. Record Klipper version/commit and printer model.
2. Validate heaters, homing, emergency stop and extrusion direction.
3. Calibrate PID and `rotation_distance`.
4. Mechanically inspect the printer.
5. Measure resonances and choose safe acceleration.
6. Tune PA at the target nozzle/material/temperature.
7. Configure firmware retraction only if the slicer emits `G10/G11`.
8. Compare generated G-code with active `printer.cfg`.

Do not change safety limits or `printer.cfg` based on a community value without checking version, hardware and test conditions. [^klipper-discourse]

[^klipper-docs]: Klipper official documentation
[^klipper-github]: Klipper source repository at the inspected revision
[^klipper-discourse]: Klipper Discourse representative corpus
[^prusaslicer-source]: PrusaSlicer source and G-code writer

<!-- generated:relations -->
## Relations
- **Related:** [Klipper operating boundaries](klipper-operating-boundaries.md) · [Input shaping](../tuning/input-shaping.md) · [Pressure advance / Linear advance](../tuning/pressure-advance.md) · [Retraction](../tuning/retraction.md)
<!-- /generated:relations -->
