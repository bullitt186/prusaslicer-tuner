---
type: cause
title: "Contaminated build surface"
description: "Skin oils and residue block adhesion."
altLabel: [greasy bed, fingerprints, verschmutztes Druckbett, Fingerabdrücke]
facets: {phase: [first-layer]}
check: "Adhesion returns after washing with dish soap and water."
fixed_by:
  - {procedure: tuning/build-surface, action: "wash with dish soap, air dry, don't touch"}
sources:
  - id: ellis-build-surface-adhesion
    title: "Ellis Print Tuning Guide — Build surface adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/build_surface_adhesion.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Contaminated build surface

Skin oils and residue block adhesion.

**Check:** Adhesion returns after washing with dish soap and water.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Build surface prep & handling](../tuning/build-surface.md) (wash with dish soap, air dry, don't touch)
- **Causes:** [Poor bed adhesion](../defects/poor-bed-adhesion.md) (#1; B)
<!-- /generated:relations -->
