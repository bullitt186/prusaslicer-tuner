---
type: cause
title: "Too much part cooling"
description: "Strong cooling freezes the line before it fuses: weak layers, perimeter separation and warping in shrinking materials."
altLabel: [fan too high, zu viel Kühlung, Lüfter zu stark]
facets: {phase: [cooling]}
check: "Lower fan and compare bonding or warping on identical geometry."
fixed_by:
  - {procedure: tuning/cooling-layer-times, action: "reduce part cooling", sets: [{key: max_fan_speed, direction: down}, {key: min_fan_speed, direction: down}]}
sources:
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
# Too much part cooling

Strong cooling freezes the line before it fuses: weak layers, perimeter separation and warping in shrinking materials.

**Check:** Lower fan and compare bonding or warping on identical geometry.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Cooling and layer times](../tuning/cooling-layer-times.md) (reduce part cooling) `max_fan_speed` ↓ `min_fan_speed` ↓
- **Causes:** [Perimeter separation](../defects/perimeter-separation.md) (#7; B) · [Poor bed adhesion](../defects/poor-bed-adhesion.md) (#9; B) · [Poor layer adhesion](../defects/poor-layer-adhesion.md) (#4; B) · [Warping / corner lifting](../defects/warping.md) (#2; B)
<!-- /generated:relations -->
