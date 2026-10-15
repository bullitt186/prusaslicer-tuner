---
type: procedure
title: Calibration matrix and dependency order
description: A context-preserving calibration sequence that separates machine, firmware, material and slicer variables.
tags: [calibration, tuning-order, flow, temperature, pressure-advance, retraction, input-shaping]
generated:
  by: process:source-consolidation-2026-10-13
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: ellis-guide
    title: Ellis Print Tuning Guide
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/index_tuning.html
  - id: klipper-pa
    title: Klipper — Pressure advance
    resource: https://www.klipper3d.org/Pressure_Advance.html
  - id: teaching-tech
    title: Teaching Tech — Calibration guide
    resource: https://teachingtechyt.github.io/calibration.html
  - id: prusa-calibration
    title: Prusa Knowledge Base — Calibration
    resource: https://help.prusa3d.com/category/calibration_199
  - id: orca-source
    title: OrcaSlicer source
    resource: https://github.com/SoftFever/OrcaSlicer
related: [tuning/tuning-order, tuning/extrusion-multiplier, tuning/pressure-advance]
---
# Calibration matrix and dependency order

Calibration results are only comparable when the relevant state is held constant. The sequence below synthesizes Ellis, Klipper, Teaching Tech, Prusa and Orca workflows; it is a dependency graph, not a universal command script. [^ellis-guide] [^klipper-pa]

| Stage | Establish | Depends on | Invalidated by |
|---|---|---|---|
| 1. Mechanical readiness | belts, gantry, nozzle, hotend, extruder, thermistors, motion | correct assembly | mechanical changes, leaks, clogs |
| 2. Firmware safety and heaters | PID, sensor bounds, homing, endstops, rotation distance | working firmware | firmware/config changes |
| 3. Bed/first layer | sheet state, Z/sensor behavior, mesh, thermal soak | mechanics and heaters | nozzle, sheet, gantry, temperature changes |
| 4. Temperature window | melt, bonding, cooling response | dry filament, reliable flow | material/spool/nozzle/speed changes |
| 5. Volumetric flow | hotend/material/nozzle flow cap | temperature, rotation distance | nozzle, hotend, material, temperature |
| 6. Flow ratio/EM | material-specific quantity | stable flow and geometry | spool/color, nozzle, width, layer height |
| 7. Input shaping | resonance suppression and smoothing | mechanically sound motion | toolhead, belts, frame, accelerometer location |
| 8. Pressure Advance/Linear Advance | extrusion pressure compensation | rotation distance, temperature, flow, motion settings | nozzle, extruder, filament, temperature, acceleration |
| 9. Retraction | travel ooze control | PA/LA, dry filament, nozzle | hotend, extruder, firmware retraction mode |
| 10. Feature tuning | supports, bridges, seams, cooling, speed | all relevant baseline stages | slicer version/profile changes |

## Procedures

- **Extruder/rotation distance:** use the firmware's measured-extrusion procedure. Klipper's official workflow uses a heated extruder, a marked filament distance, slow extrusion and a repeat when error remains material; Voron and Ellis use different mark/test distances. Keep the firmware-specific procedure instead of averaging them. [^klipper-pa]
- **Temperature:** use a tower or controlled step test at the intended layer height, speed, fan and dry-filament state. Select a usable window, not the prettiest single layer.
- **Flow:** measure hotend drop-off at the intended material/nozzle/temperature, then set a cap below it. Do not use a hotend table as a machine guarantee.
- **EM/Flow Ratio:** calibrate after mechanical and volumetric flow stability. Prusa documents both visual and measured-wall approaches; Orca's Flow Ratio is slicer-specific. [^prusa-calibration] [^orca-source]
- **PA/LA:** Klipper requires rotation distance and nozzle temperature first. Klipper's square-tower factors differ for direct drive and long Bowden; Ellis prefers a pattern method. Treat them as alternative procedures, not additive values. [^klipper-pa] [^ellis-guide]
- **Retraction:** check moisture, temperature, leaks, nozzle and PA before increasing distance. Firmware retraction must be distinguished from slicer-generated E moves.

## Controlled test record

Record printer, firmware, slicer/version, profile names, nozzle diameter/material/geometry, extruder type, filament product/color/spool, moisture treatment, chamber, layer height, widths, speed, acceleration, temperature, fan, test geometry, measured result and source procedure. Unknown values remain `unknown`.

## Failure interpretation

- A result that changes with speed suggests volumetric flow, temperature or pressure dynamics rather than simple EM.
- A result that changes with spool/color suggests material state or pigment-dependent behavior rather than a printer-global value.
- A result that changes after a motion change requires rechecking input shaping and PA.
- A result that changes only with travel geometry suggests retraction, wipe, seam, moisture or firmware-retraction mode.

## PrusaSlicer keys and firmware boundaries

Filament: `temperature`, `extrusion_multiplier`, `filament_max_volumetric_speed`, `filament_diameter`, `start_filament_gcode`. Print: `max_volumetric_speed`, `*_speed`, `*_acceleration`, `layer_height`. Printer: `retract_*`, `use_firmware_retraction`, `nozzle_diameter`. Klipper-side: `rotation_distance`, `pressure_advance`, `[input_shaper]`, `[firmware_retraction]`, `max_accel`.

[^ellis-guide]: Ellis Print Tuning Guide — tuning order and procedures
[^klipper-pa]: Klipper — Pressure advance and calibration prerequisites
[^teaching-tech]: Teaching Tech — calibration guide
[^prusa-calibration]: Prusa Knowledge Base — calibration and extrusion multiplier
[^orca-source]: OrcaSlicer calibration and profile implementation

<!-- generated:relations -->
## Relations
- **Related:** [Extrusion multiplier (flow)](extrusion-multiplier.md) · [Pressure advance / Linear advance](pressure-advance.md) · [Tuning order](tuning-order.md)
- **Linked from:** [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [FDM print defect diagnostic matrix](../troubleshooting/diagnostic-matrix.md)
<!-- /generated:relations -->
