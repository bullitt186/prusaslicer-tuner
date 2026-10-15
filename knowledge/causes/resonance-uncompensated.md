---
type: cause
title: "Resonance not compensated"
description: "Frame and toolhead resonances echo after sharp features when input shaping is missing or stale."
altLabel: [no input shaper, input shaper not calibrated, Resonanz, Input Shaper fehlt]
facets: {phase: [motion]}
check: "Ripples decay after corners with a spacing that changes with speed; measure with an accelerometer."
fixed_by:
  - {procedure: tuning/input-shaping, action: "calibrate the input shaper", sets: [{key: klipper/input_shaper, direction: set}]}
sources:
  - id: klipper-resonance
    title: "Klipper — Resonance compensation"
    resource: https://www.klipper3d.org/Resonance_Compensation.html
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:55:00Z
status: stable
---
# Resonance not compensated

Frame and toolhead resonances echo after sharp features when input shaping is missing or stale.[^klipper-resonance]

**Check:** Ripples decay after corners with a spacing that changes with speed; measure with an accelerometer.[^klipper-resonance]

[^klipper-resonance]: Klipper — Resonance compensation

<!-- generated:relations -->
## Relations
- **Fixed by:** [Input shaping](../tuning/input-shaping.md) (calibrate the input shaper) `input_shaper` =
- **Causes:** [Ringing / ghosting](../defects/ringing.md) (#1; C)
<!-- /generated:relations -->
