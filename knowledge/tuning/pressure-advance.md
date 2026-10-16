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
  - id: ellis-tower-method
    title: "Ellis Print Tuning Guide — Pressure advance tower method"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/pressure_linear_advance/tower_method.html
  - id: ellis-pa-pattern-tool
    title: "Ellis Pressure / Linear Advance pattern generator"
    resource: https://ellis3dp.com/Pressure_Linear_Advance_Tool/
  - id: klipper-pa
    title: "Klipper — Pressure advance (square_tower.stl)"
    resource: https://www.klipper3d.org/Pressure_Advance.html
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

## Test prints
- **When:** for every new filament, and after a change of nozzle, extruder, hotend or print temperature. After a big change in acceleration or input shaper, check it again. Do it after [extruder calibration](extruder-calibration.md) and before [extrusion multiplier](extrusion-multiplier.md).
- **Pattern method (first choice, any firmware):** there is no STL. Ellis' online generator writes G-code for your printer, nozzle, temperatures, accelerations and PA range.[^ellis-pa-pattern-tool] Set the generator's acceleration to your `external_perimeter_acceleration`.
- **Tower method (Klipper only, for beginners):** the MCP tool `test_prints("square_tower")` returns the file `square_tower_klipper_PA_tower.stl`.[^klipper-pa] Slice it with your normal profile, accelerations included. Change only these settings: external perimeter speed 120 mm/s, `perimeters = 1`, `fill_density = 0%`, `top_solid_layers = 0`, `slowdown_below_layer_time = 0`, high fan.[^ellis-tower-method] Once the print has started, send:
  - direct drive: `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.0025`
  - Bowden: `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.025`

  Cancel the print once the walls clearly fail. Measure the height of the cleanest corner, ignoring the seam corner. PA = START + height × FACTOR. When in doubt, take the lower value. Ellis deliberately keeps normal accelerations, while Klipper's own guide limits acceleration to 500 and square corner velocity to 1. Ellis says that the Klipper limits exaggerate bulging and lead to a PA that is too high.[^ellis-tower-method]

## Where the value lives
- **Klipper printers:** `[extruder] pressure_advance` in `printer.cfg` is the global value. Per filament, add `SET_PRESSURE_ADVANCE ADVANCE=0.040` to the filament profile's `start_filament_gcode`.
- **Prusa printers (CORE One, MK3.5):** the vendor filament profiles already put `M900 K…` into `start_filament_gcode`, with conditions per printer model and nozzle. To change PA for a Prusa filament, edit that expression. Marlin and Prusa firmware use `M900 K<v>`, and RRF uses `M572 S<v>`.
- Saving: https://ellis3dp.com/Print-Tuning-Guide/articles/pressure_linear_advance/saving.html

## PrusaSlicer keys
filament: `start_filament_gcode` · printer: `gcode_flavor` (decides the syntax) · print: `external_perimeter_acceleration`, `perimeter_acceleration`

## Related
[Tuning order](tuning-order.md) · [Extrusion multiplier](extrusion-multiplier.md) · [Stringing](../defects/stringing.md) · [Bulging](../defects/bulging.md)

[^ellis-tower-method]: Ellis Print Tuning Guide — Tower method
[^ellis-pa-pattern-tool]: Ellis Pressure / Linear Advance pattern generator
[^klipper-pa]: Klipper — Pressure advance

<!-- generated:relations -->
## Relations
- **Fixes:** [Pressure advance smoothing too long](../causes/pa-smooth-time-too-high.md) (lower smooth time, then re-tune PA) · [Pressure advance too high](../causes/pa-too-high.md) (lower PA per filament) · [Pressure advance too low](../causes/pa-too-low.md) (raise PA per filament) · [Seam start/stop pressure](../causes/seam-start-stop-pressure.md) (tune PA first, then restart/wipe)
- **Related:** [Current Klipper calibration and compatibility notes](../firmware/klipper-current.md) · [Calibration matrix and dependency order](calibration-matrix.md)
- **Calibrates:** `klipper/pressure_advance` · `klipper/pressure_advance_smooth_time` · `prusa-fw/linear_advance`
- **Linked from:** [Bulging](../defects/bulging.md) · [Over-extrusion](../defects/over-extrusion.md) · [Stringing / oozing](../defects/stringing.md) · [Under-extrusion](../defects/under-extrusion.md) · [Zits, blobs & visible seam](../defects/zits-blobs.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Extruder calibration (rotation_distance / e-steps)](extruder-calibration.md) · [Extrusion multiplier (flow)](extrusion-multiplier.md) · [Retraction](retraction.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
