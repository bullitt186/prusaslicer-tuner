---
type: cause
title: "Small contact area"
description: "Small or sharp-cornered footprints have too little area to resist lifting forces."
altLabel: [small footprint, kleine Auflagefläche]
facets: {phase: [adhesion-warping]}
check: "Lifting starts at corners or thin feet."
fixed_by:
  - {action: "add brim or mouse ears; use adhesive", sets: [{key: brim_width, direction: up}]}
sources:
  - id: ellis-build-surface-adhesion
    title: "Ellis Print Tuning Guide — Build surface adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/build_surface_adhesion.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Small contact area

Small or sharp-cornered footprints have too little area to resist lifting forces.

**Check:** Lifting starts at corners or thin feet.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (add brim or mouse ears; use adhesive) `brim_width` ↑
- **Causes:** [Poor bed adhesion](../defects/poor-bed-adhesion.md) (#6; B) · [Supports fail during the print](../defects/supports-fail.md) (#2; C) · [Warping / corner lifting](../defects/warping.md) (#5; B)
<!-- /generated:relations -->
