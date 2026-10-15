---
type: procedure
title: Input shaping
description: Reduce ringing by measuring printer resonances and selecting a shaper while controlling smoothing and acceleration.
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: klipper-resonance
    title: Klipper — Resonance compensation
    resource: https://www.klipper3d.org/Resonance_Compensation.html
  - id: klipper-measuring
    title: Klipper — Measuring resonances
    resource: https://www.klipper3d.org/Measuring_Resonances.html
calibrates: [klipper/input_shaper, klipper/max_accel]
---
# Input shaping

Ringing is normally a mechanical vibration problem: frame stiffness, belt tension/alignment, moving mass and loose hardware should be checked before treating it as a software-only issue. Klipper input shaping applies a shaped motion command to reduce measured resonances; it does not repair a loose or misaligned machine. [^klipper-resonance]

## Procedure

1. Inspect belts, pulleys, idlers, linear motion and toolhead/frame fasteners. Re-run the same ringing test after mechanical changes.
2. Measure X and Y with Klipper's ringing test or a supported accelerometer (ADXL345, MPU-9250, LIS2DW or LIS3DH). Record sensor location and printer state. [^klipper-measuring]
3. Select a shaper using the measured frequencies and the smoothing trade-off. MZV or EI are common candidates, but the lowest residual ringing is not automatically the best result if fine detail becomes rounded.
4. Increase `max_accel` only until ringing and smoothing are acceptable. Re-tune Pressure Advance after major motion or input-shaper changes.

## Diagnostics

Residual echoes with unstable spacing suggest unresolved mechanical issues or multiple resonances. Strong smoothing, lost small details or rounded corners suggests acceleration is too high for the selected shaper/frequency combination.

## Firmware boundary

This belongs in `printer.cfg` (`[input_shaper]`, `shaper_type_*`, `shaper_freq_*`, and motion limits), not in a PrusaSlicer print profile. The slicer can still impose lower acceleration values via `*_acceleration` or `max_print_speed`.

[^klipper-resonance]: Klipper — Resonance compensation
[^klipper-measuring]: Klipper — Measuring resonances

<!-- generated:relations -->
## Relations
- **Fixes:** [Acceleration or corner velocity too high](../causes/acceleration-too-high.md) (lower accel within what the shaper supports) · [Resonance not compensated](../causes/resonance-uncompensated.md) (calibrate the input shaper)
- **Related:** [Current Klipper calibration and compatibility notes](../firmware/klipper-current.md)
- **Calibrates:** `klipper/input_shaper` · `klipper/max_accel`
- **Linked from:** [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md)
<!-- /generated:relations -->
