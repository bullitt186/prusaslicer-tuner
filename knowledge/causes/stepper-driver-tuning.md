---
type: cause
title: "Stepper driver tuning artifacts"
description: "Driver chopper settings can add fine periodic wall artifacts on X/Y. Community values are experimental."
altLabel: [TMC tuning, Treiber-Tuning]
facets: {phase: [mechanics]}
check: "Artifacts only on one motion pair and unchanged by belts/bearings."
fixed_by:
  - {action: "experiment with driver settings (microsteps, interpolate, stealthChop off)"}
sources:
  - id: ellis-vfas
    title: "Ellis Print Tuning Guide — VFAs"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/vfas.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Stepper driver tuning artifacts

Driver chopper settings can add fine periodic wall artifacts on X/Y. Community values are experimental.

**Check:** Artifacts only on one motion pair and unchanged by belts/bearings.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (experiment with driver settings (microsteps, interpolate, stealthChop off))
- **Causes:** [VFAs (vertical fine artifacts)](../defects/vfas.md) (#3; D)
<!-- /generated:relations -->
