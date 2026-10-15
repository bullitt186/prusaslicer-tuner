---
type: cause
title: "First-layer lines too thin"
description: "Narrow first-layer lines have little contact area."
altLabel: [first layer width too small, erste Schicht zu dünn]
facets: {phase: [first-layer]}
check: "Adhesion improves with a wider first layer."
fixed_by:
  - {action: "widen the first layer", sets: [{key: first_layer_extrusion_width, direction: up}]}
sources:
  - id: ellis-build-surface-adhesion
    title: "Ellis Print Tuning Guide — Build surface adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/build_surface_adhesion.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# First-layer lines too thin

Narrow first-layer lines have little contact area.

**Check:** Adhesion improves with a wider first layer.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (widen the first layer) `first_layer_extrusion_width` ↑
- **Causes:** [Poor bed adhesion](../defects/poor-bed-adhesion.md) (#4; B)
<!-- /generated:relations -->
