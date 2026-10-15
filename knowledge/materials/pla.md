---
type: material
title: PLA
description: Easy, low-temp, loves cooling; overheats in enclosures.
timestamp: 2026-10-13
altLabel: [Polylactid]
prone_to:
  - {problem: defects/overheating, via: causes/chamber-too-hot-for-material, evidence: B, source: ellis-pla-overheating}
  - {problem: defects/extruder-skipping, via: causes/heat-creep, evidence: B, source: ellis-extruder-skipping}
sources:
  - id: prusament
    title: Prusament material pages and technical datasheets (PLA)
    resource: https://prusament.com/materials/
  - id: polymaker
    title: Polymaker Wiki and PolyLite PLA TDS
    resource: https://wiki.polymaker.com/
  - id: prusa-drying
    title: Prusa Knowledge Base — Drying filament
    resource: https://help.prusa3d.com/article/drying-filament_332086
  - id: ellis-pla-overheating
    title: Ellis Print Tuning Guide — PLA overheating
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/pla_overheating.html
  - id: ellis-extruder-skipping
    title: Ellis Print Tuning Guide — Extruder skipping
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:50:00Z
---
# PLA

## Product reference values

| Product | Nozzle | Bed | Fan | Drying (if needed) |
|---|---|---|---|---|
| Prusament PLA[^prusament] | 210 ± 10 °C | 40–60 °C | 100 % | 45 °C, 6 h[^prusa-drying] |
| Prusament PLA High Speed[^prusament] | 210 ± 20 °C | 50 ± 10 °C | 100 % | – |
| Polymaker PolyLite/PolyMax PLA[^polymaker] | 190–230 °C | 25–60 °C | on | 55 °C, 6 h |

Silk and high-speed PLAs run hotter than standard PLA; silk PLA strings more and needs its own EM (general practice).

## Pitfalls
- [Overheating](../defects/overheating.md) and heat-creep jams in a closed, warm printer: open the door or remove panels.[^ellis-pla-overheating] Heat creep with PLA in an enclosure is a known [extruder skipping](../defects/extruder-skipping.md) cause.[^ellis-extruder-skipping]
- Retraction: short on direct drive; 0.4–0.8 mm is a typical starting range (general practice; Polymaker's 1–3 mm generic range covers Bowden setups too).[^polymaker]

[^prusament]: Prusament material pages and technical datasheets (PLA)
[^polymaker]: Polymaker Wiki and PolyLite PLA TDS
[^prusa-drying]: Prusa Knowledge Base — Drying filament
[^ellis-pla-overheating]: Ellis Print Tuning Guide — PLA overheating
[^ellis-extruder-skipping]: Ellis Print Tuning Guide — Extruder skipping

<!-- generated:relations -->
## Relations
- **Prone to:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (B) · [Overheating (esp. PLA in enclosures)](../defects/overheating.md) (B)
- **Linked from:** [Stringing / oozing](../defects/stringing.md)
<!-- /generated:relations -->
