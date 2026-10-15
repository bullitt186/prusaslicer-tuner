---
type: defect
title: Pockmarks
description: Small pits on walls — random seam, wet filament, bad nozzle.
timestamp: 2026-10-13
altLabel: [pits, pinholes on walls, Löcher in der Wand, Pockennarben]
facets: {phase: [walls-seams]}
caused_by:
  - {cause: causes/seam-random, rank: 1, evidence: B, source: ellis-pockmarks}
  - {cause: causes/wet-filament, rank: 2, evidence: B, source: ellis-pockmarks}
  - {cause: causes/nozzle-worn-or-leaking, rank: 3, evidence: B, source: ellis-pockmarks}
sources:
  - id: ellis-pockmarks
    title: "Ellis Print Tuning Guide — Pockmarks"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/pockmarks.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Pockmarks
1. `seam_position = random` causes them, so use aligned, nearest or rear.
2. Wet filament: listen for popping when extruding in midair, and dry it (new spools can be wet too).
3. Worn nozzle: replace it.

<!-- generated:relations -->
## Relations
- **Caused by:** [Random seam placement](../causes/seam-random.md) (#1; B) · [Wet filament](../causes/wet-filament.md) (#2; B) · [Worn, dirty or leaking nozzle](../causes/nozzle-worn-or-leaking.md) (#3; B)
- **Materials prone to this:** [Nylon (PA)](../materials/nylon.md) (B)
- **Linked from:** [Zits, blobs & visible seam](zits-blobs.md)
<!-- /generated:relations -->
