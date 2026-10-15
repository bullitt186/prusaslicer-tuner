---
type: defect
title: Perimeter separation
description: Walls not bonding to each other or layer below — lower layers (elephant foot comp) or everywhere (width, speed, temp).
timestamp: 2026-10-13
altLabel: [wall separation, perimeters not bonding, Perimeter lösen sich]
facets: {phase: [walls-seams]}
caused_by:
  - {cause: causes/z-offset-too-high, rank: 1, evidence: B, source: ellis-perimeter-separation}
  - {cause: causes/elephant-foot-compensation-too-high, rank: 2, evidence: B, source: ellis-perimeter-separation}
  - {cause: causes/external-perimeter-too-narrow, rank: 3, evidence: B, source: ellis-perimeter-separation}
  - {cause: causes/em-too-low, rank: 4, evidence: B, source: ellis-perimeter-separation}
  - {cause: causes/print-speed-too-high, rank: 5, evidence: B, source: ellis-perimeter-separation}
  - {cause: causes/nozzle-temp-too-low, rank: 6, evidence: B, source: ellis-perimeter-separation}
  - {cause: causes/excessive-cooling, rank: 7, evidence: B, source: ellis-perimeter-separation}
  - {cause: causes/wet-filament, rank: 8, evidence: B, source: ellis-perimeter-separation}
sources:
  - id: ellis-perimeter-separation
    title: "Ellis Print Tuning Guide — Perimeter separation"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/perimeter_separation.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
---
# Perimeter separation
- **Only on lower layers:** too little first-layer squish, or `elefant_foot_compensation` too high (especially with bottom chamfers). Reduce it.
- **Everywhere:** external perimeter too narrow for the layer height (once layer height is > 50% of the nozzle, widen `external_perimeter_extrusion_width`), EM too low, perimeters too fast (`perimeter_speed`, `external_perimeter_speed`, `small_perimeter_speed`), or hotend too cold (raise `temperature`; ABS about 240–255 °C).
- Weak layer bonding in general: higher temperature, less cooling (`max_fan_speed`), and dry filament.

<!-- generated:relations -->
## Relations
- **Caused by:** [Nozzle too far from the bed](../causes/z-offset-too-high.md) (#1; B) · [Elephant-foot compensation too high](../causes/elephant-foot-compensation-too-high.md) (#2; B) · [External perimeter too narrow](../causes/external-perimeter-too-narrow.md) (#3; B) · [Extrusion multiplier too low](../causes/em-too-low.md) (#4; B) · [Print speed too high](../causes/print-speed-too-high.md) (#5; B) · [Nozzle temperature too low](../causes/nozzle-temp-too-low.md) (#6; B) · [Too much part cooling](../causes/excessive-cooling.md) (#7; B) · [Wet filament](../causes/wet-filament.md) (#8; B)
- **Linked from:** [Elephant foot](elephant-foot.md) · [Under-extrusion](under-extrusion.md)
<!-- /generated:relations -->
