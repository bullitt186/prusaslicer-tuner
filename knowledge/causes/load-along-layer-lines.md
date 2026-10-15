---
type: cause
title: "Load along layer lines (orientation)"
description: "FDM parts are weakest across layers; loads that pull layers apart fail regardless of tuning."
altLabel: [anisotropy, Belastung entlang der Schichten, Bauteilausrichtung]
facets: {phase: [model]}
check: "Fracture follows one layer plane; strength changes with orientation."
fixed_by:
  - {procedure: mechanical-properties/part-orientation, action: "reorient the part so load runs along layers"}
sources:
  - id: ellis-layer-adhesion
    title: "Ellis Print Tuning Guide — Poor layer adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/poor_layer_adhesion.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Load along layer lines (orientation)

FDM parts are weakest across layers; loads that pull layers apart fail regardless of tuning.

**Check:** Fracture follows one layer plane; strength changes with orientation.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Part orientation and anisotropy](../mechanical-properties/part-orientation.md) (reorient the part so load runs along layers)
- **Causes:** [Poor layer adhesion](../defects/poor-layer-adhesion.md) (#6; C)
<!-- /generated:relations -->
