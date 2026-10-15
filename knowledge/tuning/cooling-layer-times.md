---
type: procedure
title: Cooling and layer times
description: Enough part cooling plus a minimum layer time so each layer solidifies before the next.
timestamp: 2026-10-13
calibrates: [max_fan_speed, min_fan_speed, slowdown_below_layer_time, fan_below_layer_time, min_print_speed]
sources:
  - id: ellis-cooling-and-layer-times
    title: "Ellis Print Tuning Guide — Cooling and layer times"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/cooling_and_layer_times.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Cooling and layer times

## Symptoms of too little cooling
Soft or droopy small features, curled overhangs, melted tips, a glossy blobby top on small parts, and [bulging](../defects/bulging.md) on small layers.

## Guidance
- Keep the fan speed **consistent**. Changing it during the print causes banding.
- Set a minimum layer time so small layers slow down. Printing several parts spaced apart also gives each layer more time.
- PLA: more cooling is better (open the enclosure; see [overheating](../defects/overheating.md)).
- ABS/ASA in a hot chamber needs more fan than you'd expect. Ellis' example with a 5015 fan mod and a 63 °C chamber: 40–50% for large plates, up to 80% for small plates, up to 100% for single small parts, with a 15 s minimum layer time.
- Large ABS/ASA parts: be conservative with fan to avoid [warping](../defects/warping.md), and raise it only for overhangs.
- If parts curl even at low fan, it's an adhesion problem. See [poor bed adhesion](../defects/poor-bed-adhesion.md).
- Too much cooling slightly reduces strength, especially on PLA.

## PrusaSlicer keys (filament)
`cooling`, `fan_always_on`, `min_fan_speed`, `max_fan_speed`, `bridge_fan_speed`, `disable_fan_first_layers`, `fan_below_layer_time`, `slowdown_below_layer_time`, `min_print_speed`, `enable_dynamic_fan_speeds`, `overhang_fan_speed_0..3`

<!-- generated:relations -->
## Relations
- **Fixes:** [Too much part cooling](../causes/excessive-cooling.md) (reduce part cooling) · [Insufficient part cooling](../causes/insufficient-cooling.md) (raise part cooling) · [Layer time too short](../causes/layer-time-too-short.md) (raise minimum layer time / slow down small layers) · [Nozzle hits curled print](../causes/nozzle-strike-on-curled-part.md) (fix curling; use a small z-hop)
- **Calibrates:** `key/fan_below_layer_time` · `key/max_fan_speed` · `key/min_fan_speed` · `key/min_print_speed` · `key/slowdown_below_layer_time`
- **Linked from:** [Bulging](../defects/bulging.md) · [Layer shifting](../defects/layer-shift.md) · [Overheating (esp. PLA in enclosures)](../defects/overheating.md) · [Warping / corner lifting](../defects/warping.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
