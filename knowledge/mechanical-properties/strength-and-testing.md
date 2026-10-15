---
type: concept
title: Mechanical strength and test interpretation
description: FDM mechanical performance depends on orientation, process history, geometry and conditioning; strength claims need reproducible test context.
tags: [mechanical-properties, tensile-strength, anisotropy, creep, impact, testing]
generated:
  by: process:source-consolidation-2026-10-13
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: cnc
    title: CNC Kitchen — FDM mechanical testing
    resource: https://www.cnckitchen.com/
  - id: basf
    title: BASF Forward AM technical data
    resource: https://forward-am.com/
  - id: functionalprint
    title: r/functionalprint representative corpus
    resource: https://www.reddit.com/r/functionalprint/
  - id: ellis-adhesion
    title: Ellis Print Tuning Guide — layer adhesion
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/poor_layer_adhesion.html
  - id: voron-materials
    title: Voron materials selection
    resource: https://docs.vorondesign.com/materials.html
related: [mechanical-properties/part-orientation, defects/poor-layer-adhesion]
---
# Mechanical strength and test interpretation

FDM parts are anisotropic: roads, interlayer interfaces and geometric stress concentrations create different failure modes. Orientation should be chosen from the load path and crack plane, then validated using the intended material and process. [^cnc] [^ellis-adhesion]

## What to record

- exact polymer/product, additive, color and moisture state,
- nozzle diameter/material/geometry and wear,
- layer height, widths, perimeter count, infill pattern/density,
- temperature, speed, cooling, chamber and annealing,
- raster/part orientation and specimen geometry,
- conditioning time, test standard, test speed and failure mode.

Datasheet tensile values and community “strongest setting” claims are not interchangeable. BASF and other manufacturers often report standardized specimens under specified conditioning; CNC Kitchen's experiments measure specific printed geometries. Community reports are hypotheses unless the complete test context and replication are available. [^basf] [^functionalprint]

## Engineering procedure

1. Define load, temperature, duration and acceptable deformation.
2. Orient continuous roads and perimeters to carry principal tensile/bending loads where possible; avoid placing critical layer interfaces in the dominant peel direction.
3. Select walls and local reinforcement from the load path; infill percentage alone is not a strength specification.
4. Print coupons in at least the plausible orientations using the production process.
5. Measure strength, stiffness, creep or impact in the relevant environmental condition.
6. Inspect failure surfaces and retain failed specimens with the record.

## Creep and temperature

Time-dependent deformation can dominate bolted joints, clamps and warm enclosures even when short-term tensile strength looks sufficient. PA6, for example, is discouraged by Voron for some structural fastener applications because of creep under bolt pressure; this is a scoped printer-design recommendation, not a universal rejection of PA6. [^voron-materials]

Fiber reinforcement can improve stiffness/strength in selected directions while increasing anisotropy and nozzle wear. It does not make a printed part isotropic or automatically solve interlayer weakness. [^basf] [^cnc]

## Acceptance criteria

Do not accept a material or orientation based only on a top-surface appearance test. Define a measurable failure condition: load, deflection, crack initiation, dimensional drift, leak rate or cycle count. If no measurement exists, label the conclusion as a starting hypothesis.

[^cnc]: CNC Kitchen experimental material/process measurements
[^basf]: BASF Forward AM technical datasheets and processing documentation
[^functionalprint]: r/functionalprint representative community corpus
[^ellis-adhesion]: Ellis Print Tuning Guide — layer adhesion and process dependencies
[^voron-materials]: Voron materials selection and structural-part guidance

<!-- generated:relations -->
## Relations
- **Related:** [Poor layer adhesion](../defects/poor-layer-adhesion.md) · [Part orientation and anisotropy](part-orientation.md)
<!-- /generated:relations -->
