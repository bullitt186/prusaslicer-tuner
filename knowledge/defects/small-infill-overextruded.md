---
type: defect
title: Small infill areas look overextruded
description: Blobby short top-infill segments in small islands; partly normal.
timestamp: 2026-10-13
altLabel: [rough small top areas, kleine Deckflächen rau]
facets: {phase: [top-bottom]}
caused_by:
  - {cause: causes/small-island-geometry, rank: 1, evidence: B, source: ellis-small-infill}
  - {cause: causes/pa-smooth-time-too-high, rank: 2, evidence: B, source: ellis-small-infill}
  - {cause: causes/extruder-gear-backlash-or-wear, rank: 3, evidence: B, source: ellis-small-infill}
  - {cause: causes/infill-overlap-wrong, rank: 4, evidence: B, source: ellis-small-infill}
sources:
  - id: ellis-small-infill
    title: "Ellis Print Tuning Guide — Small infill areas look overextruded"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/small_infill_areas_overextruded.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Small infill areas look overextruded
Partly normal, so judge EM on the wide areas. Mitigations: `top_fill_pattern = monotonic` or `monotoniclines`, lower `top_solid_infill_speed` and `top_solid_infill_acceleration`, lower Klipper `pressure_advance_smooth_time` (about 0.02, then re-test PA), minimize extruder backlash, and adjust `infill_overlap` (about 25%).

<!-- generated:relations -->
## Relations
- **Caused by:** [Small top islands (inherent)](../causes/small-island-geometry.md) (#1; B) · [Pressure advance smoothing too long](../causes/pa-smooth-time-too-high.md) (#2; B) · [Extruder gear backlash, play or wear](../causes/extruder-gear-backlash-or-wear.md) (#3; B) · [Infill/perimeter overlap wrong](../causes/infill-overlap-wrong.md) (#4; B)
- **Related:** [Gaps or pillowing in top layers](top-surface-gaps.md)
- **Linked from:** [Over-extrusion](over-extrusion.md) · [Extrusion multiplier (flow)](../tuning/extrusion-multiplier.md) · [Infill/perimeter overlap](../tuning/infill-perimeter-overlap.md)
<!-- /generated:relations -->
