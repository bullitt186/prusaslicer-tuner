---
type: cause
title: "Acceleration or corner velocity too high"
description: "High accelerations excite resonances, cause bulging at corners and can skip steps."
altLabel: [accel too high, square corner velocity too high, Beschleunigung zu hoch]
facets: {phase: [motion]}
check: "Print at lower acceleration (or run TEST_SPEED); ringing, bulges or shifts shrink."
fixed_by:
  - {procedure: tuning/input-shaping, action: "lower accel within what the shaper supports", sets: [{key: external_perimeter_acceleration, direction: down}, {key: perimeter_acceleration, direction: down}, {key: klipper/max_accel, direction: down}]}
sources:
  - id: ellis-bulging
    title: "Ellis Print Tuning Guide — Bulging"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/bulging.html
  - id: ellis-layer-shifting
    title: "Ellis Print Tuning Guide — Layer shifting"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/layer_shifting.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Acceleration or corner velocity too high

High accelerations excite resonances, cause bulging at corners and can skip steps.

**Check:** Print at lower acceleration (or run TEST_SPEED); ringing, bulges or shifts shrink.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Input shaping](../tuning/input-shaping.md) (lower accel within what the shaper supports) `external_perimeter_acceleration` ↓ `perimeter_acceleration` ↓ `max_accel` ↓
- **Causes:** [Bulging](../defects/bulging.md) (#2; B) · [Layer shifting](../defects/layer-shift.md) (#5; B) · [Ringing / ghosting](../defects/ringing.md) (#3; B)
<!-- /generated:relations -->
