---
type: procedure
title: Extrusion multiplier (flow)
description: Per-filament flow tuned visually on top surfaces of 30x30x3 cubes; 2% then 0.5% steps.
timestamp: 2026-10-13
calibrates: [extrusion_multiplier]
sources:
  - id: ellis-extrusion-multiplier
    title: "Ellis Print Tuning Guide — Extrusion multiplier (flow)"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/extrusion_multiplier.html
  - id: ellis-test-prints
    title: "Ellis Print Tuning Guide — test_prints folder (STL files)"
    resource: https://github.com/AndrewEllis93/Print-Tuning-Guide/tree/main/test_prints
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Extrusion multiplier (EM)

## Symptoms
- **Too high:** rough or ridged top surfaces, bulging, small top areas look overfilled.
- **Too low:** gaps, valleys or shadows between top infill lines.

## Procedure
- Prerequisites: [extruder calibration](extruder-calibration.md), then [pressure advance](pressure-advance.md).
- Print 30×30×3 mm cubes with ≥ 30% infill, 2 bottom layers (and `bottom_solid_min_thickness = 0`), as many top layers as fit while keeping ≥ 2 infill layers, `top_infill_extrusion_width` = nozzle diameter in mm, `top_fill_pattern = monotonic` (ironing off), top solid infill speed about 60 mm/s, `slowdown_below_layer_time = 0`.
- Sweep EM in 2% steps (roughly 0.92–0.98), then in 0.5% steps. PrusaSlicer has no per-object EM, so print each cube separately or as separate filament copies.
- Judge the **widest** areas. When in doubt, take the higher EM.
- Don't set EM from caliper wall measurements, and don't use SuperSlicer's built-in flow test.
- Tune at your real print speeds, because of flow dropoff. See [max volumetric flow](max-volumetric-flow.md).

## Test prints
Get the files with the MCP tool `test_prints("EM_Cube")`. All cubes are 30×30×3 mm.[^ellis-test-prints]

| File | Use for |
|---|---|
| `EM_Cube-Unlabeled.stl` | a single cube, or several copies when you keep track of them yourself |
| `labeled/EM_0.8-1.2/EM_Cube-<value>.stl` | the usual range. The bottom face shows the EM value, from 0.800 to 1.200 in steps of 0.005 |
| `labeled/EM_0.5-0.8/…`, `labeled/EM_1.2-1.5/…` | filaments far outside the usual range |

- **When:** for every new filament brand or type. Also for a new color or spool when the brand varies, and after a change of nozzle diameter, line width or layer height. Always do it **after** [pressure advance](pressure-advance.md) and [first layer squish](first-layer-squish.md). An oversquished first layer propagates up into the top surface.
- **The label is a name tag only.** An STL carries no settings, so set `extrusion_multiplier` per cube yourself. PrusaSlicer has no per-object EM, so the cubes are printed one after another.
- **How:** start with a coarse sweep in 2 % steps. Ellis starts at 0.92–0.98, which is a starting range and not a rule.[^ellis-extrusion-multiplier] Then refine around the best cube in 0.5 % steps by picking the matching labeled files. Use the slicer settings from *Procedure* above. If your layers are thick, scale the cube in Z, so that ≥ 2 infill layers remain under the top layers.
- **One print instead of one per cube (Klipper/relative E):** place the cubes in a row (merged into one STL, or one object each), slice once at EM 1.0, then multiply the positive `E` of every XY move inside cube *i*'s X range by that cube's EM. Retract and deretract lines carry no XY and stay untouched. This saves the repeated start sequence (heat, mesh, homing) for each cube (field report).
- Judge the center of each top surface. The edges always look a little overextruded.

## PrusaSlicer keys
filament: `extrusion_multiplier` · print: `top_infill_extrusion_width`, `top_fill_pattern`, `bottom_solid_min_thickness` · filament: `filament_shrinkage_compensation_xy` (dimensional, comes **after** EM)

## Oddity: perimeter gaps despite good EM and PA
Usually flow dropoff at the faster perimeter speeds (https://ellis3dp.com/Print-Tuning-Guide/articles/pa_em_oddities.html). Fixes, in order: check for a clog or a flow limit; raise the temperature slightly; use a higher-flow nozzle (CHT); set a conservative `filament_max_volumetric_speed`; slow the perimeters.

## Related
[Over-extrusion](../defects/over-extrusion.md) · [Under-extrusion](../defects/under-extrusion.md) · [Small infill areas](../defects/small-infill-overextruded.md)

[^ellis-extrusion-multiplier]: Ellis Print Tuning Guide — Extrusion multiplier
[^ellis-test-prints]: Ellis Print Tuning Guide — test_prints folder

<!-- generated:relations -->
## Relations
- **Fixes:** [Extrusion multiplier too high](../causes/em-too-high.md) (lower in 2 % then 0.5 % steps) · [Extrusion multiplier too low](../causes/em-too-low.md) (raise in 2 % then 0.5 % steps)
- **Related:** [Slicer flow, width and firmware output](../slicer/flow-width-and-gcode.md) · [Calibration matrix and dependency order](calibration-matrix.md)
- **Calibrates:** `key/extrusion_multiplier`
- **Linked from:** [Bulging](../defects/bulging.md) · [Over-extrusion](../defects/over-extrusion.md) · [Stringing / oozing](../defects/stringing.md) · [Under-extrusion](../defects/under-extrusion.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Extruder calibration (rotation_distance / e-steps)](extruder-calibration.md) · [Pressure advance / Linear advance](pressure-advance.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
