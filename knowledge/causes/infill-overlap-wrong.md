---
type: cause
title: "Infill/perimeter overlap wrong"
description: "Too much overlap pushes walls out; too little leaves pinholes where infill meets perimeters."
altLabel: [infill overlap, Infill-Überlappung]
facets: {phase: [top-bottom]}
check: "Pinholes or bulges exactly at the infill/perimeter boundary after EM and PA are tuned."
fixed_by:
  - {procedure: tuning/infill-perimeter-overlap, action: "adjust overlap (≈20–25 % as a starting point)", sets: [{key: infill_overlap, direction: set}]}
sources:
  - id: ellis-bulging
    title: "Ellis Print Tuning Guide — Bulging"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/bulging.html
  - id: ellis-small-infill
    title: "Ellis Print Tuning Guide — Small infill areas look overextruded"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/small_infill_areas_overextruded.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Infill/perimeter overlap wrong

Too much overlap pushes walls out; too little leaves pinholes where infill meets perimeters.

**Check:** Pinholes or bulges exactly at the infill/perimeter boundary after EM and PA are tuned.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Infill/perimeter overlap](../tuning/infill-perimeter-overlap.md) (adjust overlap (≈20–25 % as a starting point)) `infill_overlap` =
- **Causes:** [Bulging](../defects/bulging.md) (#4; B) · [Gaps between infill and walls](../defects/infill-wall-gaps.md) (#1; B) · [Small infill areas look overextruded](../defects/small-infill-overextruded.md) (#4; B)
<!-- /generated:relations -->
