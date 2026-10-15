---
type: cause
title: "Filament tension or path drag"
description: "Too much or too little idler tension, a tangled or binding spool or a tight PTFE path makes feeding inconsistent."
altLabel: [spool drag, tangled filament, idler tension, Spule hakt, Filament verheddert]
facets: {phase: [extrusion]}
check: "Pull the filament by hand through the path; check spool rotation and idler marks on the filament."
fixed_by:
  - {action: "free the spool and PTFE path, set idler tension"}
sources:
  - id: ellis-extruder-skipping
    title: "Ellis Print Tuning Guide — Extruder skipping"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
  - id: ellis-extrusion-patterns
    title: "Ellis Print Tuning Guide — Extrusion patterns"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extrusion_patterns.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Filament tension or path drag

Too much or too little idler tension, a tangled or binding spool or a tight PTFE path makes feeding inconsistent.

**Check:** Pull the filament by hand through the path; check spool rotation and idler marks on the filament.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (free the spool and PTFE path, set idler tension)
- **Causes:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (#3; B) · [Extrusion patterns ("wood grain")](../defects/extrusion-patterns.md) (#2; B) · [Extrusion stops mid-print](../defects/extrusion-stops.md) (#6; C) · [Inconsistent extrusion](../defects/inconsistent-extrusion.md) (#1; B) · [Lines or ridges on the sides (Z banding)](../defects/z-banding.md) (#4; B)
<!-- /generated:relations -->
