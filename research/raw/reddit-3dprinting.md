# Reddit r/3Dprinting research: FDM fundamentals, calibration, materials, slicers and troubleshooting

## SOURCE_METADATA

- **Source:** [r/3Dprinting](https://www.reddit.com/r/3Dprinting/)
- **Research date:** 2026-10-13 (Europe/Berlin)
- **Corpus type:** bounded, representative discussion corpus; 25 selected discussions, not an exhaustive subreddit history.
- **Selection window:** mostly 2024–2026, with a small number of older high-signal troubleshooting/calibration threads retained when they contained a concrete setup, measurement or resolved outcome.
- **Method:** web search restricted to Reddit/r/3Dprinting, then direct-page inspection for several high-signal threads. Posts and comments were paraphrased; no substantial text is reproduced.
- **Evidence labels:**
  - **C — comparatively strong community evidence:** an explicit before/after, repeated test, or tightly specified setup with a reported outcome. Still an uncontrolled user report unless independently replicated.
  - **D — discussion/anecdote:** plausible advice, a single experience, or a recurring observation without enough controls to establish causation.
- **Interpretation rule:** vote count and apparent consensus are not treated as proof. Repetition is recorded as a recurring observation, not promoted to fact.

## CORPUS_SELECTION

| ID | Date | Focus | Conditions / concrete details | Evidence | Usable observation |
|---|---|---|---|---|---|
| R01 | 2025-07-23 | Filament drying | PLA in a consumer dryer; room about 30–35°C and 60% RH; dryer display rose from 37% to 47% after 9 h. | C/D | Dryer RH is air RH, not filament moisture. Comments converge on venting moist air; a cracked lid or open vents was reported as more useful than chasing a target RH. Weight change was suggested as a better check, but not validated in-thread. |
| R02 | 2025-02-12 | Filament drying | PLA with bubbles/brittleness; 50°C for 8 h; enclosure RH stayed near 40% until lid opening reduced it to 15–18%. | C | Ventilation materially changed the dryer reading; commenters recommended extending to 10–12 h for very wet filament, but that duration is anecdotal. |
| R03 | 2025-04-01 | Moisture and climate | User had printed for years without drying, then moved to a much more humid climate; drying immediately improved adhesion/quality. | C | Moisture sensitivity is strongly environment- and material-dependent; a PLA experience in a dry climate should not generalize to PETG/TPU/nylon or humid rooms. |
| R04 | 2026-04-04 | PET-CF drying | SirayaTech PET-CF: one print after a week exposed, then after 8 h drying; supports changed from strongly fused/rough to easier removal. Hardened nozzle and flow calibration were reported. | C | A concrete before/after supports drying as a major variable for this spool. It does not isolate drying from all other possible state changes. |
| R05 | 2025-01-02 | PETG moisture | PETG troubleshooting thread; comments repeatedly attribute stringing/under-extrusion/adhesion problems to wet material. | D | “Dry PETG” is a recurring troubleshooting recommendation, but thread-level control and resolution are weak. Treat as a cheap diagnostic step, not a universal first cause. |
| R06 | 2023-01-27 | Material drying ranges | Community table under 25°C/50% RH and a 1 kg spool: PLA 55°C >6 h; PETG/ABS 65°C >6 h; TPU 55°C >8 h; nylon 75°C >24 h; ASA 65°C >8 h; PC 75°C >12 h. | D | Useful starting ranges only. The table is a community recommendation and does not establish polymer-specific optimums or account for dryer airflow, spool size, or manufacturer limits. |
| R07 | 2026-06-02 | PETG stringing | Overture PETG; 230°C nozzle, 70°C bed, 60 mm/s, 0.4 mm retraction at 30 mm/s; user reported 7 h at 60°C and 10% drybox RH. | C/D | Comments split between moisture, temperature and retraction. One user reports less stringing at 260°C after drying, contradicting simplistic “always lower temperature” advice. |
| R08 | 2025-12-01 | Troubleshooting meta | A returning user criticizes the automatic “dry your filament” response and says it is often applied without checking the actual symptom or printer state. | D | Useful counterweight to the drying-heavy threads: recurring advice can become cargo-cult troubleshooting. Verify the failure mode before changing material state. |
| R09 | 2024-05-06 | PETG stringing | Heavily modified Ender 3, direct drive, Klipper, PrusaSlicer 2.7.4; 245°C/85°C, 3 mm retraction at 25 mm/s, PA 0.2, travel 150 mm/s, PETG fan capped at 50%. | C/D | Shows why stringing diagnosis must capture printer architecture, PA, cooling, travel and retraction together. The thread reports extensive testing but no clean causal isolation. |
| R10 | 2024-02-16 | First layer / Z offset | Ender 3 V2; 0.25 mm leveling shim; software endstop prevented lowering beyond 0.25 mm; increasing first-layer flow helped one print. | C/D | Mechanical reference height, endstop behavior and Z offset interact. First-layer flow can mask an incorrect gap; it should not be the first substitute for correct Z geometry. |
| R11 | 2023-08-08 | First-layer adhesion | Ender 3 Neo V2, Elegoo PLA, 210°C nozzle/65°C bed; tight turns failed while lines/circles were mostly fine. | D | Local bed height and Z offset were the dominant community diagnosis; a one-layer test was recommended. |
| R12 | 2022-03-01 | First layer / slicer | Ender 3, PLA, 215°C/60°C, PrusaSlicer; print moved rooms and developed peeling and infill holes. | C/D | Advice included slowing first layer to 5–10 mm/s, checking Z offset/bed height and cleaning the nozzle. User later reported corrupted/lost slicer settings as the actual resolution. |
| R13 | 2022-12-05 | First layer | Prusa printer; poor first layer resolved after menu Z calibration and lowering the nozzle. | C | The resolved outcome supports Z calibration as a high-value diagnostic for a first-layer-only problem. Bed contamination, partial clog and moisture were alternative suggestions. |
| R14 | 2026-03-21 | ASA vs ABS warping | Elegoo CC1; eSUN ABS+ printed on a cold plate without issue, eSUN ASA+ warped every 20–30 min; OrcaSlicer temperature/flow calibration had been run; brim or hairspray made ASA succeed. | C/D | Same printer/plate/profile does not imply same material behavior. Chamber temperature, plate adhesion, formulation and geometry remain confounded. |
| R15 | 2026-05-23 | ASA warping | Large ASA part; reports include 55–65°C chamber, 120°C bed, dried filament, brim/anti-warp tabs and slow cooldown; one part warped after completion at 65°C. | C/D | Keeping the part hot during printing is not enough if cooldown releases residual stress. Geometry, thermal gradient and post-print cooling are recurring factors. |
| R16 | 2026-07-29 | ABS warping | Sunlu ABS-FR box, 220×130 mm footprint, Bambu X1E; 60°C chamber, 90→110°C bed, textured PEI and 3DLAC; lowering bed back to 90°C while retaining 60°C chamber improved the result. | C | Stronger than generic advice because the user reports a within-part comparison. It supports “higher bed is not always better” when the bed-to-chamber gradient becomes the dominant problem. |
| R17 | 2026-06-04 | ABS/ASA warping | Large ABS; reports of 265–270°C hotend, 55–65°C chamber, no cooling; one successful case lowered bed from 110°C to 97°C after layer 2. | C/D | Chamber consistency and cooling control recur; bed temperature can need reduction after first-layer adhesion is established. Conditions are printer- and geometry-specific. |
| R18 | 2024-08-12 | Enclosure control | CR-10S4, enclosed custom plywood chamber, heated bed; temperature controller held 54–58°C; three 8+ h ASA prints reportedly had zero warp versus prior failures. | C | A useful before/after field test where enclosure temperature control was the principal claimed change; still one printer, one ASA and no independent measurement protocol. |
| R19 | 2024-08-19 | Calibration ordering | OrcaSlicer built-in temperature/flow/max-flow/PA/retraction tests; community sequence starts with E-steps/rotation distance, then temperature, flow, max flow as needed, PA and retraction if needed. | D | Calibration values are coupled to speed and temperature. A profile tuned for a higher flow rate may need retesting after a hotend-temperature change. |
| R20 | 2026-09-28 | Flow calibration | OrcaSlicer flow test; PETG max volumetric speed shown as 15 mm³/s; discussion proposed averaging adjacent flow results (0.1 and 0.2 → 0.15). | D | Community practice is to choose the best-looking interval/average, but the thread does not establish a measurement criterion or repeatability. |
| R21 | 2024-08-03 | Flow / PA interaction | ColorFabb PLA-HP on Bambu P1S; PA 0.018; flow test showed uneven center/edges; first test reportedly had PA disabled with similar appearance. | C/D | PA can confound visual flow tests, but the reported follow-up weakens a simple PA-only explanation. Inspect the intended measurement region and check extrusion speed/material shrinkage. |
| R22 | 2024-09-17 | PA calibration | OrcaSlicer PA calibration with 0.20, 0.40 and 0.60 mm nozzles; tool generated 0.20 mm layer height for all. | C/D | Calibration generators can contain assumptions that are not appropriate for every nozzle. The thread raised first-layer adhesion and nozzle-specific test geometry as limitations; no definitive fix was documented. |
| R23 | 2024-era discussion | PETG pressure advance | PETG corner bulging; OrcaSlicer pattern method; example values included PA 0.1194 and flow ratio 0.9217 for Sunlu PETG. | D | PA is filament/process-specific in practice; example values are not portable printer defaults. The post is useful as a warning against copying PLA PA to PETG. |
| R24 | 2026-09-21 | Nozzle / layer height | Informal survey: common 0.4 mm nozzle with 0.2 mm layer; examples include 0.6 mm with 0.4 mm layers and 0.9 mm line width, 0.8–1.0 mm nozzles for draft/functional parts, 0.2 mm for miniatures. | D | User practice clusters around ~50% nozzle diameter for everyday layers, but the range is application-driven rather than a hard rule. |
| R25 | 2025-06-10 | PrusaSlicer extrusion width | Ender 3 Pro with Klipper and PrusaSlicer; user asked whether lowering layer height requires changing 0.44 mm widths. | D | Discussion generally treated line width as a nozzle/feature choice rather than something that must track every layer-height change. Smaller geometry may justify a smaller nozzle instead. |

## COVERAGE

- **Fundamentals:** first-layer geometry, bed cleanliness/adhesion, layer height, line width, nozzle selection, cooling and thermal gradients.
- **Calibration:** temperature, flow, max volumetric flow, PA, retraction, E-steps/rotation distance, and ordering/coupling between tests.
- **Materials:** PLA, PETG, TPU, nylon, ABS, ASA, PET-CF and PLA-HP; drying, hygroscopicity, stringing and shrinkage.
- **Slicers:** PrusaSlicer and OrcaSlicer, plus a small amount of Cura-to-PrusaSlicer comparison; focus is on settings and calibration generators rather than software preference.
- **Troubleshooting:** first layer, stringing, warping, under-extrusion/flow interpretation and slicer-state corruption.
- **What is underrepresented:** TPU/nylon print-quality reports with fully specified printer settings; bridges/overhangs; supports and seams; firmware retraction; input shaping; measured dimensional accuracy; independent replication; and manufacturer-specific profiles.

## CLAIMS

### 1. Moisture is a conditional diagnostic, not a universal explanation

- **Claim:** Drying can produce large improvements for PETG, TPU, nylon, filled polymers and filament exposed in humid conditions, while dry PLA is often forgiving. **Evidence: C/D**, R01–R08.
- **Conditions:** Reported examples include PET-CF before/after 8 h drying, PETG at 60°C for 7 h, PLA in humid climates, and a dryer at 50°C for 8 h with ventilation effects.
- **Interpretation:** Treat bubbles, popping, brittle filament, rough surfaces and severe stringing as reasons to run a controlled dry-vs-undried test. Do not infer filament moisture from a dryer’s RH display alone.

### 2. Dryer RH is a process indicator, not a direct moisture measurement

- **Claim:** A dryer can show rising RH while moisture is leaving the filament; venting is repeatedly identified as necessary. **Evidence: C/D**, R01–R02.
- **Conditions:** The clearest thread reports 37%→47% RH during a 9 h PLA cycle and a drop to 15–18% after opening the lid.
- **Limit:** Comments disagree on whether small vents are sufficient; no gravimetric or Karl Fischer measurement was performed. Use manufacturer temperature limits and print-quality comparison rather than a universal RH threshold.

### 3. PETG stringing is multi-causal

- **Claim:** PETG stringing can respond to drying, nozzle temperature, retraction distance/speed, travel strategy and cooling; “PETG always strings” is too broad. **Evidence: C/D**, R07–R09.
- **Conditions:** Reports span 230°C with 0.4 mm retraction, 240°C with a retraction tower, 245°C/3 mm/25 mm/s on a direct-drive Klipper Ender 3, and clean results near 255–260°C after drying.
- **Conflict:** Some anecdotes recommend lower temperatures; others report cleaner hotter printing after drying. The correct next test is a controlled material-specific tower or retraction test, not copying a single number.

### 4. First-layer failures should start with geometry and surface state

- **Claim:** Z offset/nozzle-to-bed geometry, bed tram/mesh and surface cleanliness recur as the highest-yield first checks; first-layer flow and temperature are secondary tuning variables. **Evidence: C/D**, R10–R13.
- **Conditions:** Resolved reports include lowering the nozzle through Z calibration and a room-moved Ender 3 case ultimately traced to slicer settings.
- **Limit:** A photo alone is often ambiguous between too high, too low, contamination, extrusion restriction and slicer state. Use a one-layer test and observe line bonding across the bed.

### 5. ABS/ASA warping is dominated by shrinkage and thermal gradients on large parts

- **Claim:** A stable warm chamber, controlled cooling and geometry/adhesion measures recur more reliably than simply raising bed temperature. **Evidence: C/D**, R14–R18.
- **Conditions:** Field reports include 54–58°C controlled chambers, 55–65°C chamber targets, 90–110°C beds, 220×130 mm ABS-FR geometry and a successful 90°C bed/60°C chamber comparison.
- **Limit:** Chamber temperature is not interchangeable across printers; heat-creep, electronics and enclosure safety constraints matter. Several “60°C” recommendations are user-specific and not a safe universal setting.

### 6. Calibration values are coupled to process conditions

- **Claim:** Temperature, flow, max volumetric speed, PA, retraction and layer geometry interact; a calibration number is a profile value, not a universal printer constant. **Evidence: D with some C**, R19–R23.
- **Conditions:** The corpus includes PA/flow interaction questions, a 15 mm³/s PETG max-flow example, and PETG PA 0.1194 / flow 0.9217 examples.
- **Limit:** Reddit discussions rarely define a repeatable acceptance criterion. Use the same nozzle, layer height, speed, cooling and material lot for comparisons.

### 7. Nozzle and layer-height “rules” are heuristics

- **Claim:** Everyday practice clusters around 0.4 mm nozzle / 0.2 mm layers, with roughly 25–75% of nozzle diameter as a commonly cited layer-height range, but functional/draft/detail goals justify wider variation. **Evidence: D**, R23–R25.
- **Limit:** The corpus contains opinion and informal usage surveys rather than controlled strength or throughput testing. Avoid encoding a hard 75% limit without a process-specific reason.

## PROCEDURES

### Moisture diagnostic

1. Record material, lot, storage history, ambient temperature/RH and symptoms.
2. Keep a short control: print a small stringing or extrusion test from the current spool.
3. Dry at a manufacturer-safe temperature; vent the dryer according to its instructions so humid air can leave.
4. Print the same test immediately after drying with unchanged slicer/printer settings.
5. Compare bubbles/popping, surface roughness, stringing, support release and extrusion consistency. Treat dryer RH as a trend, not a pass/fail threshold.
6. Store the spool sealed with desiccant or print from a drybox when the material is moisture-sensitive.

### First-layer diagnostic

1. Clean the plate using the plate manufacturer’s recommended method; avoid changing several adhesion variables simultaneously.
2. Confirm nozzle condition, correct nozzle diameter and filament path.
3. Run a one-layer test across the usable bed area.
4. Adjust Z offset/mesh/tramming until adjacent lines bond without scraping or leaving gaps.
5. Only then tune first-layer temperature, speed, width or flow. If the same model fails after moving rooms or changing profiles, verify the slicer profile and generated G-code.

### New-filament calibration order (practical, not canonical)

1. Verify extruder E-steps/rotation distance and mechanical condition.
2. Choose the nozzle and intended layer height/line widths.
3. Dry moisture-sensitive filament before interpreting calibration artifacts.
4. Run a temperature test at the intended speed range.
5. Run flow/extrusion calibration at the intended layer height and a safe volumetric flow.
6. Establish maximum volumetric speed if printing near hotend limits.
7. Tune pressure advance for the same material, nozzle and process; retest if temperature, nozzle or major speed changes.
8. Tune retraction only if travel/stringing remains after moisture and temperature are controlled.
9. Validate with the real part or a representative geometry; do not optimize only a calibration tower.

### ABS/ASA large-part procedure

1. Decide whether the part size, footprint and geometry justify ABS/ASA; redesign sharp internal corners or add anti-warp tabs where possible.
2. Heat-soak the enclosure and bed so chamber temperature is stable before starting.
3. Minimize drafts and uncontrolled part cooling; verify the actual chamber temperature, not just the heater setpoint.
4. Use adhesion aids/brim only after controlling the thermal gradient; a hotter bed can worsen stress when the chamber remains cooler.
5. Let the part cool slowly in the enclosure before opening it or removing it.

## NUMERICAL_VALUES

These are observed Reddit values or recurring suggestions, not recommended defaults:

| Area | Values seen in corpus | Context / caution |
|---|---|---|
| Dryer examples | PLA 50–55°C for 3–10 h; PETG 60–65°C for 6–12 h; TPU 55°C for >8 h; nylon 75°C for >24 h; ASA 65°C for >8 h; PC 75°C for >12 h | Community anecdotes/table; follow filament and dryer limits. |
| Dryer ventilation | Lid cracked about 1 cm; open vents; periodic opening about hourly | Device-specific; opening too much can lower temperature and admit humid air. |
| PETG examples | 230–260°C nozzle; 70–85°C bed; 0.2–3 mm retraction; 25–45 mm/s retraction speed; 150–200 mm/s travel | Different hotends/materials/drive systems; not interchangeable. |
| First layer | 5–10 mm/s suggested in one Ender thread; PLA examples 203–215°C nozzle and 55–65°C bed | Diagnostic conditions, not universal profile values. |
| ABS/ASA chamber | 40°C worked for one ABS case; recurring successful reports at 54–60°C; 65°C reported for difficult ASA | Printer/enclosure safety and heat creep constraints apply. |
| ABS/ASA beds | 90–110°C common in reports; one successful case dropped from 110°C to 97°C after layer 2; another improved at 90°C with 60°C chamber | Shows that maximum bed temperature is not automatically best. |
| Flow/PA examples | PETG max volumetric speed 15 mm³/s; PA 0.018 for PLA-HP; PA 0.1194 and flow ratio 0.9217 for one Sunlu PETG example | Profile-specific measurements, not portable constants. |
| Nozzle/layer | 0.4/0.2 mm common; 0.6/0.4 mm and 0.8–1.0 mm nozzles reported for functional/draft work; 0.2 mm for miniatures | Informal survey; application and hotend capacity matter. |

## CONFLICTS_OR_LIMITS

- **“Dry everything” vs “PLA usually does not need drying”:** both appear repeatedly. The better synthesis is conditional on polymer, exposure history, ambient humidity and symptoms; use a controlled before/after test.
- **PETG temperature:** reports range from lowering to 230–235°C to printing cleaner at 255–260°C after drying. This is not a contradiction once moisture, hotend, flow rate and material formulation are treated as variables.
- **Dryer RH:** some users treat a low display number as success; others point out that the sensor measures air RH and may be inaccurate. No thread provides a validated filament moisture measurement.
- **ABS/ASA bed temperature:** higher bed temperatures sometimes improve adhesion, but multiple reports say they increase the bed-to-chamber gradient and worsen warp. Chamber stability and cooldown are confounders.
- **Calibration order:** temperature→flow→PA is common, but PA and flow are coupled and may need iteration. Reddit does not provide a single validated ordering.
- **Community authority:** high votes, repeated phrases (“dry your filament”, “PETG always strings”) and experienced-user tone are not independent evidence.
- **Sampling bias:** Reddit favors visible failures, hobbyist printers and troubleshooting narratives. Successful prints and negative results are underreported; comment chains are self-selected and often lack follow-up.
- **Date/availability:** Reddit’s UI may show relative ages or different localization; dates above follow the page/search metadata available on retrieval. Deleted comments and image-only evidence were not treated as primary support.

## GAPS

- No controlled, multi-printer comparison of drying time/temperature versus measured moisture content.
- No independent replication of the strong enclosure-temperature anecdotes.
- Little evidence for TPU and nylon print settings beyond drying recommendations.
- Insufficient coverage of bridges, overhang cooling, supports, seam placement, infill/top-surface artifacts and dimensional accuracy.
- Little direct evidence about PrusaSlicer-specific defaults or key interactions; most calibration discussion is OrcaSlicer, Klipper or printer-specific.
- No reliable quantitative threshold for acceptable stringing, flow error, PA error or warping.
- Limited reporting of failed calibration procedures and negative controls.

## CITATIONS

1. [R01 — PLA is drying for 9 hours now and is still wet?](https://www.reddit.com/r/3Dprinting/comments/1m7gk2u/pla_is_drying_for_9_hours_now_and_is_still_wet/) — 2025-07-23.
2. [R02 — Filament Drying](https://www.reddit.com/r/3Dprinting/comments/1inqg5e/filament_drying/) — 2025-02-12.
3. [R03 — “Dry your filament” they said...](https://www.reddit.com/r/3Dprinting/comments/1josmbi/dry_your_filament_they_said_for_so/) — 2025-04-01.
4. [R04 — Dry your filament they said....](https://www.reddit.com/r/3Dprinting/comments/1scabcy/dry_your_filament_they_said/) — 2026-04-04.
5. [R05 — Why does this keep happening with petg](https://www.reddit.com/r/3Dprinting/comments/1hs6dre/why_does_this_keep_happening_with_petg/) — 2025-01-02.
6. [R06 — What’s your drying settings for TPU?](https://www.reddit.com/r/3Dprinting/comments/10mg5gu/hey_guys_what_are_your_drying_settings_for_drying/) — 2023-01-27.
7. [R07 — How can I get rid of this stringing?](https://www.reddit.com/r/3Dprinting/comments/1tv4n1f/how_can_i_get_rid_of_this_stringing/) — 2026-06-02.
8. [R08 — Troubleshooting](https://www.reddit.com/r/3Dprinting/comments/1pbcrpp/troubleshooting/) — 2025-12-01.
9. [R09 — Stringing with PETG](https://www.reddit.com/r/3Dprinting/comments/1clne34/stringing_with_petg/) — 2024-05-06.
10. [R10 — What am I doing wrong with my levelling/z-offset?](https://www.reddit.com/r/3Dprinting/comments/1ascm4m) — 2024-02-16.
11. [R11 — First layer adhesion](https://www.reddit.com/r/3Dprinting/comments/15l643d) — 2023-08-08.
12. [R12 — Help with first layer](https://www.reddit.com/r/3Dprinting/comments/t3vglq) — 2022-03-01.
13. [R13 — First Layer Problems?](https://www.reddit.com/r/3Dprinting/comments/zdbdjt) — 2022-12-05.
14. [R14 — I’m confuse. ABS vs ASA warping](https://www.reddit.com/r/3Dprinting/comments/1rzo1qq/im_confuse_abs_vs_asa_warping/) — 2026-03-21.
15. [R15 — ASA warping in a nutshell](https://www.reddit.com/r/3Dprinting/comments/1tlai30/asa_warping_in_a_nutshell/) — 2026-05-23.
16. [R16 — Need advice against ABS warping](https://www.reddit.com/r/3Dprinting/comments/1v9s0pi/need_advice_against_abs_warping/) — 2026-07-29.
17. [R17 — Advice from ABS users](https://www.reddit.com/r/3Dprinting/comments/1twlz5r/advice_from_abs_users/) — 2026-06-04.
18. [R18 — If you are struggling with ABS ASA warping, add a cheap temperature control](https://www.reddit.com/r/3Dprinting/comments/1eqb350) — 2024-08-12.
19. [R19 — OrcaSlicer Calibration chicken or the egg](https://www.reddit.com/r/3Dprinting/comments/1ew5rrz/orcaslicer_calibration_chicken_or_the_egg_q_print/) — 2024-08-19.
20. [R20 — Help with my Flow calibration](https://www.reddit.com/r/3Dprinting/comments/1wsjpmn/help_with_my_flow_calibration/) — 2026-09-28.
21. [R21 — Uneven flow calibration results](https://www.reddit.com/r/3Dprinting/comments/1eiz8h7/uneven_flow_calibration_results/) — 2024-08-03.
22. [R22 — Is it normal that pressure advance calibration in OrcaSlicer always have the same height?](https://www.reddit.com/r/3Dprinting/comments/1fj3m3z) — 2024-09-17.
23. [R23 — Pressure advance calibration for PETG](https://www.reddit.com/r/3Dprinting/comments/1dqqwiw) — 2024-era page metadata.
24. [R24 — What’s your default nozzle size and line height?](https://www.reddit.com/r/3Dprinting/comments/1wlxpu6) — 2026-09-21.
25. [R25 — Should I change extrusion width if printing lower layers?](https://www.reddit.com/r/3Dprinting/comments/1l8ajne) — 2025-06-10.

