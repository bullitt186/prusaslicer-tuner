# Troubleshooting Guide dataset → knowledge graph mapping

Dataset: [hyungjungkim/3D-printing-troubleshooting-guide](https://github.com/hyungjungkim/3D-printing-troubleshooting-guide) @ `cedd5fb`, CC BY 4.0 (Kang, Ahn, Kim; Konkuk University). Split into `raw/troubleshooting-guide/` by `import_troubleshooting_guide.py`: 63 FDM entries, 12 resin/SLA entries skipped.

**Status (2026-10-13): approved and consolidated.** Deviation from the table: "out of filament", "snapped filament" and "non-manifold edges" are altLabels of the causes only (label collision with the problems). Provenance caveat: dataset entry S3D 03 also contains Prusa KB passages; it is cited as Simplify3D.

The dataset re-publishes three sources. Each consolidated claim cites the **original** page block (`simplify3d`, `prusa-kb`, `all3dp`) plus the dataset as the source it was retrieved from. Evidence:
- B: Simplify3D and Prusa KB (vendor docs)
- C: All3DP (editorial guide)

Legend:
- **existing**: the entry maps to an existing problem; its causes become edges with a new source.
- **alias**: the entry's wording becomes an `altLabel` of an existing concept.
- **new**: creates a concept.
- ✓: cause exists already. **NEW**: cause is created.
- *skip*: out of scope.

## Entry → problem

| Entry | Target | Kind | Causes (✓ existing / NEW) |
|---|---|---|---|
| S3D 01 Not extruding at start | `defects/no-extrusion-at-start` | **new** | NEW extruder-not-primed · ✓ z-offset-too-low · ✓ extruder-gear-backlash-or-wear (stripped) · ✓ partial-clog |
| S3D 02 Not sticking to the bed | `defects/poor-bed-adhesion` | existing | ✓ bed-not-level-or-unmeshed · ✓ z-offset-too-high · NEW first-layer-too-fast · ✓ bed-temp-too-low · ✓ excessive-cooling · ✓ unsuitable-build-surface · ✓ small-contact-area |
| S3D 03 Under-extrusion | `defects/under-extrusion` | existing | ✓ wrong-filament-diameter · ✓ em-too-low · ✓ z-offset-too-low · ✓ nozzle-worn-or-leaking · ✓ extruder-gear-backlash-or-wear · ✓ heat-creep · NEW poor-filament-quality |
| S3D 04 Over-extrusion | `defects/over-extrusion` | existing | ✓ em-too-high · ✓ wrong-filament-diameter |
| S3D 05 Gaps in top layers | `defects/top-surface-gaps` | **new** | NEW top-layers-insufficient · NEW infill-too-sparse · ✓ em-too-low |
| S3D 06 Stringing or oozing | `defects/stringing` | existing | ✓ retraction-insufficient · ✓ nozzle-temp-too-high · ✓ travel-over-open-space · NEW travel-too-slow · ✓ nozzle-worn-or-leaking |
| S3D 07 Overheating | `defects/overheating` | existing | ✓ insufficient-cooling · ✓ nozzle-temp-too-high · ✓ layer-time-too-short |
| S3D 08 Layer shifting | `defects/layer-shift` | existing | ✓ acceleration-too-high · ✓ loose-mechanics · ✓ stepper-driver-or-wiring |
| S3D 09 Layer separation and splitting | `defects/poor-layer-adhesion` | existing + alias | NEW layer-height-too-large · ✓ nozzle-temp-too-low · ✓ em-too-low · ✓ excessive-cooling |
| S3D 10 Grinding filament | `defects/extruder-skipping` | existing (alias exists) | ✓ retraction-excessive · ✓ nozzle-temp-too-low · ✓ volumetric-flow-exceeded · ✓ partial-clog |
| S3D 11 Clogged extruder | `causes/partial-clog` | alias + fix detail | – |
| S3D 12 Stops extruding mid print | `defects/extrusion-stops` | **new** | NEW out-of-filament · ✓ extruder-gear-backlash-or-wear (stripped) · ✓ partial-clog · ✓ stepper-driver-or-wiring |
| S3D 13 Weak infill | `defects/weak-infill` | **new** | NEW infill-too-fast · NEW infill-line-too-thin · ✓ partial-clog |
| S3D 14 Blobs and zits | `defects/zits-blobs` | existing | ✓ seam-start-stop-pressure · NEW too-many-retractions · ✓ seam-random |
| S3D 15 Gaps between infill and outline | `defects/infill-wall-gaps` | **new** | ✓ infill-overlap-wrong · ✓ print-speed-too-high |
| S3D 16 Curling or rough corners | `defects/overheating` | alias | ✓ insufficient-cooling · ✓ nozzle-temp-too-high |
| S3D 17 Scars on top surface | `defects/top-surface-scars` | **new** | ✓ em-too-high · NEW no-z-hop |
| S3D 18 Gaps in floor corners | `defects/top-surface-gaps` | alias | NEW too-few-perimeters · NEW top-layers-insufficient · NEW infill-too-sparse |
| S3D 19 Lines on the side of print | `defects/z-banding` | **new** | ✓ filament-tension-or-drag · NEW temperature-fluctuation · ✓ worn-or-binding-motion-parts |
| S3D 20 Vibrations and ringing | `defects/ringing` | existing | ✓ print-speed-too-high · ✓ acceleration-too-high · ✓ loose-mechanics |
| S3D 21 Gaps in thin walls | `defects/thin-walls-and-small-features` | **new** | NEW wall-thinner-than-line-width |
| S3D 22 Small features not printed | `defects/thin-walls-and-small-features` | alias | NEW wall-thinner-than-line-width · NEW nozzle-too-large-for-detail |
| S3D 23 Inconsistent extrusion | `defects/inconsistent-extrusion` | **new** | ✓ filament-tension-or-drag · ✓ partial-clog · NEW layer-height-too-small · NEW poor-filament-quality · ✓ extruder-gear-backlash-or-wear |
| S3D 24 Warping | `defects/warping` | existing | ✓ bed-temp-too-low · ✓ excessive-cooling · ✓ chamber-too-cold · ✓ small-contact-area |
| S3D 25 Poor surface above supports | `defects/support-surface-quality` | **new** | NEW support-interface-settings · ✓ layer-height-too-large |
| S3D 26 Dimensional accuracy | `defects/dimensional-inaccuracy` | **new** | ✓ z-offset-too-low · ✓ em-too-high · NEW shrinkage-uncompensated · ✓ loose-mechanics |
| S3D 27 Poor bridging | `defects/bridging-overhangs` | existing | ✓ bridge-flow-or-speed-wrong · NEW missing-supports · ✓ insufficient-cooling |
| PKB 28 First layer issues | `defects/poor-bed-adhesion`, `defects/first-layer-inconsistency` | existing | ✓ contaminated-build-surface · ✓ unsuitable-build-surface · ✓ z-offset-too-high/low · ✓ partial-clog · ✓ bed-not-level-or-unmeshed (MK4/XL load-cell steps: *skip*, printer-specific) |
| PKB 29 Layer shifting | `defects/layer-shift` | existing | ✓ worn-or-binding-motion-parts · ✓ loose-mechanics · ✓ nozzle-strike-on-curled-part |
| A3D 01 Out of filament | `defects/extrusion-stops` | alias | NEW out-of-filament |
| A3D 02 Nozzle too close to print bed | `causes/z-offset-too-low` | alias | – |
| A3D 03 Blocked nozzle | `causes/partial-clog` | alias (exists) | – |
| A3D 04 Print head misses the bed | – | *skip* | printer setup (wrong printer profile, end stops), not tuning |
| A3D 05 Snapped filament | `defects/extrusion-stops` | alias | NEW brittle-filament · ✓ filament-tension-or-drag |
| A3D 06 Stripped filament | `defects/extruder-skipping` | alias | ✓ filament-tension-or-drag · ✓ nozzle-temp-too-low |
| A3D 07 Extrusion stopped mid-print | `defects/extrusion-stops` | alias | (as S3D 12) |
| A3D 08 Print doesn't stick to print bed | `defects/poor-bed-adhesion` | existing | ✓ bed-not-level-or-unmeshed · ✓ z-offset-too-high · ✓ contaminated-build-surface |
| A3D 09 Supports fell apart | `defects/supports-fail` | **new** | NEW support-too-weak · ✓ small-contact-area |
| A3D 10 First layer is messy | `defects/first-layer-inconsistency` | alias | ✓ bed-not-level-or-unmeshed · ✓ bed-temp-too-high |
| A3D 11 Elephant's foot | `defects/elephant-foot` | existing | ✓ bed-temp-too-high · ✓ z-offset-too-low · ✓ elephant-foot-compensation-missing |
| A3D 12 Warping | `defects/warping` | existing | ✓ bed-temp-too-low · ✓ small-contact-area · ✓ unsuitable-build-surface |
| A3D 13 Infill messy and incomplete | `defects/weak-infill` | alias | NEW infill-too-sparse · NEW infill-too-fast · ✓ partial-clog |
| A3D 14 Gaps between infill and outer wall | `defects/infill-wall-gaps` | alias | ✓ infill-overlap-wrong · ✓ nozzle-temp-too-low · ✓ print-speed-too-high |
| A3D 15 Infill visible from outside | `defects/infill-visible-through-walls` | **new** | NEW too-few-perimeters · ✓ perimeter-order |
| A3D 16 Cracks in tall objects | `defects/poor-layer-adhesion` | alias | ✓ nozzle-temp-too-low · ✓ excessive-cooling |
| A3D 17 Layers don't line up well | `defects/layer-shift` | alias | ✓ loose-mechanics · ✓ worn-or-binding-motion-parts |
| A3D 18 Some layers are missing | `defects/under-extrusion` | alias | ✓ worn-or-binding-motion-parts |
| A3D 19 Print leans | `defects/layer-shift` | alias | ✓ loose-mechanics |
| A3D 20 Overhangs are messy | `defects/bridging-overhangs` | alias | NEW missing-supports |
| A3D 21 Surface beneath supports rough | `defects/support-surface-quality` | alias | NEW support-interface-settings · ✓ nozzle-temp-too-high |
| A3D 22 Non-manifold edges | `defects/model-errors` | **new** | NEW non-manifold-mesh |
| A3D 23 Fine detail not printing | `defects/thin-walls-and-small-features` | alias | NEW nozzle-too-large-for-detail · ✓ print-speed-too-high |
| A3D 24 Ringing | `defects/ringing` | existing | ✓ worn-or-binding-motion-parts · ✓ loose-mechanics · ✓ acceleration-too-high |
| A3D 25 Diagonal scars | `defects/top-surface-scars` | alias | ✓ travel-over-open-space · NEW no-z-hop · ✓ em-too-high |
| A3D 26 Stringy and droopy (over-extrusion) | `defects/over-extrusion` | existing | ✓ em-too-high |
| A3D 27 Uniformly thin layers (under-extrusion) | `defects/under-extrusion` | existing | ✓ wrong-filament-diameter · ✓ partial-clog · ✓ em-too-low |
| A3D 28 Melted and deformed | `defects/overheating` | alias | ✓ nozzle-temp-too-high · ✓ insufficient-cooling |
| A3D 29 Pillowing | `defects/top-surface-gaps` | alias | ✓ insufficient-cooling · NEW top-layers-insufficient |
| A3D 30 Web-like strings | `defects/stringing` | existing | ✓ retraction-insufficient · ✓ travel-over-open-space |
| A3D 31 Lost dimensional accuracy | `defects/dimensional-inaccuracy` | alias | ✓ loose-mechanics · NEW shrinkage-uncompensated · ✓ nozzle-temp-too-high |
| A3D 32 Print offset in some places | `defects/layer-shift` | alias | ✓ nozzle-strike-on-curled-part · ✓ loose-mechanics · ✓ print-speed-too-high |
| A3D 33 Bridges are messy | `defects/bridging-overhangs` | existing | ✓ insufficient-cooling · NEW missing-supports · ✓ bridge-flow-or-speed-wrong |
| A3D 34 Print stuck to print bed | `defects/part-stuck-to-bed` | **new** | NEW adhesion-too-strong |

## Summary

- **63 entries:** 62 mapped, 1 skipped (A3D 04, printer setup).
- **15 new problems:**
  - no-extrusion-at-start, extrusion-stops, top-surface-gaps (incl. pillowing)
  - weak-infill, infill-wall-gaps, infill-visible-through-walls
  - top-surface-scars, z-banding, thin-walls-and-small-features, inconsistent-extrusion
  - support-surface-quality, supports-fail, dimensional-inaccuracy, model-errors, part-stuck-to-bed
- **24 new causes:**
  - extruder-not-primed, first-layer-too-fast, poor-filament-quality
  - top-layers-insufficient, infill-too-sparse, travel-too-slow
  - layer-height-too-large, layer-height-too-small
  - out-of-filament, brittle-filament
  - infill-too-fast, infill-line-too-thin, too-many-retractions, no-z-hop, too-few-perimeters
  - temperature-fluctuation, wall-thinner-than-line-width, nozzle-too-large-for-detail
  - support-interface-settings, support-too-weak, missing-supports, shrinkage-uncompensated
  - non-manifold-mesh, adhesion-too-strong
- **Existing concepts enriched:** 14 problems get new source-backed edges and aliases. Unsourced v0.1 problems (over-extrusion, under-extrusion, warping, ringing, elephant-foot, zits-blobs, bridging-overhangs) get their first real sources.
- **Translation rule:** Simplify3D settings are mapped to PrusaSlicer keys (validated by `kg.py`). For example, *coasting* → `wipe` / `retract_before_wipe`, *outline overlap* → `infill_overlap`, *single extrusion walls* → `thin_walls`, *dense support layers* → `support_material_interface_layers`.
