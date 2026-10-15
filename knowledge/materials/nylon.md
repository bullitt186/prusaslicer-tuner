---
type: material
title: Nylon (PA)
description: Extremely hygroscopic, warps, needs dry box during printing.
timestamp: 2026-10-13
altLabel: [PA, polyamide, Polyamid]
prone_to:
  - {problem: defects/warping, via: causes/material-shrinkage, evidence: C}
  - {problem: defects/pockmarks, via: causes/wet-filament, evidence: B, source: prusa-drying}
  - {problem: defects/stringing, via: causes/wet-filament, evidence: B, source: prusa-drying}
sources:
  - id: prusament
    title: Prusament material pages and technical datasheets (PA11, PA11 CF)
    resource: https://prusament.com/materials/
  - id: polymaker
    title: Polymaker Wiki and Fiberon PA TDS
    resource: https://wiki.polymaker.com/
  - id: prusa-drying
    title: Prusa Knowledge Base — Drying filament
    resource: https://help.prusa3d.com/article/drying-filament_332086
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:50:00Z
---
# Nylon (PA / PA11 / PA12 / PA6)

"Nylon" covers very different polymers and fills. Do not transfer settings between them; use the product datasheet.

## Product reference values

| Product | Nozzle | Bed | Chamber / fan | Drying |
|---|---|---|---|---|
| Prusament PA11[^prusament] | 275 ± 10 °C | 100 ± 10 °C | chamber 55 ± 5 °C, fan 15–20 % | hygroscopic (TDS: 0.46 % water after 7 days at 25 °C / 30 % RH) |
| Prusament PA11 CF[^prusament] | 285 ± 5 °C | 110 ± 10 °C | fan 20 % | 90 °C, 6 h[^prusa-drying] |
| Polymaker Fiberon PA6-CF20 / PA12-CF10[^polymaker] | 280–300 °C | 40–50 °C | fan 0 %, **doors open**, ambient ≤ 50 °C | dryer while printing |

The conflict is real: Prusament PA11 wants a warm chamber, while Polymaker's fibre-filled PA6/PA12 want an open, cool printer. Follow the product, not the polymer family.

## Pitfalls
- Moisture: PA is among the highest-risk materials for moisture defects (stringing, bubbling, poor surfaces, weak layers).[^prusa-drying] Dry before printing and print from a dry box. See [pockmarks](../defects/pockmarks.md) and [filament moisture](filament-moisture.md).
- Adhesion: glue stick or garolite (general practice). Unfilled PA is prone to [warping](../defects/warping.md).

[^prusament]: Prusament material pages and technical datasheets (PA11, PA11 CF)
[^polymaker]: Polymaker Wiki and Fiberon PA TDS
[^prusa-drying]: Prusa Knowledge Base — Drying filament

<!-- generated:relations -->
## Relations
- **Prone to:** [Pockmarks](../defects/pockmarks.md) (B) · [Stringing / oozing](../defects/stringing.md) (B) · [Warping / corner lifting](../defects/warping.md) (C)
- **Linked from:** [Filament drying and moisture](filament-moisture.md)
<!-- /generated:relations -->
