---
type: material-process
title: Filament drying and moisture
description: Moisture changes extrusion behavior and surface quality; drying must follow the polymer and product's validated limits.
tags: [material, moisture, drying, stringing, nylon, petg, tpu]
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: prusament-petg
    title: Prusament PETG product documentation
    resource: https://prusament.com/materials/prusament-petg/
  - id: ellis-retraction
    title: Ellis Print Tuning Guide — Retraction
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/retraction.html
---
# Filament drying and moisture

Moisture is a material state, not a slicer parameter. Wet filament can produce popping, bubbles, inconsistent extrusion, surface defects and stringing; PETG documentation also identifies ooze/stringing as a characteristic that may require temperature or retraction control. [^prusament-petg]

## Diagnostic sequence

1. Compare a sealed/dried spool with the suspect spool using the same profile and a short travel-heavy test.
2. Listen for popping and inspect the surface for tiny voids or foaming. These observations support moisture as a hypothesis but do not prove it; a damaged nozzle or excessive temperature can look similar.
3. Dry using the filament manufacturer's polymer/product guidance and a controlled dryer. Do not invent a drying temperature from the polymer family alone: additives, spool construction and glass-transition limits differ.
4. Keep hygroscopic materials in a dry box during printing when the process requires it. Re-test retraction only after moisture state is controlled; otherwise retraction values confound two causes. [^ellis-retraction]

## Evidence boundary

- **B:** moisture is a credible first check for hygroscopic filaments and for popping/stringing symptoms.
- **A/B:** the correct drying time/temperature is product-specific and must come from the manufacturer or a validated process.
- A dry box can reduce re-absorption during printing but does not necessarily replace a proper drying cycle for already wet material.

Related: [stringing](../defects/stringing.md), [temperature tuning](../tuning/temperature-tuning.md), [retraction](../tuning/retraction.md).

## Related
- [Nylon (PA)](nylon.md)
- [TPU](tpu.md)

[^prusament-petg]: Prusament PETG product documentation
[^ellis-retraction]: Ellis Print Tuning Guide — Retraction

<!-- generated:relations -->
## Relations
- **Fixes:** [Wet filament](../causes/wet-filament.md) (dry the spool and print from a dry box)
- **Linked from:** [Engineering materials and reinforced filaments](engineering-materials.md) · [Nylon (PA)](nylon.md) · [PC / PC-CF](pc-cf.md)
<!-- /generated:relations -->
