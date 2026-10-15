---
type: material
title: ABS / ASA
description: Needs enclosure & heat soak; warps; surprisingly high fan OK in a hot chamber.
timestamp: 2026-10-13
altLabel: [ABS, ASA]
prone_to:
  - {problem: defects/warping, via: causes/chamber-too-cold, evidence: B, source: prusa-warping}
  - {problem: defects/warping, via: causes/material-shrinkage, evidence: B, source: prusa-warping}
sources:
  - id: prusament
    title: Prusament material pages and technical datasheets (ASA)
    resource: https://prusament.com/materials/
  - id: polymaker
    title: Polymaker Wiki and PolyLite ABS / Polymaker ASA TDS
    resource: https://wiki.polymaker.com/
  - id: prusa-asa
    title: Prusa Knowledge Base — ASA
    resource: https://help.prusa3d.com/article/asa_1809
  - id: prusa-warping
    title: Prusa Knowledge Base — Warping
    resource: https://help.prusa3d.com/article/warping_2011
  - id: prusa-drying
    title: Prusa Knowledge Base — Drying filament
    resource: https://help.prusa3d.com/article/drying-filament_332086
  - id: ellis-cooling
    title: Ellis Print Tuning Guide — Cooling and layer times
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/cooling_and_layer_times.html
generated:
  by: process:kg-maintenance
  at: 2026-10-13T23:50:00Z
---
# ABS / ASA

## Product reference values

| Product | Nozzle | Bed | Fan | Drying |
|---|---|---|---|---|
| Prusament ASA[^prusament] | 260 ± 10 °C | 110 ± 5 °C | 30 % (0–50 %) | 80 °C, 4 h[^prusa-drying] |
| Prusa KB ASA starting values[^prusa-asa] | 260 °C | 105 / 110 °C first/later | – | – |
| Polymaker PolyLite ABS[^polymaker] | 245–265 °C | 90–100 °C | off | 70 °C, 6 h |
| Polymaker ASA[^polymaker] | 230–260 °C | 75–95 °C | off | 70 °C, 7 h |

Fan advice conflicts: vendors say off or low, while in a hot, heat-soaked chamber noticeably more fan works for small parts and overhangs.[^ellis-cooling] Decide per part with a controlled comparison. On the Voron 2.4 the thick bed needs the upper end of the bed range (printer fact).

## Pitfalls
- [Warping](../defects/warping.md): enclose the printer or use a draft shield, keep the surface grease-free and use a brim for large parts.[^prusa-warping] Heat soak the chamber; 45–60 °C chamber is a typical target on enclosed Klipper printers (general practice).
- Layer splitting on tall parts: hotter nozzle, less fan.
- Fumes: filter or vent.
- Dimensional: ABS/ASA shrink measurably in XY. Compensate with `filament_shrinkage_compensation_xy` after the EM is tuned, using a measured value for the product (see [dimensional inaccuracy](../defects/dimensional-inaccuracy.md)).

[^prusament]: Prusament material pages and technical datasheets (ASA)
[^polymaker]: Polymaker Wiki and PolyLite ABS / Polymaker ASA TDS
[^prusa-asa]: Prusa Knowledge Base — ASA
[^prusa-warping]: Prusa Knowledge Base — Warping
[^prusa-drying]: Prusa Knowledge Base — Drying filament
[^ellis-cooling]: Ellis Print Tuning Guide — Cooling and layer times

<!-- generated:relations -->
## Relations
- **Prone to:** [Warping / corner lifting](../defects/warping.md) (B)
<!-- /generated:relations -->
