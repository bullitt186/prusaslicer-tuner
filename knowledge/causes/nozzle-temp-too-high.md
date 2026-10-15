---
type: cause
title: "Nozzle temperature too high"
description: "Low melt viscosity lets plastic ooze during travel and small features stay soft."
altLabel: [hotend too hot, printing too hot, Düsentemperatur zu hoch, zu heiß gedruckt]
facets: {phase: [thermal]}
check: "Print a temperature tower; stringing or sagging that improves at lower steps confirms it."
fixed_by:
  - {procedure: tuning/temperature-tuning, action: "lower in 5 °C steps inside the material window", sets: [{key: temperature, direction: down}]}
sources:
  - id: ellis-pla-overheating
    title: "Ellis Print Tuning Guide — PLA overheating"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/pla_overheating.html
  - id: ellis-retraction
    title: "Ellis Print Tuning Guide — Retraction"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Nozzle temperature too high

Low melt viscosity lets plastic ooze during travel and small features stay soft.

**Check:** Print a temperature tower; stringing or sagging that improves at lower steps confirms it.

<!-- generated:relations -->
## Relations
- **Fixed by:** [Temperature tuning](../tuning/temperature-tuning.md) (lower in 5 °C steps inside the material window) `temperature` ↓
- **Causes:** [Poor bridges & overhangs](../defects/bridging-overhangs.md) (#4; C) · [Overheating (esp. PLA in enclosures)](../defects/overheating.md) (#4; B) · [Stringing / oozing](../defects/stringing.md) (#2; B) · [Poor surface above or below supports](../defects/support-surface-quality.md) (#3; C) · [Scars on top surfaces](../defects/top-surface-scars.md) (#4; C) · [Zits, blobs & visible seam](../defects/zits-blobs.md) (#6; C)
<!-- /generated:relations -->
