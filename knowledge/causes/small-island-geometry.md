---
type: cause
title: "Small top islands (inherent)"
description: "Short top-infill segments always look slightly overextruded; partly normal."
altLabel: [small infill areas, kleine Inseln]
facets: {phase: [top-bottom]}
check: "Only small islands look rough while wide areas are fine: judge EM on wide areas."
fixed_by:
  - {action: "monotonic top fill, slower top infill", sets: [{key: top_fill_pattern, direction: set}, {key: top_solid_infill_speed, direction: down}]}
sources:
  - id: ellis-small-infill
    title: "Ellis Print Tuning Guide — Small infill areas look overextruded"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/small_infill_areas_overextruded.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Small top islands (inherent)

Short top-infill segments always look slightly overextruded; partly normal.

**Check:** Only small islands look rough while wide areas are fine: judge EM on wide areas.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (monotonic top fill, slower top infill) `top_fill_pattern` = `top_solid_infill_speed` ↓
- **Causes:** [Small infill areas look overextruded](../defects/small-infill-overextruded.md) (#1; B)
<!-- /generated:relations -->
