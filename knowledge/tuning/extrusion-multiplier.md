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

## PrusaSlicer keys
filament: `extrusion_multiplier` · print: `top_infill_extrusion_width`, `top_fill_pattern`, `bottom_solid_min_thickness` · filament: `filament_shrinkage_compensation_xy` (dimensional, comes **after** EM)

## Oddity: perimeter gaps despite good EM and PA
Usually flow dropoff at the faster perimeter speeds (https://ellis3dp.com/Print-Tuning-Guide/articles/pa_em_oddities.html). Fixes, in order: check for a clog or a flow limit; raise the temperature slightly; use a higher-flow nozzle (CHT); set a conservative `filament_max_volumetric_speed`; slow the perimeters.

## Related
[Over-extrusion](../defects/over-extrusion.md) · [Under-extrusion](../defects/under-extrusion.md) · [Small infill areas](../defects/small-infill-overextruded.md)

<!-- generated:relations -->
## Relations
- **Fixes:** [Extrusion multiplier too high](../causes/em-too-high.md) (lower in 2 % then 0.5 % steps) · [Extrusion multiplier too low](../causes/em-too-low.md) (raise in 2 % then 0.5 % steps)
- **Related:** [Slicer flow, width and firmware output](../slicer/flow-width-and-gcode.md) · [Calibration matrix and dependency order](calibration-matrix.md)
- **Calibrates:** `key/extrusion_multiplier`
- **Linked from:** [Bulging](../defects/bulging.md) · [Over-extrusion](../defects/over-extrusion.md) · [Stringing / oozing](../defects/stringing.md) · [Under-extrusion](../defects/under-extrusion.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Extruder calibration (rotation_distance / e-steps)](extruder-calibration.md) · [Pressure advance / Linear advance](pressure-advance.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
