---
type: procedure
title: Temperature tuning
description: Establish a material- and hardware-specific temperature window before optimizing cooling, flow or retraction.
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: ellis-temperature
    title: Ellis Print Tuning Guide — Temperature Tuning
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/temperature_tuning.html
  - id: klipper-pa
    title: Klipper — Pressure advance
    resource: https://www.klipper3d.org/Pressure_Advance.html
calibrates: [temperature, first_layer_temperature]
---
# Temperature tuning

Temperature changes the polymer's viscosity, wetting, cooling rate and interlayer bonding; it is not a universal “more is better” control. Tune with the same nozzle, layer height, speed, cooling and filament moisture state that matter for the intended print. Klipper explicitly requires nozzle temperature and extrusion calibration before Pressure Advance tuning. [^klipper-pa]

## Procedure

1. Dry or otherwise control the filament first; record spool, nozzle, bed, layer height, speed and fan state.
2. Print a temperature tower over a deliberately useful range around the manufacturer's profile. Compare bridging, overhangs, surface finish, stringing, corner shape and layer fracture.
3. Select a window, not a single magic number: choose the lowest temperature that gives consistent extrusion and adequate layer bonding at the target flow. Validate with a functional part.

## Evidence and limits

- **B — documented procedure:** a tower is a comparative test; its optimum is specific to the tested material, hardware and process.
- **A/B — physical interpretation:** higher temperature can improve wetting and melt capacity but can increase ooze and soften unsupported features. Fan and speed can move the apparent optimum.
- If strength is the goal, test fracture orientation and process repeatability rather than selecting by appearance alone. See [part orientation](../mechanical-properties/part-orientation.md).

## PrusaSlicer keys

Filament: `temperature`, `first_layer_temperature`, `bed_temperature`, `first_layer_bed_temperature`, `cooling`, `max_fan_speed`. Validate the chosen value against `filament_max_volumetric_speed`; temperature alone cannot make every hotend/material combination reliable at high flow.

[^ellis-temperature]: Ellis Print Tuning Guide — Temperature Tuning
[^klipper-pa]: Klipper — Pressure advance

<!-- generated:relations -->
## Relations
- **Fixes:** [Nozzle temperature too high](../causes/nozzle-temp-too-high.md) (lower in 5 °C steps inside the material window) · [Nozzle temperature too low](../causes/nozzle-temp-too-low.md) (raise within the material window)
- **Calibrates:** `key/first_layer_temperature` · `key/temperature`
- **Linked from:** [Filament drying and moisture](../materials/filament-moisture.md) · [Part orientation and anisotropy](../mechanical-properties/part-orientation.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md)
<!-- /generated:relations -->
