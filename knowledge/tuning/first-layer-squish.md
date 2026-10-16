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
  - id: ellis-test-prints
    title: "Ellis Print Tuning Guide — test_prints folder (STL files)"
    resource: https://github.com/AndrewEllis93/Print-Tuning-Guide/tree/main/test_prints
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

## Test prints
Get the files with the MCP tool `test_prints("First_Layer_Patch")`.[^ellis-test-prints]

| File | Use when the first layer height is |
|---|---|
| `First_Layer_Patch-0.2mm.stl` | 0.20 mm |
| `First_Layer_Patch-0.24mm.stl` | 0.24 mm |
| `First_Layer_Patch-0.25mm.stl` | 0.25 mm (Ellis' recommendation) |
| `First_Layer_Patch-0.3mm.stl` | 0.30 mm |

- **When:** after a nozzle, build-plate sheet, probe or toolhead change; after a change in first layer height; and when the bed adhesion or first-layer look gets worse. Retune for each sheet type, since textured PEI needs more squish than smooth PEI.
- **How:** match the patch to `first_layer_height`, because a patch that is one layer thick shows the squish of exactly one layer. Place five or more patches over the bed: the four corners and the center, plus the areas where you usually print. Print them all in one job and babystep while the patches are printing. Judge the squish from the patch closest to the center. If the patches disagree with each other, the cause is bed mesh, thermal drift or gantry tilt, not the Z offset. See [first layer inconsistency](../defects/first-layer-inconsistency.md) and [thermal drift](thermal-drift.md).
- Heat-soak the printer as you do for real prints, otherwise the offset drifts later.

## PrusaSlicer keys
- print: `first_layer_height`, `first_layer_extrusion_width`, `first_layer_speed`
- printer: `z_offset` (a slicer-side offset; prefer firmware Z offset)
- filament: `first_layer_temperature`, `first_layer_bed_temperature`

## Related
[Bed adhesion](../defects/poor-bed-adhesion.md) · [First layer inconsistency](../defects/first-layer-inconsistency.md) · [Elephant foot](../defects/elephant-foot.md)

[^ellis-first-layer-squish]: Ellis Print Tuning Guide — First layer squish
[^ellis-test-prints]: Ellis Print Tuning Guide — test_prints folder

<!-- generated:relations -->
## Relations
- **Fixes:** [Nozzle too far from the bed](../causes/z-offset-too-high.md) (lower Z in 0.01 mm babysteps) · [Nozzle too close to the bed](../causes/z-offset-too-low.md) (raise Z in 0.01 mm babysteps)
- **Calibrates:** `klipper/z_offset` · `prusa-fw/z_offset`
- **Linked from:** [Elephant foot](../defects/elephant-foot.md) · [Poor bed adhesion](../defects/poor-bed-adhesion.md) · [Under-extrusion](../defects/under-extrusion.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Extrusion multiplier (flow)](extrusion-multiplier.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
