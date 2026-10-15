---
type: concept
title: Nozzle selection
description: Select nozzle diameter, geometry and material for the required detail, throughput, wear resistance and polymer.
tags: [hardware, nozzle, brass, hardened, cht, abrasive-filament]
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: prusa-nozzle-types
    title: Prusa Knowledge Base — Prusa nozzle types for Nextruder printers
    resource: https://help.prusa3d.com/article/prusa-nozzle-types-for-nextruder-printers_928993
  - id: prusa-nozzle-profiles
    title: Prusa Knowledge Base — Creating profiles for different nozzles
    resource: https://help.prusa3d.com/article/creating-profiles-for-different-nozzles_127540
related: [fundamentals/layer-height-extrusion-width, materials/engineering-materials, defects/thin-walls-and-small-features]
---
# Nozzle selection

Nozzle diameter is a process constraint, not just a speed setting. A larger nozzle can deposit wider/taller lines and reduce print time, but loses fine detail and increases the amount of material that must cool. [^prusa-nozzle-types]

## Decision rules

- Use a smaller nozzle for fine XY detail and thin features; use a larger nozzle for robust walls, large parts and higher throughput.
- Keep layer height, extrusion widths, flow limit and temperatures consistent with the new nozzle. Merely changing the configured diameter does not make PrusaSlicer generate thicker lines. [^prusa-nozzle-profiles]
- Use brass or plated brass for non-abrasive polymers when wear and thermal behavior are acceptable. Use a hardened or wear-resistant nozzle for carbon/glass/mineral-filled materials; expect different thermal/flow behavior and validate the profile.
- Record nozzle diameter, bore geometry, material and wear state in every calibration result. A worn or partially obstructed nozzle invalidates comparisons.

## Validation

After a nozzle change, verify first layer, extrusion multiplier, maximum volumetric flow, temperature and dimensional accuracy. Do not transfer a flow limit between nozzles (for example from 0.4 mm to 0.6 mm) without testing the complete combination of hotend, nozzle, polymer and temperature.

## PrusaSlicer keys

Printer: `nozzle_diameter`, `min_layer_height`, `max_layer_height`; print: extrusion-width keys and `max_volumetric_speed`; filament: `filament_max_volumetric_speed`, `temperature`.

[^prusa-nozzle-types]: Prusa Knowledge Base — Prusa nozzle types for Nextruder printers
[^prusa-nozzle-profiles]: Prusa Knowledge Base — Creating profiles for different nozzles

<!-- generated:relations -->
## Relations
- **Fixes:** [Nozzle too large for the detail](../causes/nozzle-too-large-for-detail.md) (use a smaller nozzle or thicken the features in CAD) · [Worn, dirty or leaking nozzle](../causes/nozzle-worn-or-leaking.md) (clean or replace the nozzle; hot-tighten it)
- **Related:** [Layer height and extrusion width](../fundamentals/layer-height-extrusion-width.md) · [Thin walls and small features missing](../defects/thin-walls-and-small-features.md) · [Engineering materials and reinforced filaments](../materials/engineering-materials.md)
<!-- /generated:relations -->
