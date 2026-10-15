---
type: concept
title: Layer height and extrusion width
description: Layer height and line width trade vertical detail, XY resolution, bonding, throughput and machine limits.
tags: [fundamentals, slicer, layer-height, extrusion-width, nozzle]
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: prusa-nozzle-profiles
    title: Prusa Knowledge Base — Creating profiles for different nozzles
    resource: https://help.prusa3d.com/article/creating-profiles-for-different-nozzles_127540
  - id: prusa-layers
    title: Prusa Knowledge Base — Layers and perimeters
    resource: https://help.prusa3d.com/article/layers-and-perimeters_1748
related: [hardware/nozzle-selection, slicer/flow-width-and-gcode, defects/poor-layer-adhesion]
---
# Layer height and extrusion width

Layer height controls vertical resolution and print time; line width controls how much material each path deposits and how paths overlap. PrusaSlicer treats nozzle diameter as a machine limit and warns when layer height exceeds it; Prusa recommends staying around 70–80% of nozzle diameter at maximum because excessive layers can compromise adhesion. [^prusa-nozzle-profiles]

PrusaSlicer can derive a default width from nozzle diameter, but a wider line is not free resolution: it improves coverage and can strengthen or seal walls while reducing fine XY detail. First-layer width can aid bed contact at the cost of XY accuracy. [^prusa-nozzle-profiles]

## Practical selection

- Start with a layer height appropriate to the nozzle and feature detail; use adaptive layers when geometry justifies the added process complexity.
- Choose wall width and perimeter count from the required wall thickness, not from perimeter count alone; the rounded extrusion cross-section and overlap mean `count × width` is only an approximation. [^prusa-layers]
- Re-test volumetric flow after changing nozzle diameter, line width, layer height or temperature: `flow = layer height × line width × speed`.

## PrusaSlicer keys

Print: `layer_height`, `first_layer_height`, `default extrusion width`, `perimeter_extrusion_width`, `external_perimeter_extrusion_width`, `first_layer_extrusion_width`, `perimeters`, `external_perimeters_first`.

[^prusa-nozzle-profiles]: Prusa Knowledge Base — Creating profiles for different nozzles
[^prusa-layers]: Prusa Knowledge Base — Layers and perimeters

<!-- generated:relations -->
## Relations
- **Fixes:** [External perimeter too narrow](../causes/external-perimeter-too-narrow.md) (widen the external perimeter) · [Layer height too large for the nozzle](../causes/layer-height-too-large.md) (reduce layer height relative to the nozzle) · [Layer height too small](../causes/layer-height-too-small.md) (use a layer height suited to the nozzle) · [Wall thinner than the extrusion width](../causes/wall-thinner-than-line-width.md) (enable thin-wall handling or adjust line width to fit the wall)
- **Related:** [Poor layer adhesion](../defects/poor-layer-adhesion.md) · [Nozzle selection](../hardware/nozzle-selection.md) · [Slicer flow, width and firmware output](../slicer/flow-width-and-gcode.md)
- **Linked from:** [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md)
<!-- /generated:relations -->
