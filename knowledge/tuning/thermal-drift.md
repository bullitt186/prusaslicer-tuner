---
type: procedure
title: Thermal drift (enclosed Klipper printers)
description: Frame/gantry expansion shifts Z during the first ~hour of chamber heating; heat soak or compensate.
tags: [klipper, voron, first-layer, z-offset, ellis]
timestamp: 2026-10-13
sources:
  - id: ellis-thermal-drift
    title: "Ellis Print Tuning Guide — Thermal drift (enclosed Klipper printers)"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/first_layer_squish_consistency_issues/thermal_drift.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Thermal drift

- Symptom: first-layer squish varies between prints, or the first layer gets thinner or thicker as the print proceeds. Mainly affects large enclosed machines (Voron 2.4).
- Fixes: heat soak for ≥ 1 h for enclosed V2/Trident printers (5–10 min for open printers with thick beds); gantry backers; auto-Z calibration (Klicky / klipper_z_calibration, or an eddy-current probe with touch mode); `[z_thermal_adjust]`.
- Home Z **hot**, and re-home after QGL (https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/first_layer_squish_consistency_issues/z_offset_inconsistency.html).
See [first layer inconsistency](../defects/first-layer-inconsistency.md).

## Related
- [Voron thermal and motion mechanics](../hardware/voron-thermal-mechanics.md)

<!-- generated:relations -->
## Relations
- **Fixes:** [Frame thermal drift](../causes/frame-thermal-drift.md) (heat soak or compensate)
- **Linked from:** [First layer inconsistency](../defects/first-layer-inconsistency.md)
<!-- /generated:relations -->
