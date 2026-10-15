---
type: cause
title: "Print speed too high"
description: "High feature speeds raise flow demand, vibration and bonding time pressure."
altLabel: [printing too fast, zu schnell gedruckt, Geschwindigkeit zu hoch]
facets: {phase: [motion]}
check: "Print the same part at reduced speed; the defect shrinks."
fixed_by:
  - {action: "lower the relevant feature speeds", sets: [{key: perimeter_speed, direction: down}, {key: external_perimeter_speed, direction: down}]}
sources:
  - id: ellis-perimeter-separation
    title: "Ellis Print Tuning Guide — Perimeter separation"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/perimeter_separation.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Print speed too high

High feature speeds raise flow demand, vibration and bonding time pressure.

**Check:** Print the same part at reduced speed; the defect shrinks.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (lower the relevant feature speeds) `perimeter_speed` ↓ `external_perimeter_speed` ↓
- **Causes:** [Gaps between infill and walls](../defects/infill-wall-gaps.md) (#2; B) · [Layer shifting](../defects/layer-shift.md) (#6; C) · [Perimeter separation](../defects/perimeter-separation.md) (#5; B) · [Ringing / ghosting](../defects/ringing.md) (#4; B) · [Thin walls and small features missing](../defects/thin-walls-and-small-features.md) (#3; C)
<!-- /generated:relations -->
