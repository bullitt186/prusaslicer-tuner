---
type: material
title: PETG
description: Stringy, hygroscopic, sticks too well to smooth PEI; moderate cooling.
timestamp: 2026-10-13
altLabel: [PET-G, Polyethylenterephthalat-Glykol]
prone_to:
  - {problem: defects/stringing, via: causes/wet-filament, evidence: B, source: prusa-drying}
  - {problem: defects/stringing, evidence: B, source: ellis-retraction, note: some stringing is inherent to PETG}
  - {problem: defects/part-stuck-to-bed, via: causes/adhesion-too-strong, evidence: B, source: prusa-petg}
sources:
  - id: prusament
    title: Prusament material pages and technical datasheets (PETG)
    resource: https://prusament.com/materials/
  - id: polymaker
    title: Polymaker Wiki and PolyLite/PolyMax PETG TDS
    resource: https://wiki.polymaker.com/
  - id: prusa-petg
    title: Prusa Knowledge Base — PETG
    resource: https://help.prusa3d.com/article/petg_2059
  - id: prusa-drying
    title: Prusa Knowledge Base — Drying filament
    resource: https://help.prusa3d.com/article/drying-filament_332086
  - id: ellis-retraction
    title: Ellis Print Tuning Guide — Retraction
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:50:00Z
---
# PETG

## Product reference values

Values are product-specific; use the spool's own datasheet when it exists.

| Product | Nozzle | Bed | Fan | Drying |
|---|---|---|---|---|
| Prusament PETG[^prusament] | 250 ± 10 °C | 80 ± 10 °C | 50 % | (not given on page) |
| Prusa KB starting values[^prusa-petg] | 230 / 240 °C first/later | 85 / 90 °C first/later | – | 55 °C, 6 h[^prusa-drying] |
| Polymaker PolyLite/PolyMax PETG[^polymaker] | 230–260 °C | 70–80 °C | off–20 % | 65 °C, 6 h |

Fan guidance differs between vendors (Prusament 50 %, Polymaker off–20 %): start low for layer bonding and raise it for overhangs and bridges.

## Pitfalls
- **Stringing is the classic PETG defect.** Moisture makes it worse, so check and dry first.[^prusa-drying] Then lower the temperature in 5 °C steps inside the product window, enable `avoid_crossing_perimeters` and wipe, and keep retraction moderate. Typical direct-drive starting values are 0.6–1.0 mm at 30–40 mm/s with z-hop ≤ 0.2 mm (general practice, not a vendor value). Some stringing is normal.[^ellis-retraction] See [stringing](../defects/stringing.md).
- Bonds too strongly to smooth PEI; Prusa recommends powder-coated or satin sheets.[^prusa-petg] Use glue stick as a release agent on smooth PEI.
- Zits and blobs on the nozzle: a slightly lower temperature, a clean nozzle, a silicone sock (general practice).

[^prusament]: Prusament material pages and technical datasheets (PETG)
[^polymaker]: Polymaker Wiki and PolyLite/PolyMax PETG TDS
[^prusa-petg]: Prusa Knowledge Base — PETG
[^prusa-drying]: Prusa Knowledge Base — Drying filament
[^ellis-retraction]: Ellis Print Tuning Guide — Retraction

<!-- generated:relations -->
## Relations
- **Prone to:** [Print stuck to the bed](../defects/part-stuck-to-bed.md) (B) · [Stringing / oozing](../defects/stringing.md) (B)
- **Linked from:** [Retraction](../tuning/retraction.md)
<!-- /generated:relations -->
