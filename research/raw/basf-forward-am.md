# BASF Forward AM / Ultrafuse FFF material research

## SOURCE_METADATA

- **Source owner:** BASF Forward AM / Forward AM Technologies GmbH (official material pages, catalog, technical data sheets, metal quick-start guidance).
- **Canonical site:** https://forward-am.com/
- **Accessed:** 2026-10-13.
- **Scope:** Ultrafuse FFF/FFF-adjacent engineering materials: ASA, PC/ABS FR, PP GF30, PET CF15, PAHT CF15, PA6 GF30, PC GF30, PPSU, plus Ultrafuse 316L and 17-4 PH metal-polymer filaments. Pellet products are noted separately where their process windows differ from filament products.
- **Primary documents inspected:** the official Forward AM material catalog (updated June/September 2023 or June 2024 by product page), the individual official TDS PDFs linked below, current material pages, and the official metal quick-start guide. Search-result snippets were not used as evidence.
- **Interpretation:** “Datasheet fact” means a value or condition explicitly stated in a TDS/catalog/page. “Forward AM recommendation” means a stated recommended print setting, drying instruction, hardware requirement, or design rule. A profile starting point for PrusaSlicer is an engineering recommendation, not a guaranteed process specification.
- **Evidence grades:** **A** = explicit primary-source statement/value/procedure; **B** = primary-source cross-check or interpretation from multiple official documents; **C** = cautious engineering inference from the cited facts; **D** = limitation/gap due to absent, ambiguous, legacy, or non-comparable data.

## COVERAGE

| Material / product | FFF material type | Official process information covered | Main mechanical/qualification information covered |
|---|---|---|---|
| Ultrafuse ASA | Engineering thermoplastic | 260–280 °C nozzle; closed/passively heated chamber; 100–120 °C bed; ≥0.4 mm nozzle; 30–60 mm/s; dry 60 °C for 4–16 h | ISO 527/75-2/180; strong XY vs weak ZX anisotropy; HDT 101 °C |
| Ultrafuse PC/ABS FR Black | Halogen-free flame-retardant PC/ABS | 260–280 °C; closed/passively heated chamber; 90–110 °C bed; ≥0.4 mm; 30–50 mm/s in TDS, current page also lists high-speed profile up to 350 mm/s | UL94 V-0 at 1.5/3.0 mm; EN 45545-2 R26; HDT 86 °C; ISO mechanical data |
| Ultrafuse PP GF30 | 30% glass-fiber PP filament | 240–260 °C; no chamber; 20–40 °C bed with PP tape or 70–90 °C with PPGF adhesive; ≥0.6 mm; 30–80 mm/s; page says no drying needed | HDT 127 °C; ISO 527/180; lower ZX strength/impact; chemical/UV/low-moisture positioning |
| Ultrafuse PET CF15 | 15% carbon-fiber PET | 250–270 °C; no chamber; 65–85 °C bed; ≥0.6 mm ruby/hardened; 30–80 mm/s; dry 65 °C, 4–16 h | HDT 108 °C; ISO 527/180; very strong/stiff XY, weak ZX; conditioned test notes in TDS |
| Ultrafuse PAHT CF15 | High-temperature PA with 15% carbon fiber | 260–280 °C; no chamber; 100–120 °C bed; ≥0.6 mm ruby/hardened; 30–80 mm/s; 70 °C air dryer 4–16 h, or 80 °C vacuum ≥40 h for best mechanical properties | HDT 145 °C dry / 128 °C conditioned at 0.45 MPa; ISO mechanical data; moisture state materially changes results |
| Ultrafuse PA6 GF30 | 30% glass-fiber PA6 | 240–280 °C; passively heated closed chamber; 70–100 °C bed; ≥0.6 mm; 30–60 mm/s in TDS (catalog gives 30–80); dry 100 °C, 4–16 h | HDT 110 °C dry / 114 °C conditioned at 0.45 MPa in TDS; ISO 527/180/306; dry vs conditioned density/HDT distinction |
| Ultrafuse PC GF30 | 30% glass-fiber PC | 280–330 °C; no chamber stated; 80–100 °C bed with PC adhesive; ≥0.6 mm; 30–60 mm/s; dry 100 °C, 4–16 h | UL94 V-0 at 1.5/3.0 mm; EN 45545-2 classifications; HDT 134 °C; strong orientation dependence |
| Ultrafuse PPSU | High-temperature amorphous PPSU | 390–410 °C; 170–210 °C chamber; 190–220 °C bed; glass; ≥0.4 mm; 25–80 mm/s in catalog / 25–100 mm/s current page | HDT 215 °C; UL94 V-0; FAR 25.853, glow-wire and EN 45545-2 results; dried-specimen data |
| Ultrafuse 316L | Metal-filled FFF filament, then debind/sinter | 230–250 °C; fan off/no chamber heating in quick start; 90–100 °C bed; ≥0.4 mm; 15–50 mm/s; TDS says printable/no drying necessary | Sintered metal: 561 MPa XY / 521 MPa ZX tensile; 251/234 MPa yield; 53/36% elongation; 128 HV10; scaling/post-processing dominate |
| Ultrafuse 17-4 PH | Metal-filled FFF filament, then debind/sinter | 230–250 °C; no chamber; 90–100 °C bed; ≥0.4 mm; 15–50 mm/s; TDS says printable/no drying necessary | Sintered ISO 6892-1 data; H900 heat treatment produces the higher strength/hardness values; 990/1004 MPa tensile in listed orientations, 756/764 MPa yield |

## CLAIMS

1. **Forward AM’s FFF portfolio spans standard engineering, fiber-reinforced, high-temperature, and indirect-metal workflows.** The material-selection page lists the Ultrafuse engineering, reinforced, metal, and PPSU lines; the catalog supplies the process/mechanical tables. **Conditions:** the metal materials are not final-use polymer prints; they require debinding and sintering. **Evidence: A.**

2. **ASA is an outdoor-oriented ABS-like engineering filament, but Forward AM’s own process window assumes enclosure and drying.** The material page positions it for UV/weather/chemical resistance; the TDS gives 260–280 °C, passively heated closed chamber, 100–120 °C bed, ≥0.4 mm nozzle and 30–60 mm/s. The TDS drying recommendation is 60 °C for 4–16 h. **Evidence: A.**

3. **PC/ABS FR trades a lower process temperature than pure PC for flame-retardant engineering use.** The official page/TDS describe a halogen-free PC/ABS blend, UL94 V-0 at 1.5 and 3.0 mm, and EN 45545-2 railway classification. Its stated ordinary TDS window is 260–280 °C, closed/passively heated chamber, 90–110 °C bed, ≥0.4 mm, 30–50 mm/s. **Conditions:** the current page’s “up to 350 mm/s” is a separate high-speed claim tested with a 0.4 mm nozzle and 0.2 mm layer height; it is not interchangeable with the TDS baseline. **Evidence: A/B.**

4. **Glass- and carbon-fiber products require larger, wear-resistant nozzles in Forward AM’s recommendations.** PP GF30, PET CF15, PAHT CF15, PA6 GF30 and PC GF30 list ≥0.6 mm nozzles; PET CF15 and PAHT CF15 specifically call for ruby or hardened nozzles, while the metal guide requires hardened steel. **Conditions:** this is a Forward AM process recommendation, not a universal minimum for every printer. **Evidence: A.**

5. **Fiber reinforcement is accompanied by strong directional anisotropy.** Examples from the catalog/TDS are PET CF15 tensile strength 63.2 MPa XY vs 12.5 MPa ZX, PAHT CF15 62.9 vs 19.1 MPa, PA6 GF30 46.4 vs 12.2 MPa, and PC GF30 36.1 vs 11.2 MPa. The values are printed-part test results under the cited ISO methods, not isotropic bulk-resin properties. **Evidence: A.**

6. **Moisture control is material-specific, and “low moisture uptake” does not mean “ignore drying.”** The PP GF30 material page says the filament is fully printable without drying because PP absorbs less moisture than PA. In contrast, official TDSs recommend drying PET CF15 at 65 °C for 4–16 h, PAHT CF15 at 70 °C for 4–16 h (or 80 °C vacuum for ≥40 h for best properties), PA6 GF30 at 100 °C for 4–16 h, and PC GF30 at 100 °C for 4–16 h. **Evidence: A/B.**

7. **PAHT CF15’s own TDS demonstrates that conditioning changes the thermal result.** HDT at 0.45 MPa is listed as 145 °C dry and 128 °C conditioned; the same TDS distinguishes dry and conditioned densities and 1.8 MPa HDT. **Conditions:** the result applies to that test specimen conditioning and ISO 75-2 test, not automatically to every printed geometry. **Evidence: A.**

8. **PA6 GF30 also has dry/conditioned data and must be kept dry for stable material properties.** Its TDS recommends 100 °C for 4–16 h and reports HDT at 0.45 MPa of 110 °C dry and 114 °C conditioned. This apparent increase after conditioning is not a contradiction: conditioning changes PA6’s property balance and the reported values are separate test conditions. **Evidence: A/B.**

9. **PP GF30 is comparatively easy to store/process, but bed compatibility is central.** The filament page/TDS pair PP strapping tape with 20–40 °C and PPGF adhesive with 70–90 °C; the recommended nozzle is ≥0.6 mm and the chamber is unspecified/no active chamber requirement. **Conditions:** the two bed windows correspond to different bed surfaces. **Evidence: A.**

10. **PC GF30 is a high-temperature printer requirement, not merely a high-temperature material.** Forward AM lists 280–330 °C nozzle, ≥0.6 mm nozzle, PC adhesive and drying at 100 °C for 4–16 h; the TDS gives a 259 °C melt temperature and 142 °C glass transition. **Inference:** a conventional 250–260 °C hot end cannot reproduce the stated process window reliably. **Evidence: A for the values; C for the hardware implication.**

11. **PPSU is the most demanding polymer in the inspected set.** Forward AM lists 390–410 °C nozzle, 170–210 °C chamber, and 190–220 °C bed, while reporting HDT 215 °C and high-temperature/flame/railway/aerospace qualification data. **Conditions:** the mechanical table is for dried specimens; the page does not provide a generic open-printer recipe. **Evidence: A.**

12. **The metal filaments are indirect metal manufacturing feedstocks, not ordinary “metal-look” FFF plastics.** Forward AM states that 316L and 17-4 PH green parts contain metal powder plus polymer binder, then become brown parts after debinding and fully metal parts after sintering. The metal quick-start guide requires support-layer material for separation, D&S processing, hardened nozzles, approved adhesives, and model scaling. **Evidence: A.**

13. **Metal printing needs enclosure/airflow control even though the quick-start table lists no heated chamber.** Forward AM says temperature variations can cause warpage and recommends a fully enclosed chamber; active heating can help but is not essential. The same guide says the fan is off for the nominal metal process. **Evidence: A.**

14. **Metal nozzle wear and cleanliness are unusually important.** Forward AM attributes extra wear to high metal content, says hardened nozzles last longer, and recommends replacing a non-hardened nozzle after every 3 kg and using new, clean nozzles to avoid contaminating the downstream debinding/sintering process. **Conditions:** the 3 kg interval is the guide’s recommendation, not a universal wear-life guarantee. **Evidence: A.**

15. **The metal mechanical numbers are post-sintering values and are not comparable to green-part FFF strength.** 316L is reported at up to 561 MPa tensile, 251 MPa yield, 53% elongation and 128 HV10; 17-4 PH is reported at up to 1004 MPa tensile, 764 MPa yield and 4% elongation. The 17-4 PH TDS identifies H900 treatment as 1030 °C/50 min, nitrogen gas quench, 482 °C/1 h aging, air cooling for the high-strength state. **Evidence: A.**

16. **Metal shrinkage and geometry limits are process constraints, not slicer cosmetic details.** The official guide gives approximately 16% X/Y and 20% Z post-processing shrinkage, recommends green parts no larger than 100×100×100 mm (with 60×60×60 mm preferred), minimum 1 mm walls, unsupported wall height:width below 6:1, support angles below 45°, and fillets/chamfers to reduce cracking/delamination risk. **Evidence: A.**

17. **Forward AM’s published numbers are guidance/typical values, not specification limits.** The catalog and TDS disclaimers state that values are based on current knowledge/experience, may change, and depend on print orientation and parameters; the recipient must perform its own investigations and tests. **Evidence: A.**

## PROCEDURES

### Selecting a starting material

1. For outdoor/weather exposure, start with ASA; for flame-retardant electrical/transport housings, start with PC/ABS FR or PC GF30; for high stiffness/heat, compare PET CF15, PAHT CF15, PA6 GF30 and PC GF30; for very high service temperature/autoclave/aerospace/railway use, evaluate PPSU.
2. For chemical/fatigue/low-density applications, consider PP GF30, but validate bed adhesion and fatigue/creep for the actual geometry.
3. For 316L or 17-4 PH, treat printing, debinding and sintering as one qualified process. Choose 316L for corrosion resistance/high elongation/non-magnetic behavior; choose 17-4 PH for higher hardness/yield strength and magnetic martensitic structure.

### Polymer filament preparation

1. Keep all filaments sealed and dry; the TDS language is explicit that stable properties require dry material.
2. For ASA, PC/ABS FR, PET CF15, PAHT CF15, PA6 GF30 and PC GF30, use the cited material-specific dryer temperature/time. For PAHT CF15, use the longer 80 °C vacuum cycle when best mechanical properties are the goal.
3. Feed PAHT CF15, PET CF15, PA6 GF30, PP GF30 and PC GF30 through a ≥0.6 mm wear-resistant nozzle as specified; do not assume a brass 0.4 mm nozzle is a good long-term choice.
4. Print from a controlled dry box where practical, especially for PA and PET-based materials. This is an engineering recommendation derived from the TDS drying requirements, not a Forward AM universal dry-box specification.

### Polymer process qualification in PrusaSlicer

1. Start at the middle of the cited nozzle/bed window, then calibrate temperature, flow, pressure advance/retraction, cooling and speed for the exact printer.
2. Use the stated chamber condition: closed/passively heated for ASA, PC/ABS FR and PA6 GF30; no active chamber specified for PP GF30, PET CF15, PAHT CF15 and PC GF30; actively controlled hot chamber is required in practice for PPSU’s 170–210 °C chamber range.
3. Use Forward AM’s nozzle diameter and bed-material recommendations as hard starting constraints. For reinforced materials, validate extrusion force, corner quality, under-extrusion and nozzle wear before increasing speed.
4. Measure parts in the intended print orientation. Report XY/XZ/ZX separately; do not collapse a fiber-filled FFF data sheet into a single isotropic strength number.
5. When comparing dry/conditioned material, label the moisture condition, specimen orientation, layer height/nozzle, infill/perimeter strategy and test standard. A datasheet value is not transferable without those conditions.

### Metal filament workflow

1. Select 316L or 17-4 PH based on final metal requirements; load matching Support Layer where complex support separation is needed.
2. Use a clean hardened nozzle, approved metal adhesive and an enclosed printer. Check spool drag; Forward AM flags 3 kg spools as a potential source of under-extrusion if the holder adds too much force.
3. Use the nominal 230–250 °C nozzle, 90–100 °C bed, fan off, ≥0.4 mm nozzle and 15–50 mm/s speed only as a qualified starting profile.
4. Apply Forward AM’s scaling and design constraints before slicing: approximately XY 120% and Z 124% print scaling in the quick-start table, with final shrinkage validated against the chosen D&S route.
5. Print the green part, inspect for cracks/voids/under-extrusion, then send it through the specified debinding and sintering route. Do not use polymer FFF mechanical properties for the final metal design.

## NUMERICAL_VALUES

| Material | Nozzle °C | Chamber °C | Bed °C / surface | Nozzle | Speed mm/s | Drying recommendation | Key datasheet values |
|---|---:|---:|---|---|---:|---|---|
| ASA | 260–280 | Closed, passive | 100–120 / spray or PC adhesive | ≥0.4 mm | 30–60 | 60 °C, 4–16 h, hot-air or vacuum | HDT 101 °C; tensile XY/ZX 34.6/12 MPa |
| PC/ABS FR | 260–280 | Closed, passive | 90–110 / glass | ≥0.4 mm | 30–50 TDS; page high-speed up to 350 | 60 °C, 4–16 h | HDT 86 °C; tensile 50.1/17.3 MPa; UL94 V-0 1.5/3.0 mm |
| PP GF30 | 240–260 | — | 20–40 / PP tape, or 70–90 / PPGF adhesive | ≥0.6 mm | 30–80 | Current page: no drying needed; TDS: 60 °C, 4–16 h, keep dry | HDT 127 °C; tensile 41.7/15.9 MPa |
| PET CF15 | 250–270 | — | 65–85 / PEI or glass | ≥0.6 mm ruby/hardened | 30–80 | 65 °C, 4–16 h | HDT 108 °C; tensile 63.2/12.5 MPa; modulus XY 6178 MPa |
| PAHT CF15 | 260–280 | — | 100–120 / PEI or glass | ≥0.6 mm ruby/hardened | 30–80 | 70 °C, 4–16 h; best properties: 80 °C vacuum ≥40 h | HDT 145 °C dry / 128 °C conditioned; tensile 62.9/19.1 MPa |
| PA6 GF30 | 240–280 | Passive, closed | 70–100 / glass | ≥0.6 mm | 30–60 TDS; catalog 30–80 | 100 °C, 4–16 h | HDT 110 °C dry / 114 °C conditioned; tensile 46.4/12.2 MPa |
| PC GF30 | 280–330 | — | 80–100 / PC adhesive | ≥0.6 mm | 30–60 | 100 °C, 4–16 h | HDT 134 °C; tensile 36.1/11.2 MPa; UL94 V-0 |
| PPSU | 390–410 | 170–210 | 190–220 / glass | ≥0.4 mm | 25–80 catalog; page 25–100 | TDS/page inspected here did not expose a polymer drying cycle; mechanical data are dried specimens | HDT 215 °C; tensile 74.5/49 MPa; UL94 V-0 |
| 316L metal | 230–250 | —, fan off | 90–100 / glass + approved glue or polyimide | ≥0.4 mm hardened recommended | 15–50 | TDS: printable condition; no drying necessary | post-sinter tensile 561/521 MPa; yield 251/234 MPa; elongation 53/36%; 128 HV10 |
| 17-4 PH metal | 230–250 | — | 90–100 / glass + Magigoo/approved adhesive | ≥0.4 mm hardened recommended | 15–50 | TDS: printable condition; no drying necessary | post-sinter tensile 990/1004 MPa; yield 756/764 MPa; elongation 4/4%; hardness 291/309 HV10 |

### Test standards and conditions

- Polymer tensile values are generally ISO 527; HDT is ISO 75-2 at 0.45 MPa unless otherwise stated; impact is ISO 180 or ISO 179-2. Fiber-filled and polymer data are orientation-dependent.
- PET CF15 TDS notes specimens conditioned at 23 °C / 50% RH for 72 h for the reported tensile testing; PAHT and PA6 TDSs distinguish dry and conditioned specimen results.
- PPSU TDS values are explicitly for dried specimens; its advanced tests include UL94, FAR 25.853, IEC 60695-2-11, AITM 3.0005 and EN 45545-2.
- Metal values are sintered part results. The 17-4 PH H900 condition cited by the TDS is 1030 °C for 50 min, nitrogen gas quench, 482 °C for 1 h, air cooling.

## CONFLICTS_OR_LIMITS

- **PP GF30 drying discrepancy:** the current material page says no drying is needed due to low moisture uptake, while the official TDS recommends 60 °C for 4–16 h and keeping the material dry. Treat the page as an “as supplied/low-moisture” convenience statement and the TDS as the conservative printability/property-control procedure; validate against storage history. **Evidence: B/D.**
- **Catalog vs TDS windows:** the 2024 catalog sometimes gives 30–80 mm/s where older TDSs give 30–60 mm/s (PA6 GF30), and the current PC/ABS FR page gives a high-speed claim up to 350 mm/s while the TDS baseline is 30–50 mm/s. These are different profile/test contexts, not a single guaranteed range.
- **Mechanical-value revisions:** current pages, catalog tables and older TDS versions can differ slightly (e.g., PA6 GF30, PPSU, PC GF30). Prefer the latest material-specific TDS for a production qualification and record its version/date.
- **HDT is not continuous-use temperature:** HDT is a standardized deformation result at a specified stress, not a guaranteed service-temperature limit. PPSU’s “long-term service temperatures up to 180 °C” marketing statement is not the same as its 215 °C HDT.
- **Printed-part data are not bulk-material data:** XY/ZX differences can be several-fold, particularly with short fiber-filled filaments. Layer bonding, moisture, nozzle wear, geometry, infill, cooling and annealing can shift results.
- **Nozzle diameter is a recommendation, not a complete hardware specification:** the sources do not define minimum melt-zone length, extrusion torque, nozzle material grade for every fiber product, or an abrasion-life test. A hardened/ruby nozzle is a sensible engineering recommendation for reinforced fibers; Forward AM makes an explicit hardened-nozzle recommendation for metal.
- **Chamber guidance is incomplete for ordinary polymers:** “—” does not prove that an open frame is suitable; it only means no chamber temperature is specified in the cited table. Warpage, layer bonding and actual machine airflow still require validation.
- **Metal availability status:** the current Forward AM pages label 316L as discontinued and the metal quick-start guide is also marked discontinued, although official TDSs and workflow documentation remain accessible. Confirm commercial availability and supported D&S routes before building a profile around it.
- **Metal shrinkage is route-dependent:** the guide’s approximate 16% XY / 20% Z shrinkage and 120%/124% scaling are starting values. Furnace, orientation, geometry, density and debinding/sintering schedule can change the result.
- **Safety:** official material pages/TDSs advise ventilation/professional extraction for some products; the supplied sources are not a substitute for the current SDS or a site risk assessment.

## GAPS

- No single current, versioned Forward AM profile table was found that normalizes all materials to PrusaSlicer fields such as max volumetric speed, acceleration, cooling, retraction, extrusion multiplier, layer height and fan limits.
- No complete official nozzle-wear dataset was found for the reinforced polymer range; only material recommendations and the metal-specific “replace non-hardened nozzle after every 3 kg” guidance were located.
- No universal chamber-temperature target is published for PAHT CF15, PET CF15, PC GF30 or PP GF30 in the inspected tables; machine enclosure/airflow recommendations therefore require printer-specific validation.
- Drying cycles for PPSU were not exposed in the inspected current page/catalog/TDS content, although its properties are labeled dried-specimen data. Obtain the latest PPSU TDS or contact Forward AM before implementing a production drying profile.
- The inspected sources do not provide standardized creep, fatigue, weld-line/interlayer fracture, thermal cycling, chemical compatibility matrices, or long-term aging data for every FFF material.
- The high-speed page claims do not fully disclose volumetric flow, acceleration, cooling, layer height and test geometry for every product; do not translate speed maxima directly into a PrusaSlicer max-volumetric-speed setting.
- Metal D&S furnace ramp/hold details, allowable density/defect criteria, and full dimensional uncertainty are delegated to process guidelines/service providers rather than fully specified in the quick-start page.

## CITATIONS

### Official material pages

1. Forward AM material selection: https://forward-am.com/material-selection/
2. Ultrafuse ASA: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/engineering-filaments/ultrafuse-asa/
3. Ultrafuse PC/ABS FR: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/engineering-filaments/ultrafuse-pc-abs-fr/
4. Ultrafuse PP GF30: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/reinforced-filaments/ultrafuse-pp-gf30/
5. Ultrafuse PET CF15: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/reinforced-filaments/ultrafuse-pet-cf15/
6. Ultrafuse PAHT CF15: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/reinforced-filaments/ultrafuse-paht-cf15/
7. Ultrafuse PA6 GF30: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/reinforced-filaments/ultrafuse-pa6-gf30/
8. Ultrafuse PC GF30: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/reinforced-filaments/ultrafuse-pc-gf30/
9. Ultrafuse PPSU: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/high-temperature-filaments/ultrafuse-ppsu/
10. Ultrafuse 316L: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/metal-filaments/ultrafuse-316l/
11. Ultrafuse 17-4 PH: https://forward-am.com/material-portfolio/ultrafuse-filaments-for-fused-filaments-fabrication-fff/metal-filaments/ultrafuse-17-4-ph/

### Official catalog and TDS documents

12. Forward AM Material Catalog 2022 (PDF; file metadata says updated July 2024): https://move.forward-am.com/hubfs/Corporate%20Documentation/Forward%20AM%20Material%20Catalog%202022.pdf
13. Ultrafuse ASA TDS v2.2: https://forward-am.com/wp-content/uploads/2021/07/Ultrafuse_ASA_TDS_EN_v2.2.pdf
14. Ultrafuse PC/ABS FR Black TDS v1.2: https://forward-am.com/wp-content/uploads/2021/07/Ultrafuse_PC-ABS-FR-Black_TDS_EN_v1.2.pdf
15. Ultrafuse PP GF30 TDS v2.3: https://forward-am.com/wp-content/uploads/2021/07/Ultrafuse_PP_GF30_TDS_EN_v2.3-2.pdf
16. Ultrafuse PET CF15 TDS v3.3: https://forward-am.com/wp-content/uploads/2021/07/Ultrafuse_PET_CF15_TDS_EN_v3.3.pdf
17. Ultrafuse PAHT CF15 TDS v3.5: https://forward-am.com/wp-content/uploads/2021/07/Ultrafuse_PAHT_CF15_TDS_EN_v3.5.pdf
18. Ultrafuse PA6 GF30 TDS v1.1: https://forward-am.com/wp-content/uploads/2021/12/Ultrafuse_PA6_GF30_TDS_EN_v1.1.pdf
19. Ultrafuse PC GF30 TDS v1.2: https://forward-am.com/wp-content/uploads/2021/12/Ultrafuse_PC_GF30_TDS_EN_v1.2.pdf
20. Ultrafuse PPSU TDS v2.0: https://forward-am.com/wp-content/uploads/2021/07/Ultrafuse_PPSU_TDS_EN_v2.0.pdf
21. Ultrafuse 316L extended TDS v1.1: https://move.forward-am.com/hubfs/AES%20Documentation/Metal%20Filaments/316L/TDS/Ultrafuse_316L_TDS_EN_v1.1.pdf?hsLang=en
22. Ultrafuse 17-4 PH extended TDS v1.1: https://move.forward-am.com/hubfs/AES%20Documentation/Metal%20Filaments/17-4%20PH/TDS/Ultrafuse_17-4PH_TDS_EN_v1.1.pdf?hsLang=en

### Official process/workflow guidance

23. Ultrafuse Metal Solution quick-start guide: https://forward-am.com/gain-knowledge/ultrafuse-metal-solution-quick-start-guide/
24. Ultrafuse metal solutions overview and downloads: https://move.forward-am.com/ultrafuse-metal-solutions
25. Ultrafuse Pellets PP GF30 quick-start (pellet process, not filament process): https://forward-am.com/gain-knowledge/quick-start-guide-ultrafuse-pellets-ppgf30/
26. Ultrafuse Pellets PC GF30 quick-start (pellet process, not filament process): https://forward-am.com/gain-knowledge/quick-start-guide-ultrafuse-pc-gf30/
