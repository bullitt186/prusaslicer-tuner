---
type: material-process
title: Engineering materials and reinforced filaments
description: Engineering polymers and fiber-filled filaments require product-specific drying, thermal, nozzle and chamber conditions; datasheet values are test-condition values.
tags: [materials, engineering, pc, pa, nylon, asa, abs, cf, gf, pps, chamber, drying]
generated:
  by: process:source-consolidation-2026-10-13
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: prusament
    title: Prusament material documentation
    resource: https://prusament.com/materials/
  - id: polymaker
    title: Polymaker Wiki
    resource: https://wiki.polymaker.com/
  - id: basf
    title: BASF Forward AM
    resource: https://forward-am.com/
  - id: cnc
    title: CNC Kitchen material and process measurements
    resource: https://www.cnckitchen.com/
  - id: prusa-materials
    title: Prusa filament material guide
    resource: https://help.prusa3d.com/filament-material-guide
  - id: voron-materials
    title: Voron materials selection
    resource: https://docs.vorondesign.com/materials.html
---
# Engineering materials and reinforced filaments

Material names are families, not complete process specifications. Product grade, additives, fiber loading, diameter, color, moisture state and annealing can change the usable window. Manufacturer settings are product-specific starting points; datasheet mechanical values are only comparable when standards, conditioning, orientation and print parameters match. [^prusament] [^polymaker] [^basf]

## Process decision table

| Material class | Primary risks | Hardware/process checks |
|---|---|---|
| ABS/ASA | shrinkage, warping, drafts, chamber gradients | enclosure/heat soak, controlled cooling, adhesion, material-specific bed/nozzle |
| PC/PC blend | high thermal demand, warping, moisture, stress cracking | enclosure, dry material, high-temperature hotend/bed, compatible surface |
| PA/nylon | strong moisture uptake, warping, creep and dimensional change | dry before and during print, enclosure, conservative cooling, product-specific anneal |
| CF/GF-filled polymers | abrasive wear, altered viscosity/flow, fiber orientation | hardened/wear-resistant nozzle, recalibrate flow and max volumetric speed |
| TPU/flexible | feed path buckling, moisture, slow pressure response | constrained/direct drive path, low retraction, dry material, reduced speed |
| PPS/PEI/metal-filled systems | high thermal/process complexity; possible post-processing | manufacturer machine, chamber, nozzle and post-processing instructions only |

Prusa's material guidance and Voron documentation do not agree on one universal structural-material policy: Voron favors ABS/ASA for printed structural parts and discourages PLA/PETG for those parts, while Prusa profiles cover many printer/material combinations. Preserve printer and part-use scope rather than generalizing. [^voron-materials] [^prusa-materials]

## Moisture and drying

Moisture may appear as stringing, bubbles, popping, rough surfaces, blobs, smoke or weak interlayers. A drybox slows re-absorption but does not necessarily dry wet filament. Use the product's drying data and a dryer whose actual temperature is known. Prusa examples include PLA/rPLA 45 °C/6 h, PETG 55 °C/6 h, TPU 60 °C/4–6 h, ASA 80 °C/4 h, PC Blend 85 °C/5 h and PA11-CF 90 °C/6 h; these are not family-wide defaults. [^prusa-materials]

## Reinforcement and nozzle wear

Carbon- and glass-fiber composites require wear-resistant nozzle hardware in proportion to the product's abrasive content. A hardened nozzle does not preserve the same flow as brass; re-check temperature, extrusion multiplier/flow ratio and maximum volumetric flow. Nozzle geometry, diameter and wear state belong in the calibration record. [^polymaker] [^prusa-materials]

## Mechanical-data interpretation

CNC Kitchen, BASF, Polymaker and Prusament report data under different standards and conditioning. Do not copy tensile strength into a design value without recording orientation, layer height, perimeter/infill, temperature, specimen conditioning, test speed and failure mode. Fiber-filled data may be direction-dependent and a datasheet's injection-molding or annealed result may not represent an FDM part. [^cnc] [^basf]

## Procedure

1. Identify exact product/SKU, additive, color, diameter and spool.
2. Read the product datasheet for drying, nozzle, bed, chamber and annealing limits.
3. Dry and store with known moisture control.
4. Verify nozzle wear compatibility and calibrate extrusion/flow on the actual hardware.
5. Establish temperature and volumetric-flow windows before PA/retraction.
6. Print a representative coupon in the intended orientation and conditioning state.
7. Record failure mode, dimensional change and post-processing—not just a single strength number.

Related: [filament moisture](filament-moisture.md), [part orientation](../mechanical-properties/part-orientation.md), [nozzle selection](../hardware/nozzle-selection.md).

[^prusament]: Prusament material pages and technical datasheets
[^polymaker]: Polymaker Wiki product documentation
[^basf]: BASF Forward AM product/data-sheet documentation
[^prusa-materials]: Prusa filament material guide and drying guidance
[^voron-materials]: Voron materials selection
[^cnc]: CNC Kitchen material and process measurements

<!-- generated:relations -->
## Relations
- **Related:** [Nozzle selection](../hardware/nozzle-selection.md)
- **Linked from:** [Warping / corner lifting](../defects/warping.md) · [PC / PC-CF](pc-cf.md)
<!-- /generated:relations -->
