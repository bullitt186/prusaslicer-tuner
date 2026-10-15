---
type: defect
title: Overheating (esp. PLA in enclosures)
description: Droopy/melted small features, curled overhangs, heat creep jams with PLA in a closed printer.
timestamp: 2026-10-13
altLabel: [melted features, PLA overheating, Überhitzung, geschmolzene Details, curling or rough corners, melted and deformed]
facets: {phase: [cooling]}
caused_by:
  - {cause: causes/chamber-too-hot-for-material, rank: 1, evidence: B, source: ellis-pla-overheating}
  - {cause: causes/insufficient-cooling, rank: 2, evidence: B, source: [ellis-pla-overheating, tsg-s3d, tsg-all3dp]}
  - {cause: causes/layer-time-too-short, rank: 3, evidence: B, source: [ellis-pla-overheating, tsg-s3d]}
  - {cause: causes/nozzle-temp-too-high, rank: 4, evidence: B, source: [ellis-pla-overheating, tsg-s3d, tsg-all3dp]}
sources:
  - id: ellis-pla-overheating
    title: Ellis Print Tuning Guide — PLA overheating
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/pla_overheating.html
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-all3dp
    title: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-migration
  at: 2026-10-13 23:00:00+00:00
---
# Overheating
- PLA in an enclosed Voron: open the door or remove panels, use better part cooling (AB-BN, StealthBurner), point an external fan at it, or print with the bed heater off.
- Slicer: `max_fan_speed` / `min_fan_speed` 100% for PLA, raise `slowdown_below_layer_time` and `fan_below_layer_time`, print several parts at once, lower `temperature`.
- Heat creep in PLA also causes [extruder skipping](extruder-skipping.md).
See [cooling and layer times](../tuning/cooling-layer-times.md).

<!-- generated:relations -->
## Relations
- **Caused by:** [Chamber too hot for the material](../causes/chamber-too-hot-for-material.md) (#1; B) · [Insufficient part cooling](../causes/insufficient-cooling.md) (#2; B) · [Layer time too short](../causes/layer-time-too-short.md) (#3; B) · [Nozzle temperature too high](../causes/nozzle-temp-too-high.md) (#4; B)
- **Materials prone to this:** [PLA](../materials/pla.md) (B)
- **Linked from:** [Poor bridges & overhangs](bridging-overhangs.md) · [Cooling and layer times](../tuning/cooling-layer-times.md)
<!-- /generated:relations -->
