---
type: cause
title: "Layer time too short"
description: "Small layers are printed before the previous one has solidified."
altLabel: [minimum layer time, Schichtzeit zu kurz]
facets: {phase: [cooling]}
check: "Defects only on small cross-sections or tips; printing several parts at once helps."
fixed_by:
  - {procedure: tuning/cooling-layer-times, action: "raise minimum layer time / slow down small layers", sets: [{key: slowdown_below_layer_time, direction: up}, {key: fan_below_layer_time, direction: up}]}
sources:
  - id: ellis-pla-overheating
    title: "Ellis Print Tuning Guide — PLA overheating"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/pla_overheating.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Layer time too short

Small layers are printed before the previous one has solidified.

**Check:** Defects only on small cross-sections or tips; printing several parts at once helps.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Cooling and layer times](../tuning/cooling-layer-times.md) (raise minimum layer time / slow down small layers) `slowdown_below_layer_time` ↑ `fan_below_layer_time` ↑
- **Causes:** [Overheating (esp. PLA in enclosures)](../defects/overheating.md) (#3; B)
<!-- /generated:relations -->
