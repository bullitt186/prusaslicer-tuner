---
type: cause
title: Brittle filament snaps
description: Old, sun-exposed or cheap filament becomes brittle and snaps in the feed path, often unseen in a Bowden tube.
altLabel: [snapped filament, Filament bricht, sprödes Filament]
facets: {phase: [material-handling]}
check: Filament breaks when bent by hand; a fresh spool feeds fine.
fixed_by:
  - {action: replace the spool; reduce idler tension until it just does not slip}
sources:
  - id: tsg-all3dp
    title: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-migration
  at: '2026-10-13T23:30:00Z'
status: stable
---
# Brittle filament snaps

Old, sun-exposed or cheap filament becomes brittle and snaps in the feed path, often unseen in a Bowden tube. [^tsg-all3dp]

**Check:** Filament breaks when bent by hand; a fresh spool feeds fine.

[^tsg-all3dp]: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (replace the spool; reduce idler tension until it just does not slip)
- **Causes:** [Extrusion stops mid-print](../defects/extrusion-stops.md) (#5; C) · [Supports fail during the print](../defects/supports-fail.md) (#3; C)
<!-- /generated:relations -->
