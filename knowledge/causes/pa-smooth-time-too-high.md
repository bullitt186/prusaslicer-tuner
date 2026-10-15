---
type: cause
title: "Pressure advance smoothing too long"
description: "Klipper smooths PA over a time window; on short top-infill segments a long window leaves excess pressure."
altLabel: [pressure_advance_smooth_time too high, PA-Glättung zu lang]
facets: {phase: [extrusion]}
check: "Lower pressure_advance_smooth_time (then re-test PA) and compare small top islands."
fixed_by:
  - {procedure: tuning/pressure-advance, action: "lower smooth time, then re-tune PA", sets: [{key: klipper/pressure_advance_smooth_time, direction: down}]}
sources:
  - id: ellis-small-infill
    title: "Ellis Print Tuning Guide — Small infill areas look overextruded"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/small_infill_areas_overextruded.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Pressure advance smoothing too long

Klipper smooths PA over a time window; on short top-infill segments a long window leaves excess pressure.

**Check:** Lower pressure_advance_smooth_time (then re-test PA) and compare small top islands.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Pressure advance / Linear advance](../tuning/pressure-advance.md) (lower smooth time, then re-tune PA) `pressure_advance_smooth_time` ↓
- **Causes:** [Small infill areas look overextruded](../defects/small-infill-overextruded.md) (#2; B)
<!-- /generated:relations -->
