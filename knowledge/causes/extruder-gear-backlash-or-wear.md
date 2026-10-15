---
type: cause
title: "Extruder gear backlash, play or wear"
description: "A dead zone on reversal or worn/eccentric gears makes extrusion uneven: repeating texture, inconsistent PA and stringing."
altLabel: [extruder backlash, loose grub screw, worn drive gear, Extruder-Spiel, Zahnradspiel]
facets: {phase: [mechanics]}
check: "Mark the gears and watch reversals; inspect teeth; wood-grain texture with a fixed period points here."
fixed_by:
  - {action: "set small nonzero backlash, replace worn gears, tighten grub screws; then re-tune PA and rotation distance"}
sources:
  - id: ellis-extrusion-patterns
    title: "Ellis Print Tuning Guide — Extrusion patterns"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extrusion_patterns.html
  - id: ellis-retraction
    title: "Ellis Print Tuning Guide — Retraction"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
  - id: ellis-small-infill
    title: "Ellis Print Tuning Guide — Small infill areas look overextruded"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/small_infill_areas_overextruded.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Extruder gear backlash, play or wear

A dead zone on reversal or worn/eccentric gears makes extrusion uneven: repeating texture, inconsistent PA and stringing.

**Check:** Mark the gears and watch reversals; inspect teeth; wood-grain texture with a fixed period points here.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (set small nonzero backlash, replace worn gears, tighten grub screws; then re-tune PA and rotation distance)
- **Causes:** [Extrusion patterns ("wood grain")](../defects/extrusion-patterns.md) (#1; B) · [Extrusion stops mid-print](../defects/extrusion-stops.md) (#3; B) · [Inconsistent extrusion](../defects/inconsistent-extrusion.md) (#5; B) · [No extrusion at print start](../defects/no-extrusion-at-start.md) (#3; B) · [Small infill areas look overextruded](../defects/small-infill-overextruded.md) (#3; B) · [Stringing / oozing](../defects/stringing.md) (#8; B) · [Under-extrusion](../defects/under-extrusion.md) (#10; B)
<!-- /generated:relations -->
