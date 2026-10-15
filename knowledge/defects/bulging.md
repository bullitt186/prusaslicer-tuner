---
type: defect
title: Bulging
description: Plastic pushed outward from perimeters — layers, sharp corners, around features, above overhangs.
timestamp: 2026-10-13
altLabel: [walls bulge, Ausbeulungen, Beulen]
facets: {phase: [walls-seams]}
caused_by:
  - {cause: causes/perimeter-order, rank: 1, evidence: B, source: ellis-bulging}
  - {cause: causes/acceleration-too-high, rank: 2, evidence: B, source: ellis-bulging}
  - {cause: causes/em-too-high, rank: 3, evidence: B, source: ellis-bulging}
  - {cause: causes/infill-overlap-wrong, rank: 4, evidence: B, source: ellis-bulging}
  - {cause: causes/bridge-flow-or-speed-wrong, rank: 5, evidence: B, source: ellis-bulging}
  - {cause: causes/insufficient-cooling, rank: 6, evidence: B, source: ellis-bulging}
sources:
  - id: ellis-bulging
    title: "Ellis Print Tuning Guide — Bulging"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/bulging.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Bulging

| Where | Likely cause | Fix |
|---|---|---|
| Layers and perimeters in general | perimeter order, high accelerations | `external_perimeters_first = 1`, disable `extra_perimeters`, lower `perimeter_acceleration` / `external_perimeter_acceleration` |
| Sharp corners (STL vertices) | corner speed or jerk (Klipper `square_corner_velocity`), high speed or accel, input shaper, binding | retest those, and check the mechanics by hand |
| Around features | overextruded solid infill pushing out the perimeter | tune [PA](../tuning/pressure-advance.md) and [EM](../tuning/extrusion-multiplier.md), set `external_perimeters_first`, lower `infill_overlap` to 20–25% |
| Above overhangs and bridges | bridge flow above 100% | `bridge_flow_ratio` back to 1 (100%) |
| Lower layers | part lifted from the bed | [poor bed adhesion](poor-bed-adhesion.md) |
| Small parts in general | overheating | [cooling](../tuning/cooling-layer-times.md) |

External-perimeters-first needs good stepover and can hurt extreme overhangs.

<!-- generated:relations -->
## Relations
- **Caused by:** [Perimeter order pushes walls out](../causes/perimeter-order.md) (#1; B) · [Acceleration or corner velocity too high](../causes/acceleration-too-high.md) (#2; B) · [Extrusion multiplier too high](../causes/em-too-high.md) (#3; B) · [Infill/perimeter overlap wrong](../causes/infill-overlap-wrong.md) (#4; B) · [Bridge flow or speed wrong](../causes/bridge-flow-or-speed-wrong.md) (#5; B) · [Insufficient part cooling](../causes/insufficient-cooling.md) (#6; B)
- **Linked from:** [Over-extrusion](over-extrusion.md) · [Cooling and layer times](../tuning/cooling-layer-times.md) · [Pressure advance / Linear advance](../tuning/pressure-advance.md)
<!-- /generated:relations -->
