---
type: cause
title: "Binding or worn bearings, rails or motors"
description: "Rough bearings, rails or motors add periodic artifacts and resistance that can skip steps."
altLabel: [binding rail, worn bearing, schwergängige Achse, verschlissene Lager]
facets: {phase: [mechanics]}
check: "Move each axis by hand with motors off; print square samples aligned and at 45° to isolate the axis."
fixed_by:
  - {action: "clean, lubricate or replace bearings, rails and motors"}
sources:
  - id: ellis-layer-shifting
    title: "Ellis Print Tuning Guide — Layer shifting"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/layer_shifting.html
  - id: ellis-vfas
    title: "Ellis Print Tuning Guide — VFAs"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/vfas.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Binding or worn bearings, rails or motors

Rough bearings, rails or motors add periodic artifacts and resistance that can skip steps.

**Check:** Move each axis by hand with motors off; print square samples aligned and at 45° to isolate the axis.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (clean, lubricate or replace bearings, rails and motors)
- **Causes:** [Layer shifting](../defects/layer-shift.md) (#2; B) · [Ringing / ghosting](../defects/ringing.md) (#5; C) · [Under-extrusion](../defects/under-extrusion.md) (#13; C) · [VFAs (vertical fine artifacts)](../defects/vfas.md) (#2; B) · [Lines or ridges on the sides (Z banding)](../defects/z-banding.md) (#3; B)
<!-- /generated:relations -->
