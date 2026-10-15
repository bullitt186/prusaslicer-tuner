---
type: cause
title: "Nozzle temperature too low"
description: "Plastic that is too cold flows poorly and bonds weakly to the previous layer or perimeter; at high flow it can make the extruder skip."
altLabel: [hotend too cold, printing too cold, Düsentemperatur zu niedrig, zu kalt gedruckt]
facets: {phase: [thermal]}
check: "Raise temperature in 5–10 °C steps (starting value) with everything else fixed; better bonding or fewer skips confirm it."
fixed_by:
  - {procedure: tuning/temperature-tuning, action: "raise within the material window", sets: [{key: temperature, direction: up}]}
sources:
  - id: ellis-extruder-skipping
    title: "Ellis Print Tuning Guide — Extruder skipping"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
  - id: ellis-layer-adhesion
    title: "Ellis Print Tuning Guide — Poor layer adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/poor_layer_adhesion.html
  - id: ellis-perimeter-separation
    title: "Ellis Print Tuning Guide — Perimeter separation"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/perimeter_separation.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Nozzle temperature too low

Plastic that is too cold flows poorly and bonds weakly to the previous layer or perimeter; at high flow it can make the extruder skip.

**Check:** Raise temperature in 5–10 °C steps (starting value) with everything else fixed; better bonding or fewer skips confirm it.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Temperature tuning](../tuning/temperature-tuning.md) (raise within the material window) `temperature` ↑
- **Causes:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (#7; B) · [Gaps between infill and walls](../defects/infill-wall-gaps.md) (#3; C) · [Perimeter separation](../defects/perimeter-separation.md) (#6; B) · [Poor layer adhesion](../defects/poor-layer-adhesion.md) (#3; B)
<!-- /generated:relations -->
