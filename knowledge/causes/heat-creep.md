---
type: cause
title: "Heat creep"
description: "Heat rises past the heatbreak, filament softens early and jams; typical for PLA in a warm enclosure or a weak hotend fan."
altLabel: [Wärmekriechen, heatbreak too hot]
facets: {phase: [thermal]}
check: "Jams appear after some time printing and in warm chambers; hotend fan below 100 % or chamber hot."
fixed_by:
  - {action: "run hotend fan at 100 %, open the enclosure for PLA, reduce retraction"}
sources:
  - id: ellis-extruder-skipping
    title: "Ellis Print Tuning Guide — Extruder skipping"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Heat creep

Heat rises past the heatbreak, filament softens early and jams; typical for PLA in a warm enclosure or a weak hotend fan.

**Check:** Jams appear after some time printing and in warm chambers; hotend fan below 100 % or chamber hot.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (run hotend fan at 100 %, open the enclosure for PLA, reduce retraction)
- **Causes:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (#2; B) · [Under-extrusion](../defects/under-extrusion.md) (#11; B)
<!-- /generated:relations -->
