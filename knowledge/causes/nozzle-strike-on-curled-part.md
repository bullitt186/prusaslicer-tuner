---
type: cause
title: "Nozzle hits curled print"
description: "Curled overhangs or warped corners catch the nozzle, knocking the toolhead or part."
altLabel: [nozzle collision, Düse kollidiert]
facets: {phase: [motion]}
check: "Shift happens at a layer with curling; scuff marks on the part."
fixed_by:
  - {procedure: tuning/cooling-layer-times, action: "fix curling; use a small z-hop", sets: [{key: retract_lift, direction: up}]}
sources:
  - id: ellis-layer-shifting
    title: "Ellis Print Tuning Guide — Layer shifting"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/layer_shifting.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Nozzle hits curled print

Curled overhangs or warped corners catch the nozzle, knocking the toolhead or part.

**Check:** Shift happens at a layer with curling; scuff marks on the part.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Cooling and layer times](../tuning/cooling-layer-times.md) (fix curling; use a small z-hop) `retract_lift` ↑
- **Causes:** [Layer shifting](../defects/layer-shift.md) (#3; B)
<!-- /generated:relations -->
