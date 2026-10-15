---
type: cause
title: "Extrusion multiplier too high"
description: "More plastic than the line volume: ridged top surfaces, oversize parts, pushed-out perimeters and extra ooze."
altLabel: [flow too high, overextrusion flow, Flow zu hoch, Extrusionsmultiplikator zu hoch]
facets: {phase: [extrusion]}
check: "Print the EM cubes; top surfaces become smooth and dimensions correct at a lower value."
fixed_by:
  - {procedure: tuning/extrusion-multiplier, action: "lower in 2 % then 0.5 % steps", sets: [{key: extrusion_multiplier, direction: down}]}
sources:
  - id: ellis-bulging
    title: "Ellis Print Tuning Guide — Bulging"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/bulging.html
  - id: ellis-retraction
    title: "Ellis Print Tuning Guide — Retraction"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Extrusion multiplier too high

More plastic than the line volume: ridged top surfaces, oversize parts, pushed-out perimeters and extra ooze.

**Check:** Print the EM cubes; top surfaces become smooth and dimensions correct at a lower value.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Extrusion multiplier (flow)](../tuning/extrusion-multiplier.md) (lower in 2 % then 0.5 % steps) `extrusion_multiplier` ↓
- **Causes:** [Bulging](../defects/bulging.md) (#3; B) · [Dimensional inaccuracy](../defects/dimensional-inaccuracy.md) (#2; B) · [Over-extrusion](../defects/over-extrusion.md) (#1; B) · [Stringing / oozing](../defects/stringing.md) (#4; B) · [Scars on top surfaces](../defects/top-surface-scars.md) (#1; B)
<!-- /generated:relations -->
