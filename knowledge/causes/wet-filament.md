---
type: cause
title: "Wet filament"
description: "Absorbed water boils in the nozzle: popping, steam, ooze, rough walls and weak layers. Common with PETG, nylon, TPU and PC; new spools can be wet too."
altLabel: [moisture, damp filament, nasses Filament, feuchtes Filament, Feuchtigkeit]
facets: {phase: [material-handling]}
check: "Extrude into air: popping, hissing or steam bubbles confirm it. Print the same part from a freshly dried spool and compare."
fixed_by:
  - {procedure: materials/filament-moisture, action: "dry the spool and print from a dry box"}
sources:
  - id: ellis-layer-adhesion
    title: "Ellis Print Tuning Guide — Poor layer adhesion"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/poor_layer_adhesion.html
  - id: ellis-perimeter-separation
    title: "Ellis Print Tuning Guide — Perimeter separation"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/perimeter_separation.html
  - id: ellis-pockmarks
    title: "Ellis Print Tuning Guide — Pockmarks"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/pockmarks.html
  - id: ellis-retraction
    title: "Ellis Print Tuning Guide — Retraction"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Wet filament

Absorbed water boils in the nozzle: popping, steam, ooze, rough walls and weak layers. Common with PETG, nylon, TPU and PC; new spools can be wet too.

**Check:** Extrude into air: popping, hissing or steam bubbles confirm it. Print the same part from a freshly dried spool and compare.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Filament drying and moisture](../materials/filament-moisture.md) (dry the spool and print from a dry box)
- **Causes:** [Perimeter separation](../defects/perimeter-separation.md) (#8; B) · [Pockmarks](../defects/pockmarks.md) (#2; B) · [Poor layer adhesion](../defects/poor-layer-adhesion.md) (#5; C) · [Stringing / oozing](../defects/stringing.md) (#1; B) · [Zits, blobs & visible seam](../defects/zits-blobs.md) (#4; C)
<!-- /generated:relations -->
