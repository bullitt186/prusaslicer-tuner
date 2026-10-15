# Prusa Knowledge Base FDM Research Report

## SOURCE_METADATA

- Source: [Prusa Knowledge Base](https://help.prusa3d.com/); primary English article pages inspected directly on 2026-10-13.
- Scope: FFF/FDM first-layer and adhesion; layers/perimeters; extrusion width and nozzle profiles; materials; cooling; supports; troubleshooting; drying; calibration; printer-specific behavior.
- Repository fit: Findings map to this repo's PrusaSlicer concepts: first-layer height/Z, extrusion widths, layer height, perimeters, extrusion multiplier, temperatures, cooling, supports/brim, nozzle type, and printer/firmware family.
- Method: Primary article bodies were opened and paraphrased. Search snippets were used only for discovery. Product/query parameters are retained where they affect scope.

## COVERAGE

| Topic | Primary article | Scope |
|---|---|---|
| First layer/Z | [First Layer Calibration (i3)](https://help.prusa3d.com/article/first-layer-calibration-i3_112364); [Live adjust Z](https://help.prusa3d.com/article/live-adjust-z_112427); [First layer issues](https://help.prusa3d.com/article/first-layer-issues_1804?product=mk3-5); [MINI/MINI+ calibration](https://help.prusa3d.com/article/first-layer-calibration-mini-mini_229122) | i3/MK2/MK3/MK3.5/MINI sensor workflows; CORE One/MK4/MK3.9/XL LoadCell workflows |
| Geometry | [Layers and perimeters](https://help.prusa3d.com/article/layers-and-perimeters_1748) | PrusaSlicer; Arachne/Classic, thin walls, external perimeters |
| Nozzles/width | [Different nozzle profiles](https://help.prusa3d.com/article/creating-profiles-for-different-nozzles_127540?product=mmu1); [Nextruder nozzle types](https://help.prusa3d.com/article/prusa-nozzle-types-for-nextruder-printers_928993) | PrusaSlicer profiles; Nextruder material/nozzle matrix |
| Materials | [Filament Material Guide](https://help.prusa3d.com/filament-material-guide); [PETG](https://help.prusa3d.com/article/petg_2059?product=mmu3); [ASA](https://help.prusa3d.com/article/asa_1809) | Matrix plus detailed PETG/ASA articles |
| Cooling | [Cooling](https://help.prusa3d.com/article/cooling_127569) | MK3/MK3.5/MINI/MK4/XL/MMU; per-filament settings |
| Supports | [First print with PrusaSlicer 3.0.0](https://help.prusa3d.com/article/first-print-with-prusaslicer-3-0-0_1079761); [Paint-on supports](https://help.prusa3d.com/article/paint-on-supports_168584); [XL combining materials](https://help.prusa3d.com/article/combining-materials-xl_498103) | Generic PrusaSlicer; XL multi-tool exceptions |
| Drying | [Drying filament](https://help.prusa3d.com/article/drying-filament_332086?product=plus-1-75-mm); [USS Drybox](https://help.prusa3d.com/article/prusa-uss-drybox_1014382); [Memmert UF oven](https://help.prusa3d.com/article/drying-filament-in-memmert-uf-series-universal-oven_913458) | MK4/XL/MMU/PRO/MINI; XL multi-tool and drybox distinctions |
| Calibration/troubleshooting | [Calibration](https://help.prusa3d.com/category/calibration_199); [Extrusion multiplier](https://help.prusa3d.com/article/extrusion-multiplier-calibration_2257?product=mini); [Warping](https://help.prusa3d.com/article/warping_2011?product=enclosure); [Clogged nozzle](https://help.prusa3d.com/article/clogged-nozzle-core-one-core-one-l-xl-mk4-s-mk3-9-s_411823?product=xl) | Flow, Z, bed, motion, warping and Nextruder clog behavior |
| Compatibility | [G-code compatibility](https://help.prusa3d.com/article/the-g-code-isnt-fully-compatible-31803-core-one-26803-mk4s-27803-mk3-9s-28803-mk3-5s-13803-mk4-21803-mk3-9-23803-mk3-5-17803-xl-12803-mini_899392); [Power modes](https://help.prusa3d.com/article/power-modes_2213) | Current CORE One/MK4/MK3.9/MK3.5/XL/MINI; firmware 6.0+ modes |

## CLAIMS

Evidence format: A = exact primary article; B = paraphrased claim; C = conditions/scope; D = implication for prusaslicer-tuner.

### First layer and adhesion

1. **First-layer Z is visual and printer/sheet-specific.**
   - A: [First Layer Calibration (i3)](https://help.prusa3d.com/article/first-layer-calibration-i3_112364).
   - B: Good output is continuous and evenly flattened; gaps mean too high, while ridges, curling, transparency, blocked flow or clogging mean too low. Smooth, satin and textured sheets need separate profiles. The article gives a common i3 range around -0.400 to -1.500 but says visual appearance is decisive.
   - C: MMU, MK3, MK3.5 and older i3 families; rerun after major assembly, nozzle, extruder, axis or location changes.
   - D: Do not apply one Z offset to all machines; diagnose contamination, bed leveling, temperature and under-extrusion first.

2. **LoadCell printers require a different Z workflow.**
   - A: [Live adjust Z](https://help.prusa3d.com/article/live-adjust-z_112427).
   - B: CORE One, MK4/S, MK3.9/S and XL automatically calibrate the first layer. A temporary correction can be made while printing; PrusaSlicer Z offset is per-G-code, and negative means more squish. LoadCell live correction is not saved for the next print.
   - C: LoadCell families versus persistent live-Z on PINDA/SuperPINDA/MINDA machines.
   - D: Branch diagnosis by family: inspect Z offset, sheet, LoadCell checks and filament drag for LoadCell; stored live-Z and sensor alignment for legacy machines.

3. **Adhesion should be triaged before changing flow.**
   - A: [First layer issues](https://help.prusa3d.com/article/first-layer-issues_1804?product=mk3-5).
   - B: Check clean sheet, correct seating, recommended temperatures, slower first layers and a brim before excessive squish or adhesive. A difficult material may justify a 5–10 °C bed trial; the article suggests about 75% speed for the first three layers.
   - C: MK4, XL, MK3.9, MK3.5 and MINI, with legacy and XL-specific notes.
   - D: Tuning order should be surface, seating, calibration, temperature, speed and brim before extrusion multiplier.

### Nozzles, widths and geometry

4. **A custom nozzle profile needs diameter and extrusion-width configuration.**
   - A: [Creating profiles for different nozzles](https://help.prusa3d.com/article/creating-profiles-for-different-nozzles_127540?product=mmu1).
   - B: Set nozzle diameter and HF status under Printer settings, then widths under Print settings → Advanced. Width 0 derives about 1.125 times nozzle diameter; percentage width is calculated from layer height, not nozzle diameter. General guidance is about 110% of nozzle diameter; first-layer width may be 120–140%.
   - C: PrusaSlicer profiles; MK3/S/+ nozzle-check G-code is also covered.
   - D: Compare printer and print profiles together; distinguish default, first-layer and support widths.

5. **Layer height is constrained by nozzle diameter and bonding.**
   - A: [Creating profiles for different nozzles](https://help.prusa3d.com/article/creating-profiles-for-different-nozzles_127540?product=mmu1).
   - B: Prusa recommends maximum layer height around 70–80% of nozzle diameter; higher values compromise layer adhesion.
   - C: Rule of thumb, not a universal physical law.
   - D: Warn on suspicious layer-height/nozzle pairs rather than rewriting them.

6. **Arachne is generally preferred, but Classic can help precision geometry.**
   - A: [Layers and perimeters](https://help.prusa3d.com/article/layers-and-perimeters_1748).
   - B: Detect thin walls can make one perimeter serve inside and outside, but walls thinner than one extrusion width may still disappear. External-perimeters-first can improve dimensional accuracy while slightly reducing smoothness. Arachne dynamically adjusts widths; Classic may help concave-corner accuracy.
   - C: PrusaSlicer behavior.
   - D: Map symptoms to detect thin walls, external-perimeters-first, perimeter generator and widths before blaming mechanics.

7. **Larger nozzles trade detail for throughput and can increase warping.**
   - A: [Prusa Nozzle types for Nextruder printers](https://help.prusa3d.com/article/prusa-nozzle-types-for-nextruder-printers_928993).
   - B: Diameters above 0.6 mm reduce fine detail but can make functional parts faster/stronger; more molten material can worsen ASA/PC Blend warping. Abrasive composites may require hardened nozzles.
   - C: Nextruder nozzle/material matrix.
   - D: Include nozzle material/type, diameter and material compatibility in profile identity.

### Materials, cooling and moisture

8. **Cooling is a material-specific compromise.**
   - A: [Cooling](https://help.prusa3d.com/article/cooling_127569).
   - B: Cooling solidifies ordinary layers and bridges, but can worsen warping or layer separation. Keep-fan-on is normally enabled except for ABS, ASA, PC and some flexibles. Auto cooling varies fan and speed with layer time; extremely slow printing can cause heat creep.
   - C: MK3, MK3.5, MINI, MK4, XL and MMU; per-filament settings.
   - D: Diagnose cooling, min/max fan, bridge fan, fan-below-layer-time, slowdown-below-layer-time and min print speed with material.

9. **PETG needs adhesion protection and sheet-specific handling.**
   - A: [PETG](https://help.prusa3d.com/article/petg_2059?product=mmu3).
   - B: Starting temperatures are about 230/240 °C nozzle and 85/90 °C bed, first/later. Powder-coated TXT or satin is recommended; smooth PEI can bond too strongly unless separated with glue stick. Cooling improves detail/stringing; less cooling can improve strength.
   - C: MK4, XL, MMU, MINI and MK3.
   - D: Warn before recommending smooth-PEI PETG and separate strength from surface-quality tuning.

10. **ASA/ABS-class parts need thermal management, not only hotter beds.**
    - A: [ASA](https://help.prusa3d.com/article/asa_1809); [Warping](https://help.prusa3d.com/article/warping_2011?product=enclosure).
    - B: ASA starts around 260 °C nozzle and 105/110 °C bed. High ambient/enclosure is advised for large parts; draft shield is an alternative. Warping guidance also emphasizes matching profiles, grease-free surface, moderate Z squish, cooling and brim/adhesion strategy.
    - C: ASA page lists MK4, XL, MMU, enclosure and MINI.
    - D: Treat chamber/draft shield, bed, cooling, brim and surface as one system.

11. **Moisture presents as apparent slicer defects.**
    - A: [Drying filament](https://help.prusa3d.com/article/drying-filament_332086?product=plus-1-75-mm).
    - B: Moisture can cause poor surfaces, stringing, low layer adhesion, blobs, bubbling and smoke. PA, PP, PVA/BVOH and TPU are higher-risk. XL unused tools remain heated at about 70 °C idle, so even PLA can cause multi-tool stringing when wet.
    - C: MK4, XL, MMU, PRO and MINI; XL multi-tool behavior explicit.
    - D: Check dryness before retraction, temperature or flow tuning.

12. **Drying is material/equipment-specific; dryboxes do not dry wet filament.**
    - A: [Drying filament](https://help.prusa3d.com/article/drying-filament_332086?product=plus-1-75-mm); [USS Drybox](https://help.prusa3d.com/article/prusa-uss-drybox_1014382); [Memmert UF oven](https://help.prusa3d.com/article/drying-filament-in-memmert-uf-series-universal-oven_913458).
    - B: Example values: PLA/rPLA 45 °C/6 h, PETG 55 °C/6 h, TPU 60 °C/4–6 h, ASA 80 °C/4 h, PC Blend 85 °C/5 h, PA11-CF 90 °C/6 h. Household ovens can fluctuate enough to damage low-temperature filament; transfer dried filament immediately to sealed storage.
    - C: Manufacturer/material examples, not universal values.
    - D: Keep drying guidance attached to material records and do not auto-override arbitrary profiles.

### Calibration, supports and troubleshooting

13. **Extrusion multiplier is per material/spool and not a first response.**
    - A: [Extrusion multiplier calibration](https://help.prusa3d.com/article/extrusion-multiplier-calibration_2257?product=mini).
    - B: It can vary by material, color, brand and spool. Over-extrusion causes scars/buildup; minor under-extrusion causes gaps. Typical values are 0.9–1.1, with 1.0 = 100%; visual iteration can use 1–2% changes. Precise formula is extrusion width divided by average measured wall thickness.
    - C: MK4, MINI, MK3, MK3.5 and MK3.9; examples assume 0.4 mm nozzle and 0.1–0.2 mm layers.
    - D: Keep PrusaSlicer multiplier distinct from firmware Flow/M221; eliminate clogs, moisture, wrong width and Z errors first.

14. **Supports are a geometry/material decision.**
    - A: [First print with PrusaSlicer 3.0.0](https://help.prusa3d.com/article/first-print-with-prusaslicer-3-0-0_1079761); [Paint-on supports](https://help.prusa3d.com/article/paint-on-supports_168584).
    - B: PrusaSlicer provides manual-only, automatic, everywhere and build-plate modes. Painted enforcers/blockers refine automatic support generation and are stored in 3MF. Narrower support extrusion width can make supports easier to remove.
    - C: Generic PrusaSlicer; paint-on article lists MMU, MINI, MK3 and older products.
    - D: Inspect mode, overhang threshold, painted regions, support width and interfaces before global settings.

15. **XL multi-tool jobs add bed-temperature, ooze and support constraints.**
    - A: [Combining materials (XL/+)](https://help.prusa3d.com/article/combining-materials-xl_498103).
    - B: Bed temperature can be sourced from different active extruders on first and later layers. Keep ooze prevention enabled to avoid hot-idle degradation and clogs. Organic supports, wipe towers, interface layers and tall thin snug supports have special constraints.
    - C: XL/+ multi-tool only.
    - D: Inspect per-extruder temperatures, idle temperature, ooze prevention, support style, wipe tower and dryness together.

16. **Partial clogs and wrong high-flow profiles mimic under-extrusion.**
    - A: [Clogged nozzle](https://help.prusa3d.com/article/clogged-nozzle-core-one-core-one-l-xl-mk4-s-mk3-9-s_411823?product=xl).
    - B: Check filament past the Nextruder gear and exit at the nozzle. Partial clogs appear as gaps/missing layers or filament curling onto the nozzle. High-flow nozzles require HF print profiles.
    - C: CORE One/CORE One L/XL/MK4/S/MK3.9/S Nextruder families.
    - D: Verify nozzle type/profile and hardware before changing multiplier or widths.

17. **G-code compatibility and firmware mode affect reproducibility.**
    - A: [G-code compatibility](https://help.prusa3d.com/article/the-g-code-isnt-fully-compatible-31803-core-one-26803-mk4s-27803-mk3-9s-28803-mk3-5s-13803-mk4-21803-mk3-9-23803-mk3-5-17803-xl-12803-mini_899392); [Power modes](https://help.prusa3d.com/article/power-modes_2213).
    - B: Current printers detect G-code incompatible with saved hardware settings. Firmware 6.0+ Normal/Stealth mode caps acceleration, feedrate and jerk in Stealth mode.
    - C: CORE One, MK4/S, MK3.9/S, MK3.5/S, XL and MINI.
    - D: Profile comparisons must record printer family, nozzle/HF status, firmware context and power mode.

## PROCEDURES

### Recommended diagnosis order

1. Identify printer family, nozzle diameter/type, sheet, material, PrusaSlicer version/profile and firmware/hardware mode.
2. Inspect first layer. Use First Layer Calibration/Live Z for PINDA/SuperPINDA/MINDA machines; inspect LoadCell, sheet, Z offset, filament drag and mechanics on LoadCell machines.
3. Clean and seat the sheet; check debris, grease, bends and loose filament.
4. Verify material temperatures, first-layer speed and cooling. Trial +5–10 °C bed or about 75% first-layer speed as controlled tests.
5. Check wet filament, clog/partial clog, HF profile, nozzle diameter and spool/PTFE drag.
6. Check layer height, widths, perimeters, Arachne/Classic, thin walls, external-perimeters-first, brim and supports.
7. Calibrate extrusion multiplier only after the above are stable; change one variable at a time.

### Nozzle-profile procedure

1. Import a matching built-in nozzle profile.
2. Set nozzle diameter and high-flow status under Printer → Extruder.
3. Set explicit default/perimeter/first-layer/support widths under Print → Advanced.
4. Check layer-height limit, support behavior and MK3 nozzle-check G-code.
5. Re-run first-layer calibration after nozzle or mechanical changes.

### Moisture procedure

1. If surfaces, stringing, bubbles, smoke, blobs or adhesion worsen, isolate moisture.
2. Dry according to manufacturer/Prusa guidance and actual dryer accuracy.
3. Transfer directly to sealed storage with desiccant; a drybox slows uptake but does not remove moisture.
4. Treat XL multi-tool jobs as higher risk due to heated idle tools.

### Extrusion-multiplier procedure

1. Stabilize nozzle, layer height, width, temperature, cooling and dryness.
2. Print a controlled cube/vase test.
3. Measure three wall locations and average them, or use the visual top-layer method.
4. Apply width divided by measured wall, or change visually by 1–2%; repeat.
5. Record the result per material/color/spool.

## NUMERICAL_VALUES

| Value | Meaning | Qualification |
|---|---|---|
| -0.400 to -1.500 | Common i3 Z range | Visual result overrides number |
| -1.500 to -0.200 | Typical Live Adjust Z range | Sensor-based families |
| 0.2 mm | Approximate calibration layer | Not a universal limit |
| 70–80% | Max layer height as nozzle-diameter fraction | Rule of thumb |
| 1.125 times nozzle diameter | Derived width when width is zero | PrusaSlicer derivation |
| about 110% | General width starting point | Relative to nozzle diameter |
| 120–140% | First-layer width guidance | Adhesion versus XY resolution |
| 5–10 °C | Bed-temperature trial increase | Material/sheet dependent |
| about 75% | First-three-layer speed trial | Troubleshooting guidance |
| 230/240 °C | PETG nozzle first/later | Prusa starting values |
| 85/90 °C | PETG bed first/later | Powder-coated/satin preferred |
| 260 °C | ASA nozzle | Starting value |
| 105/110 °C | ASA bed first/later | Enclosure/high ambient for large parts |
| 0.9–1.1 | Typical extrusion multiplier | Per filament/spool |
| 90–110 | Typical firmware Flow | Not stored multiplier |
| 1–2% | Visual multiplier step | Controlled iteration |
| 70 °C | XL idle-tool temperature cited | Moisture/stringing risk |
| 45 °C/6 h | PLA/rPLA drying example | Prusament table |
| 55 °C/6 h | PETG drying example | Prusament table |
| 60 °C/4–6 h | TPU drying example | Prusament table |
| 80 °C/4 h | ASA drying example | Prusament table |
| 85 °C/5 h | PC Blend drying example | Prusament table |
| 90 °C/6 h | PA11-CF drying example | Prusament table |
| ±0.02 mm | Prusament diameter variation cited | Not generic-filament guarantee |

## CONFLICTS_OR_LIMITS

- Legacy persistent live-Z guidance does not transfer directly to CORE One/MK4/XL automatic sensing.
- Percentage extrusion width is calculated from layer height, while common-width guidance is expressed against nozzle diameter; these are different bases.
- More squish can improve adhesion but block flow or damage PEI; PETG can bond too strongly to smooth PEI.
- Cooling helps bridges/overhangs but can reduce bonding or increase warping for ABS/ASA/PC/flexibles.
- Drying tables are material/spool/equipment guidance, not guarantees; household ovens can be inaccurate.
- Abrasive composites may require hardened nozzles; diameter alone is insufficient.
- XL wipe towers, organic supports and interface layers have constraints absent from generic support guidance.
- KB content is dynamic and mixes current PrusaSlicer 3.0.0/current models with legacy calibration pages; record access date and software/firmware context.
- This is a focused FDM tuning audit, not every assembly, maintenance or material subpage.

## GAPS

- No exhaustive per-material extraction for every page in the guide: PC, Nylon, PP, PVA/BVOH, Flex, CPE, PVB, HIPS, composites, PEI/PPSU/PPS.
- No full sheet-specific cleaning/preparation audit; follow each sheet/material article before automating adhesive or solvent advice.
- No full dedicated extraction of Pressure Advance/Linear Advance, bed-level correction, PID, XYZ or temperature calibration procedures.
- No empirical validation against the repo's actual user profiles or physical printers.
- No exhaustive per-model extraction for MINI, MK3.5, MK4S, CORE One L or each MMU generation.

## CITATIONS

1. [First Layer Calibration (i3)](https://help.prusa3d.com/article/first-layer-calibration-i3_112364)
2. [MINI/MINI+ calibration](https://help.prusa3d.com/article/first-layer-calibration-mini-mini_229122)
3. [Live adjust Z](https://help.prusa3d.com/article/live-adjust-z_112427)
4. [First layer issues](https://help.prusa3d.com/article/first-layer-issues_1804?product=mk3-5)
5. [Layers and perimeters](https://help.prusa3d.com/article/layers-and-perimeters_1748)
6. [Creating profiles for different nozzles](https://help.prusa3d.com/article/creating-profiles-for-different-nozzles_127540?product=mmu1)
7. [Prusa Nozzle types for Nextruder printers](https://help.prusa3d.com/article/prusa-nozzle-types-for-nextruder-printers_928993)
8. [Cooling](https://help.prusa3d.com/article/cooling_127569)
9. [Filament Material Guide](https://help.prusa3d.com/filament-material-guide)
10. [PETG](https://help.prusa3d.com/article/petg_2059?product=mmu3)
11. [ASA](https://help.prusa3d.com/article/asa_1809)
12. [Drying filament](https://help.prusa3d.com/article/drying-filament_332086?product=plus-1-75-mm)
13. [USS Drybox](https://help.prusa3d.com/article/prusa-uss-drybox_1014382)
14. [Memmert UF oven](https://help.prusa3d.com/article/drying-filament-in-memmert-uf-series-universal-oven_913458)
15. [First print with PrusaSlicer 3.0.0](https://help.prusa3d.com/article/first-print-with-prusaslicer-3-0-0_1079761)
16. [Paint-on supports](https://help.prusa3d.com/article/paint-on-supports_168584)
17. [Combining materials XL/+](https://help.prusa3d.com/article/combining-materials-xl_498103)
18. [Extrusion multiplier](https://help.prusa3d.com/article/extrusion-multiplier-calibration_2257?product=mini)
19. [Warping](https://help.prusa3d.com/article/warping_2011?product=enclosure)
20. [Clogged nozzle](https://help.prusa3d.com/article/clogged-nozzle-core-one-core-one-l-xl-mk4-s-mk3-9-s_411823?product=xl)
21. [Calibration](https://help.prusa3d.com/category/calibration_199)
22. [G-code compatibility](https://help.prusa3d.com/article/the-g-code-isnt-fully-compatible-31803-core-one-26803-mk4s-27803-mk3-9s-28803-mk3-5s-13803-mk4-21803-mk3-9-23803-mk3-5-17803-xl-12803-mini_899392)
23. [Power modes](https://help.prusa3d.com/article/power-modes_2213)

