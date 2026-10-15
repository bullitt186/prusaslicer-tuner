---
type: procedure
title: Max volumetric flow
description: Find how many mm³/s the hotend can melt; cap it per filament so speed never outruns the hotend.
timestamp: 2026-10-13
calibrates: [filament_max_volumetric_speed, max_volumetric_speed]
sources:
  - id: ellis-determining-max-volumetric-flow-rate
    title: "Ellis Print Tuning Guide — Max volumetric flow"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/determining_max_volumetric_flow_rate.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Max volumetric flow

- 1.75 mm filament: mm³ = mm × 2.4. Speed = flow ÷ (layer height × line width). For example, 24 mm³/s at 0.2 × 0.4 ≈ 300 mm/s.
- Test: `M83`, then `G1 E100 F<mm/s×60>` at increasing speeds until less than about 97–98 mm goes in. Verify with 200–300 mm, then use a value **slightly below** the result, since real prints add back pressure.
- Typical values for a 0.4 brass nozzle: V6/Revo 11, Dragon SF 15, Dragon HF 24, Rapido HF 24, Rapido UHF 30. Hardened steel flows less, and CHT nozzles flow more.
- Higher temperature raises the achievable flow but adds ooze.
- Too close to the limit leads to [extruder skipping](../defects/extruder-skipping.md), [under-extrusion](../defects/under-extrusion.md) and perimeter gaps.

## PrusaSlicer keys
filament: `filament_max_volumetric_speed` (the per-material cap; use it) · print: `max_volumetric_speed` (global cap, 0 = off). The lower of the two applies.

<!-- generated:relations -->
## Relations
- **Fixes:** [Volumetric flow above the hotend limit](../causes/volumetric-flow-exceeded.md) (measure the limit and cap flow per filament)
- **Calibrates:** `key/filament_max_volumetric_speed` · `key/max_volumetric_speed`
- **Linked from:** [Extruder skipping / clicking](../defects/extruder-skipping.md) · [Under-extrusion](../defects/under-extrusion.md) · [TPU (flexible)](../materials/tpu.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Extrusion multiplier (flow)](extrusion-multiplier.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
