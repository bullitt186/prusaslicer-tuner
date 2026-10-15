---
type: cause
title: "Elephant-foot compensation too high"
description: "Over-compensation pulls bottom perimeters apart."
altLabel: [Elefantenfuß-Kompensation zu hoch]
facets: {phase: [first-layer]}
check: "Perimeter gaps only in the lowest layers."
fixed_by:
  - {action: "reduce elephant-foot compensation", sets: [{key: elefant_foot_compensation, direction: down}]}
sources:
  - id: ellis-perimeter-separation
    title: "Ellis Print Tuning Guide — Perimeter separation"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/perimeter_separation.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Elephant-foot compensation too high

Over-compensation pulls bottom perimeters apart.

**Check:** Perimeter gaps only in the lowest layers.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (reduce elephant-foot compensation) `elefant_foot_compensation` ↓
- **Causes:** [Perimeter separation](../defects/perimeter-separation.md) (#2; B)
<!-- /generated:relations -->
