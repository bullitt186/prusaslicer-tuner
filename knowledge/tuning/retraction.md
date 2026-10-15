---
type: procedure
title: Retraction
description: Tune retraction length/speed only after PA, EM, moisture and mechanics are ruled out; small values for direct drive.
timestamp: 2026-10-13
calibrates: [filament_retract_length, filament_retract_speed, filament_deretract_speed, retract_length, retract_speed, deretract_speed, klipper/firmware_retraction]
sources:
  - id: ellis-retraction
    title: "Ellis Print Tuning Guide — Retraction"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Retraction

Often a sensible default is enough. Tune only if [stringing](../defects/stringing.md) persists after pressure advance, EM, dry filament and a mechanical check.

## Starting values
| | Direct drive | Bowden |
|---|---|---|
| Length | 0.5 mm (stay < 1 mm, never > 2 mm) | 1 mm (setup dependent) |
| Speed | 30–35 mm/s retract and deretract | 30–35 mm/s |
| Tower step | 0.1 mm | 0.5 mm |
- Z-hop (`retract_lift`): 0.2–0.3 mm at most. More hop **increases** stringing.
- Retraction that's too fast and retraction that's too slow can both string.

## Tower procedure (Ellis, SuperSlicer tool)
Fan 80–100%. Three towers about 10 °C apart, starting about 10 °C above your normal temperature. Choose 1–2 rings above the point where stringing stops. In PrusaSlicer you can approximate this with a height range modifier or by printing separate test objects per value.

## PrusaSlicer keys, and override precedence
- printer (per extruder): `retract_length`, `retract_speed`, `deretract_speed`, `retract_lift`, `retract_lift_above`, `retract_lift_below`, `retract_before_travel`, `retract_layer_change`, `wipe`, `retract_before_wipe`, `retract_restart_extra`, `travel_ramping_lift`, `travel_slope`, `travel_max_lift`, `use_firmware_retraction`
- filament: `filament_retract_length`, `filament_retract_speed`, `filament_deretract_speed`, `filament_retract_lift`, `filament_wipe`, … **A filament value other than `nil` overrides the printer value.** Always check both. Prefer filament-level changes for material-specific fixes.
- print: `avoid_crossing_perimeters` (keeps travel inside the part, which helps PETG), `only_retract_when_crossing_perimeters`
- Klipper: with `use_firmware_retraction = 1`, the values come from `[firmware_retraction]` in `printer.cfg`, not from the slicer.

## Related
[Stringing](../defects/stringing.md) · [Pressure advance](pressure-advance.md) · [PETG](../materials/petg.md)

<!-- generated:relations -->
## Relations
- **Fixes:** [Retraction too long or too fast](../causes/retraction-excessive.md) (shorten and slow retraction) · [Retraction too short or too slow](../causes/retraction-insufficient.md) (raise length, then speed (direct drive stays small))
- **Related:** [Current Klipper calibration and compatibility notes](../firmware/klipper-current.md)
- **Calibrates:** `key/deretract_speed` · `key/filament_deretract_speed` · `key/filament_retract_length` · `key/filament_retract_speed` · `key/retract_length` · `key/retract_speed` · `klipper/firmware_retraction`
- **Linked from:** [Stringing / oozing](../defects/stringing.md) · [Filament drying and moisture](../materials/filament-moisture.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
