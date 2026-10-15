# r/FixMyPrint diagnostic source research

## SOURCE_METADATA

- **Source:** [Reddit r/FixMyPrint](https://www.reddit.com/r/FixMyPrint/)
- **Research date:** 2026-10-13 (Europe/Berlin)
- **Method:** targeted web search plus direct Reddit page reads where available; selected threads for diagnostic value rather than popularity alone.
- **Corpus size:** 30 discussion threads. This is a representative sample, not an exhaustive history of the subreddit.
- **Evidence labels:**
  - **C — corroborated pattern:** appears in multiple independent threads and/or includes a clear user-reported improvement after the test/fix.
  - **D — discussion-level evidence:** a plausible reply, an unresolved thread, a one-off result, or a recommendation whose success is not demonstrated in the thread.
- **Interpretive rule:** a Reddit diagnosis is preserved as conditional. Printer kinematics, hotend/extruder design, slicer, material, nozzle, enclosure and ambient conditions can change the result.
- **Copyright:** all observations below are paraphrased; no substantial Reddit text is reproduced.

## CORPUS_SELECTION

The sample spans the requested symptom families and intentionally mixes Ender/Creality, Prusa, Anycubic, Bambu, RatRig/CoreXY and other machines; Bowden and direct-drive setups; PLA/PLA+/silk PLA/PETG/ABS/ASA contexts; and both solved and unresolved cases.

| ID | Symptom focus | Thread/date | Context retained |
|---|---|---|---|
| S1 | Stringing | [Stringing on my prints](https://www.reddit.com/r/FixMyPrint/comments/1rcq0uh/stringing_on_my_prints/) — 2026-02-23 | Ender 3 V2 Neo, OrcaSlicer, SUNLU PLA+ 2.0, 0.4 mm, 195/55 °C, Bowden-style 8 mm retraction; later drying outcome was still being tested. |
| S2 | Stringing | [Stringing no matter the changes](https://www.reddit.com/r/FixMyPrint/comments/1w78ur1/stringing_no_matter_the_changes/) — 2026-09-04 | Ender 3 V2, Sprite SE/direct-drive conversion, Klipper/Orca, Sunlu PLA+ 2.0, 220/55 °C; 12 h drying reportedly solved it. |
| S3 | Stringing | [Stringing increased with drying](https://www.reddit.com/r/FixMyPrint/comments/17z2kk2/stringing_increased_with_drying/) — 2023-11-19 | PLA+, 210/65 °C; 4 h at about 54 °C seemed worse; later retraction and temperature tests reduced stringing. |
| S4 | Stringing | [Still stringing after drying filament and tweaking retraction](https://www.reddit.com/r/FixMyPrint/comments/ycaowh/still_stringing_after_drying_filament_and_tweaking_retraction_settings/) — 2022-11-08 | Ender 3, Bondtech dual-gear, Bowden tube, PLA, PrusaSlicer; unresolved/iterative tuning. |
| E1 | Under-extrusion | [How do I fix this underextrusion?](https://www.reddit.com/r/FixMyPrint/comments/14ioasi/how_do_i_fix_this_underextrusion/) — 2023-06-25 | E-steps already calculated; first layers good, later layers open; replies discuss flow, layer height, nozzle width and first-layer squish. |
| E2 | Under-extrusion after hardware change | [Under extrusion after upgrading to aluminum extruder](https://www.reddit.com/r/FixMyPrint/comments/hysyn9/under_extrusion_after_upgrading_to_aluminum_extruder/) — 2020-07-27 | Extruder replacement changed the drive geometry; e-step recalibration restored correct baseline and made the prior 1.05 multiplier excessive. |
| E3 | Under-extrusion/flow | [Under extrusion?](https://www.reddit.com/r/FixMyPrint/comments/pshjmr/under_extrusion/) — 2021-09-21 | Anycubic Chiron, Simplify3D, PLA, 200/60 °C, 5 mm retraction; improved after probe re-leveling and higher extrusion multiplier, with e-step calibration still advised. |
| E4 | Over-extrusion | [Over extrusion?](https://www.reddit.com/r/FixMyPrint/comments/uyal3r/over_extrusion/) — 2022-05-26 | Top/first-layer overfill; discussion separates e-step calibration from slicer extrusion multiplier and Z height. |
| E5 | E-step/flow conflict | [E-step calibration says I’m under extruding but print don’t show that](https://www.reddit.com/r/FixMyPrint/comments/ur5plq/estep_calibration_says_im_under_extruding_but_print_dont_show_that_should_i_still_fix_the_value/) — 2022-05-16 | CR-10S; cold, unloaded 100 mm test initially differed from in-system test; flow compensation may have hidden the mechanical error. |
| E6 | Extrusion/partial clog | [Over or Under Extrusion?](https://www.reddit.com/r/FixMyPrint/comments/18c4v1l/over_or_under_extrusion/) — 2023-12-08 | Brim looked acceptable while upper layers under-extruded; reported e-step error caused nozzle back-pressure and a filament mess. |
| W1 | Warping | [Print keeps warping off the bed](https://www.reddit.com/r/FixMyPrint/comments/1m20yn/print_keeps_warping_of_the_bed/) — 2025-07-17 | PLA; first layer initially good, corners lifted later; suggestions include soap cleaning, uniform bed heat soak, mouse ears/brim and adhesive. |
| W2 | Warping/adhesion | [Brim prints perfectly and first layer of actual model warps](https://www.reddit.com/r/FixMyPrint/comments/yo853i/brim_prints_perfectly_and_first_layer_of_actual_model_warps/) — 2022-11-07 | Brim versus part geometry; cleaning, adhesive and first-layer/flow differences considered. |
| A1 | First-layer adhesion | [First layer lifting right behind extruder](https://www.reddit.com/r/FixMyPrint/comments/1eg8dzc/first_layer_lifiting_right_behind_extruder/) — 2024-07-31 | Cleaning, Z-offset and first-layer fan/bed temperature were debated; later update reported improvement after cleaning, re-leveling, +bed heat and low first-layer fan. |
| A2 | Bed adhesion | [Brim not sticking to build plate](https://www.reddit.com/r/FixMyPrint/comments/10do8qc/brim_not_sticking_to_build_plate/) — 2023-02-07 | Advice converges on too-high nozzle/Z offset or contaminated surface; dish-soap cleaning was reported as a major improvement. |
| A3 | Bed/mesh/adhesion | [Help](https://www.reddit.com/r/FixMyPrint/comments/1jkhji8/help/) — 2025-04-08 | Uneven bed; suggestions include hot-water/dish-soap cleaning, Z offset, brim contact, temperature and lower initial cooling. |
| R1 | Ringing/ghosting | [Worst ringing/ghosting known to man](https://www.reddit.com/r/FixMyPrint/comments/1cl36o5/worst_ringingghosting_known_to_man/) — 2024-05-05 | Input shaping, pressure advance and speed/acceleration already tried; frame squareness and over-tight belts proposed as alternative causes. |
| R2 | Directional ringing | [How to fix the y-Vibration ghosting on a CR-10S?](https://www.reddit.com/r/FixMyPrint/comments/13omwdy/how_to_fix_the_yvibration_ghosting_on_a_cr10s/) — 2023-05-18 | CR-10S, PLA 215/60 °C, 60 mm/s; directional asymmetry prompts belt/idler inspection and input-shaping/acceleration tests. |
| R3 | Ringing | [Severe ghosting/ringing down the entire vertical print](https://www.reddit.com/r/FixMyPrint/comments/1krncqt/severe_ghostingringing_down_the_entire_vertical_print/) — 2025-04-24 | Input shaping unavailable/insufficient; lower acceleration, jerk and print speed suggested. |
| L1 | Layer shift | [Massive layer shift on Ender3](https://www.reddit.com/r/FixMyPrint/comments/130ebpy/massive_layer_shift_on_ender3/) — 2023-05-03 | Belt tension was not the whole story; wheels let the head bind and an 80 mm fan was reported to resolve a related failure. |
| L2 | Layer shift | [Why would it shift itself like that mid-print?](https://www.reddit.com/r/FixMyPrint/comments/1srgk6f/why_would_it_shift_itself_like_that_midprint/) — 2026-04-21 | Shift associated with belt/motor tooth skip, collision or lost steps; one filament produced failures while PLA did not. |
| O1 | Overheating/heat creep | [Heat creep or something else?](https://www.reddit.com/r/FixMyPrint/comments/1fposh9/heat_creep_or_something_else/) — 2024-09-26 | Ender 3 Pro, Spider all-metal hotend, Bowden, Duramic PLA+, 210–230 °C, 65 mm/s; hotend cooling and PLA sensitivity in all-metal setups discussed. |
| O2 | Heat creep/clog | [I keep getting clogs/heat creep then underextrusion](https://www.reddit.com/r/FixMyPrint/comments/u6v8w6/i_keep_getting_clogsheat_creep_then_underextrusion/) — 2022-04-19 | Recurrent clog after ~15 minutes on PLA; hotend fan failure was identified and replacing it reportedly fixed the issue. |
| O3 | Thermal/cooling failure | [I get cloggings everytime I try to print something longer than 1h](https://www.reddit.com/r/FixMyPrint/comments/v21iec/i_get_cloggings_everytime_i_try_to_print_something_longer_than_1h/) — 2022-06-09 | Long-print-only clog; distinction between hotend fan and part-cooling fan mattered; changing the fan solved the clog according to the update. |
| O4 | Small-layer overheating | [Top layers curling up](https://www.reddit.com/r/FixMyPrint/comments/1jawk5/top_layers_curling_up/) — 2025-03-13 | Creality Hyper PLA, 200/60 °C, full fan, 0.20 mm; minimum layer time, slower printing and improved ducting debated. |
| B1 | Bridges | [How can I improve bridge test results?](https://www.reddit.com/r/FixMyPrint/comments/1e56id8/how_can_i_improve_bridge_test_results/) — 2024-07-10 | Neptune 4 Plus with a new fan shroud; bridge test still sagged; speed, flow and cooling were the main variables. |
| B2 | Bridges/overhangs | [Stringing / Oozing — particularly bad on overhangs and bridges](https://www.reddit.com/r/FixMyPrint/comments/16i5itn/stringing_oozing_particularly_bad_on_overhangs_and_bridges/) — 2023-09-14 | Bridge/overhang geometry, supports, bridge speed/flow and thick-bridge settings; other features printed acceptably. |
| B3 | Bridges/overhangs | [Help with settings to mitigate stringing on over hang](https://www.reddit.com/r/FixMyPrint/comments/1riudz4/help_with_settings_to_mitigate_stringing_on_over/) — 2026-03-02 | PETG, 0.6 mm nozzle/0.3 mm line width; overhang-specific cooling/speed, wider lines, thinner layers and wall ordering discussed. |
| P1 | Supports | [Layer above support looks really rough](https://www.reddit.com/r/FixMyPrint/comments/1rkq5kj/layer_above_support_looks_really_rough/) — 2026-03-04 | Windstorm S1/Orca, 0.2 mm layers, top Z 0.26/bottom Z 0.2, two interface layers; top-Z gap and interface density were central. |
| P2 | Supports | [Stringing under supports](https://www.reddit.com/r/FixMyPrint/comments/1rjtakp/stringing_under_supports/) — 2026-03-03 | Bulbasaur-like overhang; surface quality under supports; interface layers/density, orientation and separate support material proposed. |
| P3 | Supports | [How to add supports to this?](https://www.reddit.com/r/FixMyPrint/comments/xmrw6p/how_to_add_supports_to_this/) — 2022-09-24 | Prusa Mini/PrusaSlicer; removable support strategy, orientation, bridge-first geometry and brim stability. |
| P4 | Automatic/tree supports | [Overhang support settings](https://www.reddit.com/r/FixMyPrint/comments/1uh3cic/overhang_support_settings/) — 2026-06-27 | A1 Mini, PolyTerra PLA, 0.2 mm; slicer did not support a small triangular region; painted/manual support and thin-wall/Arachne issues. |

## COVERAGE

| Requested family | Threads | Main variables represented |
|---|---:|---|
| Stringing | 4 | moisture, temperature, retraction, Z-hop, travel path, Bowden/direct-drive context |
| Under-/over-extrusion | 6 | e-steps, extrusion multiplier/flow, first-layer geometry, nozzle width/layer height, partial clogs |
| Warping | 2 | cooling/thermal contraction, bed cleanliness, heat soak, brim/mouse ears, material/geometry |
| Adhesion | 3 | Z offset/leveling/mesh, plate cleaning, first-layer fan/temperature, brim/adhesive |
| Ringing | 3 | belts, frame, idlers, acceleration/speed, input shaping, directional mechanics |
| Layer shifts | 2 | collisions, belt/motor skip, binding, lost steps, material-dependent curling |
| Overheating/heat creep | 4 | hotend fan, heat-break cooling, enclosed/ambient heat, minimum layer time, small cross-sections |
| Supports/bridges | 8 | support placement, top-Z gap, interface, bridge speed/flow/cooling, overhang geometry, orientation |

The corpus is strongest for common FDM troubleshooting heuristics and weakest for controlled experiments, exact printer firmware state, measured temperatures, and negative results that were fully documented. Most posts are image-led and omit complete machine configuration.

## CLAIMS

### Stringing

1. **Symptom → likely causes:** fine webs between separated features are repeatedly associated with wet filament, excessive nozzle temperature, poorly tuned retraction, and sometimes travel/Z-hop or a mechanical leak. **[C]** S1–S4 collectively support this, but no single cause explains every case.
2. **Test:** keep printer and geometry fixed; run a temperature tower and a retraction tower after verifying the filament is genuinely dry. For Bowden systems, test a longer retraction range than for direct drive; do not transfer the numeric range blindly. **[C/D]** S1 records 8 mm/60 mm/s on an Ender Bowden, while S2’s Sprite conversion prompted advice in the sub-1 mm range; S3 reported improvement around 1–1.5 mm at 210–205 °C. These are setup-specific, not defaults.
3. **Fix:** drying can be decisive, including for a new or vacuum-packed spool, but a short warm-bed session may be insufficient. **[C]** S2 reports that roughly 12 hours resolved severe stringing; S1’s one-hour/short drying attempt did not. S3 is a useful counterexample: the user initially reported worse results after four hours, and the thread remained inconclusive about moisture versus settings.
4. **Limit:** lowering temperature may reduce ooze but can reduce layer adhesion; increasing retraction can introduce heat-break loading or clog risk, especially on an all-metal hotend. **[D]** This is advice in S2/S3 and should be tested against material and hotend design.
5. **Test for non-material causes:** inspect nozzle/hotend alignment and leaks, compare travel paths, and temporarily disable Z-hop. **[D]** S1 includes Z-hop and “avoid crossing perimeters” as alternate hypotheses; S2 includes perpendicularity and a direct-drive/Bowden mismatch. Neither is a controlled confirmation.

### Under-extrusion, over-extrusion and flow

1. **Order matters:** establish the mechanical extrusion distance/e-step or rotation-distance baseline after hardware changes, then tune filament-specific flow/extrusion multiplier. **[C]** E2 reports that replacing the extruder changed the correct calibration; E4/E5 repeat the distinction; E5 shows how a slicer multiplier can mask a wrong mechanical value.
2. **Test:** for an e-step check, disconnect the hotend/nozzle or otherwise measure unloaded filament motion, mark a known length, command a measured extrusion, and repeat. Then run a flow/extrusion-multiplier test with the real nozzle/material/layer height. **[C/D]** E5 specifically improved the diagnosis after repeating the test with the Bowden disconnected; E1/E3 recommend flow calibration after the baseline. Reddit replies do not establish one universal test protocol.
3. **Symptom qualification:** first layers can look good while later layers under-extrude because first-layer width/flow/squish, layer height, line width or a slicer setting can hide the volumetric error. **[C]** E1 and E3 show this pattern; E6 adds partial-clog/back-pressure as a competing explanation.
4. **Cause separation:** if a change to e-steps, nozzle, extruder, filament path or hotend precedes the defect, suspect the changed hardware before using a large flow multiplier. **[C]** E2 and E6 support this; large multipliers are repeatedly characterized as a possible band-aid.
5. **Over-extrusion test:** inspect a single-wall/flow calibration result and the top surface at a controlled Z height; if only the first layer is overfilled, adjust first-layer Z/flow rather than reducing global flow immediately. **[D]** E4 includes the competing diagnoses of excessive flow and nozzle too close to the bed.
6. **Material context:** flow is not necessarily constant across brands, additives, colors or layer heights. **[C/D]** E1/E3 discuss PETG versus silk PLA and layer-height dependence; the thread evidence is experiential rather than metrologically controlled.

### Warping and bed adhesion

1. **Symptom → cause:** corner lift after an apparently successful first layer can be a thermal-contraction/airflow problem rather than simple initial adhesion failure. **[C]** W1, W2 and A1 distinguish “the first layer looked good” from later corner lift.
2. **Test:** clean the plate with a compatible detergent/water method, re-level or re-probe, verify Z offset with a first-layer pattern, and repeat the same geometry with the same material. If only large corners fail, add a brim or mouse ears and compare. **[C]** W1/W2/A1/A2 repeatedly use these discriminating tests; A1 reports improvement after cleaning, re-leveling and a small Z-offset correction.
3. **Fix:** reduce first-layer cooling, use an appropriate bed/first-layer temperature, preheat long enough for a large bed to equalize, and use a brim/mouse ears or approved adhesive when geometry/material requires it. **[C/D]** W1, A1 and A3 support the combination; exact temperatures vary and one reply’s “guaranteed” multi-setting recipe should not be treated as evidence.
4. **Limit:** increasing bed temperature can help adhesion but can also soften/warp PLA lower layers; high temperature is not a universal fix. **[D]** W1 and the older adhesion discussion in A1/W2 expose this trade-off.

### Ringing/ghosting and layer shifts

1. **Ringing diagnosis:** repeated echoes after sharp corners are not automatically an input-shaping problem. Loose hardware, an over-tight belt, idler/bearing problems, a non-square frame, high acceleration, or directional bed motion can produce similar artifacts. **[C]** R1–R3 and L1 support a mechanical-first differential.
2. **Test:** print the same ringing test in X and Y, inspect belt/idler travel, check frame squareness and fasteners, then lower acceleration/speed before or alongside input-shaper tuning. Change one variable at a time. **[C/D]** R1/R2 explicitly recommend frame/belt checks and controlled changes; R3 reports lower motion parameters as the fallback when shaping is unavailable.
3. **Layer shift:** a sudden, persistent XY offset is consistent with a skipped belt tooth, a motor losing steps, a collision, or binding—not with ordinary “poor layer adhesion.” **[C]** L1/L2. Inspect for a curled/warped part hitting the nozzle, excessive friction, loose pulley grub screws, belt tension, and motor/driver overload.
4. **Test:** reproduce at lower acceleration/speed and with a less warp-prone filament; observe whether the head collides at the layer where the shift begins. **[D]** L2 reports that one filament failed while PLA did not, but does not isolate whether the filament caused curling, drag, or another load.

### Overheating, cooling and heat creep

1. **Time-dependent under-extrusion/clogging**—clean at the beginning, then failing after 15 minutes or only on long prints—is a strong heat-creep/hotend-cooling hypothesis, especially with PLA and an all-metal heat break. **[C]** O1–O3 show the repeated time-dependent pattern.
2. **Test:** verify the hotend fan is the correct fan, runs continuously at full intended speed, blows in the correct direction, and has an unobstructed heatsink; distinguish it from the controllable part-cooling fan. Try a known-good filament and slower/lower-load print. **[C]** O1–O3 use these checks; O2/O3 report a fan replacement resolving the issue.
3. **Fix:** restore heat-break airflow, clean the heatsink, correct ducting, reduce hotend temperature/retraction/load when appropriate, and be cautious when moving PLA from PTFE-lined to all-metal hotends. **[C/D]** O1/O2; the exact fix depends on hotend geometry and ambient/enclosure temperature.
4. **Small-feature overheating:** curled tips and deformed small layers can be insufficient part cooling or insufficient time per layer. **[C]** O4. Use minimum layer time/slowdown, stronger directed part cooling, lower temperature where adhesion permits, or print multiple parts; do not infer a hotend-fan failure from a top-layer curl alone.

### Supports and bridges

1. **Support underside roughness:** a large gap between the support interface and the part can make the support functionally ineffective; roughness is not necessarily stringing. **[C]** P1 reports 0.26 mm top Z at 0.2 mm layers, and replies repeatedly identify top-Z distance/interface as the primary test.
2. **Test:** print only a 10–20 minute section; vary top-Z distance, interface layers/density/pattern, support angle/placement and material one variable at a time. **[C/D]** P1/P2/P4. Smaller gaps often improve the underside but increase scarring or make removal harder, and the viable value is material/printer-dependent.
3. **Overhang versus bridge:** a curved or unsupported overhang is not automatically a bridge. A bridge needs useful anchors and a span geometry; supports or a CAD reorientation may be the correct intervention. **[C]** B2/B3/P3/P4 distinguish these cases.
4. **Bridge test:** adjust bridge speed, bridge flow, line width/thick-bridge behavior and bridge cooling separately from ordinary perimeter settings. Slower speed and strong cooling are common hypotheses; too much or too little flow can both create gaps/sag. **[C/D]** B1–B3; B1 is unresolved, so the values are test suggestions rather than a confirmed recipe.
5. **Geometry often dominates:** rotate the part, shorten the span, add a chamfer/tear-away sacrificial bridge, orient walls/infill to shorten the bridge, or paint/manual-place support where automatic tree supports miss a small region. **[C/D]** P3/P4 and B2. This is often more robust than endlessly increasing support density.
6. **Material interface:** PETG-on-PLA or dedicated support material may improve release, but the result depends on the pair, temperature and printer. **[D]** P2 reports the suggestion without a controlled outcome in the sampled thread.

## PROCEDURES

The following procedures are distilled from the corpus as safe diagnostic sequences. They are not claims that every Reddit reply is correct.

### General isolation loop

1. Record printer kinematics (bed-slinger/CoreXY/delta), hotend (PTFE-lined/all-metal), extruder (Bowden/direct), nozzle diameter, material/brand/color, nozzle/bed temperature, layer height, speed/acceleration, fan behavior, retraction, slicer and firmware.
2. Photograph the whole part and a close-up; note the exact layer/feature where the defect starts.
3. Reproduce with a small test object or cut-down section so one iteration is short.
4. Change one causal variable at a time; retain the original profile and label each test.
5. Confirm any improvement on the original geometry before recording a fix as stable.

### Extrusion baseline

1. Inspect for a nozzle leak, worn nozzle, loose Bowden fitting, flattened filament, extruder idler/gear slip and partial clog.
2. Calibrate e-steps/rotation distance with the hotend unloaded or with a measurement method that accounts for the melt path; save the mechanical value.
3. Run a material-specific flow/extrusion-multiplier test at the intended nozzle, layer height and temperature.
4. If under-extrusion appears only after time or during high-flow regions, test heat creep, maximum volumetric flow and clogging before increasing flow.

### Stringing

1. Dry the actual spool with a controlled temperature/time method suitable for the polymer; a brief heated-bed session is weak evidence of dryness.
2. Run a temperature tower for layer adhesion first, then a retraction tower appropriate to Bowden/direct drive.
3. Check hotend leaks, nozzle cleanliness, travel speed/path, Z-hop and “avoid crossing perimeters” only after the baseline is sound.
4. Re-test on the same spool and a known-good spool; a material-specific result should not be generalized to all PLA/PETG.

### Adhesion and warping

1. Degrease the build plate with the manufacturer-compatible method; avoid assuming IPA removes all residues.
2. Verify mechanical level/mesh and Z offset with a first-layer pattern; distinguish “too high” from “too low/squished.”
3. Compare first-layer fan off/reduced versus normal cooling, and adjust bed/first-layer temperature in small increments.
4. For large flat PLA/PETG/ABS/ASA geometry, compare a brim, mouse ears, draft protection/enclosure and longer bed heat soak.

### Ringing/layer shift

1. Check frame, fasteners, pulley grub screws, belts, idlers, V-wheels/rails and cable drag.
2. Run X/Y directional tests and lower acceleration/speed to see if the artifact scales with motion.
3. For a layer shift, identify whether the nozzle hit a curled feature; inspect the exact shift layer before changing motor current or firmware.
4. Only after mechanics are sound, tune input shaping/pressure advance/jerk or equivalent motion parameters.

### Thermal/cooling

1. Verify hotend fan versus part fan, direction, voltage, continuous operation and duct obstruction.
2. Test a short print, then a long print, and compare whether failure time is temperature-dependent.
3. For small layers, use minimum layer time or deliberate slowdown and verify actual part-cooling airflow at the nozzle.
4. Treat enclosure temperature and all-metal heat breaks as material-specific constraints, especially for PLA.

### Supports/bridges

1. Inspect the slicer preview: classify the region as support, overhang or bridge.
2. Print a small isolated section; vary top-Z, interface layers/density, bridge speed, bridge flow and bridge cooling separately.
3. If auto-support misses a critical triangle or narrow wall, paint/manual-place support or change orientation/model geometry.
4. Prefer a shorter span, thicker/wider bridge line, or a different orientation over simply making supports denser.

## NUMERICAL_VALUES

These values are **observed in the sampled discussions**, not recommended universal settings:

| Variable | Values seen | Context/interpretation |
|---|---|---|
| Stringing temperatures | 195/55 °C; 210 °C; 220/55 °C; 205–210 °C | PLA/PLA+ cases; temperature effects were material- and setup-dependent. |
| Stringing retraction | 0.6, 1.0, 1.5 mm; 8 mm @ 60 mm/s; 1.2 mm @ 40 mm/s; 5 mm | Direct-drive Sprite versus Bowden examples; do not transfer between extruders. |
| Drying attempts | 50 °C for 1 h; about 54 °C for 4 h; 60 °C for 5 h; 65 °C for ~24 h; 12 h reported successful | Evidence suggests time/airflow matter; the subreddit does not establish a validated drying standard. |
| Adhesion offsets | ±0.01 mm update; 0.1–0.2 mm mentioned in advice | Direction depends on whether the nozzle is too high or too close; many replies are imprecise about sign convention. |
| Adhesion speeds | 10–20 mm/s first layer; 50 mm/s movement mentioned | Advice, not controlled comparisons. |
| Bridge speed | 20–25 mm/s suggested in one recent discussion | D-level suggestion; bridge geometry/nozzle/material matter. |
| Layer height/nozzle | 0.20 mm layer; 0.16 mm suggested locally; 0.4 and 0.6 mm nozzles | Overhang/support quality changes with geometry and line width. |
| Support gaps | 0.26 mm top Z, 0.20 mm bottom Z at 0.20 mm layers; 0.16–0.20 mm mentioned as possible experiments | P1/P2; lower gap improves support contact but may worsen removal/scarring. |
| Cooling | 10% first-layer fan; full fan; 70%+ on one RatRig anecdote | Not portable across fan ducts or materials. |
| Motion | 60 mm/s CR-10S ringing case; 65 mm/s heat-creep case; 400 mm/s anecdote in debate | Speed alone is not comparable without acceleration, flow and machine architecture. |
| Heat/bed | PLA 55–60 °C; PLA+/PETG examples up to 65–70 °C; ABS example 225/80 °C | Material and enclosure context is essential. |

## CONFLICTS_OR_LIMITS

- **Drying is not a universal explanation for stringing.** S2 reports a strong improvement after longer drying, while S1 remained poor after a short attempt and S3 reports stringing becoming worse after drying. Dryness, temperature, retraction, spool composition and test quality are confounded.
- **Retraction values conflict because hardware differs.** Bowden examples use several millimeters; direct-drive conversion advice is below 1 mm. The corpus supports calibration, not a fixed number.
- **First-layer symptoms are ambiguous.** A brim can look good while the model fails because of geometry, differing brim/model flow, contamination, local bed flatness or thermal contraction. “Lower Z” and “raise Z” both appear in the threads because the visual diagnosis was not always unambiguous.
- **Fan wording is dangerously underspecified.** “Cooling fan” may mean hotend fan or part-cooling fan. Heat-creep threads show that confusing them can send troubleshooting in the wrong direction.
- **Ringing and layer shifts are image-diagnosis problems.** Reddit replies frequently infer belts or input shaping without measurements. Directional tests and a mechanical inspection are stronger evidence than appearance alone.
- **Support and bridge advice is geometry-dependent.** A slicer preview may label a region as an overhang, bridge or unsupported wall; the appropriate fix can be a model/orientation change rather than a numeric setting.
- **Thread outcomes are uneven.** Some posts contain confirmed updates; others end after suggestions. Upvotes are not validation, and comment consensus can reflect common folklore.
- **Reddit metadata can be unstable.** Some direct pages expose relative dates or fail to render fully; dates above use the displayed date where available, otherwise the search result’s relative/date interpretation. Permalinks are preserved by Reddit post ID.

## GAPS

- Few posts provide measured filament moisture, actual fan RPM/airflow, thermistor logs, accelerometer data, belt tension, motor current or repeatable dimensional measurements.
- Sparse coverage of nylon, PC, TPU, carbon-filled materials, abrasive nozzles and high-temperature enclosed printers.
- Limited PrusaSlicer-native terminology in the corpus; many users describe Cura, OrcaSlicer or Bambu Studio settings instead.
- Little controlled comparison of nozzle diameter, line width and maximum volumetric flow as a root cause of under-extrusion.
- Few complete before/after profiles, G-code snippets or machine-state dumps; firmware version and acceleration are often missing.
- Supports/bridges are overrepresented by image-based subjective quality judgments, with little quantified span length, fan airflow or bridge tensile result.
- The corpus is biased toward users who ask for help and commenters who offer likely fixes; successful silent users and failed advice are under-observed.

## CITATIONS

All citations are Reddit discussion permalinks from r/FixMyPrint. The corpus list above is the primary citation index; the same IDs are used throughout CLAIMS.

- S1–S4: [1rcq0uh](https://www.reddit.com/r/FixMyPrint/comments/1rcq0uh/stringing_on_my_prints/), [1w78ur1](https://www.reddit.com/r/FixMyPrint/comments/1w78ur1/stringing_no_matter_the_changes/), [17z2kk2](https://www.reddit.com/r/FixMyPrint/comments/17z2kk2/stringing_increased_with_drying/), [ycaowh](https://www.reddit.com/r/FixMyPrint/comments/ycaowh/still_stringing_after_drying_filament_and_tweaking_retraction_settings/)
- E1–E6: [14ioasi](https://www.reddit.com/r/FixMyPrint/comments/14ioasi/how_do_i_fix_this_underextrusion/), [hysyn](https://www.reddit.com/r/FixMyPrint/comments/hysyn9/under_extrusion_after_upgrading_to_aluminum_extruder/), [pshjmr](https://www.reddit.com/r/FixMyPrint/comments/pshjmr/under_extrusion/), [uyal3r](https://www.reddit.com/r/FixMyPrint/comments/uyal3r/over_extrusion/), [ur5plq](https://www.reddit.com/r/FixMyPrint/comments/ur5plq/estep_calibration_says_im_under_extruding_but_print_dont_show_that_should_i_still_fix_the_value/), [18c4v1](https://www.reddit.com/r/FixMyPrint/comments/18c4v1l/over_or_under_extrusion/)
- W1–A3: [1m20yn](https://www.reddit.com/r/FixMyPrint/comments/1m20yn/print_keeps_warping_of_the_bed/), [yo853i](https://www.reddit.com/r/FixMyPrint/comments/yo853i/brim_prints_perfectly_and_first_layer_of_actual_model_warps/), [1eg8dzc](https://www.reddit.com/r/FixMyPrint/comments/1eg8dzc/first_layer_lifiting_right_behind_extruder/), [10do8qc](https://www.reddit.com/r/FixMyPrint/comments/10do8qc/brim_not_sticking_to_build_plate/), [1jkhji8](https://www.reddit.com/r/FixMyPrint/comments/1jkhji8/help/)
- R1–L2: [1cl36o5](https://www.reddit.com/r/FixMyPrint/comments/1cl36o5/worst_ringingghosting_known_to_man/), [13omwdy](https://www.reddit.com/r/FixMyPrint/comments/13omwdy/how_to_fix_the_yvibration_ghosting_on_a_cr10s/), [1krncqt](https://www.reddit.com/r/FixMyPrint/comments/1krncqt/severe_ghostingringing_down_the_entire_vertical_print/), [130ebpy](https://www.reddit.com/r/FixMyPrint/comments/130ebpy/massive_layer_shift_on_ender3/), [1srgk6f](https://www.reddit.com/r/FixMyPrint/comments/1srgk6f/why_would_it_shift_itself_like_that_midprint/)
- O1–O4: [1fposh9](https://www.reddit.com/r/FixMyPrint/comments/1fposh9/heat_creep_or_something_else/), [u6v8w6](https://www.reddit.com/r/FixMyPrint/comments/u6v8w6/i_keep_getting_clogsheat_creep_then_underextrusion/), [v21iec](https://www.reddit.com/r/FixMyPrint/comments/v21iec/i_get_cloggings_everytime_i_try_to_print_something_longer_than_1h/), [1jawk5](https://www.reddit.com/r/FixMyPrint/comments/1jawk5/top_layers_curling_up/)
- B1–P4: [1e56id8](https://www.reddit.com/r/FixMyPrint/comments/1e56id8/how_can_i_improve_bridge_test_results/), [16i5itn](https://www.reddit.com/r/FixMyPrint/comments/16i5itn/stringing_oozing_particularly_bad_on_overhangs_and_bridges/), [1riudz4](https://www.reddit.com/r/FixMyPrint/comments/1riudz4/help_with_settings_to_mitigate_stringing_on_over/), [1rkq5j](https://www.reddit.com/r/FixMyPrint/comments/1rkq5j/layer_above_support_looks_really_rough/), [1rjtakp](https://www.reddit.com/r/FixMyPrint/comments/1rjtakp/stringing_under_supports/), [xmrw6p](https://www.reddit.com/r/FixMyPrint/comments/xmrw6p/how_to_add_supports_to_this/), [1uh3cic](https://www.reddit.com/r/FixMyPrint/comments/1uh3cic/overhang_support_settings/)
