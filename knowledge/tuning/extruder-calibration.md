---
type: procedure
title: Extruder calibration (rotation_distance / e-steps)
description: Make 100 mm commanded equal 100 mm extruded; per-printer firmware value, not a slicer setting.
timestamp: 2026-10-13
calibrates: [klipper/rotation_distance, prusa-fw/e_steps]
sources:
  - id: ellis-extruder-calibration
    title: "Ellis Print Tuning Guide — Extruder calibration (rotation_distance / e-steps)"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/extruder_calibration.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Extruder calibration

**Scope:** printer firmware (Klipper `[extruder] rotation_distance`; Marlin `M92 E`). This is **not** in PrusaSlicer profiles. Don't confuse it with the per-filament [extrusion multiplier](extrusion-multiplier.md).

## Procedure (summary)
- Klipper: temporarily set `max_extrude_only_distance: 101` (and `min_extrude_temp: 0` for a cold test), then `RESTART`.
- Bowden: test cold, with the tube disconnected. Direct drive: testing hot is acceptable, but repeat the test to confirm it's consistent.
- Mark 120 mm above the extruder entry, then send `M83` and `G1 E100 F60` (1 mm/s). Measure what's left: actual = 120 − remaining.
- Klipper: `new_rd = old_rd × actual / 100`. Try it with `SET_EXTRUDER_ROTATION_DISTANCE EXTRUDER=extruder DISTANCE=<v>` and iterate, always from the latest value. Save it in `printer.cfg` and run `RESTART`.
- Marlin: `new = old × 100 / actual`, then `M92 E<v>` and `M500`.
- Inconsistent results between runs point to a mechanical problem or a partial clog, not to calibration.

## Related
[Tuning order](tuning-order.md) · [Pressure advance](pressure-advance.md) · [Extruder skipping](../defects/extruder-skipping.md)

<!-- generated:relations -->
## Relations
- **Fixes:** [Extruder not calibrated](../causes/extruder-not-calibrated.md) (calibrate rotation distance / e-steps)
- **Calibrates:** `klipper/rotation_distance` · `prusa-fw/e_steps`
- **Linked from:** [Under-extrusion](../defects/under-extrusion.md) · [Extrusion multiplier (flow)](extrusion-multiplier.md) · [Pressure advance / Linear advance](pressure-advance.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
