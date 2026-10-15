---
type: procedure
title: Tuning order
description: The order in which to calibrate a printer/filament so later steps aren't invalidated by earlier ones.
tags: [tuning, order, ellis]
timestamp: 2026-10-13
sources:
  - id: ellis-Print-Tuning-Guide
    title: "Ellis Print Tuning Guide — Tuning order"
    resource: https://ellis3dp.com/Print-Tuning-Guide/
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Tuning order

Calibrate before you tweak. Each step assumes the previous ones are done. Before blaming a setting for a defect, check that its prerequisites hold.

1. [Extruder calibration](extruder-calibration.md): per printer, firmware-side.
2. [Build surface prep](build-surface.md): clean the plate.
3. [First layer squish](first-layer-squish.md): Z offset.
4. [Pressure advance](pressure-advance.md): per filament and per printer.
5. [Extrusion multiplier](extrusion-multiplier.md): per filament.
6. [Cooling and layer times](cooling-layer-times.md): per filament.
7. [Retraction](retraction.md): usually only needed if stringing remains after steps 1–6.
8. [Infill/perimeter overlap](infill-perimeter-overlap.md): cosmetic, last.
9. [Max volumetric flow](max-volumetric-flow.md): independent. Do it once per hotend/nozzle/material family.

Re-tune pressure advance after changing the filament, nozzle, hotend, extruder, Bowden length, a large temperature step, or input shaper.

Rule of thumb when a photo shows a defect: change **one** variable at a time and choose the cheapest likely fix first. Mechanical and moisture causes often outrank slicer settings.

<!-- generated:relations -->
## Relations
- **Related:** [Calibration matrix and dependency order](calibration-matrix.md)
- **Linked from:** [Extruder calibration (rotation_distance / e-steps)](extruder-calibration.md) · [Pressure advance / Linear advance](pressure-advance.md)
<!-- /generated:relations -->
