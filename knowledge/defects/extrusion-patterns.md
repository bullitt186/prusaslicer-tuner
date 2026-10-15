---
type: defect
title: Extrusion patterns ("wood grain")
description: Repeating innie-outie texture along lines, often from extruder gear backlash.
timestamp: 2026-10-13
altLabel: [wood grain, Holzmaserung, Extrusionsmuster]
facets: {phase: [extrusion]}
caused_by:
  - {cause: causes/extruder-gear-backlash-or-wear, rank: 1, evidence: B, source: ellis-extrusion-patterns}
  - {cause: causes/filament-tension-or-drag, rank: 2, evidence: B, source: ellis-extrusion-patterns}
sources:
  - id: ellis-extrusion-patterns
    title: "Ellis Print Tuning Guide — Extrusion patterns"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extrusion_patterns.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Extrusion patterns / wood grain
- Cause: extruder gear backlash that is too small (wear plus patterns) or too large (clacking, inconsistent PA, stringing), worn drive gear teeth, wrong filament tension, or eccentric gears. Diagonal patterns can be axis mechanics instead.
- Fix: set a small but nonzero backlash (measured with filament loaded and tensioned), replace worn gears, then **re-tune PA and rotation_distance**. `external_perimeters_first = 1` reduces the visible effect.
- No slicer setting fixes the root cause. See [VFAs](vfas.md) for vertical artifacts.

<!-- generated:relations -->
## Relations
- **Caused by:** [Extruder gear backlash, play or wear](../causes/extruder-gear-backlash-or-wear.md) (#1; B) · [Filament tension or path drag](../causes/filament-tension-or-drag.md) (#2; B)
- **Related:** [Inconsistent extrusion](inconsistent-extrusion.md)
- **Linked from:** [Pressure advance / Linear advance](../tuning/pressure-advance.md)
<!-- /generated:relations -->
