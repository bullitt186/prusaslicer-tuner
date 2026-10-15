---
type: procedure
title: Infill/perimeter overlap
description: Pinholes where top infill meets perimeters after EM/PA are tuned — adjust overlap.
timestamp: 2026-10-13
calibrates: [infill_overlap]
sources:
  - id: ellis-infill-perimeter-overlap
    title: "Ellis Print Tuning Guide — Infill/perimeter overlap"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/infill_perimeter_overlap.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Infill/perimeter overlap

Pinholes at the junction of top infill and perimeters, once EM and PA are good, are common in PrusaSlicer. Raise `infill_overlap` (print; default 25%) until they close. Ellis used about 40% with connected infill. Too high bulges the perimeters, and too low detaches the infill. Related: [small infill areas](../defects/small-infill-overextruded.md).

<!-- generated:relations -->
## Relations
- **Fixes:** [Infill/perimeter overlap wrong](../causes/infill-overlap-wrong.md) (adjust overlap (≈20–25 % as a starting point))
- **Calibrates:** `key/infill_overlap`
- **Linked from:** [Gaps between infill and walls](../defects/infill-wall-gaps.md) · [Tuning order](tuning-order.md)
<!-- /generated:relations -->
