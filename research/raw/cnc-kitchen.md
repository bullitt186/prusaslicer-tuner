# CNC Kitchen — FDM Mechanical Properties and Process Research

## SOURCE_METADATA

- **Publisher/author:** CNC Kitchen / Stefan Hermann.
- **Primary source scope:** CNC Kitchen’s own articles, embedded videos, test descriptions, plots/results as transcribed in the articles, and the linked open-source Gradient Infill code. This report does not rely on search-result snippets or third-party summaries.
- **Access date:** 2026-10-13.
- **Units:** Values are reported as CNC Kitchen reports them. MPa = stress; kJ/m² = notched impact strength; N/kg = failure load; mm³/s = volumetric flow. “Standing/upright/vertical” generally means loading across layer interfaces; “lying/flat/horizontal” generally loads in-plane.
- **Evidence key used below:**
  - **A — direct primary measurement:** numeric result and test condition are stated by CNC Kitchen.
  - **B — repeated/paired comparison:** multiple samples, orientations, materials, or chamber/temperature conditions support the observation.
  - **C — author interpretation/recommendation:** useful engineering guidance, but not itself a measured universal law.
  - **D — limitation/qualification:** stated uncertainty, scatter, geometry dependence, material/brand dependence, or an unresolved explanation.
- **Important scope limitation:** These are mostly small-batch, author-designed coupons/hooks and DIY test rigs. They are comparative process experiments, not universal material datasheets or standardized qualification campaigns.

## COVERAGE

| Topic | Primary CNC Kitchen sources | Main result |
|---|---|---|
| Tensile strength and anisotropy | [Stop Printing Flat: The 45° Secret for Stronger Parts](https://www.cnckitchen.com/blog/stop-printing-flat-the-45-secret-for-stronger-parts); [Layer Height vs Strength](https://www.cnckitchen.com/blog/the-influence-of-layer-height-on-the-strength-of-fdm-3d-prints) | Orientation dominates: flat PLA 63 MPa versus upright 31 MPa in one 2025 test; intermediate angles are nonlinear. |
| Layer adhesion vs temperature | [The Influence of Extrusion Temperature on Layer Adhesion](https://www.cnckitchen.com/blog/the-influence-of-extrusion-temperature-on-layer-adhesion) | Too cold and too hot both reduce interlayer strength; PLA peaked near 230 °C, PETG near 245 °C in the tested filaments. |
| Layer height | [Layer Height vs Strength](https://www.cnckitchen.com/blog/the-influence-of-layer-height-on-the-strength-of-fdm-3d-prints) | For the tested 0.4 mm nozzle/PLA, strength dropped above 0.2 mm; thinner than 0.15 mm did not improve bonding. |
| Walls, extrusion width, nozzle size | [Extrusion Width vs Strength and Quality](https://www.cnckitchen.com/blog/the-effect-of-extrusion-width-on-strength-and-quality-of-3d-prints); [Big Nozzles](https://www.cnckitchen.com/blog/big-nozzles-how-do-they-make-your-3d-prints-stronger) | Wider lines improve layer adhesion up to a point; large-nozzle strength gains were mainly more material/thicker walls and higher throughput, not intrinsically better plastic. |
| Infill efficiency | [Gradient Infill for 3D Prints](https://www.cnckitchen.com/blog/gradient-infill-for-3d-prints); [Beginner 3D Printing Guide](https://www.cnckitchen.com/blog/the-beginner-3d-printing-guide-i-wish-i-had) | Shell/wall material is often more efficient than simply increasing infill; gradient infill helped beams but not a small hook. |
| Chamber temperature | [Does a HEATED CHAMBER make your 3D prints STRONGER?](https://www.cnckitchen.com/blog/does-a-heated-chamber-make-your-3d-prints-stronger) | 65 °C chamber raised ABS interlayer strength from 21 to 29 MPa and PC Blend to 77% of flat reference strength. |
| Material comparisons | [Comparing PLA, PETG & ASA](https://www.cnckitchen.com/blog/comparing-pla-petg-amp-asa-feat-prusament); [Essentium PCTG Review](https://www.cnckitchen.com/blog/essentium-pctg-review); [The difference of PLA and PLA+](https://www.cnckitchen.com/blog/the-difference-of-pla-and-pla-tested-feat-polymaker); [Prusament PC Blend Review](https://www.cnckitchen.com/blog/prusament-pc-blend-review); [Carbon Fiber Nylon PA6 vs PA12](https://www.cnckitchen.com/blog/carbon-fiber-nylon-in-3d-printing-pa6-vs-pa12-tested) | No single “strongest” material: stiffness, static strength, toughness, heat resistance, layer strength, moisture response, and creep trade off. |
| Impact | PLA/PETG/ASA comparison; PLA/PLA+; PCTG; PC Blend; CF Nylon | Impact behavior can reverse rankings from slow tensile tests; orientation and moisture strongly matter. |
| Creep | [Carbon Fiber Nylon in 3D Printing: PA6 vs PA12 Tested](https://www.cnckitchen.com/blog/carbon-fiber-nylon-in-3d-printing-pa6-vs-pa12-tested) | Unannealed CF-PA6 showed severe bolt-test creep; annealing reduced it. PA12 was much better; spring test geometry was acknowledged as imperfect. |
| Flow/nozzle process limit | [Extrusion System Benchmark Tool](https://www.cnckitchen.com/blog/extrusion-system-benchmark-tool-for-fast-prints); [DIY High Flow 3D Printing Nozzle](https://www.cnckitchen.com/blog/diy-high-flow-3d-printing-nozzle) | Hotend melt capacity, not just motion speed, limits flow; under-extrusion rapidly appears beyond the tested system’s sustainable flow. |

## CLAIMS (conditions + evidence A-D)

### 1. FDM parts are strongly anisotropic; orientation should follow the load path

- **Conditions:** Azurefilm Green PLA, 0.2 mm layers, Prusa CORE One; tensile coupons printed flat, upright, and at 30°, 45°, 60°.
- **Measured evidence:** Flat averaged **63 MPa**; upright **31 MPa**; 30° **44 MPa**; 45° **40 MPa**; 60° **36 MPa**. CNC Kitchen reports 30° as **42% above upright** and 45° as **27% above upright**.
- **Evidence A:** Direct tensile measurements are stated.
- **Evidence B:** Five orientations were tested, and the comparison is internally consistent with the expected in-plane/interlayer distinction.
- **Evidence C:** Orient parts so critical tensile/shear loads run in the print plane; if no orientation is ideal, use an angle as a compromise between layer separation, surface quality, supports, and bed contact.
- **Evidence D:** Results are for one PLA/printer/layer setup and a small coupon set; the article says the angle-strength curve is S-shaped rather than linear. “30° is best” is not a universal rule.
- **Primary video:** The article embeds the matching CNC Kitchen video; the article URL above is retained as the exact primary source for the conditions and values.

### 2. Layer height above roughly half the nozzle diameter reduced strength in one PLA study; very thin layers did not improve bonding

- **Conditions:** Prusament PLA, Prusa i3 MK2.5, hardened **0.4 mm** steel nozzle; layer heights **0.05, 0.10, 0.15, 0.20, 0.30, 0.40 mm**; hooks printed flat and standing; default Slic3r PE settings, 3 perimeters, top/bottom adjusted for consistent wall thickness; standing parts printed three at a time.
- **Measured evidence:** Flat hooks from 0.05–0.20 mm failed around **80 kg**; 0.30 mm was lower; 0.40 mm much lower. Standing hooks showed the same pattern; 0.30 mm carried about half the load and 0.40 mm almost none. The author reports all standing values at least **50% below** flat values. **0.15 mm** was the strongest of the tested standing heights.
- **Evidence A:** Direct failure loads and tested layer heights are stated.
- **Evidence B:** Flat and standing orientations were paired; results were weight-normalized because thicker layers produced lighter/less-dense parts.
- **Evidence C:** For a 0.4 mm nozzle, stay at or below about **0.2 mm** for strength; the useful generalization is nozzle diameter/layer height ratio, with strength suffering when the ratio falls below about **2**.
- **Evidence D:** The test hook combines tension and bending, not a standardized tensile specimen; some under-extrusion and scatter were observed; another filament brand could behave better.
- **Primary video embedded by article:** `https://www.youtube-nocookie.com/embed/fbSQvJJjw2Q`.

### 3. Extrusion temperature has an optimum: too cold weakens welding, but too hot also reduced layer strength

- **Conditions:** PLA and PETG from dasFilament, Prusa MK3, four standing mini tensile samples per temperature plus flat references, constant-speed DIY tensile machine. PLA: **190–270 °C** in 20 °C steps. PETG: **200–260 °C** in 15 °C steps. A second batch adjusted flow to keep sample weights within ±1%.
- **Measured evidence:** PLA standing strength: **20 MPa at 190 °C**, **37 at 200**, **39 at 210**, peak **40 at 230**, then **37 at 250** and **32 at 270**; flat reference about **60 MPa**. PETG: **18 MPa at 200 °C**, **22 at 215**, **30 at 230**, peak **32 at 245**, then **24 at 260**; flat reference **55 MPa**.
- **Evidence A:** Temperature-strength data are directly reported.
- **Evidence B:** Both materials show the same qualitative optimum curve; flat samples changed little with temperature, isolating layer welding more than bulk polymer strength.
- **Evidence C:** Use the low end of a filament’s range for visual quality and the upper end, possibly slightly above the stated range, when strength is the priority—provided emissions, degradation, moisture, and hardware limits are controlled.
- **Evidence D:** The 190 °C PLA condition was already under-extruded and extra flow caused a jam; high temperatures produced stringing, voids, and bubbles. CNC Kitchen says the mechanism of the high-temperature drop is unresolved and hypothesizes moisture/bubbles at the interface rather than proven bulk degradation.
- **Primary video embedded by article:** the article’s own linked video is the primary video artifact; the article is used for exact conditions/results.

### 4. Wider extrusion can improve interlayer strength, but it is not equivalent to arbitrary flow over-extrusion

- **Conditions:** SpoolWorks PLA, Prusa i3 MK2S, **0.4 mm** nozzle, **210 °C**, **50% fan**, **0.16 mm** layers, 20 °C ambient; extrusion widths from **90% to 250%** of nozzle diameter (**0.36–1.00 mm**); 3DBenchies, layer-adhesion samples, and hooks.
- **Measured evidence:** Layer adhesion rose from 90% width to a maximum around **150%**, then fell; pure material strength was about **60 MPa**. Quality looked similar through about **140%**; overhang artifacts appeared around **160%**, and 250% produced a textured surface. Hook comparison: 2 perimeters/100% failed at **20 kg**; 4 perimeters/100% at **33 kg**; 3 perimeters/133% at **37 kg**; 2 perimeters/200% at **39 kg**.
- **Evidence A:** Direct widths, settings, and failure values are stated.
- **Evidence B:** Same nozzle/material/process family was tested across a broad width range and in both coupon and hook geometries.
- **Evidence C:** Wider lines can be a practical strength/time lever because they squeeze material into the prior layer; verify hotend flow and cooling capacity.
- **Evidence D:** After about 150%, rougher surfaces may act as stress risers and explain the decline; the article does not establish that the weld itself got worse. Wider extrusion also reduces detail and can overload the melt zone.

### 5. Large nozzles improved strength per time mainly by depositing more material, not by intrinsically stronger welds

- **Conditions:** SpoolWorks PLA, Prusa MK3S; standing hooks with **0.4 mm** and **0.8 mm** nozzles, plus 0.4 mm nozzle at **210% extrusion width** to emulate a large nozzle; no infill; flow limited to **3 mm³/s** to avoid melt-capacity confounding; wall thicknesses **0.84 mm** and **1.68 mm**; 0.8 mm tests at **0.15 and 0.30 mm** layer height.
- **Measured evidence:** Across 23 samples, failures ranged **116–808 N**. At 0.84 mm wall thickness, the 0.4 mm/2-wall and 0.8 mm/1-wall averages were about **139 and 140 N**. At 1.68 mm, variants clustered around **347–380 N**; strength per gram was about **42–47 N/g** for the thicker-wall group versus about **27 N/g** for thin-wall samples. Flat reference reached **808 N**.
- **Evidence A:** Direct load and wall-thickness results are stated.
- **Evidence B:** Real large nozzle, emulated large nozzle, and matched wall thickness were compared while restricting flow.
- **Evidence C:** For equivalent wall thickness/material quantity, nozzle diameter alone is not a strength multiplier; large nozzles win when the goal is strength per unit time. A 0.8 mm nozzle at double line width and double layer height can theoretically place about **4×** the material per time, subject to flow, cooling, and quality limits.
- **Evidence D:** The 0.8 mm nozzle at 0.15 mm layers looked poor; the article recommends not going below roughly one-quarter nozzle diameter without tuning. The experiment used no infill, so it does not prove the same scaling for every geometry.

### 6. Walls/perimeters usually buy more useful strength than simply increasing infill

- **Conditions/evidence:** CNC Kitchen repeatedly states this as a design/process conclusion in the large-nozzle article and beginner guide; the large-nozzle hook matrix directly varied wall thickness, while the gradient-infill study compared material allocation.
- **Measured evidence:** In the large-nozzle study, matched increases in wall thickness tracked strength, while nozzle identity did not materially change strength per gram. In the gradient-infill beam, material concentrated near the outside increased stiffness at equal weight.
- **Evidence A:** The wall-thickness/nozzle comparison has direct hook measurements; the beam has direct bending measurements.
- **Evidence B:** Results agree across independent experiments: shell/wall placement matters strongly for bending-dominated parts.
- **Evidence C:** Start with adequate perimeters/wall thickness, then add infill for load paths that actually need a core; do not assume 100% infill is automatically the strongest or most efficient design.
- **Evidence D:** The exact wall-vs-infill optimum depends on geometry, load case, infill orientation, top/bottom skins, and whether the part is in tension, compression, shear, or bending. This is a recommendation, not a universal quantified ratio.

### 7. Gradient infill can improve bending efficiency, but not every part benefits

- **Conditions:** Python post-processor for Cura G-code; infill extrusion varied mostly from **300% near walls to 50% or 0% toward the center**, across a **3–10 mm** gradient. Gyroid worked directly; rectilinear/triangle lines were chopped into roughly **1 mm** segments. Direct drive was favored.
- **Measured evidence:** Bending beams were almost **30% stiffer at equal weight** and almost **60% stiffer at equal print time** versus the comparison beams. A small test hook showed **no significant improvement** versus simply increasing infill percentage.
- **Evidence A:** The article reports measured bending comparisons and test settings.
- **Evidence B:** It intentionally compares equal-weight and equal-time cases, which separates structural allocation from throughput.
- **Evidence C:** Concentrate infill toward highly stressed outer regions for bending-like parts; use FEA/topology when possible rather than treating a fixed gradient as universal.
- **Evidence D:** Results are shape-dependent; the hook wasted material in locations that did not need it. Rapid flow changes can cause extruder slip and need a responsive extrusion system.

### 8. A warm or actively heated chamber can raise interlayer strength for ABS and PC Blend

- **Conditions:** QIDI X-Max 3; 0.4 mm nozzle, ABS at **250 °C**, PC Blend at **275 °C**, **0.2 mm** layers, 2 perimeters, 100% infill. Three chamber cases: open door/top at room temperature (sensor max **26 °C**), passively heated chamber just under **50 °C**, and active heater set to **65 °C**. At least four specimens per condition were destroyed.
- **Measured evidence:** ABS flat reference **39 MPa**; standing/open **21 MPa**; passive **23 MPa**; active 65 °C **29 MPa**, about **75%** of reference. PC Blend open reached **65%** of flat reference; passive reached **72%**; 65 °C reached **77%**.
- **Evidence A:** Direct chamber conditions and interlayer results are stated.
- **Evidence B:** Three ambient/chamber conditions were compared on the same printer and material families.
- **Evidence C:** For ABS/PC-class materials, enclosure and chamber heat can be a process-strength variable, not only a warping fix.
- **Evidence D:** Passive chamber temperature depends on bed size, bed temperature, insulation, room temperature, and geometry. PLA/PETG can suffer heat creep in a hot chamber. The active-heater experiment is specific to the QIDI setup and selected materials.

### 9. Static strength, stiffness, ductility, impact, and heat resistance can rank materials differently

- **Conditions:** Prusament PLA/PETG/ASA on a stock MK3S using stock profiles; PLA **215 °C**, PETG **250 °C**, ASA **260 °C**; mostly no enclosure, 100% PLA fan, 30–50% PETG fan, 20% ASA fan. Flat/standing hooks, bending stiffness, notched IZOD impact, and loaded bars in a convection oven.
- **Measured evidence:** Flat hook failure: PLA **73 kg**, ASA **57 kg**, PETG **55 kg**. Standing layer-adhesion hook: PLA **40 kg**, PETG **25 kg**, ASA **17 kg**; ASA in approximately **30 °C** enclosure reached **20 kg**. Bending modulus: PLA **3300 MPa**, ASA **2300 MPa**, PETG **1900 MPa**. Notched impact: PLA **5 kJ/m²**, PETG **8.6**, ASA **18**. Softening/failure: PLA began giving at **60 °C** and failed around **65 °C**; PETG began around **80 °C** and failed around **85 °C**; ASA began around **110 °C** and failed around **120 °C**.
- **Evidence A:** Direct comparative values are stated.
- **Evidence B:** Multiple mechanical modes were tested on the same Prusament lineup and printer context.
- **Evidence C:** PLA is a strong/stiff default; PETG is more ductile and moderately heat-resistant; ASA is much better for impact and heat but needs better thermal control for layer adhesion.
- **Evidence D:** These are brand-specific Prusament results and non-standard hook/oven tests. Static hook behavior and impact behavior are not interchangeable; PETG’s slow-load ductility did not translate into a large impact advantage.

### 10. Modified PLA can trade static strength/stiffness for toughness; “PLA+” is not automatically more heat-resistant

- **Conditions:** Polymaker PolyLite PLA and PolyMax PLA, dried before testing; nozzle **215 °C**; flat/upright tensile coupons, hooks with 3 perimeters/30% infill, 3-point bending, notched impact, loaded bars in an oven.
- **Measured evidence:** PolyLite flat tensile **57 MPa**, standing **43 MPa** (~75% of flat); PolyLite bending modulus **3000 MPa**, PolyMax **2200 MPa**. Hooks: PolyLite flat **72 kg**, upright **44 kg**; PolyMax flat **48 kg**, upright **34 kg**. Impact: PolyLite about **5 kJ/m²**; PolyMax about **4×** tougher. Both failed around **65 °C** in the oven.
- **Evidence A:** Direct measurements and settings are stated.
- **Evidence B:** The same comparison includes slow tensile, hook, bending, impact, and heat tests.
- **Evidence C:** Choose tougher modified PLA when failure mode/energy absorption matters more than maximum static strength or stiffness.
- **Evidence D:** “PLA+” is a family label; other formulations can differ, and one oven result cannot establish all modified PLAs.

### 11. PCTG showed unusually good layer-strength ratio and impact resistance, but remained PETG-like in heat/stiffness

- **Conditions:** Essentium PCTG printed from a drybox at **270 °C**, 30% fan, powder-coated PEI at **85 °C**; flat and standing tensile samples; notched impact; bending modulus and oven heat test.
- **Measured evidence:** Flat tensile **48–51 MPa** with yielding/necking; standing **38 MPa**, or **40 MPa with 10% cooling**, about **75%** of flat strength. Notched impact **24 kJ/m²**; standing impact **1.5 kJ/m²**. Bending modulus **1600 MPa**; softened around **80 °C**.
- **Evidence A:** Direct primary measurements and print setup are stated.
- **Evidence B:** Flat/upright and cooling variants provide a layer-strength comparison.
- **Evidence C:** PCTG can be attractive where layer adhesion and impact matter more than stiffness/heat; print hot, dry, and with limited cooling.
- **Evidence D:** Two rolls were supplied by the manufacturer; material grade/color/conditioning affect transferability. The author explicitly rejects interpreting PCTG as polycarbonate.

### 12. Moisture and annealing are central for carbon-fiber nylon; dry strength may not persist in service

- **Conditions:** SUNLU CF-PA6 and CF-PA12; annealed **8 h at 110 °C**; moisture-conditioned for 3 days at 75% RH equivalent in a **35 °C** environment, then equilibrated at least one day. Creep: M4 bolt at **0.8 N·m** (~50% tensile-strength preload), and springs loaded at **25%** tensile strength for roughly a week.
- **Measured evidence:** Dry bending: PLA deflected **1.2 mm**, CF-PA12 **1.15 mm**, CF-PA6 **0.7 mm**. Moisture-conditioned PA6 stiffness fell to nearly one-third; annealed conditioned PA6 retained about **41%** of the dry reference stiffness. Dry tensile: PA12 nearly **120 MPa**; PA6 about **140 MPa** and split at a secondary point. Moisture-conditioned PA6 retained only **56%** of dry strength. Dry PA6 absorbed about **15%** of impact hammer energy; conditioned PA6 absorbed **over 50%**. In the bolt test, unannealed PA6 needed retightening almost daily; PA12 only once after half a week; annealing greatly reduced PA6 creep. All springs lengthened, with PA6 worst and annealed PA6 lowest creep; spring deformation partly recovered after 48 hours.
- **Evidence A:** Direct conditioning, strength, stiffness, impact, and creep results are stated.
- **Evidence B:** Dry/conditioned and annealed/unannealed cases expose competing effects: moisture reduces strength/stiffness but increases toughness; annealing reduces PA6 creep.
- **Evidence C:** For nylon mechanisms, qualify the part in its expected humidity state and consider annealing where the material/process allows it; do not size a dry nylon part from dry numbers alone.
- **Evidence D:** The author warns the spring geometry measures creep in bending and is very sensitive to small dimensional differences; one-week tests do not represent years of service. Moisture conditioning was accelerated and approximate rather than a full environmental qualification.

### 13. Melt capacity limits high-speed printing; flow must be characterized per printer/hotend/material

- **Conditions:** Stock Ender-3 Pro, PLA at **200 °C**, automated stepped-flow test using 200 mm blobs weighed on a milligram scale; related high-flow nozzle experiments used multiple hotends/nozzles.
- **Measured evidence:** Flow stayed near constant to about **4 mm³/s**, was about **5% under-extruded at 6 mm³/s**, and then fell sharply. At **220 °C**, usable flow rose to about **8 mm³/s**; at **240 °C**, about **12 mm³/s**. In a separate nozzle benchmark, stock 0.6 mm V6 printed well to **10–15 mm³/s** but failed higher; Volcano was good to about **20 mm³/s**; a DIY high-flow nozzle worked to about **25 mm³/s**; CHT and a double-wire DIY nozzle were similar to about **30 mm³/s**, with degradation beginning around **40 mm³/s** and severe issues at **50 mm³/s**.
- **Evidence A:** Direct flow/temperature/nozzle observations are stated.
- **Evidence B:** The automated test is repeatable and the article explicitly warns that printer, wear, material, and temperature change the result.
- **Evidence C:** Measure maximum volumetric speed rather than copying a profile; increase temperature only within material/safety limits and watch for matte surfaces, gaps, slipping, and incomplete melting.
- **Evidence D:** Flow benchmarks measure extrusion delivery/melt capacity, not final part strength. High-flow hardware can trade resistance for melting performance; the same volumetric rate does not guarantee identical polymer history or weld quality.

## PROCEDURES

### Common mechanical-test pattern

1. Print controlled coupons/hooks in selected orientations and settings.
2. Use a DIY universal tensile machine or hook rig with constant-speed loading to reduce operator variation.
3. Compare flat samples as an in-plane/material reference and standing samples as an interlayer reference.
4. Report average failure load/stress where available, while noting scatter and fracture mode.
5. For impact, use notched specimens in a hammer/IZOD-style rig and infer absorbed energy from hammer energy loss.
6. For heat resistance, load a bar in the middle, raise a convection-oven temperature gradually, and record softening and failure temperatures.
7. For stiffness, use a 3-point bending setup and measure deflection under known or “calibrated” loads.

### Process-variable procedures

- **Temperature:** Keep geometry/printer/material constant, print multiple standing mini tensile samples per temperature, include flat samples to separate bulk strength from layer adhesion, and optionally normalize specimen mass/flow.
- **Layer height:** Print the same hook at several layer heights, keep wall thickness approximately comparable, test both orientations, and normalize by sample weight because thicker layers can leave larger gaps.
- **Extrusion width/nozzle:** Match wall thickness across nozzle/perimeter combinations; remove infill if it introduces geometry-dependent reinforcement; constrain volumetric flow when the question is nozzle/wall physics rather than melt capacity.
- **Chamber:** Use one printer and three ambient conditions (open, passive, active), record actual chamber temperature rather than relying only on setpoint, and compare standing samples to flat references.
- **Creep:** Use a known bolt torque to create compressive preload and a separate spring/weight fixture at a low fraction of tensile strength; observe over days and include annealed/unannealed samples.
- **Moisture:** Test dry/as-printed and conditioned states; record conditioning humidity/temperature/time and allow samples to equilibrate before testing.
- **Flow benchmark:** Extrude equal filament lengths at stepped volumetric rates, weigh the resulting blobs, and plot actual versus commanded mass. Re-run for each hotend/nozzle/material/temperature combination.

## NUMERICAL_VALUES

| Source/result | Conditions | Values |
|---|---|---|
| PLA orientation | Azurefilm Green PLA, 0.2 mm, CORE One | Flat 63 MPa; 30° 44; 45° 40; 60° 36; upright 31 MPa |
| PLA temperature | dasFilament, standing mini tensile coupons | 190 °C 20 MPa; 200 37; 210 39; 230 40; 250 37; 270 32; flat ~60 MPa |
| PETG temperature | dasFilament, standing mini tensile coupons | 200 °C 18 MPa; 215 22; 230 30; 245 32; 260 24; flat 55 MPa |
| Extrusion width | SpoolWorks PLA, 0.4 mm nozzle, 210 °C, 0.16 mm | 90–250% width = 0.36–1.00 mm; layer adhesion peaks ~150%; material ~60 MPa; hook loads 20/33/37/39 kg for 2@100%, 4@100%, 3@133%, 2@200% |
| Large-nozzle hooks | SpoolWorks PLA, no infill, 3 mm³/s max | 23 samples 116–808 N; 0.84 mm walls ~139/140 N; 1.68 mm walls 347–380 N; thick-wall strength/weight ~42–47 N/g |
| Layer height | Prusament PLA, 0.4 mm nozzle | 0.05–0.20 mm flat ~80 kg; 0.30 lower; 0.40 much lower; standing 0.30 ~half and 0.40 near zero; ratio threshold about 2 |
| PLA/PETG/ASA hooks | Prusament, stock MK3S | Flat 73/55/57 kg; standing 40/25/17 kg; ASA ~30 °C enclosure 20 kg |
| PLA/PETG/ASA stiffness | same comparison | 3300/1900/2300 MPa respectively |
| PLA/PETG/ASA impact | notched IZOD | 5/8.6/18 kJ/m² respectively |
| PLA/PETG/ASA heat | loaded oven bars | PLA gives 60/fails 65 °C; PETG gives 80/fails 85 °C; ASA gives 110/fails 120 °C |
| Heated chamber ABS | eSUN ABS, QIDI X-Max 3 | flat 39 MPa; open 21; passive <50 °C 23; active 65 °C 29 MPa |
| Heated chamber PC Blend | Prusament PC Blend, same setup | open 65% of flat; passive 72%; active 65 °C 77% |
| Brick layers | 0.25 mm, 4 perimeters, no infill | Conventional PLA 944 N, PETG 950 N; brick PLA 1072 N (+14%), PETG +10% |
| Gradient infill beam | 25–300% flow gradient over 4 mm in key comparison | ~30% stiffer at equal weight; ~60% stiffer at equal print time; small hook no significant gain |
| PCTG | 270 °C, 30% fan, drybox, 85 °C bed | flat 48–51 MPa; standing 38; standing with 10% cooling 40; impact 24 kJ/m² flat/1.5 standing; modulus 1600 MPa; soft ~80 °C |
| PLA vs PLA+ | PolyLite/PolyMax at 215 °C | PolyLite flat/standing 57/43 MPa; modulus 3000 vs 2200 MPa; hooks 72/44 vs 48/34 kg; impact PolyMax ~4× PolyLite; both failed ~65 °C |
| CF nylon stiffness | dry bending under same load | PLA 1.2 mm; CF-PA12 1.15; CF-PA6 0.7 |
| CF nylon moisture | 75% RH-equivalent conditioning, 35 °C, 3 days | PA6 moisture ~3%; PA12 ~0.7%; conditioned PA6 stiffness nearly one-third dry; annealed conditioned PA6 ~41% of dry reference |
| CF nylon strength/impact | dry vs conditioned | PA12 dry ~120 MPa, dry strength loss ~15% without annealing; PA6 dry ~140 MPa, conditioned strength 56% of dry; PA6 impact ~15% hammer energy dry and >50% conditioned |
| Flow | stock Ender-3 Pro, PLA, 200 °C | stable to ~4 mm³/s; ~5% under at 6; severe drop beyond; ~8 at 220 °C, ~12 at 240 °C |

## CONFLICTS_OR_LIMITS

1. **“Thicker is stronger” versus “thinner is stronger” is test-dependent.** CNC Kitchen’s layer-height study finds no benefit below 0.15 mm and a strength penalty above 0.2 mm for a 0.4 mm nozzle/Prusament PLA. The nozzle/flow studies show thicker extrusion and larger layers can greatly improve strength per time when they increase deposited wall material. These are not contradictory: layer-height ratio, line geometry, wall density, melt capacity, and failure direction differ.
2. **Static tensile rankings are not impact rankings.** PLA led the Prusament flat-hook test, but ASA led impact by a large margin. PolyMax PLA lost slow-load strength versus PolyLite while gaining impact toughness. Use the load case, not one headline number.
3. **Layer-adhesion percentages are not universal material constants.** PCTG reached about 75% of its flat strength, PC Blend 65–77% depending on chamber, while ASA in the older Prusament comparison was only 29% without enclosure. Brand, grade, nozzle temperature, fan, chamber, moisture, geometry, and printer all matter.
4. **Temperature recommendations are conditional.** The temperature study supports an optimum curve, not “hotter is always better.” At high temperature the author saw stringing/voids/bubbles and speculated about moisture; at low temperature PLA was under-extruded and jammed when flow was increased.
5. **CNC Kitchen’s article values mix standardized-like tests and custom fixtures.** Notched impact and tensile stress are more portable than hook kilograms, loaded oven bars, “calibrated” soda-can bending, or visual failure observations. Hook values should be used comparatively within that article’s matrix.
6. **Heated chamber benefits are material-specific.** The ABS/PC Blend chamber study supports higher layer strength, but warm chambers can cause PLA/PETG heat creep and are not automatically beneficial for every filament.
7. **Moisture has opposing effects in nylon.** It reduces PA6 stiffness and tensile strength but increases impact toughness. “Dry” is not automatically “best” unless the service environment is also dry and the design prioritizes stiffness/strength over toughness.
8. **Creep evidence is short-term and geometry-sensitive.** The PA6/PA12 bolt test ran about a week; the author explicitly flags bending springs as highly sensitive to geometry. Do not treat the creep ranking as a lifetime guarantee.
9. **Nozzle size is confounded with process throughput.** The large-nozzle study capped flow at 3 mm³/s to isolate material amount; real fast-print profiles hit hotend, cooling, acceleration, and extrusion-control limits. The high-flow benchmark shows those limits can dominate.

## GAPS

- No broad factorial dataset combining material, nozzle diameter, extrusion width, layer height, flow, cooling, chamber temperature, and orientation on the same standardized specimen.
- Limited statistical reporting: many studies use three or four samples or report averages without confidence intervals or full raw-data tables.
- Limited repeatability across printers, hotends, nozzle materials, filament batches, colors, drying histories, and environmental humidity.
- Few long-duration creep datasets at multiple stresses, temperatures, orientations, and humidity levels; the nylon study is informative but short.
- Few fatigue, cyclic, notch-sensitivity, fracture-toughness, shear, compression, or wear tests relevant to functional machine parts.
- Impact results are not directly transferable between custom notched rigs, IZOD-like methods, and real part drop/crash loads.
- The heated-chamber results do not sweep chamber temperatures or cooling rates, and do not quantify residual stress/warping alongside strength.
- The temperature study does not resolve why excessive nozzle temperature reduced layer adhesion; moisture and interfacial bubbles remain a hypothesis.
- Wall-vs-infill guidance is strong qualitatively but lacks a common geometry matrix that isolates perimeter count, wall thickness, infill percentage, infill angle, skin thickness, and mass.
- Brick-layer slicing is promising but remains a proof of concept: the best layer height, geometry robustness, top-surface handling, supports, and reproducibility in mainstream slicers are unresolved.
- Values should not be pasted directly into PrusaSlicer profiles without local calibration; CNC Kitchen’s own process data repeatedly show that melt capacity, moisture, chamber, cooling, and material batch change results.

## CITATIONS

### Primary CNC Kitchen articles

1. [Stop Printing Flat: The 45° Secret for Stronger Parts](https://www.cnckitchen.com/blog/stop-printing-flat-the-45-secret-for-stronger-parts) — orientation, 30°/45°/60° tensile results, design trade-offs.
2. [The influence of layer height on the strength of FDM 3D prints](https://www.cnckitchen.com/blog/the-influence-of-layer-height-on-the-strength-of-fdm-3d-prints) — 0.4 mm nozzle, 0.05–0.40 mm layer-height study.
3. [The Influence of Extrusion Temperature on Layer Adhesion](https://www.cnckitchen.com/blog/the-influence-of-extrusion-temperature-on-layer-adhesion) — PLA/PETG temperature sweeps and standing/flat tensile comparisons.
4. [Extrusion Width vs Strength and Quality](https://www.cnckitchen.com/blog/the-effect-of-extrusion-width-on-strength-and-quality-of-3d-prints) — 90–250% extrusion width, layer adhesion and hook tests.
5. [Big nozzles — How do they make your 3D prints stronger?](https://www.cnckitchen.com/blog/big-nozzles-how-do-they-make-your-3d-prints-stronger) — matched wall thickness, 0.4/0.8 mm nozzle, strength per time/weight.
6. [Gradient Infill for 3D Prints](https://www.cnckitchen.com/blog/gradient-infill-for-3d-prints) — variable infill flow, bending efficiency, hook limitation; [source code](https://github.com/CNCKitchen/GradientInfill).
7. [Does a HEATED CHAMBER make your 3D prints STRONGER?](https://www.cnckitchen.com/blog/does-a-heated-chamber-make-your-3d-prints-stronger) — ABS and PC Blend at open/passive/65 °C chamber conditions.
8. [Brick Layers — Make 3D prints stronger!](https://www.cnckitchen.com/blog/brick-layers-make-3d-prints-stronger) — interlocking perimeter order, PLA/PETG layer-adhesion results.
9. [Comparing PLA, PETG & ASA — feat. PRUSAMENT](https://www.cnckitchen.com/blog/comparing-pla-petg-amp-asa-feat-prusament) — static strength, layer adhesion, stiffness, impact, heat.
10. [The difference of PLA and PLA+ tested!](https://www.cnckitchen.com/blog/the-difference-of-pla-and-pla-tested-feat-polymaker) — PolyLite/PolyMax strength, stiffness, impact, heat.
11. [Essentium PCTG Review](https://www.cnckitchen.com/blog/essentium-pctg-review) — hot/dry PCTG tensile, layer adhesion, impact, stiffness, temperature.
12. [Prusament PC Blend Review](https://www.cnckitchen.com/blog/prusament-pc-blend-review) — PC Blend mechanical, impact, temperature, moisture/nozzle observations.
13. [Carbon Fiber Nylon in 3D Printing: PA6 vs PA12 Tested](https://www.cnckitchen.com/blog/carbon-fiber-nylon-in-3d-printing-pa6-vs-pa12-tested) — moisture, annealing, creep, stiffness, strength, impact.
14. [Extrusion System Benchmark Tool for fast Prints](https://www.cnckitchen.com/blog/extrusion-system-benchmark-tool-for-fast-prints) — automated flow-capacity method and Ender-3/PLA results.
15. [DIY High Flow 3D Printing Nozzle](https://www.cnckitchen.com/blog/diy-high-flow-3d-printing-nozzle) — nozzle/hotend volumetric-flow comparisons.
16. [Beginner 3D Printing Guide I Wish I Had](https://www.cnckitchen.com/blog/the-beginner-3d-printing-guide-i-wish-i-had) — concise recommendations on layer height, walls, infill, and material properties.

### Embedded primary videos identified from CNC Kitchen article links

- Layer-height study: `https://www.youtube-nocookie.com/embed/fbSQvJJjw2Q`
- Brick-layer study: `https://www.youtube-nocookie.com/embed/5hGm6cubFVs`
- Gradient-infill study: `https://www.youtube-nocookie.com/embed/hq53gsYREHU`
- Extrusion-system benchmark: `https://www.youtube-nocookie.com/embed/lBi0-NotcP0`
- Essentium PCTG review: `https://www.youtube-nocookie.com/embed/-FtnXYDi7z0`

The report uses the article text for exact conditions and numeric results because the articles provide the primary written test record; the videos are listed as corroborating primary artifacts rather than independently transcribed sources.
