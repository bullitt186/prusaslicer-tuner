---
type: cause
title: "Retraction too long or too fast"
description: "Long or fast retractions grind filament, pull molten plastic into the cold zone and jam soft filaments like TPU."
altLabel: [too much retraction, Retraktion zu stark, Rückzug zu lang]
facets: {phase: [retraction-travel]}
check: "Clicking or chewed filament near the drive gear after many retractions; problem shrinks with shorter retraction."
fixed_by:
  - {procedure: tuning/retraction, action: "shorten and slow retraction", sets: [{key: filament_retract_length, direction: down}, {key: filament_retract_speed, direction: down}]}
sources:
  - id: ellis-extruder-skipping
    title: "Ellis Print Tuning Guide — Extruder skipping"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Retraction too long or too fast

Long or fast retractions grind filament, pull molten plastic into the cold zone and jam soft filaments like TPU.

**Check:** Clicking or chewed filament near the drive gear after many retractions; problem shrinks with shorter retraction.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Retraction](../tuning/retraction.md) (shorten and slow retraction) `filament_retract_length` ↓ `filament_retract_speed` ↓
- **Causes:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (#4; B)
<!-- /generated:relations -->
