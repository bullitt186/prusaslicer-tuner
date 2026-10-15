---
type: cause
title: "Frame thermal drift"
description: "Frame and gantry expand during the first hour of chamber heating and shift Z."
altLabel: [thermal expansion, Z drift, thermische Drift]
facets: {phase: [thermal]}
check: "First layer differs between cold and heat-soaked starts."
fixed_by:
  - {procedure: tuning/thermal-drift, action: "heat soak or compensate"}
sources:
  - id: ellis-first-layer-inconsistency
    title: "Ellis Print Tuning Guide — First layer inconsistency"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/first_layer_squish_consistency_issues/first_layer_inconsistency.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Frame thermal drift

Frame and gantry expand during the first hour of chamber heating and shift Z.

**Check:** First layer differs between cold and heat-soaked starts.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Thermal drift (enclosed Klipper printers)](../tuning/thermal-drift.md) (heat soak or compensate)
- **Causes:** [First layer inconsistency](../defects/first-layer-inconsistency.md) (#2; B)
<!-- /generated:relations -->
