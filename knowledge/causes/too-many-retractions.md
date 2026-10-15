---
type: cause
title: Unnecessary retractions
description: Every retract/prime cycle risks a zit; retracting on moves that never cross open space adds defects for nothing.
altLabel: [too many retractions, unnötige Retraktionen]
facets: {phase: [retraction-travel]}
check: Zits sit at travel starts inside a single island.
fixed_by:
  - {action: only retract when crossing perimeters; set a minimum travel before retracting, sets: [{key: only_retract_when_crossing_perimeters, direction: enable}, {key: retract_before_travel, direction: up}]}
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
status: stable
---
# Unnecessary retractions

Every retract/prime cycle risks a zit; retracting on moves that never cross open space adds defects for nothing. [^tsg-s3d]

**Check:** Zits sit at travel starts inside a single island.

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (only retract when crossing perimeters; set a minimum travel before retracting) `only_retract_when_crossing_perimeters` on `retract_before_travel` ↑
- **Causes:** [Zits, blobs & visible seam](../defects/zits-blobs.md) (#7; B)
<!-- /generated:relations -->
