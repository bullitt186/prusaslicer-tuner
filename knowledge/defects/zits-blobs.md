---
type: defect
title: Zits, blobs & visible seam
description: Small bumps on walls, usually at layer starts/seams or retraction points.
timestamp: 2026-10-13
altLabel: [zits, blobs, visible seam, Pickel, Naht sichtbar]
facets: {phase: [walls-seams]}
caused_by:
  - {cause: causes/pa-too-low, rank: 1, evidence: C}
  - {cause: causes/seam-start-stop-pressure, rank: 2, evidence: B, source: tsg-s3d}
  - {cause: causes/seam-random, rank: 3, evidence: B, source: tsg-s3d}
  - {cause: causes/wet-filament, rank: 4, evidence: C}
  - {cause: causes/retraction-insufficient, rank: 5, evidence: C}
  - {cause: causes/nozzle-temp-too-high, rank: 6, evidence: C}
  - {cause: causes/too-many-retractions, rank: 7, evidence: B, source: tsg-s3d}
sources:
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-migration
  at: '2026-10-13T23:30:00Z'
---
# Zits, blobs and the seam
General knowledge, informed by Ellis' PA and retraction articles.
- At the seam: tune [PA](../tuning/pressure-advance.md) first, then `seam_position` (aligned or rear). Hide the seam in a corner. Keep `retract_restart_extra` at 0 (or slightly negative). Use `wipe` / `filament_wipe` and `retract_before_wipe`.
- Random spots: `seam_position = random` causes [pockmarks](pockmarks.md). Moisture also causes them.
- Blobs after travel: [stringing](stringing.md) causes apply (temperature, retraction, `deretract_speed`).

<!-- generated:relations -->
## Relations
- **Caused by:** [Pressure advance too low](../causes/pa-too-low.md) (#1; C) · [Seam start/stop pressure](../causes/seam-start-stop-pressure.md) (#2; B) · [Random seam placement](../causes/seam-random.md) (#3; B) · [Wet filament](../causes/wet-filament.md) (#4; C) · [Retraction too short or too slow](../causes/retraction-insufficient.md) (#5; C) · [Nozzle temperature too high](../causes/nozzle-temp-too-high.md) (#6; C) · [Unnecessary retractions](../causes/too-many-retractions.md) (#7; B)
- **Linked from:** [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md)
<!-- /generated:relations -->
