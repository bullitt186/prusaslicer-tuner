---
type: material
title: TPU (flexible)
description: Slow, low retraction, very hygroscopic; direct drive strongly preferred.
timestamp: 2026-10-13
altLabel: [flexible filament, TPE, flexibles Filament]
prone_to:
  - {problem: defects/stringing, via: causes/wet-filament, evidence: B, source: prusa-drying}
  - {problem: defects/extruder-skipping, via: causes/retraction-excessive, evidence: C}
sources:
  - id: prusament
    title: Prusament material pages (TPU 95A)
    resource: https://prusament.com/materials/
  - id: polymaker
    title: Polymaker Wiki and PolyFlex TPU TDS
    resource: https://wiki.polymaker.com/
  - id: prusa-drying
    title: Prusa Knowledge Base — Drying filament
    resource: https://help.prusa3d.com/article/drying-filament_332086
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:50:00Z
---
# TPU 95A

## Product reference values

| Product | Nozzle | Bed | Speed | Drying |
|---|---|---|---|---|
| Prusament TPU 95A[^prusament] | 230 ± 10 °C | 65 ± 10 °C | slow (no numeric value) | usually none; if needed ≥ 4 h at 60 °C, then drybox |
| Prusa KB drying table[^prusa-drying] | – | – | – | 60 °C, 4–6 h |
| Polymaker PolyFlex TPU95[^polymaker] | 210–230 °C | 25–60 °C | 30–50 mm/s | 70 °C, 8 h |

## Pitfalls
- Flow: soft filament buckles at high flow. A max volumetric speed of about 1.5–4 mm³/s is a typical starting range for TPU 95A on direct drive (general practice); validate with [max volumetric flow](../tuning/max-volumetric-flow.md).
- Retraction: minimal and slow on direct drive (0–1 mm as a starting range, general practice). Long or fast retractions jam the filament in the extruder. Polymaker's 3–6 mm generic retraction range assumes other extruder types.[^polymaker]
- Moisture: TPU is a higher-risk material for moisture defects, so stringing and blobs often mean it needs drying.[^prusa-drying]
- Can bond permanently to PEI: use glue stick as a release agent.

[^prusament]: Prusament material pages (TPU 95A)
[^polymaker]: Polymaker Wiki and PolyFlex TPU TDS
[^prusa-drying]: Prusa Knowledge Base — Drying filament

<!-- generated:relations -->
## Relations
- **Prone to:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (C) · [Stringing / oozing](../defects/stringing.md) (B)
- **Linked from:** [Filament drying and moisture](filament-moisture.md)
<!-- /generated:relations -->
