---
type: cause
title: "Random seam placement"
description: "Each layer starts at a new spot, leaving start/stop pits all over the walls."
altLabel: [random seam, zufällige Naht]
facets: {phase: [walls-seams]}
check: "Pits scattered on walls, not on one line."
fixed_by:
  - {action: "use aligned, nearest or rear seam", sets: [{key: seam_position, direction: set}]}
sources:
  - id: ellis-pockmarks
    title: "Ellis Print Tuning Guide — Pockmarks"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/pockmarks.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Random seam placement

Each layer starts at a new spot, leaving start/stop pits all over the walls.

**Check:** Pits scattered on walls, not on one line.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (use aligned, nearest or rear seam) `seam_position` =
- **Causes:** [Pockmarks](../defects/pockmarks.md) (#1; B) · [Zits, blobs & visible seam](../defects/zits-blobs.md) (#3; B)
<!-- /generated:relations -->
