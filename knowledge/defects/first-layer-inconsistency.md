---
type: defect
title: First layer inconsistency
description: Squish varies across the bed or between prints.
timestamp: 2026-10-13
altLabel: [uneven first layer, ungleichmäßige erste Schicht, messy first layer]
facets: {phase: [first-layer]}
caused_by:
  - {cause: causes/bed-not-level-or-unmeshed, rank: 1, evidence: B, source: [ellis-first-layer-inconsistency, tsg-prusa, tsg-all3dp]}
  - {cause: causes/frame-thermal-drift, rank: 2, evidence: B, source: ellis-first-layer-inconsistency}
  - {cause: causes/sheet-not-seated, rank: 3, evidence: B, source: [ellis-first-layer-inconsistency, tsg-prusa]}
  - {cause: causes/bed-temp-too-high, rank: 4, evidence: C, source: tsg-all3dp}
sources:
  - id: ellis-first-layer-inconsistency
    title: Ellis Print Tuning Guide — First layer inconsistency
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/first_layer_squish_consistency_issues/first_layer_inconsistency.html
  - id: tsg-prusa
    title: Prusa Knowledge Base, print quality troubleshooting (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://help.prusa3d.com/category/print-quality-troubleshooting_225
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
# First layer inconsistency
- **Across the bed:** heat-soaked bed mesh before every print (`BED_MESH_CALIBRATE` in `PRINT_START`, bicubic, about 5×5), square the gantry and de-rack the frame, tighten loose hardware, Z belts about 140 Hz on V2. Debris under the sheet. Use `PROBE_ACCURACY` (stddev ≤ 0.004).
- **Between prints:** [thermal drift](../tuning/thermal-drift.md), home Z hot, re-home after QGL, check the probe's temperature drift.
- Slicer: z-hop off on the first layer (`retract_lift_above` > first layer height).
Mostly a printer-side problem: check it with your firmware and printer tooling (Klipper: probe, mesh and Z config).

<!-- generated:relations -->
## Relations
- **Caused by:** [Bed not level or mesh missing](../causes/bed-not-level-or-unmeshed.md) (#1; B) · [Frame thermal drift](../causes/frame-thermal-drift.md) (#2; B) · [Sheet not seated flat](../causes/sheet-not-seated.md) (#3; B) · [Bed temperature too high](../causes/bed-temp-too-high.md) (#4; C)
- **Linked from:** [First layer squish (Z offset)](../tuning/first-layer-squish.md) · [Thermal drift (enclosed Klipper printers)](../tuning/thermal-drift.md)
<!-- /generated:relations -->
