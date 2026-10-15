---
type: procedure
title: First layer squish (Z offset)
description: Fine-tune nozzle-to-bed distance live with 0.01 mm babysteps using scattered test patches.
timestamp: 2026-10-13
calibrates: [klipper/z_offset, prusa-fw/z_offset]
sources:
  - id: ellis-first-layer-squish
    title: "Ellis Print Tuning Guide — First layer squish (Z offset)"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/first_layer_squish.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# First layer squish

## Symptoms
- **Too much squish:** lines fade or disappear, the surface is wavy, hairs or lumps appear on top.
- **Too little squish:** gaps between lines that let light through, and a gappy second layer. Heat soak and flow dropoff can look the same.
- **Target:** lines are clearly visible with no gaps. Pinholes where infill meets the perimeter are OK.

## Procedure
1. First layer height ≥ 0.25 mm. First layer line width ≥ 120%.[^ellis-first-layer-squish]
2. Scatter patches over the bed, then babystep 0.01 mm during the print (Klipper: `SET_GCODE_OFFSET Z_ADJUST=±0.01 MOVE=1`).[^ellis-first-layer-squish]
3. Save: `Z_OFFSET_APPLY_PROBE` (probe as virtual endstop) or `Z_OFFSET_APPLY_ENDSTOP`, then `SAVE_CONFIG`. Marlin: `M500`.
4. Textured PEI: judge from the top surface, and it usually needs a bit more squish.

## PrusaSlicer keys
- print: `first_layer_height`, `first_layer_extrusion_width`, `first_layer_speed`
- printer: `z_offset` (a slicer-side offset; prefer firmware Z offset)
- filament: `first_layer_temperature`, `first_layer_bed_temperature`

## Related
[Bed adhesion](../defects/poor-bed-adhesion.md) · [First layer inconsistency](../defects/first-layer-inconsistency.md) · [Elephant foot](../defects/elephant-foot.md)

[^ellis-first-layer-squish]: Ellis Print Tuning Guide — First layer squish

<!-- generated:relations -->
## Relations
- **Fixes:** [Nozzle too far from the bed](../causes/z-offset-too-high.md) (lower Z in 0.01 mm babysteps) · [Nozzle too close to the bed](../causes/z-offset-too-low.md) (raise Z in 0.01 mm babysteps)
- **Calibrates:** `klipper/z_offset` · `prusa-fw/z_offset`
- **Linked from:** [Elephant foot](../defects/elephant-foot.md) · [Poor bed adhesion](../defects/poor-bed-adhesion.md) · [Under-extrusion](../defects/under-extrusion.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
