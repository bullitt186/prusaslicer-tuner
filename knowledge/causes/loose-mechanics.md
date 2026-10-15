---
type: cause
title: "Loose belts, pulleys or toolhead parts"
description: "Slack belts, loose pulley grub screws or loose toolhead parts let the toolhead lag or slip."
altLabel: [belt tension, loose pulley, loose toolhead, Riemenspannung, lockere Riemenscheibe]
facets: {phase: [mechanics]}
check: "Check belt tension by frequency, pulley set screws and wobble on the toolhead by hand."
fixed_by:
  - {procedure: hardware/voron-thermal-mechanics, action: "tension belts, tighten pulleys and toolhead hardware"}
sources:
  - id: ellis-layer-shifting
    title: "Ellis Print Tuning Guide — Layer shifting"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/layer_shifting.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Loose belts, pulleys or toolhead parts

Slack belts, loose pulley grub screws or loose toolhead parts let the toolhead lag or slip.

**Check:** Check belt tension by frequency, pulley set screws and wobble on the toolhead by hand.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Voron thermal and motion mechanics](../hardware/voron-thermal-mechanics.md) (tension belts, tighten pulleys and toolhead hardware)
- **Causes:** [Dimensional inaccuracy](../defects/dimensional-inaccuracy.md) (#5; C) · [Layer shifting](../defects/layer-shift.md) (#1; B) · [Ringing / ghosting](../defects/ringing.md) (#2; B) · [Supports fail during the print](../defects/supports-fail.md) (#4; C)
<!-- /generated:relations -->
