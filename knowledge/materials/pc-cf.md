---
type: material
title: PC / PC-CF
description: High temp, abrasive (CF → hardened nozzle), enclosure, warps; temperature trades stringing against surface and layer bonding; brand-specific EM.
generated:
  by: process:session-lessons-2026-10-13
  at: 2026-10-13T14:00:00Z
status: stable
sources:
  - id: iemai
    title: IEMAI PC-CF community reports (r/prusa3d, Prusa Forum)
    resource: https://www.reddit.com/r/prusa3d/comments/1qm59iy/iemai_pccf_troubleshooting/
timestamp: 2026-10-13
altLabel: [PC, polycarbonate, Polycarbonat, carbon fiber PC]
prone_to:
  - {problem: defects/warping, via: causes/material-shrinkage, evidence: C}
  - {problem: defects/stringing, evidence: C}
---
# PC / PC-CF

## Baseline
- Typical: nozzle 260–290 °C, bed 100–115 °C, enclosed chamber, low fan (0–30%).
- **CF fill is abrasive**, so use a hardened or ObXidian nozzle (`filament_abrasive = 1` in PrusaSlicer 2.9+ flags this). Hardened nozzles flow less, so lower `filament_max_volumetric_speed`.
- Dry it (about 80–90 °C). Warps, so use a brim and heat soak.
- Keep nozzle and bed targets 5–10 °C below Klipper `max_temp`. A target equal to `max_temp` shuts down on the first overshoot.

## Temperature is a trade-off
- **Cooler** (around 265 °C): less ooze and stringing, but a more matte, rougher surface and weaker layer bonding.
- **Hotter** (275–285 °C): better layer bonding and a smoother, glossier surface, but more stringing and warping.[^iemai]
- Do not drop the temperature to fix stringing before trying PA, retraction length and travel. Lower it only if you accept the surface and strength cost.

## Brand differences: do not copy vendor-template values
A user filament that inherits `Prusament PC Blend Carbon Fiber @Template` also inherits Prusament's EM 1.04 and 285 °C. Those values are **not a reference** for another brand.[^iemai]

**IEMAI PC-CF**[^iemai]:
- EM reported between 0.85 and 1.00. 1.04 over-extrudes (messy top layer, blobs, corners dragged up). Check the top surface (ridges mean too much) and the bottom (gaps mean too little).
- Coarser and more matte than Prusament, even when well tuned. Short fibres make overhangs poor. Ironing helps top surfaces.
- Reported working: 275 °C (first layer up to 285), bed 110 °C, chamber 50 °C, about 10 mm³/s. Adhesion is weak on satin and textured sheets; glue stick or Magigoo PC fixes it.
- The rough CF surface makes caliper readings of the diameter run high. Prefer an EM test over entering a measured `filament_diameter`.

## PrusaSlicer keys
filament: `temperature`, `first_layer_temperature`, `bed_temperature`, `first_layer_bed_temperature`, `chamber_temperature`, `extrusion_multiplier`, `filament_diameter`, `filament_max_volumetric_speed`, `filament_abrasive`, `max_fan_speed`, `enable_dynamic_fan_speeds`, `overhang_fan_speed_0..3`
print: `enable_dynamic_overhang_speeds`, `ironing`, `brim_width`

## Related
- [Engineering materials and reinforced filaments](engineering-materials.md)
- [Filament drying and moisture](filament-moisture.md)

[^iemai]: IEMAI PC-CF community reports, see `research/raw/iemai-pccf.md`

<!-- generated:relations -->
## Relations
- **Prone to:** [Stringing / oozing](../defects/stringing.md) (C) · [Warping / corner lifting](../defects/warping.md) (C)
<!-- /generated:relations -->
