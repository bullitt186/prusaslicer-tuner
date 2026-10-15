---
type: concept
title: Part orientation and anisotropy
description: FDM parts are direction-dependent because layer interfaces and raster paths create anisotropic strength and failure modes.
tags: [mechanical-properties, orientation, anisotropy, layer-bonding, strength]
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: cnckitchen-anisotropy
    title: CNC Kitchen — 3D printing material and process testing
    resource: https://www.cnckitchen.com/blog/3d-printed-parts-mechanical-properties
  - id: ellis-layer-adhesion
    title: Ellis Print Tuning Guide — Layer adhesion
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/poor_layer_adhesion.html
---
# Part orientation and anisotropy

FDM strength is usually not isotropic: in-plane roads and interlayer interfaces do not fail in the same way. Orientation therefore changes tensile strength, bending leverage, fatigue exposure, dimensional accuracy and the likelihood that a crack will follow a layer boundary. [^cnckitchen-anisotropy]

## Engineering procedure

1. Define the load path and the likely crack plane before orienting the part.
2. Prefer an orientation that puts the principal tensile load along continuous roads and keeps critical interfaces out of the dominant peel direction.
3. Increase wall count or local reinforcement only after orientation and layer bonding are credible; infill percentage alone is not a reliable proxy for strength.
4. Validate with coupons printed in the same material, temperature, layer height, width, speed and cooling as the part. Report orientation and failure mode with measured strength.

## Important limits

The strongest orientation depends on geometry, raster strategy, polymer, temperature history and load case. A generic “XY is stronger than Z” rule is a starting hypothesis, not a design value. Poor layer adhesion can dominate even when the orientation is favorable; see [poor layer adhesion](../defects/poor-layer-adhesion.md) and [temperature tuning](../tuning/temperature-tuning.md).

## PrusaSlicer keys

`perimeters`, `infill_density`, `infill_pattern`, `top_solid_layers`, `bottom_solid_layers`, `fill_angle`, `extrusion_width`, `layer_height`, `temperature`, cooling and speed keys. Geometry orientation itself is stored in the project, not as a single profile key.

## Related
- [Mechanical strength and test interpretation](strength-and-testing.md)

[^cnckitchen-anisotropy]: CNC Kitchen — 3D printing material and process testing
[^ellis-layer-adhesion]: Ellis Print Tuning Guide — Layer adhesion

<!-- generated:relations -->
## Relations
- **Fixes:** [Load along layer lines (orientation)](../causes/load-along-layer-lines.md) (reorient the part so load runs along layers)
- **Related:** [Mechanical strength and test interpretation](strength-and-testing.md)
- **Linked from:** [Engineering materials and reinforced filaments](../materials/engineering-materials.md) · [PrusaSlicer profile to knowledge map](../slicer/profile-knowledge-map.md) · [Temperature tuning](../tuning/temperature-tuning.md)
<!-- /generated:relations -->
