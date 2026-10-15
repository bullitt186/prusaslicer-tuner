---
type: concept
title: Klipper operating boundaries
description: Keep Klipper motion, extrusion and calibration limits consistent with slicer output and distinguish firmware state from profile settings.
tags: [firmware, klipper, acceleration, pressure-advance, volumetric-flow]
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: klipper-config
    title: Klipper — Configuration reference
    resource: https://www.klipper3d.org/Config_Reference.html
  - id: klipper-pa
    title: Klipper — Pressure advance
    resource: https://www.klipper3d.org/Pressure_Advance.html
---
# Klipper operating boundaries

Klipper owns machine-side state such as `rotation_distance`, `pressure_advance`, input shaping and motion limits. The slicer supplies planned paths and may add lower per-print limits. A good slicer number cannot compensate for an incorrect firmware calibration or a firmware cap that is lower than the requested process.

## Boundary checks

- Confirm `rotation_distance`/extruder calibration before tuning Pressure Advance; Klipper's own procedure calls this out. [^klipper-pa]
- Confirm `[extruder]` temperature control, `max_extrude_only_distance`, `max_extrude_only_velocity`, and any `max_extrude_cross_section` safety limits before interpreting a flow test.
- Compare Klipper `max_velocity`, `max_accel`, `minimum_cruise_ratio` and square-corner settings with PrusaSlicer `*_speed`, `*_acceleration` and travel limits. The effective motion is the restrictive combination.
- If `use_firmware_retraction = 1`, retraction length/speed are controlled by `[firmware_retraction]` in `printer.cfg`; a filament-level slicer override is then not the authoritative value.

## Safe diagnostic order

Read-only: identify the printer, firmware, nozzle, filament and profile; inspect the effective slicer values; then inspect the relevant Klipper sections. Change one layer at a time and re-run a small test. Never conclude that a profile edit fixed a firmware-side defect without checking the generated G-code and active configuration.

## Related
- [Current Klipper compatibility notes](klipper-current.md)
- [Profile knowledge map](../slicer/profile-knowledge-map.md)

[^klipper-config]: Klipper — Configuration reference
[^klipper-pa]: Klipper — Pressure advance

<!-- generated:relations -->
## Relations
- **Related:** [Current Klipper calibration and compatibility notes](klipper-current.md)
- **Linked from:** [Voron thermal and motion mechanics](../hardware/voron-thermal-mechanics.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md)
<!-- /generated:relations -->
