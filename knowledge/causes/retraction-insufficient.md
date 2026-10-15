---
type: cause
title: "Retraction too short or too slow"
description: "Pressure is not relieved before travel, so the nozzle oozes between islands."
altLabel: [not enough retraction, Retraktion zu gering, Rückzug zu kurz]
facets: {phase: [retraction-travel]}
check: "Retraction test: strings shrink as length/speed increase (after PA, EM, temperature and moisture are ruled out)."
fixed_by:
  - {procedure: tuning/retraction, action: "raise length, then speed (direct drive stays small)", sets: [{key: filament_retract_length, direction: up}, {key: filament_retract_speed, direction: up}]}
sources:
  - id: ellis-retraction
    title: "Ellis Print Tuning Guide — Retraction"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Retraction too short or too slow

Pressure is not relieved before travel, so the nozzle oozes between islands.

**Check:** Retraction test: strings shrink as length/speed increase (after PA, EM, temperature and moisture are ruled out).

<!-- generated:relations -->
## Relations
- **Fixed by:** [Retraction](../tuning/retraction.md) (raise length, then speed (direct drive stays small)) `filament_retract_length` ↑ `filament_retract_speed` ↑
- **Causes:** [Stringing / oozing](../defects/stringing.md) (#6; B) · [Zits, blobs & visible seam](../defects/zits-blobs.md) (#5; C)
<!-- /generated:relations -->
