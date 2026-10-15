---
type: procedure
title: Pressure advance / Linear advance
description: Compensates extruder pressure lag on accel/decel; fixes corner bulges and line-start gaps. Per filament and per printer.
timestamp: 2026-10-13
calibrates: [klipper/pressure_advance, klipper/pressure_advance_smooth_time, prusa-fw/linear_advance]
sources:
  - id: ellis-introduction
    title: "Ellis Print Tuning Guide — Pressure advance / Linear advance"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/pressure_linear_advance/introduction.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Pressure advance (PA)

PA redistributes material during acceleration and deceleration; it doesn't change the total amount extruded.

## Diagnosis from a print
- **PA too low:** bulging or blobs at corners and line ends, gaps along straight perimeter lines, oozing right after moves.
- **PA too high:** divots or underextrusion at corners and line ends, gaps between perimeters at corners.
- Gaps **and** bulges at the same time, or no clean corner at any value, point to extruder backlash or a loose part, not to PA. See [extrusion patterns](../defects/extrusion-patterns.md).

## Procedure
- Use the **pattern method** (Ellis' online generator, https://ellis3dp.com/Print-Tuning-Guide/articles/pressure_linear_advance/pattern_method.html). Match the generator's acceleration to your external perimeter acceleration. Pick the sharpest corner. When two values are close, take the higher one. Refine in 0.001–0.002 steps for direct drive.
- The tower method is a simpler alternative. The lines method is deprecated.
- Typical example from Ellis: about 0.04 (direct drive). Bowden values are much higher.
- Klipper `pressure_advance_smooth_time`: lower values (e.g. 0.02) help small infill areas, but too low causes extruder skipping.

## Where the value lives
- **Klipper printers:** `[extruder] pressure_advance` in `printer.cfg` is the global value. Per filament, add `SET_PRESSURE_ADVANCE ADVANCE=0.040` to the filament profile's `start_filament_gcode`.
- **Prusa printers (CORE One, MK3.5):** the vendor filament profiles already put `M900 K…` into `start_filament_gcode`, with conditions per printer model and nozzle. To change PA for a Prusa filament, edit that expression. Marlin and Prusa firmware use `M900 K<v>`, and RRF uses `M572 S<v>`.
- Saving: https://ellis3dp.com/Print-Tuning-Guide/articles/pressure_linear_advance/saving.html

## PrusaSlicer keys
filament: `start_filament_gcode` · printer: `gcode_flavor` (decides the syntax) · print: `external_perimeter_acceleration`, `perimeter_acceleration`

## Related
[Tuning order](tuning-order.md) · [Extrusion multiplier](extrusion-multiplier.md) · [Stringing](../defects/stringing.md) · [Bulging](../defects/bulging.md)

<!-- generated:relations -->
## Relations
- **Fixes:** [Pressure advance smoothing too long](../causes/pa-smooth-time-too-high.md) (lower smooth time, then re-tune PA) · [Pressure advance too high](../causes/pa-too-high.md) (lower PA per filament) · [Pressure advance too low](../causes/pa-too-low.md) (raise PA per filament) · [Seam start/stop pressure](../causes/seam-start-stop-pressure.md) (tune PA first, then restart/wipe)
- **Related:** [Current Klipper calibration and compatibility notes](../firmware/klipper-current.md) · [Calibration matrix and dependency order](calibration-matrix.md)
- **Calibrates:** `klipper/pressure_advance` · `klipper/pressure_advance_smooth_time` · `prusa-fw/linear_advance`
- **Linked from:** [Bulging](../defects/bulging.md) · [Over-extrusion](../defects/over-extrusion.md) · [Stringing / oozing](../defects/stringing.md) · [Under-extrusion](../defects/under-extrusion.md) · [Zits, blobs & visible seam](../defects/zits-blobs.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Extruder calibration (rotation_distance / e-steps)](extruder-calibration.md) · [Extrusion multiplier (flow)](extrusion-multiplier.md) · [Retraction](retraction.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
