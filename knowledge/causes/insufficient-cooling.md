---
type: cause
title: "Insufficient part cooling"
description: "Plastic stays soft: sagging bridges, curled overhangs, melted small features."
altLabel: [not enough fan, zu wenig Kühlung, Lüfter zu schwach]
facets: {phase: [cooling]}
check: "Compare with higher fan and a cooler ambient; problems concentrate on small or overhanging features."
fixed_by:
  - {procedure: tuning/cooling-layer-times, action: "raise part cooling", sets: [{key: max_fan_speed, direction: up}, {key: min_fan_speed, direction: up}]}
sources:
  - id: ellis-bulging
    title: "Ellis Print Tuning Guide — Bulging"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/bulging.html
  - id: ellis-pla-overheating
    title: "Ellis Print Tuning Guide — PLA overheating"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/pla_overheating.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Insufficient part cooling

Plastic stays soft: sagging bridges, curled overhangs, melted small features.

**Check:** Compare with higher fan and a cooler ambient; problems concentrate on small or overhanging features.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Cooling and layer times](../tuning/cooling-layer-times.md) (raise part cooling) `max_fan_speed` ↑ `min_fan_speed` ↑
- **Causes:** [Poor bridges & overhangs](../defects/bridging-overhangs.md) (#1; B) · [Bulging](../defects/bulging.md) (#6; B) · [Overheating (esp. PLA in enclosures)](../defects/overheating.md) (#2; B) · [Gaps or pillowing in top layers](../defects/top-surface-gaps.md) (#4; C)
<!-- /generated:relations -->
