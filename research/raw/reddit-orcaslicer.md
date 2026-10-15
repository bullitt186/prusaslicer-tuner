# r/OrcaSlicer source research: calibration, flow, pressure advance, profiles and slicer interactions

## SOURCE_METADATA

- **Source:** Reddit, [`r/OrcaSlicer`](https://www.reddit.com/r/OrcaSlicer/)
- **Research date:** 2026-10-13 (Europe/Berlin)
- **Corpus size:** 22 discussion threads selected from targeted Reddit search results and opened/search-indexed thread pages; representative, not exhaustive.
- **Selection window:** 2023–2026, with emphasis on current OrcaSlicer calibration workflows and printer/firmware interactions.
- **Method:** targeted searches for calibration order, flow ratio, pressure advance, max volumetric speed, profiles, supports, seams, retraction and firmware; retained threads with visible printer/material/software context or a concrete procedure/value.
- **Source caveat:** Reddit search exposes ranking-biased replies, partial comment trees, deleted material and sometimes only relative dates. Dates are retained as shown where exact dates were available; relative dates are not converted into fabricated exact dates.
- **Evidence notation:**
  - **C** = community evidence: user report, reply, or repeated community pattern. Useful operational evidence, not controlled testing.
  - **D** = documentation evidence: OrcaSlicer wiki/documentation linked or directly consulted to distinguish documented behavior from user inference.
  - **C/D** = community observation that aligns with, or should be read alongside, documentation.

## CORPUS_SELECTION

| ID | Thread / date | Context captured | Provenance |
|---|---|---|---|
| O01 | [Calibration Tools Order](https://www.reddit.com/r/OrcaSlicer/comments/1jq1lx6/) — 2025-04-02 | General Orca workflow; temperature, flow, PA and retraction ordering; drying and assembly caveats | User question; community replies |
| O02 | [Are we supposed to keep all parameters default when doing Calibrations?](https://www.reddit.com/r/OrcaSlicer/comments/1kj89ig/) — 2025-05-10 | Calibration dependencies; filament profile; reported max-flow result of 23 and conservative 10% reduction to 21 | User question; community replies |
| O03 | [Flow Ratio Pass 1 calibration: relative or absolute?](https://www.reddit.com/r/OrcaSlicer/comments/1s46gmz/) — 2026-03-26 | Orca 2-pass versus YOLO flow-ratio semantics; current-value-relative interpretation | User question; community replies |
| O04 | [Flow calibration broken?](https://www.reddit.com/r/OrcaSlicer/comments/1vlaz6g/) — 2026-08-11 | Orca 2.4.2; visually similar coupons and preview scale; reported volumetric values from +20 to -20 | User report; community test/reply |
| O05 | [Issues with flow rate calibration](https://www.reddit.com/r/OrcaSlicer/comments/194ufon/) — 2024-01-12 | Elegoo Neptune 4 Plus, PLA, starting flow 0.98; Pass 1/Pass 2 formula and extruder calibration | User report; community replies |
| O06 | [Flow calibration: lines in the swirl section](https://www.reddit.com/r/OrcaSlicer/comments/1voi0l1/) — 2026-08-14 | Wet-filament/over-extrusion hypotheses; first-layer dependency; proposed end-to-end order | User report; community troubleshooting |
| O07 | [best way to configurate max volumetric speed](https://www.reddit.com/r/OrcaSlicer/comments/1f87gu1/) — 2024-09-03 | Nozzle diameter/type question; 0.4/0.6/0.8 tests; filament, color and hotend limits | User question; community replies |
| O08 | [prints are very slow](https://www.reddit.com/r/OrcaSlicer/comments/1kx5o7k/) — 2025-05-28 | K1 Max / Neptune 4 Max; 50–150 mm/s despite higher speed settings; 9–10 mm³/s profile cap | User report; solved community diagnosis |
| O09 | [Speed Inconsistency](https://www.reddit.com/r/OrcaSlicer/comments/1hq2hi0/) — 2024-12-31 | 0.8 mm nozzle, Neptune 4 context; 54 mm/s at 0.4 mm layer/0.8 mm nozzle; flow-rate arithmetic | User question; community replies |
| O10 | [Strange speed issue](https://www.reddit.com/r/OrcaSlicer/comments/1jmce2l/) — 2025-03-29 | Stock Creality K1 Max, Orca 2.2.0; PLA 12 mm³/s and PETG 21 mm³/s profile limits | User report; solved by flow calibration |
| O11 | [Max Volumetric Speed Over 20, Keep Going?](https://www.reddit.com/r/OrcaSlicer/comments/1ceg65r/) — 2024-04-27 | X1C, Elegoo Rapid PETG; 5–20 mm³/s test, sheen transition, cosmetic versus failure limit, 10% margin advice | User report; community discussion |
| O12 | [Max flow rate calibration question](https://www.reddit.com/r/OrcaSlicer/comments/1vqrbgb/) — 2026-08-17 | Test interpretation; wide/high calibration lines explain lower test speed; start/end expansion procedure | User question; community procedure |
| O13 | [My Pressure Advance Tests are also not working](https://www.reddit.com/r/OrcaSlicer/comments/1amfkg1/) — 2024-02-09 | Artillery Sidewinder X2, Orca 1.9.0, Marlin; PA test ineffective because Linear Advance was not enabled | User report; community diagnosis |
| O14 | [Pressure Advance ignored?](https://www.reddit.com/r/OrcaSlicer/comments/1kq6lzi/) — 2025-05-19 | Ender 3 stock/old Marlin context; G-code flavor and firmware support; PA-looking artifacts not proof of PA | User report; community replies |
| O15 | [Adaptive Pressure Advance for Prusa Core One](https://www.reddit.com/r/OrcaSlicer/comments/1shfv5e/) — 2026-04-10 | Core One+, Marlin 2; M572, adaptive PA, concern about changing PA during print and firmware handling | User discussion; feature author/Prusa-reply claims visible in thread |
| O16 | [Print time estimate went off after increasing Pressure Advance](https://www.reddit.com/r/OrcaSlicer/comments/1rgsv3r/) — 2026-02-28 | Ender-5 Pro, Marlin 2; K 0.5→0.7, underestimated print time; extruder feedrate/acceleration hypothesis | User report and self-analysis |
| O17 | [Is there a guide for firmware retraction + Pressure Advance?](https://www.reddit.com/r/OrcaSlicer/comments/1bb4kle/) — 2024-03-10 | Klipper, firmware retraction, rotation distance, filament flow and PA; slicer versus macro use cases | Cross-posted discussion; community replies |
| O18 | [Support Setting Recommendations For This Terrain Piece](https://www.reddit.com/r/OrcaSlicer/comments/1lc7vn2/) — 2025-06-15 | Organic/tree supports, ABS, fused supports; overhang tuning, orientation and test sections | User report; community replies |
| O19 | [Missing Support Interfaces with Tree Supports - OrcaSlicer 2.0.0](https://www.reddit.com/r/OrcaSlicer/comments/1d46y4o/) — 2024-05-30 | Orca 2.0.0; tree interfaces missing; top Z distance 0, hybrid trees and 1.4 mm tip-diameter workaround | User report; multiple follow-ups |
| O20 | [Seam painting being ignored?](https://www.reddit.com/r/OrcaSlicer/comments/1df4ayx/) — 2024-06-13 | Seam blockers/enforcers, aligned seams and scarf seam; seam shown at scarf end | User report; community diagnosis |
| O21 | [What am I missing?](https://www.reddit.com/r/OrcaSlicer/comments/1lfohdi/) — 2025-06-19 | Seam painting on both sides, impossible seam constraints on columns/holes | User report; community explanation |
| O22 | [How to enable firmware retraction](https://www.reddit.com/r/OrcaSlicer/comments/173aww6/) — 2023-10-08 | Klipper; location of Orca “Use Firmware Retraction” under printer settings | User question; solved UI answer |

## COVERAGE

- **Calibration:** temperature, first-layer readiness, flow ratio (YOLO and legacy two-pass), pressure advance, retraction, max volumetric speed and calibration order.
- **Profiles:** printer/filament/process separation, material/nozzle-specific values, custom-profile persistence and the distinction between slicer settings and printer/AMS state.
- **Printers/firmware:** Creality K1/K1 Max, Neptune 4/4 Plus/4 Max, X1C, Ender 3/Ender 5 Pro, Artillery Sidewinder X2, Prusa Core One+ and generic Klipper/Marlin setups.
- **Materials:** PLA, PLA+, PETG, Rapid PETG, ABS and unspecified filaments; brand/color effects appear in the discussion but are not consistently controlled.
- **Supports/seams:** support Z gaps, interface generation, tree/hybrid supports, tip diameter, seam painting, aligned/back seams and scarf-seam interactions.
- **Firmware interactions:** Marlin Linear Advance versus Klipper Pressure Advance, G-code flavor, firmware retraction, extruder limits and possible print-time-estimate divergence.
- **Documentation baseline:** the current OrcaSlicer wiki documents calibration order, flow-ratio formulas, PA firmware prerequisites and volumetric-speed test interpretation. Reddit reports are retained as operational experience and failure cases, not silently upgraded into documentation.

## CLAIMS

### Calibration workflow and dependencies

1. **The most repeated community workflow is temperature → flow → pressure advance → retraction, with max volumetric speed either before flow or after the other material calibrations.** The Orca wiki documents temperature, flow, PA and retraction as the core order; Reddit users commonly insert max-flow before flow, while others leave it last. **[C/D; O01, O02, O06; documentation: Calibration guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration)**
2. **Calibration results are conditional on a mechanically sound printer, dry material and a good first layer.** Multiple users explicitly warn that bad first-layer quality can make flow and line-based PA tests misleading; wet filament is offered as an alternative explanation for ambiguous results. **[C/D; O01, O06, O13; documentation: PA guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/pressure_advance_calib)**
3. **There is no single universally accepted calibration order once speed and hotend limits are part of the goal.** Users disagree over whether max volumetric speed precedes flow or follows PA/retraction; the stable common point is to choose temperature first and rerun dependent tests if the operating temperature changes materially. **[C; O01, O02, O06, O11]**
4. **Orca calibration projects can change settings and should be treated as temporary test projects.** Community users recommend starting a fresh project after interpreting a test; the wiki explicitly says to create a new project to exit calibration mode. **[C/D; O02, O13; documentation: Calibration guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration)**

### Flow ratio / flow calibration

5. **Legacy Pass 1/Pass 2 flow calibration is relative to the current flow ratio, not an absolute replacement.** The documented formula is `OldFlowRatio × (100 + modifier) / 100`; community replies also distinguish this from YOLO, which applies an additive modifier to the current value. **[C/D; O03, O05; documentation: flow-ratio calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/flow_ratio_calib)**
6. **A visually weak distinction between flow-ratio coupons does not by itself prove the test is broken.** In an Orca 2.4.2 report, commenters attributed the apparent sameness to the preview scale and small modifier range; the reported generated volumetric values still varied substantially. **[C; O04]**
7. **Flow-ratio selection is a surface/geometry judgment, not simply “choose the fullest-looking block.”** Users mention smooth top surfaces, gaps between arcs, fingernail feel and dimensional/over-extrusion symptoms; a visually fuller coupon can still be over-extruded. **[C/D; O04, O05, O06; documentation: flow-ratio calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/flow_ratio_calib)**
8. **Extruder/rotation-distance calibration is treated by the community as an upstream check before filament flow calibration.** This is advice repeated in flow and retraction discussions, but it is not a measurement of how often a miscalibrated extruder is actually the cause. **[C; O05, O06, O17]**

### Max volumetric speed / profiles

9. **Max volumetric speed acts as a speed cap even when nominal process speeds are much higher.** K1/K1 Max and Neptune reports describe prints running at roughly 50–150 mm/s despite 200–550 mm/s settings because filament profiles were capped around 9–12 mm³/s; preview flow coloring is suggested for confirming the cap. **[C; O08, O09, O10]**
10. **The max-flow result is material-, machine-, nozzle- and setup-dependent; community opinion differs on whether separate nozzle profiles are necessary.** One side recommends per-nozzle profiles, while another reports only marginal differences among 0.4/0.6/0.8 mm and uses one conservative value per filament type. The documentation explicitly lists material, machine and nozzle as variables and warns that brand/color can matter. **[C/D; O07, O11; documentation: volumetric-speed calibration](https://www.orcaslicer.com/wiki/calibration/volumetric_speed_calib)**
11. **A max-volumetric-speed calibration value can be chosen at the first cosmetic transition or at outright failure, depending on the goal.** X1C/Elegoo Rapid PETG users distinguish a quality/cosmetic limit from a speed/prototype limit and discuss leaving roughly 10% margin; this is a user policy, not a universal Orca rule. **[C; O11]**
12. **The speed seen during the max-flow test is not directly the speed the same volumetric value will produce in a normal print.** Users explain that the calibration changes line width and layer height, making test speed a by-product of the target volumetric flow; Orca then derives normal-print speed from layer geometry and the cap. **[C/D; O12; documentation: volumetric-speed calibration](https://www.orcaslicer.com/wiki/calibration/volumetric_speed_calib)**
13. **Profile organization is a design choice, but the strongest recurring recommendation is to keep material-dependent calibrations in filament profiles and project/style decisions in process profiles.** A 2026 discussion describes printer, filament and process layers; replies recommend filament-specific flow, PA and max-flow values, sometimes split by nozzle size/color, while keeping process profiles closer to print-intent presets. **[C; O17]**
14. **Slicer filament profiles and printer/AMS-visible profiles are not always the same state.** In the H2D/Bambu-oriented discussion, users report that Orca custom profiles can be used by the slicer without appearing as custom entries on the printer screen; generic material slots may still be what the printer accepts. **[C; O03-adjacent profile discussion](https://www.reddit.com/r/OrcaSlicer/comments/1v7ve34/)**

### Pressure advance and firmware

15. **Orca’s PA test cannot make unsupported firmware implement PA/Linear Advance.** A Sidewinder X2 user on Orca 1.9.0 saw little test effect until commenters identified that Marlin Linear Advance was not enabled; similar Ender 3 reports distinguish stock/old Marlin from a firmware build with `LIN_ADVANCE`. **[C; O13, O14]**
16. **Marlin and Klipper use related but not identical mechanisms and naming.** Community replies call Marlin’s implementation Linear Advance and Klipper’s Pressure Advance; the Orca documentation states that Marlin requires Linear Advance/M900 to be enabled. **[C/D; O13, O14; documentation: PA calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/pressure_advance_calib)**
17. **G-code flavor and firmware capability matter when using PA values generated by Orca.** A Core One+ discussion cites `M572` and Marlin 2 flavor, while the feature author cautions that adaptive PA changing values during a print may behave differently on Marlin than Klipper. The thread does not establish a universal compatibility guarantee. **[C; O15]**
18. **Higher Marlin Linear Advance K can affect actual print time through extruder motion limits even when the slicer estimate does not model it.** An Ender-5 Pro user reports K 0.5→0.7 increasing a 2h40 estimate to about 3h20 and hypothesizes extruder feedrate/acceleration caps; this is a plausible single-printer diagnosis, not a general Orca timing rule. **[C; O16]**
19. **Adaptive PA is especially relevant to high-speed/high-flow use, but the Reddit evidence is exploratory.** The Orca documentation describes PA varying with volumetric flow and acceleration; the Reddit feature discussion reports uncertainty about Marlin stutter/artifacts and no confirmed result on the Core One+. **[C/D; O12, O15; documentation: adaptive PA](https://github.com/OrcaSlicer/OrcaSlicer/wiki/adaptive_pressure_advance_calib)**

### Retraction and firmware retraction

20. **Firmware retraction is a printer-setting switch in Orca, not merely a filament retraction-length value.** The Klipper UI question was resolved by enabling “Use Firmware Retraction” under Printer Settings → Basic Information → Advanced. **[C; O22]**
21. **Community users distinguish slicer-managed retraction from firmware retraction/macros.** One Klipper discussion argues that modern slicers’ wipe/ramp behavior can make firmware retraction less useful for ordinary travel moves, while firmware/macros remain useful for pause, park and material-change operations. This is opinionated workflow guidance, not a firmware requirement. **[C; O17]**
22. **Retraction should be tuned after temperature/flow/PA in the common workflow, and excessive stringing can be a material-moisture or temperature problem rather than only a distance problem.** The corpus supports testing retraction after upstream extrusion conditions are stable, but contains no controlled value range shared across printers. **[C; O01, O06, O17]**

### Supports and seams

23. **Support removal problems are often downstream of stringing, over-extrusion, temperature and support/object separation.** A Cura-to-Orca user was advised to fix upstream calibration first, then increase top Z/interface separation at the cost of contact-surface quality. **[C; O18]**
24. **Tree-support interface generation has produced version/settings-specific reports rather than one reliable fix.** Orca 2.0.0 users report missing interfaces; replies describe top Z distance 0, hybrid trees, and later a 1.4 mm tip-diameter workaround. These values are thread-specific and can be unsuitable for dissimilar support materials. **[C; O19]**
25. **Support interface geometry depends on available space and the support-generation mode.** The 1.4 mm tip report is explained as creating enough room for the interface pattern; other replies note that zero Z spacing may be acceptable for PLA/PETG separation but can fuse same-material supports. **[C; O19]**
26. **Seam painting is a constraint system, not an absolute command to place a seam anywhere.** Users explain that Orca must place a seam somewhere on closed/segmented geometry; if blockers make the requested placement impossible, the slicer may choose another location. Painting enforced regions can be more reliable than attempting to block nearly the whole surface. **[C; O20, O21]**
27. **Scarf seams can make the visible artifact appear away from the painted seam start.** In one report, a reply attributes the visible mark to the end of the scarf rather than the beginning; another user later reports that disabling scarf seam resolved a blocker complaint. **[C; O20]**

## PROCEDURES

1. **Baseline before calibration:** record printer model, nozzle diameter/type, firmware, Orca version, material brand/color, drying state and active printer/filament/process profiles. Confirm extruder steps/rotation distance and first-layer/bed behavior. **[C/D; O01, O02, O06, O17]**
2. **Practical filament workflow:** dry material and stabilize the printer; choose a temperature from a temperature tower; run flow-ratio calibration; save the result to the filament profile; rerun a quick first-layer/surface check; then tune PA, retraction and max volumetric speed as needed. If the target use is high speed, run max-flow early enough to establish a realistic speed ceiling, but rerun dependent tests after major temperature changes. **[C/D; O01, O02, O06, O11; Orca Calibration guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration)**
3. **Flow ratio:** for legacy Pass 1/2, apply the documented multiplicative formula to the current value and start the second pass from a fresh calibration project. For YOLO, treat the modifier as relative to the current flow ratio; judge smoothness, gaps and dimensions together. **[C/D; O03, O05; flow-ratio guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/flow_ratio_calib)**
4. **Max volumetric speed:** begin with the documented 5→20 mm³/s range and 0.5 step unless the filament is known to be outside it; stop at a quality transition for cosmetic parts or at failure for a speed-focused profile, then apply a deliberate margin. Validate the resulting filament cap in Preview → Flow. **[C/D; O08, O11, O12; volumetric-speed guide](https://www.orcaslicer.com/wiki/calibration/volumetric_speed_calib)**
5. **Pressure advance:** verify firmware support first. For Marlin, confirm Linear Advance is compiled/enabled and the selected G-code flavor emits the expected command; for Klipper, ensure the PA setting is actually accepted by the printer. Use the direct-drive/Bowden test variant that matches the hardware and save the result in the material profile. **[C/D; O13, O14; PA guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/pressure_advance_calib)**
6. **Firmware retraction:** decide whether ordinary travel retractions are slicer-managed or firmware-managed; if using firmware retraction with Klipper, enable the printer setting and avoid assuming slicer distance values are active in the same way. Keep pause/material-change macros separate from ordinary travel tuning. **[C; O17, O22]**
7. **Supports:** first eliminate obvious stringing/over-extrusion/temperature issues; then adjust top Z/interface spacing and support-interface speed in small test sections. For missing tree interfaces, test generation mode, available tip diameter and interface spacing before changing a whole profile. **[C; O18, O19]**
8. **Seams:** inspect the actual layer geometry from both sides, paint enforced seams where possible, and do not block every candidate region on geometry that requires a seam. If scarf seam is enabled, inspect both its start and visible end before concluding that seam painting is ignored. **[C; O20, O21]**

## NUMERICAL_VALUES

Numbers below preserve source context; they are not universal recommendations.

| Value | Context | Evidence |
|---|---|---|
| 0.98 | Neptune 4 Plus PLA starting flow ratio in a legacy Pass 1/2 discussion | C, O05 |
| 0.931 | Result of applying a -5% modifier to 0.98 in that same discussion | C, O05 |
| 0.95–1.05 | Orca wiki recommended flow-ratio range | D, [material settings](https://github.com/OrcaSlicer/OrcaSlicer/wiki/material_flow_ratio_and_pressure_advance) |
| -0.05 to +0.05, step 0.01 | Orca wiki recommended YOLO range/step | D, [flow-ratio guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/flow_ratio_calib) |
| 0.005 step | Orca wiki “perfectionist” YOLO step | D, [flow-ratio guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/flow_ratio_calib) |
| 5→20 mm³/s, step 0.5 | Default max-volumetric-speed test range documented by Orca | D, [volumetric-speed guide](https://www.orcaslicer.com/wiki/calibration/volumetric_speed_calib) |
| ~9–12 mm³/s | Profile caps blamed for slow K1/K1 Max prints; 12 for PLA in one K1 Max profile | C, O08, O10 |
| 21 mm³/s | Elegoo Rapid PETG/X1C user’s stated hotend/profile figure and conservative post-test value in another thread | C, O02, O11 |
| 23 mm³/s → 21 mm³/s | Revo high-flow 0.4 mm / 60 W anecdote; user applied ~10% margin | C, O02 |
| 0.4/0.6/0.8 mm | Nozzle sizes compared in max-flow discussion; users disagree on whether separate max-flow profiles are needed | C, O07 |
| 0.02 | Default PA value mentioned in Sidewinder X2 test report | C, O13 |
| 0.5 → 0.7 | Marlin K change associated with longer actual print time on Ender-5 Pro | C, O16 |
| 0.20 mm | Top support Z distance in Orca 2.0.0 missing-interface report | C, O19 |
| 0 / 0.25–0.28 mm | Reported top-Z experiments for support-interface generation and ABS overhang finish | C, O18, O19 |
| 1.4 mm | Reported tree-support tip diameter that restored interface generation for one user | C, O19 |
| 250–550 mm/s | Nominal process-speed settings in slow-print reports; actual speed was limited by flow/acceleration | C, O08, O10 |

## CONFLICTS_OR_LIMITS

- **Calibration order is not fully settled.** Orca documentation provides a baseline order, but Reddit users disagree about where max volumetric speed belongs and whether PA precedes or follows flow for their use case.
- **Max-flow profile granularity conflicts.** Some users recommend separate values for nozzle diameter/type; others find the differences small and use one conservative value per filament. The correct choice depends on hotend, nozzle, geometry and desired quality.
- **Flow-ratio interpretation is easy to confuse.** Legacy two-pass multiplication, YOLO additive modifiers and final filament values are discussed together; applying a correct formula to the wrong calibration mode can produce a bad profile.
- **PA terminology is firmware-dependent.** Reddit replies sometimes call all advance behavior “pressure advance,” while Marlin users may mean Linear Advance. Orca’s UI can expose a setting even when the printer firmware cannot act on it.
- **Adaptive PA evidence is immature for Marlin.** The wiki documents the feature, but the Core One+ thread explicitly leaves questions about artifacts, stutter and firmware handling unresolved.
- **Support Z-gap advice is material-dependent.** Zero spacing may help a same-material interface generate, but can fuse supports; dissimilar PLA/PETG support interfaces change the trade-off.
- **Seam painting cannot override topology.** A painted blocker is not proof that the slicer is malfunctioning when geometry leaves no valid seam-free path.
- **Reddit success reports are not controlled experiments.** The corpus contains no systematic incidence rates, complete 3MF files, measured nozzle wear, humidity measurements or matched before/after tests for most claims.

## GAPS

- Little direct evidence on Orca retraction numeric ranges across direct-drive versus Bowden printers; most threads explain workflow or firmware toggles rather than report controlled towers.
- Sparse complete profiles showing all linked values for temperature, flow ratio, PA, max volumetric speed, cooling and retraction together.
- Limited coverage of PrusaSlicer-compatible Marlin printers compared with Bambu/Klipper/Creality ecosystems.
- Few high-quality comparisons of nozzle material (brass, hardened, high-flow) with the same filament and temperature.
- Support evidence is concentrated on tree-interface generation and removal; less on dense support, bridge flow, organic-support branch parameters or soluble materials.
- Seam evidence is mostly visual troubleshooting; there is little version-controlled reproduction data for seam painting/scarf-seam behavior.
- Reddit’s 2026 threads and the current wiki may change; re-check release-specific behavior before turning any value into a stable profile default.

## CITATIONS

Primary Reddit permalinks are preserved in `CORPUS_SELECTION` and are the evidence base for community claims. Documentation used to distinguish documented behavior from user reports:

- [OrcaSlicer Calibration guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration) — documented baseline order and calibration-project behavior.
- [Flow Ratio Calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/flow_ratio_calib) — YOLO and legacy two-pass methods/formulas.
- [Pressure Advance calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/pressure_advance_calib) — direct/Bowden variants and Marlin Linear Advance prerequisite.
- [Material Flow Ratio and Pressure Advance](https://github.com/OrcaSlicer/OrcaSlicer/wiki/material_flow_ratio_and_pressure_advance) — profile fields and adaptive-PA semantics.
- [Adaptive Pressure Advance](https://github.com/OrcaSlicer/OrcaSlicer/wiki/adaptive_pressure_advance_calib) — documented flow/acceleration model and experimental limits.
- [Max Volumetric Speed calibration](https://www.orcaslicer.com/wiki/calibration/volumetric_speed_calib) — default test range and material/machine/nozzle dependence.

