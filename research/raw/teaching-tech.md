# Teaching Tech 3D Printer Calibration Guide — source research

## SOURCE_METADATA

- **Source:** Teaching Tech, “3D Printer Calibration”
- **Canonical URL:** https://teachingtechyt.github.io/calibration.html
- **Source type:** Primary author-maintained calibration guide and G-code generators; companion to Teaching Tech videos.
- **Accessed:** 2026-10-13
- **Scope inspected:** Introduction and site limitations; frame/mechanical checks; PID; first layer/ABL/Z offset; baseline; E-steps; slicer flow; stepper current; retraction; temperature; acceleration/jerk/junction deviation; input shaping note; linear advance; XYZ steps/dimensional accuracy; speed/max-flow tuning.
- **Method note:** This report paraphrases the page. Commands, formulas, and numeric values are transcribed only where needed to preserve operational meaning.

## COVERAGE

| Requested area | Coverage on source page |
|---|---|
| Mechanical checks | Frame fasteners, V-rollers, lubrication, bed leveling, PTFE seating, nozzle, belts, fans; stepper current as a later diagnostic. |
| PID | Hot end and bed Marlin autotune, fan/filament conditions, EEPROM and non-EEPROM persistence. |
| Extruder/rotation calibration | Extruder E-steps procedure; separate XYZ steps procedure using a dial gauge; warning against cube-based steps calibration. |
| First layer | Manual leveling, ABL/manual mesh, Z offset, five-square test, interpretation. |
| Temperature | Five-segment tower, filament-specific selection, strength/ooze/overhang trade-offs. |
| Flow | Single-wall hollow cube, slicer-generated G-code, measurement/calculation, visual override and cross-test limitation. |
| Retraction | Distance, speed, extra restart, prime speed and Z-hop; one-parameter-at-a-time tower; slicer translation caveats. |
| Bridging | Mentioned as an observation in the temperature tower and baseline profile (100% fan for bridging); no standalone bridge procedure or acceptance range. |
| Input shaping/ringing | Acceleration/jerk/junction-deviation tower and a short input-shaping note; no input-shaper measurement/tuning workflow. |
| Dimensional accuracy | Raw X/Y/Z motion with dial gauge; flow/shrinkage and slicer dimensional compensation discussed separately. |
| Speed/acceleration | Max extrusion/feedrate test, speed/max-flow vase tower, acceleration tower, firmware limits and firmware-specific persistence. |

## CLAIMS

Evidence grades used here:

- **A:** Explicit procedure, command, formula, range, or condition stated on the primary page.
- **B:** Explicit interpretation/rule-of-thumb or worked example on the primary page.
- **C:** Source-linked supporting material or firmware documentation named by the page; not independently evaluated here.
- **D:** Inference/limitation from absence, scope, or a page-specific example; not a universal specification.

1. **Mechanical calibration should follow a physical inspection.** Loose fasteners, incorrect V-roller tension, poor lubrication, bed geometry/level, unseated PTFE, a partially blocked or loose nozzle, belt/pulley problems, and failed fans can masquerade as calibration problems. **Conditions:** especially after disassembly/component replacement; V-roller systems only for the roller check. **Evidence: A.**
2. **PID should be retuned after thermal-system changes.** The page calls out hot-end changes including a silicone sock or fan/duct change, and bed changes such as glass, spring steel, or insulation. **Conditions:** tune near real printing conditions, with filament loaded and normal part cooling. **Evidence: A.**
3. **A good first layer needs both bed geometry correction and nozzle-to-bed distance.** ABL/mesh compensates for warp/tilt but does not set Z offset; manual leveling remains useful before ABL. **Conditions:** G29 or restored M420 mesh after G28; sensor type determines the sign/approximate character of Z offset. **Evidence: A.**
4. **Extruder E-steps are hardware/filament-path calibration, not slicer flow.** Measure commanded versus actual filament movement, save the corrected M92 value, and repeat for verification. **Conditions:** best with the extruder detached from the hot end; otherwise use slow extrusion and a slightly higher temperature. **Evidence: A.**
5. **Slicer flow is best calibrated from a single-wall cube sliced by the user’s own slicer.** A single wall reduces perimeter-overlap variables; visual under/over-extrusion remains the final check. **Conditions:** zero infill/top layers, one perimeter, known wall/extrusion width, baseline flow 1.0/100%. **Evidence: A/B.**
6. **The measured flow value does not directly transfer to this site’s generated G-code.** The site’s generators derive from Simplify3D G-code with a base flow of 0.90, whereas the user’s cube is sliced independently. **Conditions:** use the calibrated value in the user’s slicer profile; use M221 only as a temporary correction to make a generated test printable. **Evidence: A.**
7. **Retraction and temperature are coupled.** Higher temperature generally increases ooze/stringing; lower temperature can reduce it but risks weak interlayer bonding or jams. **Conditions:** tune one retraction parameter per print and revisit both temperature and retraction as needed. **Evidence: A/B.**
8. **Retraction tower results are not fully portable across slicers.** Layer-time slowdowns, Z-hop speed, retraction acceleration, coast/wipe, extruder feedrate limits, travel speed/acceleration, linear advance, and slicer semantics can change the result. **Evidence: A.**
9. **Ringing/ghosting is presented primarily as a motion-system trade-off.** Higher acceleration and jerk/junction deviation shorten print time but increase vibration and surface artefacts; too-low acceleration can produce corner bulging. **Conditions:** select the segment with the best compromise, not the fastest or smoothest in isolation. **Evidence: A/B.**
10. **Input shaping is only a high-level option in this guide.** The page says it compensates for resonant frequency by altering stepper inputs and is available in Klipper and RepRapFirmware; it does not give a measurement sequence, shaper type, frequency sweep, accelerometer procedure, or acceptance threshold. **Evidence: A for the description; D for the missing workflow.**
11. **Printed-cube dimensions are not a valid basis for X/Y/Z steps calibration.** Flow, material shrinkage, and other print variables affect the cube; raw axis motion should be measured instead. **Conditions:** use a rigid, correctly aligned dial-gauge setup. **Evidence: A/B.**
12. **Maximum reliable feedrate is material-, machine-, and environment-dependent.** The guide explicitly warns that filament type, brand, color, and ambient temperature affect the calculated value; conservative operation is advised. **Evidence: A.**
13. **Bridging has no standalone calibration protocol in this source.** Bridges are used as one visual criterion in the temperature tower, and the base profile specifies full fan for bridging. **Evidence: A for the observations; D for the lack of a dedicated method/range.**

## PROCEDURES

### 1. Site-wide safety and test setup

1. Treat downloaded/generated G-code as potentially unsafe: preview it, remain present and able to stop the printer, and print at your own risk.
2. The site is a JavaScript modifier of Simplify3D-derived G-code, not a general web slicer. Its default assumptions include Marlin-style absolute extrusion, normally 1.75-mm filament, 0.4-mm nozzle, 0.2-mm layers, 0.90 flow, and 100% bridge fan; user inputs modify the final G-code.
3. Establish a baseline before broad calibration or major hardware changes with the generated XYZ 20-mm cube. If major defects remain, return to the frame/mechanical checks.

### 2. Mechanical/frame check

1. Inspect all fasteners, especially printhead/gantry and hot-end hardware.
2. On V-slot/V-roller machines, adjust each eccentric nut until there is no wobble but the assembly is not over-tight; excess tension accelerates wheel wear.
3. Lubricate hardened rods, linear rails, and lead screws regularly with suitable synthetic grease.
4. Level the bed and confirm saved Z offset where ABL is fitted.
5. Heat the nozzle and extrude filament; a non-uniform stream or sideways jet suggests a partial blockage. Tighten the nozzle only while hot, with appropriate care.
6. Check PTFE is fully seated in its coupler and the coupler is tight; a retaining clip may prevent movement.
7. Check belt alignment/tension and pulley grub screws.
8. Confirm mainboard, hot-end, part-cooling, and PSU fans spin freely.

### 3. PID autotune

1. Use a terminal such as Pronterface or OctoPrint. Load filament and set normal part cooling; the page gives `M106 S255` for full fan.
2. Hot end: with the nozzle clear of the bed, run `M303 E0 S200 U1`; substitute the normal nozzle temperature for `200`.
3. Save the result with `M500`.
4. Bed: with `PIDTEMPBED` enabled, run `M303 E-1 S60 U1`; substitute the normal bed temperature for `60`, then `M500`.
5. If EEPROM saving is unavailable, place the returned `M301` (hot end) and/or `M304` (bed) values in slicer start G-code. The page shows the syntax as `M301 E0 P[...] I[...] D[...]` and `M304 P[...] I[...] D[...]`; its example numbers are explicitly bogus placeholders.

### 4. First layer, manual leveling, ABL and Z offset

1. Heat the bed to printing temperature; heat the nozzle close to printing temperature, stopping short of oozing if desired.
2. Move the nozzle around the corners and adjust leveling knobs until a standard office-paper sheet just fits. A clean 0.1-mm feeler gauge is an alternative.
3. Run the generated five-square first-layer test: center plus four corners. Adjust knobs live while printing, or use it to adjust Z offset/validate ABL. Reprint after adjustments to check repeatability.
4. For ABL, manually bring the bed roughly into level first. Probe with `G29` at print start or restore a previously stored mesh with `M420 S1`; either follows `G28`.
5. Set the Z offset after mesh generation. The page’s examples: BLTouch/EZABL/Pinda typically require a negative offset; manual mesh is near zero; a CR-6-style strain gauge can require a positive offset. If available, babystep during the first layer, then save.
6. Interpret the layer: too high gives poor squish/adhesion or a line printed in air; too low spreads the line, can cause elephant’s foot, and in extreme cases blocks extrusion.

### 5. Extruder E-steps / rotation distance equivalent

1. Prefer disconnecting the extruder output from the hot end. Otherwise heat to normal print temperature plus 10 °C and extrude slowly.
2. Query the current value with `M92`; if only `ok` is returned, use `M503` and read the E value.
3. Lift the nozzle clear, select relative extrusion with `G91` (Klipper/RepRapFirmware equivalent: `M83`). Mark filament 120 mm from the extruder entry.
4. Run `G1 E100 F50` (100 mm at 50 mm/min). Measure the remaining mark-to-entry distance; 20 mm remaining means 100 mm actually passed.
5. Use the page calculator: actual extrusion equals 120 mm minus the measured remaining distance; calculate the corrected E-steps. Set with `M92 E<new value>`, save with `M500`, and repeat to verify.
6. Restore absolute movement with `G90` (Klipper/RepRapFirmware equivalent: `M82`). If the printer cannot save EEPROM, put the M92 command in start G-code. For independent multi-extruder values, enable Marlin `DISTINCT_E_FACTORS`, or issue the appropriate M92 during tool change.

### 6. Slicer flow

1. Import the linked cube STL and generate G-code in the target slicer.
2. Use 0% infill, zero top layers, a known wall/extrusion width (the example is 0.4 mm), one perimeter, and baseline flow/extrusion multiplier 100%/1.0. Vase mode is optional and discouraged for Cura because the page reports a tested flow change that invalidates the test.
3. Print the hollow cube. Measure the wall at multiple locations/sides with digital calipers and average; trim away elephant’s-foot and top abnormalities if needed.
4. Calculate a new flow from target wall thickness versus measured wall thickness, then inspect actual surfaces/gaps and adjust by appearance. Do not apply the result blindly to Teaching Tech’s generated G-code; its generator flow baseline and slicer settings differ.

### 7. Retraction

1. Use the tower generator or the linked V2 STL. Tune one parameter per print: distance first, then speed, extra restart, prime speed, and Z-hop as needed.
2. Inspect segments for stringing and select the lowest-stringing region that still restarts cleanly. The page’s example is direct-drive PLA with linear advance, 0.4–1.4 mm distance in 0.2-mm steps; it selects approximately 0.4–0.6 mm as an example, not a universal range.
3. Match relevant conditions when transferring to a slicer: disable/align minimum-layer-time slowdowns, use 20 mm/s Z-hop speed if applicable, account for retraction acceleration and extruder feedrate limits, and remember coast/wipe and travel speed/acceleration are off or controlled in the generated test.
4. Revisit retraction after linear advance/pressure advance tuning.

### 8. Temperature and bridge-related observations

1. Generate a five-segment tower with the lowest temperature at the bottom and highest at the top; remain inside firmware minimum-extrusion and maximum-safety limits.
2. Compare surface finish, overhangs, bridges, stringing/ooze, and snap-test layer adhesion. Higher temperature tends toward stronger interlayer bonding and gloss but more ooze and potentially poorer detail; lower temperature tends toward less ooze and sharper detail but weaker bonding and possible jams.
3. The page’s worked example is 180–260 °C in 20 °C steps on an Ender 3 direct drive with PLA and linear advance; this is an example test range, not a material specification. It notes the coolest segment was brittle, a middle segment strongest, and high-temperature spikes were distorted by inadequate cooling.
4. No separate bridge tower or bridge acceptance range is supplied; use the bridge result only as one temperature/cooling observation.

### 9. Acceleration, jerk/junction deviation, and ringing

1. Determine Marlin mode with `M503`: `M205` containing X/Y/Z indicates jerk; `M205` containing J indicates junction deviation. Klipper uses acceleration plus square corner velocity; RepRapFirmware uses max instantaneous speed change.
2. Print the hollow acceleration tower: normal base, no top layers, two perimeters. The site generator changes `M201`, `M204`, and `M205` for the test; restore or save values afterward.
3. Compare corner bulging at low acceleration with ringing/ghosting at high acceleration. Choose the compromise segment.
4. Example Marlin persistence: set print acceleration with `M204 P400`, ensure per-axis `M201` limits do not cap it, then `M500`. Tune jerk with e.g. `M205 X8 Y8` or junction deviation with e.g. `M205 J0.05`, then save.
5. Klipper example: set `[printer] max_accel: 400`, optionally `max_accel_to_decel: 400`, then tune `square_corner_velocity`; restart/save config. RepRapFirmware uses `M204 P... T...` and `M205 X... Y...` with its documented units/axes.
6. If slicer-injected acceleration settings override firmware, set/check them in Cura, PrusaSlicer, or SuperSlicer.

### 10. Input shaping

- The page only states the principle: input shaping compensates for machine resonance by modifying stepper inputs, and is available in Klipper and RepRapFirmware. It points to videos but provides no standalone test, sensor setup, frequency calculation, shaper selection, or numeric tuning range.

### 11. Linear advance / pressure advance

1. Enable/compile the feature where required; note incompatibility with TMC2208 legacy mode and the interaction with S-curve acceleration.
2. Use Marlin’s pattern generator and inspect a single layer. Select the line with the most uniform width; repeat over a narrower interval for finer resolution.
3. K is filament-dependent. The page suggests starting around K=1.0 for Bowden/flexible filament and K=0.2 for direct-drive/rigid filament, then test above and below.
4. Set with `M900 K<value>` and save with `M500`, or put material-specific M900 in start G-code. `M900 K0` disables it temporarily. Ensure the first layer is reliable because the test is visual.

### 12. XYZ steps and dimensional accuracy

1. Prefer a rigid dial gauge; calipers are a less useful alternative. Mount it parallel/perpendicular to the measured axis, avoid flex, and ensure Z homing cannot bottom the gauge.
2. Read current values via LCD or `M503`. Home safely, position and zero the gauge mid-travel, and request a 10-mm move (100 mm would be better but often exceeds gauge travel). Reverse the move and verify return to zero; repeat two 10-mm moves to check consistency.
3. A worked tolerance example is 9.95 mm for a requested 10 mm, i.e. 0.05 mm/10 mm = 0.5%; the page says this may be acceptable depending on user tolerance.
4. Before changing steps, check belts, pulley grub screws, V-rollers, lubricated lead screws, driver current, and firmware features such as square-wave stepping. Inconsistent return suggests backlash/binding.
5. Only after these checks, calculate new X/Y/Z steps from target/requested versus measured motion, set with M92, save with M500, and repeat.
6. For persistent printed-part dimensional errors after axis motion is correct, consider small flow adjustment or slicer dimensional compensation (PrusaSlicer X/Y compensation, Cura horizontal expansion), recognizing that hole and external-dimension accuracy can trade off. Do not use a 20-mm cube alone to calibrate steps.

### 13. Speed, max flow, and maximum feedrate

1. Optional simplified hot-end/extruder test: clear the drive gear, heat to normal temperature, load filament, select relative mode with `G91`, then run `G1 E50 F120` (50 mm at 2 mm/s).
2. Repeat at higher F values, e.g. `F180`, `F240`, `F300`, `F360`, until extrusion becomes inconsistent, the extruder skips, or the hobbed gear chews filament. Back off and repeat the candidate speed several times for repeatability; restore `G90`.
3. Enter reliable feedrate and filament diameter into the calculator to estimate volumetric flow and an XY feedrate from layer height and extrusion width. The resulting value is conditional on those inputs and environmental/material variables.
4. For the full speed/max-flow tower, use vase mode: one continuous external perimeter after the base, no retraction/travel confounders, and M220 feedrate changes at height intervals. Stop early if extrusion fails to avoid a blockage.
5. Check firmware limits before testing. Marlin uses M203 for feedrate and M201/M204 for acceleration; Klipper uses `MAX_VELOCITY`, `MAX_ACCEL`, `MAX_ACCEL_TO_DECEL` or `SET_VELOCITY_LIMIT`; RepRapFirmware uses M203/M201/M204 with feedrate in mm/min and acceleration in mm/s². Raise limits only as needed and save/persist deliberately.

## NUMERICAL_VALUES

| Topic | Values/commands on the page | Status/conditions |
|---|---|---|
| Base profile | 120×120×250 mm minimum build volume; 1.75-mm filament; 0.4-mm nozzle; 0.2-mm layer; auto width typically 120% nozzle; default 60 mm/s; perimeter 60%, solid infill 80%, travel 166%, first layer 50%; Z travel 20 mm/s; flow 0.90; 100% bridge fan; first layer 100% height/120% width | Generator defaults, not universal printer recommendations. |
| PID examples | `M106 S255`; hot end `M303 E0 S200 U1`; bed `M303 E-1 S60 U1`; save `M500` | Replace temperatures with normal print values; fan/filament conditions recommended. |
| First layer | 0.1-mm feeler gauge alternative; five squares | Paper method is qualitative; no acceptance thickness is specified beyond fit/squish interpretation. |
| E-steps | Mark at 120 mm; command 100 mm; `G1 E100 F50`; ideal remaining mark distance 20 mm | Best with hot end detached; otherwise +10 °C and slow extrusion. |
| Flow example | 0.4-mm target wall/width; one wall; 100%/1.0 baseline; 0% infill/top | Example settings, not a universal extrusion width. |
| Retraction example | Direct-drive PLA + linear advance: 0.4–1.4 mm in 0.2-mm increments; example result 0.4–0.6 mm | Worked example only; no general Bowden/direct-drive range claimed. |
| Temperature example | 180–260 °C in 20 °C increments | Ender 3 direct drive, PLA, linear advance example. |
| Driver current formulas | A4988: `VREF = 8 × max current × sense resistor`; DRV8825 with 0.1 Ω: `VREF = max current / 2`; TMC2100/legacy TMC2208: RMS=peak/1.41 and `VREF=(RMS×2.5)/1.77`; LV8729 R100 `max/2`, R220 `max×1.1` | Verify exact driver/sense resistor; formula scope is the tested hardware. |
| TMC current example | `M906 X680`; save `M500`; TMC5160 sense resistor 0.075 rather than 0.11 | RMS current and firmware configuration dependent. |
| Max extrusion test | Start `G1 E50 F120`; examples increment F by 60 mm/min = 1 mm/s; restore `G90` | Stop at failure and back off for repeatability. |
| Worked volumetric example | Page calculator displays 7.22 mm³/s and 90 mm/s XY for its inputs | Calculator outputs are input-dependent; not a universal limit. |
| Acceleration example | Tower 300–800 mm/s² in 100 increments; junction deviation 0.08; example preferred acceleration 400 vs prior 500; `M204 P400`; example jerk 8; junction deviation 0.05; Klipper SCV example 8.0 | Worked examples, not recommended defaults. |
| Dimensional example | 10-mm move measured 9.95 mm = 0.05 mm error = 0.5%; 25-mm gauge travel warning; 100 mm preferable but often unavailable | Acceptability depends on user tolerances and measurement setup. |
| Speed limits examples | Marlin `M203 X500 Y500`; Klipper `SET_VELOCITY_LIMIT VELOCITY=500`; Klipper acceleration 600; RRF feedrate conversion 500 mm/s × 60 = 30,000 mm/min | Temporary/firmware-limit examples; do not copy without machine validation. |

## CONFLICTS_OR_LIMITS

- The page’s generator defaults and tests are not a universal slicer profile: they derive from Simplify3D and are modified by JavaScript. Results should be interpreted for the purpose of each test, not as a general print-quality score.
- Flow calibration is intentionally not portable to the generator’s nominal 0.90 flow; user-slicer settings, extrusion width, cooling, and minimum-layer-time behavior alter results.
- Temperature values shown on the page are a single PLA/Ender 3 example, not material standards. Firmware min/max bounds remain controlling.
- Retraction results can diverge when minimum-layer-time, travel speed, acceleration, Z-hop, coast/wipe, linear/pressure advance, firmware extruder limits, or slicer semantics differ.
- Stepper-current formulas depend on driver mode, motor rating, sense resistor, and whether peak or RMS current is being discussed. The page itself warns that some Creality boards use R150 rather than R100 and therefore invalidate a default formula.
- High feedrate/acceleration tests can cause jams, skipped steps, overheating, layer shifts, or mechanical wear. The guide repeatedly expects live monitoring and conservative limits.
- “Input shaping” is not comprehensively documented on this page; it is a capability note plus video links, not a reproducible tuning protocol.
- Bridging is not a dedicated calibration tab. There is no bridge-speed, bridge-flow, bridge-fan, span-length, or pass/fail range in the source.
- XYZ steps calibration is for raw machine movement, not final printed dimensions. Final dimensions additionally depend on flow, shrinkage, holes/geometry, and slicer compensation.
- The page contains occasional firmware-specific or version-specific instructions (Marlin, Klipper, RepRapFirmware). Commands and persistence behavior should be checked against the installed firmware version.

## GAPS

- No standalone bridge calibration procedure, bridge test geometry, span-length matrix, or numerical acceptance criteria.
- No input-shaper calibration workflow: no accelerometer wiring, resonance measurement, frequency sweep, shaper choice, damping, or validation print.
- No formal pass/fail thresholds for PID stability, first-layer flatness, flow deviation, stringing, ringing, dimensional error, or maximum volumetric flow.
- No complete numerical ranges for retraction distance/speed, temperature by material, acceleration, jerk, junction deviation, SCV, or speed; most numbers are examples or user-entered tower endpoints.
- No explicit conversion procedure for Klipper rotation distance despite the E-steps procedure noting `M83`; the page is centered on Marlin M92 terminology.
- No independent experimental dataset or uncertainty analysis. Most evidence is procedural guidance, visual inspection, worked examples, and linked videos.
- No claims here that the external video demonstrations, linked firmware documentation, or calculators were independently validated; they are catalogued as supporting links only.

## CITATIONS

Primary source and page-linked resources:

1. Teaching Tech calibration guide: https://teachingtechyt.github.io/calibration.html
2. Teaching Tech calibration companion video (linked from page): https://www.youtube.com/watch?v=rp3r921DBGI
3. Teaching Tech calibration site V2 video (linked from page): https://www.youtube.com/watch?v=9kDK7czgMxc
4. Marlin M303 PID autotune: https://marlinfw.org/docs/gcode/M303.html
5. Marlin M92 steps per unit: https://marlinfw.org/docs/gcode/M092.html
6. Marlin M221 flow override: https://marlinfw.org/docs/gcode/M221.html
7. Marlin M906 motor current: https://marlinfw.org/docs/gcode/M906.html
8. Marlin M204 acceleration: https://marlinfw.org/docs/gcode/M204.html
9. Marlin M205 jerk/junction deviation: https://marlinfw.org/docs/gcode/M205.html
10. Marlin M201 axis acceleration limits: https://marlinfw.org/docs/gcode/M201.html
11. Marlin M203 maximum feedrate: https://marlinfw.org/docs/gcode/M203.html
12. Marlin M900 linear advance K: https://marlinfw.org/docs/gcode/M900.html
13. Marlin Linear Advance Pattern Generator: https://marlinfw.org/tools/lin_advance/k-factor.html
14. Klipper configuration/reference linked by the page: https://www.klipper3d.org/Config_Reference.html
15. RepRapFirmware M205 reference linked by the page: https://duet3d.dozuki.com/Wiki/M205
16. Prusa acceleration calculator linked by the page: https://blog.prusaprinters.org/calculator_3416/
17. Teaching Tech linked test models: `retractiontestv2.stl`, `temperaturetowerv2.stl`, `accelerationtower.stl`, and `speedtower.stl`, all downloadable from the links embedded in the canonical page.

