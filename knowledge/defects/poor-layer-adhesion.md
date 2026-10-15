---
type: defect
title: Poor layer adhesion
description: Layers split under modest force because interlayer bonding is weaker than the applied load or because the process is inconsistent.
sources:
  - id: ellis-layer-adhesion
    title: Ellis Print Tuning Guide — Poor layer adhesion
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/poor_layer_adhesion.html
  - id: klipper-pa
    title: Klipper — Pressure advance
    resource: https://www.klipper3d.org/Pressure_Advance.html
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-all3dp
    title: All3DP, common 3D printing problems (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
altLabel: [delamination, layer separation, layers splitting, Schichthaftung, Delamination, cracks in tall objects, layer splitting]
facets: {phase: [thermal]}
caused_by:
  - {cause: causes/em-too-low, rank: 1, evidence: B, source: [ellis-layer-adhesion, tsg-s3d]}
  - {cause: causes/volumetric-flow-exceeded, rank: 2, evidence: B, source: ellis-layer-adhesion}
  - {cause: causes/nozzle-temp-too-low, rank: 3, evidence: B, source: [ellis-layer-adhesion, tsg-s3d, tsg-all3dp]}
  - {cause: causes/excessive-cooling, rank: 4, evidence: B, source: [ellis-layer-adhesion, tsg-s3d, tsg-all3dp]}
  - {cause: causes/wet-filament, rank: 5, evidence: C}
  - {cause: causes/load-along-layer-lines, rank: 6, evidence: C}
  - {cause: causes/layer-height-too-large, rank: 7, evidence: B, source: tsg-s3d}
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13 12:00:00+00:00
status: stable
---
# Poor layer adhesion

Poor interlayer adhesion is distinct from a first-layer adhesion failure and from perimeters that do not touch. Look for cracks that follow layer lines, a part that separates cleanly between layers, or a large strength improvement after changing thermal conditions.

## Discriminating checks

- **Whole print weak or flow visibly low:** verify extruder rotation distance, nozzle condition, extrusion multiplier and maximum volumetric flow first. See [under-extrusion](under-extrusion.md).
- **Only high-flow regions weak:** lower the material flow cap or speed, or raise temperature within the product's safe window. Klipper requires extrusion calibration and nozzle temperature to be established before Pressure Advance tuning. [^klipper-pa]
- **Weakness improves when cooling is reduced or the chamber is warmer:** thermal bonding is a credible cause; validate with identical geometry and a controlled comparison.
- **Only one axis or one interface fails:** inspect orientation, fan duct asymmetry, drafts, layer time and geometry before changing material settings.

Do not infer tensile strength from a single visual cube. Report material, moisture state, nozzle, layer height, width, speed, temperature, fan, chamber and failure plane.

PrusaSlicer keys: `temperature`, `filament_max_volumetric_speed`, `max_volumetric_speed`, `perimeter_speed`, `cooling`, `min_fan_speed`, `max_fan_speed`, `layer_height`, `extrusion_width`.

[^ellis-layer-adhesion]: Ellis Print Tuning Guide — Poor layer adhesion
[^klipper-pa]: Klipper — Pressure advance

<!-- generated:relations -->
## Relations
- **Caused by:** [Extrusion multiplier too low](../causes/em-too-low.md) (#1; B) · [Volumetric flow above the hotend limit](../causes/volumetric-flow-exceeded.md) (#2; B) · [Nozzle temperature too low](../causes/nozzle-temp-too-low.md) (#3; B) · [Too much part cooling](../causes/excessive-cooling.md) (#4; B) · [Wet filament](../causes/wet-filament.md) (#5; C) · [Load along layer lines (orientation)](../causes/load-along-layer-lines.md) (#6; C) · [Layer height too large for the nozzle](../causes/layer-height-too-large.md) (#7; B)
- **Related:** [Layer height and extrusion width](../fundamentals/layer-height-extrusion-width.md) · [Mechanical strength and test interpretation](../mechanical-properties/strength-and-testing.md)
- **Linked from:** [Part orientation and anisotropy](../mechanical-properties/part-orientation.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md)
<!-- /generated:relations -->
