---
type: integration
title: PrusaSlicer profile to knowledge map
description: Map observable print symptoms and tuning concepts to effective PrusaSlicer profile keys, authority boundaries and diagnostic knowledge topics.
okf_version: "0.2"
tags: [integration, prusaslicer, profiles, diagnosis, mcp, knowledge-map]
generated:
  by: process:profile-knowledge-integration
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: repo-profiles
    title: PrusaSlicer profile conventions used by the profile resolver
    resource: https://github.com/prusa3d/PrusaSlicer-settings
  - id: prusaslicer-source
    title: PrusaSlicer source and preset schemas
    resource: https://github.com/prusa3d/PrusaSlicer
  - id: klipper-docs
    title: Klipper documentation
    resource: https://www.klipper3d.org/
---
# PrusaSlicer profile to knowledge map

This integration map is the bridge between a symptom or tuning question, the effective PrusaSlicer value, and the topic document that explains the mechanism and test. It is deliberately not a second copy of the profile reference: the profile resolver remains authoritative for the actual value and inheritance chain, while the knowledge documents remain authoritative for diagnosis and recommendations.

## Operating rule

Always resolve the effective value before recommending a change. A value may come from a user preset, a vendor preset, a built-in default, or a filament override. Read the profile type and source annotation together; an apparently identical key in two profile types is not interchangeable. PrusaSlicer preset schemas and generated G-code also vary by version and firmware flavor.[^prusaslicer-source]

For Klipper printers, treat firmware as a separate authority. Pressure advance, firmware retraction, acceleration limits, input shaping and printer kinematics can override or constrain what the slicer emits.[^klipper-docs]

## Authority and profile-key map

| Concept | First profile type to inspect | PrusaSlicer keys | Firmware or external authority | Knowledge topics |
|---|---|---|---|---|
| Extrusion calibration | filament, then printer firmware | `extrusion_multiplier`, `filament_diameter` | Klipper `rotation_distance` / Marlin E-steps | [extrusion multiplier](../tuning/extrusion-multiplier.md), [under-extrusion](../defects/under-extrusion.md), [over-extrusion](../defects/over-extrusion.md) |
| Maximum melt throughput | print, then filament | `max_volumetric_speed`, `filament_max_volumetric_speed`, temperature and speed keys | Hotend, nozzle and material capability | [maximum volumetric flow](../tuning/max-volumetric-flow.md), [extruder skipping](../defects/extruder-skipping.md), [flow and width](flow-width-and-gcode.md) |
| Pressure advance / linear advance | filament start G-code and printer firmware | `start_filament_gcode`, `start_gcode`, `gcode_flavor` | Klipper `[extruder] pressure_advance`; Marlin `M900 K` | [pressure advance](../tuning/pressure-advance.md), [ringing](../defects/ringing.md), [stringing](../defects/stringing.md) |
| Retraction | filament override, then printer | `filament_retract_*`, `filament_wipe`, `retract_*`, `wipe`, `use_firmware_retraction` | Klipper `[firmware_retraction]` when firmware retraction is enabled | [retraction](../tuning/retraction.md), [stringing](../defects/stringing.md), [zits and blobs](../defects/zits-blobs.md) |
| First layer | print and filament | `first_layer_height`, `first_layer_extrusion_width`, `first_layer_temperature`, `first_layer_bed_temperature`, `brim_width`, `elefant_foot_compensation` | Z offset, probe mesh, bed condition and mechanics | [first layer](../tuning/first-layer-squish.md), [poor bed adhesion](../defects/poor-bed-adhesion.md), [elephant foot](../defects/elephant-foot.md) |
| Melt, bonding and cooling | filament | `temperature`, `first_layer_temperature`, `cooling`, fan and layer-time keys | Chamber, ambient temperature and material drying | [temperature tuning](../tuning/temperature-tuning.md), [cooling](../tuning/cooling-layer-times.md), [layer adhesion](../defects/poor-layer-adhesion.md) |
| Motion and ringing | print, then printer | `*_speed`, `*_acceleration`, `machine_max_acceleration_*` | Klipper input shaper, `max_accel`, belts, frame and toolhead | [input shaping](../tuning/input-shaping.md), [ringing](../defects/ringing.md), [layer shift](../defects/layer-shift.md) |
| Geometry and feature behavior | print and printer | `layer_height`, `nozzle_diameter`, `*_extrusion_width`, `perimeters`, `infill_overlap`, seam and support keys | Actual nozzle, extrusion system and part orientation | [layer height and width](../fundamentals/layer-height-extrusion-width.md), [part orientation](../mechanical-properties/part-orientation.md), [bridges and overhangs](../defects/bridging-overhangs.md) |

The map distinguishes a slicer input from a physical cause. For example, raising `temperature` may be a useful controlled test for interlayer bonding, but it does not prove that temperature was the root cause if wet filament or excessive cooling was not controlled.

## Setting index (generated from the graph)

Every slicer key or firmware parameter that a fix or procedure touches, where it lives, and which causes change it in which direction. Generated from `fixed_by.sets`, `calibrates` and the filament-over-printer override rule.

<!-- generated:keymap -->
| Setting | Scope / set in | Changed by fixes for | Calibrated by | Overrides |
|---|---|---|---|---|
| `avoid_crossing_perimeters` | print (slicer) | [Travel crosses open air](../causes/travel-over-open-space.md) on | — | — |
| `bed_temperature` | filament (slicer) | [Bed temperature too high](../causes/bed-temp-too-high.md) ↓; [Bed temperature too low](../causes/bed-temp-too-low.md) ↑ | — | — |
| `bridge_flow_ratio` | print (slicer) | [Bridge flow or speed wrong](../causes/bridge-flow-or-speed-wrong.md) ↓ | — | — |
| `bridge_speed` | print (slicer) | [Bridge flow or speed wrong](../causes/bridge-flow-or-speed-wrong.md) ↓ | — | — |
| `brim_width` | print (slicer) | [Material shrinkage stress](../causes/material-shrinkage.md) ↑; [Small contact area](../causes/small-contact-area.md) ↑; [Supports too weak](../causes/support-too-weak.md) ↑ | — | — |
| `chamber_temperature` | filament (slicer) | [Chamber too cold for the material](../causes/chamber-too-cold.md) ↑ | — | — |
| `deretract_speed` | printer (slicer) | — | [Retraction](../tuning/retraction.md) | — |
| `elefant_foot_compensation` | print (slicer) | [Elephant-foot compensation too high](../causes/elephant-foot-compensation-too-high.md) ↓; [No elephant-foot compensation](../causes/elephant-foot-compensation-missing.md) ↑ | — | — |
| `enable_dynamic_overhang_speeds` | print (slicer) | [Overhangs printed too fast](../causes/overhang-too-fast.md) on | — | — |
| `external_perimeter_acceleration` | print (slicer) | [Acceleration or corner velocity too high](../causes/acceleration-too-high.md) ↓ | — | — |
| `external_perimeter_extrusion_width` | print (slicer) | [External perimeter too narrow](../causes/external-perimeter-too-narrow.md) ↑ | — | — |
| `external_perimeter_speed` | print (slicer) | [Print speed too high](../causes/print-speed-too-high.md) ↓ | — | — |
| `external_perimeters_first` | print (slicer) | [Perimeter order pushes walls out](../causes/perimeter-order.md) on | — | — |
| `extrusion_multiplier` | filament (slicer) | [Extrusion multiplier too high](../causes/em-too-high.md) ↓; [Extrusion multiplier too low](../causes/em-too-low.md) ↑ | [Extrusion multiplier (flow)](../tuning/extrusion-multiplier.md) | — |
| `extrusion_width` | print (slicer) | [Wall thinner than the extrusion width](../causes/wall-thinner-than-line-width.md) = | — | — |
| `fan_below_layer_time` | filament (slicer) | [Layer time too short](../causes/layer-time-too-short.md) ↑ | [Cooling and layer times](../tuning/cooling-layer-times.md) | — |
| `filament_deretract_speed` | filament (slicer) | — | [Retraction](../tuning/retraction.md) | `deretract_speed` |
| `filament_diameter` | filament (slicer) | [Wrong filament diameter setting](../causes/wrong-filament-diameter.md) = | — | — |
| `filament_max_volumetric_speed` | filament (slicer) | [Volumetric flow above the hotend limit](../causes/volumetric-flow-exceeded.md) ↓ | [Max volumetric flow](../tuning/max-volumetric-flow.md) | `max_volumetric_speed` |
| `filament_retract_length` | filament (slicer) | [Retraction too long or too fast](../causes/retraction-excessive.md) ↓; [Retraction too short or too slow](../causes/retraction-insufficient.md) ↑ | [Retraction](../tuning/retraction.md) | `retract_length` |
| `filament_retract_lift` | filament (slicer) | [No z-hop over printed surfaces](../causes/no-z-hop.md) ↑; [Z-hop too high](../causes/zhop-too-high.md) ↓ | — | `retract_lift` |
| `filament_retract_speed` | filament (slicer) | [Retraction too long or too fast](../causes/retraction-excessive.md) ↓; [Retraction too short or too slow](../causes/retraction-insufficient.md) ↑ | [Retraction](../tuning/retraction.md) | `retract_speed` |
| `filament_shrinkage_compensation_xy` | filament (slicer) | [Shrinkage not compensated](../causes/shrinkage-uncompensated.md) = | — | — |
| `filament_wipe` | filament (slicer) | [Seam start/stop pressure](../causes/seam-start-stop-pressure.md) on; [Travel crosses open air](../causes/travel-over-open-space.md) on | — | `wipe` |
| `fill_density` | print (slicer) | [Infill too sparse](../causes/infill-too-sparse.md) ↑ | — | — |
| `first_layer_bed_temperature` | filament (slicer) | [Bed temperature too high](../causes/bed-temp-too-high.md) ↓; [Bed temperature too low](../causes/bed-temp-too-low.md) ↑ | — | — |
| `first_layer_extrusion_width` | print (slicer) | [First-layer lines too thin](../causes/first-layer-lines-too-thin.md) ↑ | — | — |
| `first_layer_speed` | print (slicer) | [First layer printed too fast](../causes/first-layer-too-fast.md) ↓ | — | — |
| `first_layer_temperature` | filament (slicer) | — | [Temperature tuning](../tuning/temperature-tuning.md) | — |
| `infill_extrusion_width` | print (slicer) | [Infill lines too thin](../causes/infill-line-too-thin.md) ↑ | — | — |
| `infill_overlap` | print (slicer) | [Infill/perimeter overlap wrong](../causes/infill-overlap-wrong.md) = | [Infill/perimeter overlap](../tuning/infill-perimeter-overlap.md) | — |
| `infill_speed` | print (slicer) | [Infill printed too fast](../causes/infill-too-fast.md) ↓ | — | — |
| `layer_height` | print (slicer) | [Layer height too large for the nozzle](../causes/layer-height-too-large.md) ↓; [Layer height too small](../causes/layer-height-too-small.md) ↑ | — | — |
| `max_fan_speed` | filament (slicer) | [Insufficient part cooling](../causes/insufficient-cooling.md) ↑; [Too much part cooling](../causes/excessive-cooling.md) ↓ | [Cooling and layer times](../tuning/cooling-layer-times.md) | — |
| `max_volumetric_speed` | print (slicer) | — | [Max volumetric flow](../tuning/max-volumetric-flow.md) | — |
| `min_fan_speed` | filament (slicer) | [Insufficient part cooling](../causes/insufficient-cooling.md) ↑; [Too much part cooling](../causes/excessive-cooling.md) ↓ | [Cooling and layer times](../tuning/cooling-layer-times.md) | — |
| `min_print_speed` | filament (slicer) | — | [Cooling and layer times](../tuning/cooling-layer-times.md) | — |
| `only_retract_when_crossing_perimeters` | print (slicer) | [Unnecessary retractions](../causes/too-many-retractions.md) on | — | — |
| `perimeter_acceleration` | print (slicer) | [Acceleration or corner velocity too high](../causes/acceleration-too-high.md) ↓ | — | — |
| `perimeter_speed` | print (slicer) | [Print speed too high](../causes/print-speed-too-high.md) ↓ | — | — |
| `perimeters` | print (slicer) | [Too few perimeters](../causes/too-few-perimeters.md) ↑ | — | — |
| `retract_before_travel` | printer (slicer) | [Unnecessary retractions](../causes/too-many-retractions.md) ↑ | — | — |
| `retract_length` | printer (slicer) | — | [Retraction](../tuning/retraction.md) | — |
| `retract_lift` | printer (slicer) | [No z-hop over printed surfaces](../causes/no-z-hop.md) ↑; [Nozzle hits curled print](../causes/nozzle-strike-on-curled-part.md) ↑; [Z-hop too high](../causes/zhop-too-high.md) ↓ | — | — |
| `retract_restart_extra` | printer (slicer) | [Seam start/stop pressure](../causes/seam-start-stop-pressure.md) ↓ | — | — |
| `retract_speed` | printer (slicer) | — | [Retraction](../tuning/retraction.md) | — |
| `seam_position` | print (slicer) | [Random seam placement](../causes/seam-random.md) = | — | — |
| `skirts` | print (slicer) | [Extruder not primed](../causes/extruder-not-primed.md) ↑ | — | — |
| `slowdown_below_layer_time` | filament (slicer) | [Layer time too short](../causes/layer-time-too-short.md) ↑ | [Cooling and layer times](../tuning/cooling-layer-times.md) | — |
| `support_material` | print (slicer) | [Unsupported overhang or bridge](../causes/missing-supports.md) on | — | — |
| `support_material_contact_distance` | print (slicer) | [Support interface or gap wrong](../causes/support-interface-settings.md) = | — | — |
| `support_material_interface_layers` | print (slicer) | [Support interface or gap wrong](../causes/support-interface-settings.md) ↑ | — | — |
| `support_material_spacing` | print (slicer) | [Supports too weak](../causes/support-too-weak.md) ↓ | — | — |
| `support_material_xy_spacing` | print (slicer) | [Support interface or gap wrong](../causes/support-interface-settings.md) = | — | — |
| `temperature` | filament (slicer) | [Nozzle temperature too high](../causes/nozzle-temp-too-high.md) ↓; [Nozzle temperature too low](../causes/nozzle-temp-too-low.md) ↑ | [Temperature tuning](../tuning/temperature-tuning.md) | — |
| `thin_walls` | print (slicer) | [Wall thinner than the extrusion width](../causes/wall-thinner-than-line-width.md) on | — | — |
| `top_fill_pattern` | print (slicer) | [Small top islands (inherent)](../causes/small-island-geometry.md) = | — | — |
| `top_solid_infill_speed` | print (slicer) | [Small top islands (inherent)](../causes/small-island-geometry.md) ↓ | — | — |
| `top_solid_layers` | print (slicer) | [Too few top solid layers](../causes/top-layers-insufficient.md) ↑ | — | — |
| `top_solid_min_thickness` | print (slicer) | [Too few top solid layers](../causes/top-layers-insufficient.md) ↑ | — | — |
| `travel_speed` | print (slicer) | [Travel moves too slow](../causes/travel-too-slow.md) ↑ | — | — |
| `wipe` | printer (slicer) | [Seam start/stop pressure](../causes/seam-start-stop-pressure.md) on | — | — |
| `xy_size_compensation` | print (slicer) | [Shrinkage not compensated](../causes/shrinkage-uncompensated.md) = | — | — |
| `bed_mesh` | klipper | [Bed not level or mesh missing](../causes/bed-not-level-or-unmeshed.md) = | — | — |
| `firmware_retraction` | klipper | — | [Retraction](../tuning/retraction.md) | — |
| `input_shaper` | klipper | [Resonance not compensated](../causes/resonance-uncompensated.md) = | [Input shaping](../tuning/input-shaping.md) | — |
| `max_accel` | klipper | [Acceleration or corner velocity too high](../causes/acceleration-too-high.md) ↓ | [Input shaping](../tuning/input-shaping.md) | — |
| `pressure_advance` | klipper | [Pressure advance too high](../causes/pa-too-high.md) ↓; [Pressure advance too low](../causes/pa-too-low.md) ↑ | [Pressure advance / Linear advance](../tuning/pressure-advance.md) | — |
| `pressure_advance_smooth_time` | klipper | [Pressure advance smoothing too long](../causes/pa-smooth-time-too-high.md) ↓ | [Pressure advance / Linear advance](../tuning/pressure-advance.md) | — |
| `rotation_distance` | klipper | [Extruder not calibrated](../causes/extruder-not-calibrated.md) = | [Extruder calibration (rotation_distance / e-steps)](../tuning/extruder-calibration.md) | — |
| `run_current` | klipper | [Extruder motor current wrong](../causes/extruder-motor-current.md) =; [Stepper driver or wiring fault](../causes/stepper-driver-or-wiring.md) ? | — | — |
| `z_offset` | klipper | [Nozzle too close to the bed](../causes/z-offset-too-low.md) =; [Nozzle too far from the bed](../causes/z-offset-too-high.md) = | [First layer squish (Z offset)](../tuning/first-layer-squish.md) | — |
| `e_steps` | prusa-fw | [Extruder not calibrated](../causes/extruder-not-calibrated.md) = | [Extruder calibration (rotation_distance / e-steps)](../tuning/extruder-calibration.md) | — |
| `linear_advance` | prusa-fw | [Pressure advance too high](../causes/pa-too-high.md) ↓; [Pressure advance too low](../causes/pa-too-low.md) ↑ | [Pressure advance / Linear advance](../tuning/pressure-advance.md) | — |
| `z_offset` | prusa-fw | [Nozzle too close to the bed](../causes/z-offset-too-low.md) =; [Nozzle too far from the bed](../causes/z-offset-too-high.md) = | [First layer squish (Z offset)](../tuning/first-layer-squish.md) | — |
<!-- /generated:keymap -->

## Preset-type resolution

Use this order when translating a knowledge recommendation into a profile edit:

1. **Filament preset:** material temperature, cooling, flow multiplier, maximum volumetric speed, and filament-specific retraction or start G-code.
2. **Print preset:** layer height, widths, feature speeds, acceleration, infill, supports, seams and print-level volumetric limits.
3. **Printer preset:** nozzle diameter, machine limits, retraction defaults, firmware flavor and start/end G-code.
4. **Physical-printer preset:** the selected machine and host; it does not replace checks of the live firmware configuration.
5. **Firmware and hardware:** Klipper or printer firmware, nozzle condition, extruder, hotend, belts, chamber and bed. These can make a slicer-only change ineffective or unsafe.

The profile resolver's `[user]`, `[Vendor:Section]` and `[default]` source labels must be retained in any recommendation. A recommendation without that provenance is incomplete because changing an inherited vendor value may require a user override or a copied preset.[^repo-profiles]

## Symptom-to-setting workflow

For a photo or defect report, an agent should:

1. Identify the leading defect and one or two competing hypotheses.
2. Open the linked topic document in the table above and extract its discriminating test.
3. Resolve the active filament, print and printer profiles with `profiles.py show`; inspect both user overrides and inherited values.
4. Check firmware-side authority when the row names Klipper, linear/pressure advance, firmware retraction, input shaping or motion limits.
5. Compare the current value and source against the topic's evidence and operating conditions.
6. Propose one controlled change, its expected observation, and a rollback or validation test.

Do not jump directly from a symptom to a numeric value. First record material/product, nozzle, firmware, layer height, speed or volumetric flow, temperature, cooling, moisture state and whether the profile value is inherited. If a context dimension is unknown, state that uncertainty rather than filling it with a universal setting.

## Recommendation contract

Every setting recommendation returned by the skill should contain:

| Field | Required content |
|---|---|
| Diagnosis | Observable evidence and competing explanation if relevant |
| Profile | Printer, print and filament preset names |
| Type and key | Exact profile type and exact key, including firmware key when applicable |
| Current value | Effective value plus `[user]`, vendor or default source |
| Proposed test | One change, expected observation and test geometry |
| Conditions | Material, nozzle, layer height, speed/flow, temperature, cooling and moisture context |
| Knowledge link | Topic document and source-backed rationale |

This makes the answer actionable for a human and machine-readable for a later MCP retrieval or profile diff.

## Profile diff strategy

When a known-good print exists, compare profiles by type rather than comparing a flattened file blindly. Prioritize differences in this order: firmware/hardware authority, material temperature and cooling, maximum volumetric flow, extrusion multiplier, pressure advance, retraction, layer/width geometry, then feature speeds and supports. A difference is a candidate cause, not proof; validate it with the topic's discriminating test.

## Related topics

- [Calibration matrix](../tuning/calibration-matrix.md)
- [Slicer flow, width and firmware output](flow-width-and-gcode.md)
- [Klipper operating boundaries](../firmware/klipper-operating-boundaries.md)
- [Diagnostic matrix](../troubleshooting/diagnostic-matrix.md)

[^repo-profiles]: The repository's resolver conventions are aligned with the PrusaSlicer preset distribution and inheritance model; the live local profile and `profiles.py` output remain authoritative for this installation.
[^prusaslicer-source]: PrusaSlicer source and preset schemas document profile keys, generated extrusion geometry and firmware-specific G-code behavior.
[^klipper-docs]: Klipper documentation describes pressure advance, input shaping, motion limits and firmware-side configuration that may constrain slicer settings.

<!-- generated:relations -->
## Relations
- **Related:** [Slicer flow, width and firmware output](flow-width-and-gcode.md)
- **Linked from:** [Klipper operating boundaries](../firmware/klipper-operating-boundaries.md) · [FDM print defect diagnostic matrix](../troubleshooting/diagnostic-matrix.md)
<!-- /generated:relations -->
