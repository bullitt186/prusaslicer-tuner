---
type: cause
title: "Extrusion multiplier too low"
description: "Less plastic than the line volume: gaps between lines, thin walls and weak bonding everywhere at all speeds."
altLabel: [flow too low, Flow zu niedrig, Extrusionsmultiplikator zu niedrig]
facets: {phase: [extrusion]}
check: "EM cubes: gaps close at a higher value; the defect does not depend on speed."
fixed_by:
  - {procedure: tuning/extrusion-multiplier, action: "raise in 2 % then 0.5 % steps", sets: [{key: extrusion_multiplier, direction: up}]}
sources:
  - id: ellis-layer-adhesion
    title: "Ellis Print Tuning Guide — Poor layer adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/poor_layer_adhesion.html
  - id: ellis-perimeter-separation
    title: "Ellis Print Tuning Guide — Perimeter separation"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/perimeter_separation.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Extrusion multiplier too low

Less plastic than the line volume: gaps between lines, thin walls and weak bonding everywhere at all speeds.

**Check:** EM cubes: gaps close at a higher value; the defect does not depend on speed.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Extrusion multiplier (flow)](../tuning/extrusion-multiplier.md) (raise in 2 % then 0.5 % steps) `extrusion_multiplier` ↑
- **Causes:** [Dimensional inaccuracy](../defects/dimensional-inaccuracy.md) (#3; B) · [Perimeter separation](../defects/perimeter-separation.md) (#4; B) · [Poor layer adhesion](../defects/poor-layer-adhesion.md) (#1; B) · [Gaps or pillowing in top layers](../defects/top-surface-gaps.md) (#3; B) · [Under-extrusion](../defects/under-extrusion.md) (#1; B)
<!-- /generated:relations -->
