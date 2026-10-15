---
type: cause
title: "Perimeter order pushes walls out"
description: "Printing inner walls first lets them push the outer wall outward."
altLabel: [inner perimeters first, Perimeter-Reihenfolge]
facets: {phase: [walls-seams]}
check: "Bulges near features; improves with external perimeters first (can hurt extreme overhangs)."
fixed_by:
  - {action: "print external perimeters first", sets: [{key: external_perimeters_first, direction: enable}]}
sources:
  - id: ellis-bulging
    title: "Ellis Print Tuning Guide — Bulging"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/bulging.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Perimeter order pushes walls out

Printing inner walls first lets them push the outer wall outward.

**Check:** Bulges near features; improves with external perimeters first (can hurt extreme overhangs).

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (print external perimeters first) `external_perimeters_first` on
- **Causes:** [Bulging](../defects/bulging.md) (#1; B) · [Infill visible through walls](../defects/infill-visible-through-walls.md) (#2; C)
<!-- /generated:relations -->
