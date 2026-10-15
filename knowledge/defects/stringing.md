---
type: defect
title: Stringing / oozing
description: Thin strings or wisps between separate parts of a print. Usually moisture, temperature, PA or retraction — in that rough order.
timestamp: 2026-10-13
altLabel: [oozing, whiskers, hairy prints, spider webs, Fäden, Fädenziehen, Spinnweben, web-like strings]
facets: {phase: [retraction-travel]}
caused_by:
  - {cause: causes/wet-filament, rank: 1, evidence: B, source: ellis-retraction}
  - {cause: causes/nozzle-temp-too-high, rank: 2, evidence: B, source: [ellis-retraction, tsg-s3d]}
  - {cause: causes/pa-too-low, rank: 3, evidence: B, source: ellis-retraction}
  - {cause: causes/em-too-high, rank: 4, evidence: B, source: ellis-retraction}
  - {cause: causes/zhop-too-high, rank: 5, evidence: B, source: ellis-retraction}
  - {cause: causes/retraction-insufficient, rank: 6, evidence: B, source: [ellis-retraction, tsg-s3d, tsg-all3dp]}
  - {cause: causes/travel-over-open-space, rank: 7, evidence: B, source: [ellis-retraction, tsg-s3d, tsg-all3dp]}
  - {cause: causes/extruder-gear-backlash-or-wear, rank: 8, evidence: B, source: ellis-retraction}
  - {cause: causes/nozzle-worn-or-leaking, rank: 9, evidence: B, source: [ellis-retraction, tsg-s3d]}
  - {cause: causes/travel-too-slow, rank: 10, evidence: B, source: tsg-s3d}
sources:
  - id: ellis-retraction
    title: Ellis Print Tuning Guide — Retraction
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-all3dp
    title: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-migration
  at: 2026-10-13 23:00:00+00:00
---
# Stringing

## How it looks
Fine hairs or "spider web" strings between towers, islands or features, and blobs where travel ends.

## Causes and fixes (cheapest and most likely first)
1. **Wet filament**, especially PETG, nylon and TPU. Popping or steam when extruding in midair confirms it. Dry the filament; nothing else will fix it.
2. **Temperature too high.** Lower `temperature` in 5 °C steps (stay inside the material window; see [PLA](../materials/pla.md) or the relevant material topic). For PC/PC-CF, a lower temperature costs surface finish and layer bonding, so try PA and retraction first ([PC / PC-CF](../materials/pc-cf.md)).[^ellis-retraction]
3. **Pressure advance too low.** Raise it per [pressure advance](../tuning/pressure-advance.md). It often reduces the retraction needed.
4. **Over-extrusion.** Check `extrusion_multiplier` ([EM](../tuning/extrusion-multiplier.md)).
5. **Excessive z-hop.** `retract_lift` / `filament_retract_lift` above 0.2–0.3 mm strings more.[^ellis-retraction]
6. **Retraction length or speed.** Direct drive: 0.5–1 mm at 30–35 mm/s. Bowden: about 1 mm and up. See [retraction](../tuning/retraction.md).[^ellis-retraction]
7. **Travel crosses open air.** Enable `avoid_crossing_perimeters` (print), and consider `wipe` / `filament_wipe`. This only helps when there is a path around the gap: holes and cut-outs inside a single island. Between **separate islands** (two towers, the two prongs of a U-shaped part) the nozzle has to cross open air anyway, so only temperature, PA and retraction help there.
8. **Mechanical:** extruder backlash or a loose grub screw (a dead zone on reversal), Bowden tube moving in its coupling, a dirty, worn or leaking nozzle (hot-tighten it).
9. **PETG strings inherently.** Some stringing may be unavoidable.

## Keys to read first
filament: `temperature`, `filament_retract_length`, `filament_retract_speed`, `filament_deretract_speed`, `filament_retract_lift`, `filament_wipe`, `extrusion_multiplier`, `start_filament_gcode` (PA)
printer: `retract_length`, `retract_speed`, `deretract_speed`, `retract_lift`, `wipe`, `use_firmware_retraction`
print: `avoid_crossing_perimeters`, `travel_speed`
Klipper: `[extruder] pressure_advance`, `[firmware_retraction]`

Remember that `filament_retract_*` values other than `nil` override the `retract_*` values in the printer profile.

[^ellis-retraction]: Ellis Print Tuning Guide — Retraction

<!-- generated:relations -->
## Relations
- **Caused by:** [Wet filament](../causes/wet-filament.md) (#1; B) · [Nozzle temperature too high](../causes/nozzle-temp-too-high.md) (#2; B) · [Pressure advance too low](../causes/pa-too-low.md) (#3; B) · [Extrusion multiplier too high](../causes/em-too-high.md) (#4; B) · [Z-hop too high](../causes/zhop-too-high.md) (#5; B) · [Retraction too short or too slow](../causes/retraction-insufficient.md) (#6; B) · [Travel crosses open air](../causes/travel-over-open-space.md) (#7; B) · [Extruder gear backlash, play or wear](../causes/extruder-gear-backlash-or-wear.md) (#8; B) · [Worn, dirty or leaking nozzle](../causes/nozzle-worn-or-leaking.md) (#9; B) · [Travel moves too slow](../causes/travel-too-slow.md) (#10; B)
- **Related:** [Scars on top surfaces](top-surface-scars.md)
- **Materials prone to this:** [Nylon (PA)](../materials/nylon.md) (B) · [PC / PC-CF](../materials/pc-cf.md) (C) · [PETG](../materials/petg.md) (B) · [TPU (flexible)](../materials/tpu.md) (B)
- **Linked from:** [Zits, blobs & visible seam](zits-blobs.md) · [Filament drying and moisture](../materials/filament-moisture.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [FDM print defect diagnostic matrix](../troubleshooting/diagnostic-matrix.md) · [Pressure advance / Linear advance](../tuning/pressure-advance.md) · [Retraction](../tuning/retraction.md)
<!-- /generated:relations -->
