---
type: cause
title: "Unsuitable build surface"
description: "Fake or worn PEI, the wrong side of the sheet or a surface that does not suit the material."
altLabel: [fake PEI, wrong plate side, ungeeignete Druckplatte]
facets: {phase: [first-layer]}
check: "Compare on a known-good genuine sheet."
fixed_by:
  - {procedure: tuning/build-surface, action: "use a suitable genuine sheet or an adhesive/release agent"}
sources:
  - id: ellis-build-surface-adhesion
    title: "Ellis Print Tuning Guide — Build surface adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/build_surface_adhesion.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Unsuitable build surface

Fake or worn PEI, the wrong side of the sheet or a surface that does not suit the material.

**Check:** Compare on a known-good genuine sheet.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Build surface prep & handling](../tuning/build-surface.md) (use a suitable genuine sheet or an adhesive/release agent)
- **Causes:** [Poor bed adhesion](../defects/poor-bed-adhesion.md) (#5; B) · [Warping / corner lifting](../defects/warping.md) (#6; C)
<!-- /generated:relations -->
