# Prusa Forum source research: printers, PrusaSlicer, materials, first layer, extrusion, nozzles and MMU

## SOURCE_METADATA

- **Source:** [Prusa3D Forum](https://forum.prusa3d.com/), primarily the English PrusaSlicer, Original Prusa and MMU3 sections.
- **Research date:** 2026-10-13 (Europe/Berlin).
- **Corpus size:** 25 discussion threads, selected and opened from targeted forum searches. This is a representative corpus, not an exhaustive history of the forum. F24 groups two closely related threads in one table row; both are counted.
- **Selection window:** 2019–2026, with older PrusaSlicer/MK3/Mini material retained where it gives useful baseline context and newer MK4/MK4S/MMU3/Core One material emphasized.
- **Method:** targeted searches for first layer, calibration, PrusaSlicer profiles, extrusion multiplier, retraction/stringing, materials, nozzle diameter, MMU3 sensors, firmware and troubleshooting; pages were opened where the forum exposed post dates and reply context. Summaries below are paraphrased.
- **Forum-status caveat:** forum moderators and experienced users repeatedly describe the forum as mainly user-to-user; moderators are not necessarily Prusa employees. Do not treat a confident reply, moderator badge or “best answer” as an official Prusa position.
- **Evidence grades used in CLAIMS:** **B** = repeated/corroborated pattern or a directly documented official-origin procedure; **C** = one detailed report or one solved procedure with useful context; **D** = unresolved, speculative, indirect or weakly documented claim. **OFFICIAL** is used only for Prusa-origin release material or a reply whose Prusa affiliation is explicit.

## CORPUS_SELECTION

| ID | Thread / date | Model, firmware, profile, material and issue context | Reply provenance |
|---|---|---|---|
| F01 | [Why does PrusaSlicer shrink the first layer?](https://forum.prusa3d.com/forum/prusaslicer/why-does-prusaslicer-shrink-the-first-layer/) — 2021-05-24 reply date visible | MK3S+, FW 3.11.0, PrusaSlicer 2.6.1; elephant-foot compensation and first-layer geometry | Community; experienced-user explanation |
| F02 | [Underextruding on first layer while rest of the layers are perfect](https://forum.prusa3d.com/forum/prusaslicer/underextruding-on-first-layer-while-rest-of-the-layers-are-perfect/?language=en) — 2020-12-11 | Printer not clearly identified in exposed excerpt; profile update suspected; Live-Z values reported | Community troubleshooting |
| F03 | [First Layer height behaviour in PrusaSlicer](https://forum.prusa3d.com/forum/prusaslicer/first-layer-height-behaviour-in-prusaslicer/?language=en) — date not surfaced in opened excerpt | Custom Marlin printer and rebuilt MK2.5S, 0.4 mm nozzle; first-layer height, flow calculation, auto-leveling | Community/technical discussion |
| F04 | [First layer width](https://forum.prusa3d.com/forum/prusaslicer/first-layer-width/?language=en) — 2022-03-04 | PrusaSlicer extrusion-width UI; user comparing Simplify3D and PrusaSlicer | Community |
| F05 | [PrusaSlicer 2.9.4 default value for first layer width for MK3.5 and Mk4](https://forum.prusa3d.com/forum/prusaslicer/prusaslicer-2-9-4-default-value-for-first-layer-width-for-mk3-5-and-mk4/) — 2025-12-16 | MK3.5, MK4, Core One and XL comparisons; 0.4/0.6/0.8 nozzle discussion; first-layer width default | Community; experienced users |
| F06 | [First / Initial Layer flow](https://forum.prusa3d.com/forum/prusaslicer/first-initial-layer-flow/) — 2021 thread; exact opening date not surfaced | PrusaSlicer custom G-code using `M221`, `layer_num` and `extrusion_multiplier` | Community; code example, not official documentation |
| F07 | [PrusaSlicer Initial Layer Flow](https://forum.prusa3d.com/forum/prusaslicer/prusaslicer-initial-layer-flow/?language=en) — 2019-09-17 | Textured sheet, low Live-Z, first-layer over-extrusion; proposed flow override versus cleaning/leveling | Community |
| F08 | [Just got my built PRUSA i3 MK3.. complete from the box](https://forum.prusa3d.com/forum/original-prusa-i3-mk3s-mk3-assembly-and-first-prints-troubleshooting/just-got-my-built-prusa-i3-mk3-complete-from-the-box/) — date not surfaced; reply context opened | MK3, first-layer calibration, Live-Z direction and material/color/brand variation | Community |
| F09 | [MMU3 filament sensor and/or communication issues](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-assembly-and-first-prints-troubleshooting/mmu3-filament-sensor-and-or-communication-issues/) — 2025-11-27 | MK4S + MMU3; latest MMU firmware; SuperFINDA calibration, missing FINDA state and communication symptoms | Community; unresolved in exposed opening |
| F10 | [MMU3 failed on filament 1](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-hardware-firmware-and-software-help/mmu3-failed-on-filament-1/) — 2025-08-06 reply date visible | MK3S+, printer FW 3.14.1-8237, MMU FW 3.0.3; FINDA stuck at 1, loading failure | Community; solved by debris/sensor check |
| F11 | [Newbie Questions on MMU3](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-general-discussion-announcements-and-releases/newbie-questions-on-mmu3/?language=en) — 2024-09 | MK4/MK4S MMU3 Nextruder conversion; whether the modified filament sensor still works | Community; moderator/expert replies, not verified Prusa staff |
| F12 | [6.0.0-RC1 Firmware for Original Prusa MK4 & MK3.9](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-general-discussion-announcements-and-releases/6-0-0-rc1-firmware-for-original-prusa-mk4-mk3-9/?language=it) — 2023-era release thread | MK4/MK3.9 + MMU3; xBuddy cable, firmware pairing, menu enablement, filament-sensor and FINDA calibration | **OFFICIAL-ORIGIN:** release/setup material reproduced in forum announcement; replies community |
| F13 | [MMU3 at CoreOneL will not work, always unloading the Filament](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-assembly-and-first-prints-troubleshooting/mmu3-at-coreonel-will-not-work-always-unloading-the-filament/) — 2026-05-15 | Core One L + MMU3; MMU 3.0.4, Core One L FW 6.5.3+12780, 980 mm PTFE, calibrated sensors; load/unload loop | Community; unresolved in exposed page |
| F14 | [The importance of the filament detection sensor calibration (MK3S) and other problems](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-assembly-and-first-prints-troubleshooting/the-importance-of-the-filament-detection-sensor-mk3s-and-other-problems/?language=fr) — date not surfaced in opened excerpt | MK3S + MMU3; sensor chimney geometry and calibration sensitivity; strongly negative individual report | Community; anecdotal |
| F15 | [MMU3 Setup and First Print Experience](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-general-discussion-announcements-and-releases/mmu3-setup-and-first-print-experience/?foro=allread&foro_n=b1b8d9de73) — 2023-era thread | MK3S+/MMU2, MK4/MMU3 and Core One context; PETG, ASA, PVB and PLA; IR reading, buffer, cutter debris and tuning | Community build report |
| F16 | [First layer issue](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4-hardware-firmware-and-software-help/first-layer-issue-20/?language=fr) — 2024-04-24 | MK4; old/new G-code and recalibration tried; Prusa Support reportedly listed underextrusion, slicer settings, nozzle, filament tension, dirty sheet/nozzle and bed spacers | **SUPPORT-REPORTED:** user relays Prusa Support checklist; forum replies community |
| F17 | [First Layer Issue](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4-how-do-i-print-this-printing-help/first-layer-issue-17/) — 2023-07-26 | MK4; support-material first-layer density, nozzle tip contamination, sheet cleaning and probing ooze | Community; Prusa Support mentioned by user |
| F18 | [First layer patterns](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4-assembly-and-first-prints-troubleshooting/first-layer-patterns?language=it) — 2023-07-21 | MK4; PLA, wet filament suspected, patterned first layer; switching to supplied Galaxy Black changed outcome | Community |
| F19 | [MK4 First Layer Problem with PETG](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4-hardware-firmware-and-software-help/mk4-first-layer-problem-with-petg/?language=en) — 2023-08-30 opening; 2023-10-27 support-assisted reply | MK4, FW 4.7.2, PrusaSlicer 2.6.0, Generic PETG, 0.2 Quality; smooth/satin/textured sheets, loadcell and heatbed screw tension | **SUPPORT-REPORTED:** user attributes procedure to Prusa Support; community confirmations |
| F20 | [First layer height issues](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4-hardware-firmware-and-software-help/first-layer-height-issues/) — 2023-era thread | Multiple MK4s, later firmware reported to improve consistency; comparison with MK3S+; bed flatness and saved Z-offset question | Community |
| F21 | [First layer issues with newly upgraded MK4S](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4s-assembly-and-first-prints-troubleshooting/first-layer-issues-with-newly-upgraded-mk4s/) — 2025-03-24 | MK4 to MK4S upgrade, high-flow nozzle, gaps/dragging; check high-flow profile and firmware hardware nozzle type | Community |
| F22 | [Extrusion multiplier](https://forum.prusa3d.com/forum/prusaslicer/extrusion-multiplier-3/) — 2021-09-06 reply date visible | TPU, first-layer actual height versus slicer-calculated height; `M221` layer-specific flow workaround | Community; advanced-user procedure |
| F23 | [wipe distance after retraction gets too short on solid layers](https://forum.prusa3d.com/forum/prusaslicer/wipe-distance-after-retraction-gets-too-short-on-solid-layers/) — 2024-02-27 | MINI+, PLA, 2.5→2.7 mm retraction, wipe behavior on top solid layers | Community; unresolved behavior question |
| F24 | [Stringing](https://forum.prusa3d.com/forum/prusaslicer/stringing-4/?language=en) and [Is Prusament PETG Matte Black abrasive?](https://forum.prusa3d.com/forum/english-forum-general-discussion-announcements-and-releases/is-prusament-petg-matte-black-abrasive/) — 2021-06-10 / 2023-10-21 | Stringing: old PLA, 215 C, hardened A2 nozzle, 1.1 mm retraction; PETG Matte Black pigment/nozzle-wear question | Community; two related material/nozzle reports grouped for coverage, counted as two threads |

## COVERAGE

- **Printers:** MK2.5S, MK3/MK3S/MK3S+, Mini/MINI+, MK3.5, MK4, MK4S, Core One L; custom Marlin printer also appears in F03.
- **Firmware/software:** MK3 FW 3.11.0 and 3.14.1; MK4 FW 4.7.2 and 5.0-era threads; Core One L FW 6.5.3+12780; MMU3 3.0.3/3.0.4; PrusaSlicer 2.3, 2.6.0/2.6.1 and 2.9.4.
- **Materials:** PLA, PETG, TPU, ASA, PVB, PCTG/other filaments mentioned in the MMU corpus, supplied Galaxy Black, generic and third-party filament, old/wet filament and pigmented PETG.
- **Hardware:** smooth/satin/textured PEI sheets, loadcell, bed screws/Y-carriages, PINDA, Nextruder high-flow nozzle, brass/hardened nozzles, PTFE path, FINDA/SuperFINDA, MMU selector/idler and filament sensors.
- **PrusaSlicer settings:** elephant-foot compensation, first-layer height/width, first-layer flow, extrusion multiplier, `M221`, retraction and wipe, nozzle diameter/profile selection, high-flow printer profiles and support first-layer density.
- **Failure modes:** first-layer too high/low or uneven, adhesion and warping, first-layer under/over-extrusion, stringing, retraction/wipe limitations, nozzle contamination, MMU sensor/load/unload loops, firmware/profile mismatch.
- **Evidence balance:** overwhelmingly community reports and community troubleshooting. One forum firmware/setup announcement is Prusa-origin material; several users relay steps received from Prusa Support. No broad incidence estimates can be inferred.

## OFFICIAL_PRUSA_EVIDENCE

1. **Forum operating model:** A PrusaSlicer feature-request thread states that the forum is mainly user-to-user and that staff/devs rarely post; GitHub Issues are the tracked route for bugs and feature requests. This is a forum-status observation, not a technical printer claim: [Feature request – display Estimated print time](https://forum.prusa3d.com/forum/prusaslicer/feature-request-display-estimated-print-time-also-in-hours-in-float-number/) (2024-03-22).
2. **MK4/MMU3 setup material:** The [6.0.0-RC1 firmware thread](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-general-discussion-announcements-and-releases/6-0-0-rc1-firmware-for-original-prusa-mk4-mk3-9/?language=it) contains Prusa-origin release/setup content: use the MMU3 xBuddy cable; enable the rebuilt MMU extruder and MMU unit in separate settings; recalibrate the filament sensor and FINDA; pair printer FW 6.0.0-RC1 with MMU3 FW 3.0.3. These are version-specific instructions, not timeless defaults.
3. **Support procedure relayed by a user:** In [MK4 First Layer Problem with PETG](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4-hardware-firmware-and-software-help/mk4-first-layer-problem-with-petg/?language=en), the author says Prusa Support/Marcin recommended testing PLA, checking the loadcell self-test, checking Y-carriage orientation/play, and reinstalling the heatbed with the nine screws equally tightened without overtightening. The forum does not expose a direct support post, so this remains support-reported, not independently verified official text.
4. **Support checklist relayed by a user:** In [First layer issue](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4-hardware-firmware-and-software-help/first-layer-issue-20/?language=fr), the author quotes support as asking them to consider underextrusion, model/slicer settings, nozzle, filament tension, dirty sheet/nozzle and bed-spacer position. Again, this is a user relay.
5. **No official authority inferred:** Moderator replies in the selected corpus are categorized as community unless the account or post is explicitly Prusa-origin. “Moderator,” “Veteran Member,” “Illustrious Member” and “best answer” are not sufficient evidence of employment by Prusa Research.

## CLAIMS

### First layer, bed and calibration

1. **PrusaSlicer can intentionally inset the first layer through elephant-foot compensation.** Condition: the apparent shrinkage is a consistent geometric inset on an MK3S+/PrusaSlicer setup, not a random adhesion failure. The forum explanation attributes it to the Print Settings compensation value and notes that it may be adjusted for a particular setup. **[B; F01]**
2. **A first layer that looks too high/low should be diagnosed from line shape and machine context, not by copying another printer’s Z number.** MK3/Mini reports describe bringing the nozzle down until lines flatten, then backing off if ridges form; the Mini thread explicitly says the numerical value is machine-specific and changes with nozzle wear. **[B; F08, F16, F17, F20]**
3. **Sheet type and cleanliness are first-order variables.** Smooth, satin and textured sheets can behave differently; users repeatedly recommend comparing materials/sheets and washing contamination off when IPA alone does not restore adhesion. **[B; F07, F16, F17, F19]** This is a practical forum pattern, not a universal cleaning specification.
4. **Nozzle contamination or ooze before probing can make an MK4 first layer appear too high.** Multiple MK4 reports identify a small old-filament tip or ooze as the apparent cause; the support-reported F16 checklist also includes nozzle condition. **[B; F16, F17, F19]**
5. **Bed mechanics can create spatially uneven first layers even when the slicer file and filament are unchanged.** The MK4 PETG report says equal, non-overtightened heatbed screws solved the problem; other threads discuss bed spacers, Y-carriage play and loadcell checks. **[B; F16, F19]**
6. **Filament can be the differentiating variable in a first-layer pattern.** In the MK4 patterned-first-layer report, switching from suspected poor/wet filament to supplied Galaxy Black changed the result. **[C; F18]** This does not prove moisture as the only cause.
7. **A good first layer followed by failure at 0.1 mm layers is not automatically a Z-offset problem.** The 0.1 mm discussion says the first layer can be good while later-layer adhesion/detail fails, and an experienced reply argues that Z offset is then unlikely to be the main cause. **[C; F03, F20]**
8. **First-layer width is an available PrusaSlicer control, and current preset values vary by profile/version.** The forum identifies Print Settings → Advanced → Extrusion widths, while the 2.9.4 discussion reports 0.5 mm on several 0.4 mm-nozzle profiles and older values around 0.42–0.45 mm. **[B; F04, F05]** The values are profile/version context, not a universal recommendation.
9. **Increasing first-layer flow is usually a workaround, not the first diagnosis.** Community replies show how to emit layer-specific `M221`, but also advise correcting leveling, first-layer height/width and surface condition before using flow to mask the root cause. **[B; F06, F07, F22]**

### Profiles, extrusion, materials and nozzles

10. **PrusaSlicer’s extrusion multiplier and printer-side `M221` flow are different controls and can fight each other.** The forum distinguishes slicer-calculated extrusion multiplier from firmware flow percentage, and warns that changing both complicates diagnosis. **[B; F06, F22]**
11. **A profile update can alter first-layer behavior without a mechanical change.** One user reports a bad first layer after profile updates and different Live-Z requirements when using older G-code; the report is plausible but does not isolate which profile field changed. **[C; F02]**
12. **Extrusion multiplier calibration is repeatedly proposed as a prerequisite before chasing fine stringing with retraction, wipe or Z-lift.** This is a strong community recommendation in the selected PrusaSlicer threads, but it is not a controlled comparison and is not necessarily sufficient for wet filament or machine-specific stringing. **[B; F22, F24]**
13. **Retraction values are starting points and depend on printer drive, material and model.** A moderator gives 0.4 mm as a personal MK3 PLA/PETG value and says TPU may need retraction disabled; another thread shows a MINI+ PLA user changing 2.5→2.7 mm while investigating wipe behavior. **[B; F23, F24]** These values must not be transplanted across architectures.
14. **Old or wet filament is a recurring alternative explanation for stringing.** The stringing report involves 3.5-year-old PLA and a drying attempt; replies recommend trying a known-good/dry spool before extensive retraction changes. **[C; F24]**
15. **Changing nozzle diameter requires more than changing the one diameter field.** The nozzle discussion points to selecting/creating a matching printer profile and adjusting extrusion widths; an experienced reply cites roughly 80% of nozzle diameter as a maximum-layer-height rule of thumb. **[C; F04, F05, F24]** The 80% figure is a forum rule of thumb, not a guarantee for every nozzle/material/printer.
16. **Pigment/additive wear advice is qualitative and disputed.** The Matte Black PETG discussion says more pigment/additives can increase abrasion and distinguishes glow, filled and fiber materials, but it does not provide a measured wear rate for that exact Prusament spool. **[D; F24]**

### MMU3, sensors and firmware

17. **After MK4/MMU3 conversion, the Nextruder sensor position/configuration and calibration are part of the setup, not optional tuning.** The firmware thread states that the extruder hardware mode changes sensor position and requires recalibration; the newbie thread discusses the altered sensor behavior. **[B/OFFICIAL; F11, F12]**
18. **A stuck FINDA state can be caused by a filament sliver/debris or sensor position.** In the MK3S+/MMU3 report, FINDA=1 with no visible filament was solved by moving filament through the fitting to free the ball/debris path. **[C; F10]**
19. **MMU3 load/unload faults are multi-interface failures.** The corpus repeatedly mentions FINDA/SuperFINDA, Nextruder filament sensor, selector/idler tension, PTFE length/ends, pulley debris and firmware pairing. Similar symptoms therefore require preserving the exact printer, MMU, firmware and conversion context. **[B; F09–F15]**
20. **Core One L/MMU3 reports cannot be generalized to MK4S/MMU3.** The Core One L case has MMU 3.0.4, Core One FW 6.5.3+12780, a 980 mm PTFE path and a load/unload loop even after calibration; the page does not show a confirmed resolution. **[C; F13]**
21. **MMU3 can be usable after substantial setup tuning.** The long-term setup report describes more than 1,000 tool changes without faults and highlights IR visibility, buffer behavior, cutter debris and adjustable sensor geometry. This is a successful individual build report, not a reliability estimate. **[C; F15]**
22. **High-flow nozzle/profile/hardware selection must agree after an MK4→MK4S upgrade.** The upgrade thread advises checking the high-flow PrusaSlicer profile and the printer’s hardware nozzle type; replies also suggest swapping to a regular-flow nozzle as an A/B test. **[C; F21]**

## PROCEDURES

1. **First-layer triage:** record printer model, firmware, nozzle type/diameter, sheet type, filament brand/color and PrusaSlicer printer/print/filament profiles. Clean the sheet using the appropriate routine; remove nozzle ooze before probing; run the model’s calibration and observe whether lines are rounded/gapped or ridged/smeared. **[B; F07, F08, F16, F17, F19]**
2. **Separate geometry from adhesion:** if the part is uniformly inset at the base, inspect elephant-foot compensation and first-layer width; if the surface is spatially uneven, inspect bed screws/carriages/loadcell and sheet condition before changing flow. **[B; F01, F04, F19]**
3. **A/B-test material:** use a known-good spool or the supplied filament on the same printer, sheet and G-code. If the pattern follows the spool, investigate moisture, diameter/temperature and material profile; do not immediately change Z or bed mechanics. **[C; F18, F19, F24]**
4. **Profile-change audit:** when a profile update changes the first layer, compare the old/new 3MF or profile values, especially first-layer height/width, extrusion multiplier, temperatures, cooling, nozzle type and start G-code. Do not assume the update was “just a bug.” **[C; F02, F05, F21]**
5. **Extrusion/stringing sequence:** verify material condition and temperature first; calibrate extrusion multiplier; then tune retraction/wipe/Z-lift for the specific drive system and model. Keep firmware `M221` and slicer extrusion multiplier conceptually separate. **[B; F06, F22, F24]**
6. **Nozzle-change sequence:** select the matching printer/nozzle profile, update diameter and extrusion widths, check maximum layer height, then run a small first-layer and dimensional test before a long print. Treat the forum’s 80%-of-diameter figure as a starting heuristic only. **[C; F04, F05, F24]**
7. **MK4/MK4S first-layer isolation:** clean/remove ooze, run loadcell/self-test, compare PLA/PETG and sheets, check bed screw torque and Y-carriage play, and verify high-flow nozzle/profile state after an MK4S upgrade. **[B; F16, F17, F19, F21]**
8. **MMU3 setup/fault sequence:** verify cable and firmware pairing; enable the rebuilt extruder/MMU modes; recalibrate Nextruder filament sensor and FINDA/SuperFINDA; inspect selector/idler, PTFE ends/length, pulley debris and sensor states; then reproduce with one known-good filament. **[B/OFFICIAL for the version-specific setup steps; F10–F15]**
9. **When a procedure is unresolved:** preserve the failure log, exact firmware/profile context and a minimal reproduction. Do not promote a one-user sensor shift, temperature value or firmware downgrade as a general fix. **[B; F09, F13, F20]**

## NUMERICAL_VALUES

Numbers are preserved as source context, not recommendations unless explicitly labeled as such.

| Value | Context | Evidence |
|---|---|---|
| FW 3.11.0; PrusaSlicer 2.6.1 | MK3S+ elephant-foot compensation thread | C, F01 |
| `-1.167` to `-1.223`; `-1.170` | User-reported MK3/MK3S first-layer Live-Z values after profile/G-code changes | C, F02 |
| 0.20 mm | Community-described good first-layer default in the height discussion; not a universal requirement | C, F03 |
| 0.35 mm+ | Suggested test height for a larger nozzle in the custom/MK2.5S discussion | D, F03 |
| 1.40 mm | Simplify3D first-layer-width value the user wanted to reproduce | C, F04 |
| 0.50 mm; older 0.42–0.45 mm | Reported PrusaSlicer 2.9.4 first-layer widths for 0.4 mm-nozzle profiles | C, F05 |
| `M221 S75`; `M221 S{100 * extrusion_multiplier[0]}` | Forum custom-G-code example for layer-specific flow | C, F06 |
| 110% / 105% / 100% | Community examples for temporary first-layer flow overrides | D, F06, F07 |
| 0.4 mm nozzle; 0.6/0.8 mm comparisons | F05 profile comparison context | C, F05 |
| 0.4 mm; ~80% maximum-layer-height heuristic | Nozzle-diameter discussion, quoted as a rule of thumb | C, F24 |
| 3.0.3 MMU; 6.0.0-RC1 printer FW | Version pairing in the MK4/MMU3 release/setup thread | OFFICIAL, F12 |
| 3.0.4 MMU; 6.5.3+12780 Core One L | Core One L load/unload-loop report | C, F13 |
| 980 mm PTFE; 700 mm and 1000 mm tests | Core One L/MMU3 user experiments | C, F13 |
| 4.7.2 printer FW; PrusaSlicer 2.6.0; Generic PETG; 0.2 Quality | MK4 PETG first-layer problem context | C, F19 |
| 9 heatbed screws | Support-reported MK4 heatbed reassembly procedure | C/support-reported, F19 |
| 0.2 mm / up to 0.23 mm / >0.3 mm | User measurements for MK4 PLA/PETG first layers on different sheets | C, F19 |
| 2.5→2.7 mm | MINI+ PLA retraction experiment while investigating wipe distance | C, F23 |
| 215 C; 1.1 mm; 35 mm/s | Stringing report: old filament, hardened A2 nozzle, retraction and speeds | C, F24 |
| 0.4 mm retraction; TPU retraction disabled | Moderator’s personal MK3 starting values, not universal defaults | C, F24 |
| 1,000+ tool changes | Successful MMU3 setup author’s reported run length | C, F15 |

## CONFLICTS_OR_LIMITS

- **Forum authority is uneven.** The corpus contains no broad official troubleshooting program. Most useful replies are community experience; moderators explicitly say they are not necessarily Prusa employees.
- **First-layer Z values are not portable.** PINDA/loadcell state, nozzle wear, sheet, bed assembly, firmware and printer generation change the meaning of a numeric offset.
- **Cleaning advice is situational.** Dish soap/water, IPA and nozzle-cleaning practices recur, but the corpus does not establish one universal chemical or sequence for every sheet coating.
- **Flow versus geometry is easy to conflate.** First-layer width, first-layer height, extrusion multiplier and `M221` can produce similar visual changes while affecting different parts of the toolpath/firmware pipeline.
- **Temperature and material advice conflicts.** The selected corpus does not provide controlled temperature towers or humidity measurements for most reports; do not turn a single 190/205/210/215/220 C anecdote into a default.
- **Pigment/nozzle wear is not quantified.** The Matte Black PETG discussion is qualitative and community-authored; filled/fiber/glow materials have clearer abrasive risk than ordinary pigmented PETG, but exact replacement intervals are absent.
- **MMU “tension” is ambiguous.** It may refer to spool drag, MMU idler, Nextruder idler, selector mechanics or PTFE routing. Ask which interface before applying a fix.
- **Firmware/profile claims are version-bound.** The 6.0.0-RC1 setup content and the 4.7.2 MK4 PETG case should not be read as current firmware documentation without checking current Prusa release notes.
- **Search and display limitations.** Some forum pages expose reply dates but not the opening date in the indexed excerpt; those rows retain “date not surfaced” rather than inventing a date. Localized URL variants are retained where they were the accessible permalink.

## GAPS

- No systematic random sample or forum-wide incidence rates.
- Limited XL and current Core One/Core One+ first-party troubleshooting compared with MK3/MK4/MMU3.
- Sparse complete `.3mf` files, profile exports, G-code diffs, nozzle wear measurements, filament humidity histories and controlled A/B tests.
- Little direct forum evidence for pressure/linear advance, volumetric limits, acceleration, support-interface tuning and seam behavior compared with first-layer/MMU problems.
- Official Prusa Support replies are mostly reported by customers rather than directly visible in the forum pages.
- Some older pages and localized URLs expose only relative/crawled dates; where an exact date was not visible it is explicitly marked as unavailable.
- The corpus includes current-looking 2026 threads; firmware/profile details should be rechecked before operational use.

## CITATIONS

The primary citations are the 24 forum permalinks in `CORPUS_SELECTION`. Particularly central sources are:

- [PrusaSlicer 2.9.4 first-layer width for MK3.5/MK4](https://forum.prusa3d.com/forum/prusaslicer/prusaslicer-2-9-4-default-value-for-first-layer-width-for-mk3-5-and-mk4/)
- [MK4 First Layer Problem with PETG](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4-hardware-firmware-and-software-help/mk4-first-layer-problem-with-petg/?language=en)
- [First layer issue — MK4](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4-hardware-firmware-and-software-help/first-layer-issue-20/?language=fr)
- [6.0.0-RC1 Firmware for Original Prusa MK4 & MK3.9](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-general-discussion-announcements-and-releases/6-0-0-rc1-firmware-for-original-prusa-mk4-mk3-9/?language=it)
- [MMU3 failed on filament 1](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-hardware-firmware-and-software-help/mmu3-failed-on-filament-1/)
- [MMU3 at CoreOneL will not work, always unloading the Filament](https://forum.prusa3d.com/forum/original-prusa-i3-mmu3-assembly-and-first-prints-troubleshooting/mmu3-at-coreonel-will-not-work-always-unloading-the-filament/)
- [Extrusion multiplier](https://forum.prusa3d.com/forum/prusaslicer/extrusion-multiplier-3/)
- [Is Prusament PETG Matte Black abrasive?](https://forum.prusa3d.com/forum/english-forum-general-discussion-announcements-and-releases/is-prusament-petg-matte-black-abrasive/)

