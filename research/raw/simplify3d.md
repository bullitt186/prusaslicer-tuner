# Simplify3D Print Quality Troubleshooting — source research

## SOURCE_METADATA

- **Publisher:** Simplify3D Software
- **Guide:** Print Quality Guide / Print Quality Troubleshooting Guide
- **Primary index:** <https://www.simplify3d.com/resources/print-quality-troubleshooting/>
- **Accessed:** 2026-10-13
- **Source form:** The index links to one page per symptom. The individual pages expose normal HTML headings, but no dependable section-level fragment IDs were exposed in the retrieved primary content. The “anchors” below therefore use the exact page URL plus the exact section heading (for example, `Common Solutions → Retraction distance`) rather than inventing a fragment URL.
- **Method:** Primary page content inspected directly; thumbnail summaries were used to enumerate coverage, and individual linked troubleshooting pages were read for procedures and limits. Claims are paraphrased.
- **Scope:** The requested symptom families are covered in detail below. The full guide inventory is recorded under COVERAGE.

## COVERAGE

The index covers: Not Extruding at Start of Print; Not Sticking to the Bed; Under-Extrusion; Over-Extrusion; Gaps in Top Layers; Stringing or Oozing; Overheating; Layer Shifting; Layer Separation and Splitting; Grinding Filament; Clogged Extruder; Stops Extruding Mid Print; Weak Infill; Blobs and Zits; Gaps Between Infill and Outline; Curling or Rough Corners; Scars on Top Surface; Gaps in Floor Corners; Lines on the Side of Print; Vibrations and Ringing; Gaps in Thin Walls; Small Features Not Printed; Inconsistent Extrusion; Warping; Poor Surface Above Supports; Dimensional Accuracy; Poor Bridging.

Detailed mappings below cover:

- extrusion quantity: under- and over-extrusion, inconsistent extrusion, startup extrusion, blobs/zits and gaps;
- travel/extrusion defects: stringing, retraction/coasting and travel-path choices;
- thermal and adhesion defects: first layer, overheating, curling, warping, layer bonding and temperature;
- motion defects: layer shifting and ringing;
- geometry/unsupported regions: thin-wall gaps, infill-outline gaps, top-layer gaps, support interfaces, overhangs and bridging.

## CLAIMS

### 1. Under-extrusion

- **Page / anchor:** [Under-Extrusion](https://www.simplify3d.com/resources/print-quality-troubleshooting/under-extrusion/) — `Under-Extrusion`; `Common Solutions → Incorrect filament diameter`; `Common Solutions → Increase the extrusion multiplier`.
- **Condition:** Gaps appear between adjacent extrusions; the guide’s diagnostic is a simple 20 mm-tall cube with at least three perimeter outlines. Inspect the top: gaps between the three perimeters indicate under-extrusion; bonded, touching perimeters suggest a different fault.
- **Evidence A — cause:** The configured filament diameter may not match the real filament. The guide calls out 1.75 mm and 2.85 mm as common nominal diameters.
- **Evidence B — test:** Check the Other tab and verify against the spool; measure the filament with calipers rather than relying only on packaging.
- **Evidence C — correction:** If diameter is correct, select the relevant extruder on the Extruder tab and increase its extrusion multiplier/flow.
- **Evidence D — limit / retest:** The guide gives 1.0 → 1.05 as a 5% increase and recommends reprinting the cube after a 5% increase. It describes PLA as often near 0.9 and ABS as closer to 1.0, but these are typical examples, not universal calibration targets.

### 2. Over-extrusion

- **Page / anchor:** [Over-Extrusion](https://www.simplify3d.com/resources/print-quality-troubleshooting/over-extrusion/) — `Over-Extrusion`; see also [Under-Extrusion](https://www.simplify3d.com/resources/print-quality-troubleshooting/under-extrusion/) — `Common Solutions`.
- **Condition:** Excess plastic makes the print messy and can distort external dimensions.
- **Evidence A — cause:** The printer has no closed-loop measurement of actual nozzle output; incorrect filament diameter or extrusion settings can make actual flow exceed the software’s expectation.
- **Evidence B — test:** Use the same diameter and three-perimeter cube logic as the under-extrusion procedure, while inspecting for excess material and dimensional growth.
- **Evidence C — correction:** Verify filament diameter first; then reduce the extrusion multiplier for the affected extruder. The page explicitly says to apply the under-extrusion settings in the opposite direction.
- **Evidence D — limit:** No independent over-extrusion percentage or dimensional tolerance is supplied; the guide delegates calibration detail to the under-extrusion page.

### 3. Stringing / oozing

- **Page / anchor:** [Stringing or Oozing](https://www.simplify3d.com/resources/print-quality-troubleshooting/stringing-or-oozing/) — `Stringing or Oozing`; `Common Solutions → Retraction distance`; `Retraction speed`; `Temperature is too high`; `Long movements over open spaces`; `Movement Speed`.
- **Condition:** Fine plastic hairs remain between separate printed regions, typically because melt leaks during travel.
- **Evidence A — test:** Confirm retraction is enabled for each extruder. Increase retraction distance by 1 mm and print another test.
- **Evidence B — correction / limit:** Direct-drive extruders are usually described as needing about 0.5–2.0 mm; Bowden systems may need as much as 15 mm. These are starting ranges, not hard machine limits.
- **Evidence C — correction / limit:** Retraction speed has a stated working band of 1200–6000 mm/min (20–100 mm/s). Too slow allows leakage; too fast can separate filament from the melt or grind it.
- **Evidence D — thermal/travel corrections:** If retraction is reasonable, lower nozzle temperature by 5–10 °C. Enable `Avoid crossing outline for travel movement` to shorten or eliminate open-air travel; increasing X/Y travel speed can also reduce ooze time if the machine can safely handle it.

### 4. Warping, curling and rough corners

- **Pages / anchors:** [Warping](https://www.simplify3d.com/resources/print-quality-troubleshooting/warping/) — `Common Solutions → Use a Heated Bed`; `Disable Fan Cooling`; `Use a Heated Enclosure`; `Brims and Rafts`. [Curling or Rough Corners](https://www.simplify3d.com/resources/print-quality-troubleshooting/curling-or-rough-corners/) — `Curling or Rough Corners`.
- **Condition:** Large parts curl or lift, especially high-temperature materials such as ABS; later-print curling is treated as a thermal/cooling symptom.
- **Evidence A — cause/test:** Cooling and shrinkage create a mismatch between the contracting plastic and the comparatively stable build platform. If curling starts later, use the overheating diagnosis; if it starts at the beginning, use the first-layer/bed-adhesion diagnosis.
- **Evidence B — correction:** For ABS-like materials, use a heated bed; the guide gives 100–120 °C as a common ABS bed range. Disable external cooling for ABS when appropriate.
- **Evidence C — correction:** Enclose the printer or use a heated enclosure to keep the whole build volume warm; keep enclosure doors closed during the print.
- **Evidence D — fallback:** Add a brim or raft to hold edges down. The guide does not prescribe a universal brim width, raft size, chamber temperature, or material-specific thermal profile.

### 5. Layer shifting

- **Page / anchor:** [Layer Shifting](https://www.simplify3d.com/resources/print-quality-troubleshooting/layer-shifting/) — `Common Solutions → Toolhead is moving too fast`; `Mechanical or Electrical Issues`.
- **Condition:** Whole layers become laterally misaligned relative to earlier layers.
- **Evidence A — test:** Listen for clicking or missed steps while printing; this indicates the motors cannot achieve the commanded position at the selected speed.
- **Evidence B — correction:** Reduce both `Default Printing Speed` and `X/Y Axis Movement Speed`; the guide recommends trying a 50% reduction. Consider lower firmware acceleration for gentler speed changes.
- **Evidence C — mechanical test:** Check belts for correct tension—loose belts can slip, while over-tight belts can add bearing friction. Check motor-pulley set screws/grub screws for looseness.
- **Evidence D — electrical limits:** Persistent shifts can also come from insufficient motor current or overheating motor drivers. The guide presents these as checks/examples, not a complete electrical diagnostic or numeric current/temperature limit.

### 6. Ringing / vibrations

- **Page / anchor:** [Vibrations and Ringing](https://www.simplify3d.com/resources/print-quality-troubleshooting/vibrations-and-ringing/) — `Common Solutions → Printing too fast`; `Firmware acceleration`; `Mechanical issues`.
- **Condition:** Oscillating echoes or ripples appear on surfaces after rapid direction changes.
- **Evidence A — cause/test:** Excessive speed and abrupt direction changes create inertial force and lingering vibration. Lower both extrusion travel speed (`Default Printing Speed`) and rapid travel (`X/Y Axis Movement Speed`) and compare results.
- **Evidence B — correction:** Reduce firmware acceleration so speed ramps are more gradual.
- **Evidence C — mechanical test:** If software and firmware changes do not resolve it, observe the running printer for loose screws, broken brackets, or another vibration source.
- **Evidence D — limit:** No numeric speed, acceleration, resonance, or vibration threshold is supplied; tuning is iterative and machine-specific.

### 7. Blobs and zits

- **Page / anchor:** [Blobs and Zits](https://www.simplify3d.com/resources/print-quality-troubleshooting/blobs-and-zits/) — `Common Solutions → Retraction and coasting settings`; `Avoid unnecessary retractions`; `Non-stationary retractions`; `Choose the location of your start points`.
- **Condition:** Small isolated surface defects appear at perimeter starts or stops.
- **Evidence A — test:** Watch one perimeter closely. A defect at loop start points to priming/restart; a defect at loop end points to nozzle pressure/coasting.
- **Evidence B — correction / limit:** Reduce restart priming with a negative `Extra Restart Distance`; the guide illustrates 1.0 mm retraction plus −0.2 mm extra restart as 0.8 mm restart priming. For end-of-loop blobs, enable coasting and increase it; 0.2–0.5 mm is described as typically noticeable.
- **Evidence C — correction:** Avoid unnecessary retractions with `Only retract when crossing open spaces` and use `Avoid crossing outline for travel movement` where practical.
- **Evidence D — correction / limit:** For Bowden pressure blobs, enable `Wipe Nozzle`, start with 5 mm `Wipe Distance`, and enable `Perform retraction during wipe movement`. If residual zits remain, choose a fixed or randomized start-point location; no universal XY coordinate is prescribed.

### 8. Gaps in top layers

- **Page / anchor:** [Gaps in Top Layers](https://www.simplify3d.com/resources/print-quality-troubleshooting/gaps-in-top-layers/) — `Common Solutions → Not enough top solid layers`; `Infill percentage is too low`; `Under-Extrusion`.
- **Condition:** Holes remain between extrusions in otherwise solid top skin.
- **Evidence A — cause/test:** A solid skin must bridge hollow infill; too few top layers can sag into infill voids. First increase top solid layers.
- **Evidence B — numerical correction:** The guide’s rule of thumb is a top solid section at least 0.5 mm thick: 0.25 mm layers imply at least 2 solid layers; 0.1 mm layers may need 5. An example change is 3 → 5 top solid layers.
- **Evidence C — correction:** If gaps persist, increase infill because it forms the foundation. The guide illustrates 10% infill as leaving 90% hollow and 30% → 50% as an example increase.
- **Evidence D — diagnosis limit:** If layer count and infill increases do not help, treat it as under-extrusion and run the three-perimeter cube test; there is no universal infill percentage that guarantees a closed top.

### 9. Gaps between infill and outline

- **Page / anchor:** [Gaps Between Infill and Outline](https://www.simplify3d.com/resources/print-quality-troubleshooting/gaps-between-infill-and-outline/) — `Common Solutions → Not enough outline overlap`; `Printing too fast`.
- **Condition:** A visible channel separates perimeter outlines from internal infill.
- **Evidence A — cause/test:** The overlap between infill and the inner perimeter is too small. Check `Outline overlap` in the Infill tab.
- **Evidence B — numerical correction:** The setting is a percentage of extrusion width; the guide’s example is 20% → 30% overlap.
- **Evidence C — cause/test:** Infill may be moving too quickly to bond to the outline. Reduce `Default Printing Speed` and compare.
- **Evidence D — numerical correction/limit:** The guide’s example is 3600 mm/min (60 mm/s) reduced by 50%, then gradually increased until the printer’s best speed is found. No universal final speed is given.

### 10. Thin-wall gaps and inconsistent extrusion

- **Pages / anchors:** [Gaps in Thin Walls](https://www.simplify3d.com/resources/print-quality-troubleshooting/gaps-in-thin-walls/) — `Common Solutions → Adjust the thin wall behavior`; `Change the extrusion width to fit better`. [Inconsistent Extrusion](https://www.simplify3d.com/resources/print-quality-troubleshooting/inconsistent-extrusion/) — `Common Solutions` headings.
- **Condition:** Thin perimeters do not touch, or extrusion varies along the path.
- **Evidence A — thin-wall test/correction:** In Advanced, change `Internal Thin Wall Type` from gap fill to `Allow single extrusion fill` so a dynamically sized single line fills the gap.
- **Evidence B — numerical correction:** For consistent walls, choose a manual extrusion width that fits the geometry; the guide illustrates a 1.0 mm wall with a 0.5 mm extrusion.
- **Evidence C — extrusion-feed tests:** Check that the spool unwinds freely, filament is not tangled, and Bowden tubing is not adding resistance; manually extrude and observe whether the stream is even. Clean the nozzle if it is not.
- **Evidence D — limits/corrections:** Avoid extremely low layer heights such as 0.01 mm; keep extrusion width roughly 100–150% of nozzle diameter. The guide gives 0.2 mm width with a 0.4 mm nozzle as an example that is too narrow. Also test a fresh, dry, high-quality spool and inspect drive-gear tension.

### 11. Poor overhang surface / supports

- **Page / anchor:** [Poor Surface Above Supports](https://www.simplify3d.com/resources/print-quality-troubleshooting/poor-surface-above-supports/) — `Common Solutions → Lower Your Layer Height`; `Support Infill Percentage`; `Vertical Separation Layers`; `Horizontal Part Offset`; `Use a Second Extruder`.
- **Condition:** The underside above support material is rough, droops, or bonds too strongly to the support.
- **Evidence A — overhang test/correction:** Lower layer height to take smaller steps around the overhang. The guide illustrates 0.2 → 0.1 mm and says an example machine may improve from needing support above 45° to performing around 60°; this is printer/material-specific, not a universal overhang limit.
- **Evidence B — support-density correction:** Increase `Support Infill Percentage` if the supported underside droops. A common starting range is 20–40%; dense support structures can concentrate higher density near the interface.
- **Evidence C — separation test/correction:** For same-material supports, use at least 1–2 `Upper Vertical Separation Layers` as a common starting point. Zero layers may bond to the part.
- **Evidence D — horizontal/material correction:** Use 0.2–0.4 mm `Horizontal Offset` as a common range, then tune. With a second material such as dissolvable PVA, the guide says zero vertical separation and about 0.1 mm horizontal offset may be feasible because the materials bond less readily.

### 12. Poor bridging

- **Page / anchor:** [Poor Bridging](https://www.simplify3d.com/resources/print-quality-troubleshooting/poor-bridging/) — `Common Solutions → Verify bridging settings are being used`; `Check the angle used for the bridging infill`; `Adjust settings for optimal performance`; `Use supports for longer bridges`.
- **Condition:** Bridge lines sag, droop, or leave gaps.
- **Evidence A — classification test:** In Preview, choose `Feature Type`; bridging should appear yellow. If not, check `Unsupported area threshold` and ensure the region exceeds that threshold. Optionally enable `Apply bridging settings to perimeters`.
- **Evidence B — direction test/correction:** Confirm the bridge lines run in the span direction. Simplify3D normally computes this automatically; `Use fixed bridging angle` permits an alternate test angle.
- **Evidence C — numerical starting points:** Set `Bridging extrusion multiplier` to 100% or higher; lower values may not seal the underside. Tune `Bridging speed multiplier` experimentally because some machines prefer slow and others fast. Use a high `Bridging fan speed override` for rapid cooling.
- **Evidence D — fallback/limit:** If tuning cannot produce a stable span, add supports. No maximum unsupported bridge length, universal bridge speed, or universal fan percentage is provided.

### 13. First-layer adhesion and startup extrusion

- **Pages / anchors:** [Not Sticking to the Bed](https://www.simplify3d.com/resources/print-quality-troubleshooting/not-sticking-to-the-bed/) — `Common Solutions` headings. [Not Extruding at Start of Print](https://www.simplify3d.com/resources/print-quality-troubleshooting/not-extruding-at-start-of-print/) — `Common Solutions → Extruder was not primed before beginning the print`; `Nozzle starts too close to the bed`; `The filament has stripped against the drive gear`; `The extruder is clogged`.
- **Condition:** First layer fails to adhere, or no plastic exits at the start while later layers may work.
- **Evidence A — bed/nozzle test:** Level the bed first. If the nozzle starts too far away, aim for slight filament squish and use a small negative Z offset; the guide’s example is −0.05 mm. If it starts too close, delayed extrusion for the first 1–2 layers that normalizes around layers 3–4 is the distinguishing symptom; use a small positive Z offset, illustrated as +0.05 mm.
- **Evidence B — speed correction:** Slow the first layer using `First Layer Speed`; 50% is given as an example setting.
- **Evidence C — thermal/surface correction:** The guide gives PLA bed temperature around 60–70 °C and ABS around 100–120 °C as starting points. Disable cooling initially (example: layer 1 at 0%, layer 5 at 100%); for ABS, 0% for the whole print is described as common. Clean the surface with water or isopropyl alcohol and match tape/surface to material.
- **Evidence D — startup extrusion correction:** Prime with a skirt or manual extrusion. If filament shavings/flattened filament are visible, inspect for drive-gear stripping; if priming and Z correction fail, investigate a clogged nozzle and follow the printer maker’s cleaning procedure.

### 14. Temperature and layer bonding

- **Pages / anchors:** [Overheating](https://www.simplify3d.com/resources/print-quality-troubleshooting/overheating/) — `Common Solutions → Insufficient Cooling`; `Printing at too high of a temperature`; `Printing too fast`; `When all else fails: Try printing multiple parts at once`. [Layer Separation and Splitting](https://www.simplify3d.com/resources/print-quality-troubleshooting/layer-separation-and-splitting/) — `Common Solutions → Layer height is too large`; `Print temperature is too low`.
- **Condition:** Small features deform when they stay hot; separate layers crack when they do not bond; temperature must balance flow through the nozzle against rapid solidification.
- **Evidence A — overheating correction:** Increase fan cooling. If that is insufficient, lower nozzle temperature by 5–10 °C, but do not lower it so far that the material cannot pass through the nozzle.
- **Evidence B — cooling-time correction:** For short layers, use Speed Overrides to slow layers taking less than a chosen duration; the guide illustrates a 15-second threshold. Printing multiple copies can create extra cooling time between layers.
- **Evidence C — layer-height test/correction:** Keep layer height about 20% below nozzle diameter as the guide’s rule of thumb. For a 0.4 mm nozzle, it gives about 0.32 mm as the upper example before bonding becomes unreliable.
- **Evidence D — material-temperature correction:** If layer height is acceptable but bonding is weak, increase temperature by 10 °C and retest. The guide uses ABS at 190 °C as too cool and roughly 220–235 °C as a stronger-bond example; these are material examples, not a universal ABS profile.

## PROCEDURES

1. **Extrusion quantity:** Print a 20 mm-tall cube with ≥3 perimeters; inspect the top; verify measured filament diameter; adjust the selected extruder’s multiplier in 5% increments and reprint.
2. **Stringing:** Enable retraction on every extruder; change distance by 1 mm; keep speed in the 20–100 mm/s starting band; lower temperature 5–10 °C if needed; test open-space avoidance and travel speed.
3. **Blobs:** Observe whether each defect is at the start or end of a perimeter. Adjust negative extra restart for starts; enable/increase coasting for ends; then test wipe/retraction-during-wipe and relocate start points.
4. **Top-skin gaps:** Ensure top solid thickness is at least 0.5 mm; increase top layers; increase infill if the skin lacks foundation; then run the under-extrusion test.
5. **Bed adhesion:** Level bed → set nozzle height for slight squish → slow first layer → tune bed temperature/cooling → clean or change surface → add brim/raft.
6. **Warping:** For high-shrink materials, heat the bed, reduce/disable fan, enclose the printer, then add brim/raft if required.
7. **Motion defects:** For shifts or ringing, reduce print and travel speeds; lower firmware acceleration; inspect belts, pulleys, screws, brackets, motor current and driver cooling.
8. **Supports/overhangs:** Lower layer height; increase support density; tune vertical separation and horizontal offset; consider dense interface layers or a soluble/second support material.
9. **Bridges:** Verify yellow bridge classification; check unsupported-area threshold; verify span direction; tune bridge extrusion ≥100%, speed and high cooling; add supports for long/unstable spans.

## NUMERICAL_VALUES

| Topic | Value in guide | Interpretation / limit |
|---|---:|---|
| Under-extrusion test cube | 20 mm tall; ≥3 perimeters | Diagnostic geometry, not a pass/fail dimensional tolerance. |
| Common filament diameters | 1.75 mm; 2.85 mm | Nominal examples; measure actual filament. |
| Multiplier example | 1.00 → 1.05 | 5% more extrusion; guide recommends 5% increments for under-extrusion. |
| Typical multiplier examples | PLA near 0.9; ABS near 1.0 | Typical starting values only. |
| Top solid thickness | ≥0.5 mm | Rule of thumb; 0.25 mm layers → ≥2; 0.1 mm → about 5. |
| Top-layer example | 3 → 5 solid layers | Example retest, not a universal setting. |
| Infill examples | 10% (90% hollow); 30% → 50% | Foundation examples for top skin. |
| Retraction distance | Direct drive 0.5–2.0 mm; Bowden up to 15 mm | Starting ranges; hardware dependent. |
| Retraction speed | 1200–6000 mm/min = 20–100 mm/s | Stated sweet-spot band; material/machine dependent. |
| Stringing temperature adjustment | −5 to −10 °C | Retest after adjustment. |
| Coasting distance | 0.2–0.5 mm | Usually enough to have a noticeable impact. |
| Wipe distance | 5 mm | Suggested starting point for non-stationary retraction. |
| Infill-outline overlap | 20% → 30% example | Percentage of extrusion width. |
| Infill speed test | 3600 mm/min = 60 mm/s; reduce 50% | Then increase gradually. |
| Thin extrusion width | 100–150% of nozzle diameter | Width far below nozzle diameter can destabilize flow; 0.2 mm vs 0.4 mm is the example. |
| Very low layer-height example | 0.01 mm | Presented as too little clearance for consistent extrusion. |
| Nozzle/layer rule | Layer height about 20% below nozzle diameter | 0.4 mm nozzle → about 0.32 mm upper example. |
| Layer-bond temperature test | +10 °C | Retest adhesion; material dependent. |
| ABS bonding example | 190 °C poor; about 220–235 °C stronger | Example range, not universal. |
| Extruder temperature context | 190–310 °C | Broad guide context for extruded plastic, not a recommended setpoint range for every material. |
| First-layer Z-offset examples | −0.05 mm / +0.05 mm | Small illustrative corrections; layer is often about 0.2 mm. |
| First-layer speed example | 50% | Simplify3D percentage example. |
| Bed temperature | PLA 60–70 °C; ABS 100–120 °C | Starting ranges. |
| Fan setpoints example | Layer 1 at 0%; layer 5 at 100% | Example ramp; ABS may use 0% for full print. |
| ABS warping bed | 100–120 °C | Common heated-bed range in warping page. |
| Support density | 20–40% | Common starting range. |
| Same-material support separation | 1–2 upper vertical separation layers | Common starting point. |
| Support horizontal offset | 0.2–0.4 mm | Common range; tune per machine/material. |
| Soluble/second-material support | 0 vertical layers; about 0.1 mm horizontal offset | Often feasible because bonding is reduced. |
| Overhang example | 0.2 → 0.1 mm layers; 45° → around 60° | Illustrative machine-dependent improvement. |
| Bridge extrusion | 100% or more | Lower values may fail to seal the underside. |
| Bridge cooling | High fan override | No universal percentage supplied. |
| Small-layer cooling example | <15 seconds | Speed Override trigger example. |
| Warping example | 100 mm ABS part; 230 °C to 30 °C; almost 1.5 mm shrinkage | Illustrative thermal-shrinkage example, not a general coefficient. |

## CONFLICTS_OR_LIMITS

- **No universal printer profile:** Nearly every numerical value is explicitly or implicitly a starting point/example; the guide repeatedly recommends retesting and tuning for the material and machine.
- **Temperature ranges are contextual:** PLA/ABS bed and nozzle examples should not be transplanted to other polymers. The guide does not provide a complete material table.
- **Speed guidance is relative:** A 50% reduction is a diagnostic experiment, not a recommended final speed. Ringing and shifting pages provide no numeric final speed or acceleration.
- **Overhang angle is not a hard limit:** The 45° and 60° values occur as an example of improved performance after halving layer height, not a guaranteed capability.
- **Bridge settings are under-specified:** The page says bridge extrusion should generally be ≥100% and cooling should be high, but gives no universal bridge speed, fan percentage, or unsupported-span maximum.
- **Extrusion calibration is indirect:** The guide notes that common printers do not measure actual nozzle output, so multiplier and diameter corrections require physical test prints.
- **Anchor limitation:** The site exposes page-level URLs and heading text; stable HTML fragment anchors were not available in the primary retrieval. Use the page URL plus the quoted heading label to locate the passage.
- **Scope limitation:** The guide is a troubleshooting primer, not a controlled calibration standard. It does not define measurement uncertainty, acceptable dimensional error, torque values, belt tension, motor current, driver temperature, or validated material-specific cooling curves.

## GAPS

- No quantitative acceptance criteria for “good” stringing, ringing, bridge sag, support surface roughness, first-layer squish, or dimensional accuracy.
- No universal nozzle-size, material, fan-percentage, chamber-temperature, bridge-length, acceleration, or travel-speed tables.
- No closed-loop extrusion calibration procedure using measured extruder steps or mass/volume; the guide relies on diameter checks, multipliers, and visual test prints.
- No detailed nozzle-cleaning or extruder-disassembly procedure; clogged-extruder content defers to the printer manufacturer.
- No explicit calibration-order decision tree for cases where several symptoms overlap, such as under-extrusion plus top-skin gaps or overheating plus warping.
- No stable section fragments were exposed, so citations should point to the page and exact heading rather than relying on a guessed `#anchor`.

## CITATIONS

1. [Print Quality Guide / thumbnail overview](https://www.simplify3d.com/resources/print-quality-troubleshooting/)
2. [Not Extruding at Start of Print](https://www.simplify3d.com/resources/print-quality-troubleshooting/not-extruding-at-start-of-print/)
3. [Not Sticking to the Bed](https://www.simplify3d.com/resources/print-quality-troubleshooting/not-sticking-to-the-bed/)
4. [Under-Extrusion](https://www.simplify3d.com/resources/print-quality-troubleshooting/under-extrusion/)
5. [Over-Extrusion](https://www.simplify3d.com/resources/print-quality-troubleshooting/over-extrusion/)
6. [Gaps in Top Layers](https://www.simplify3d.com/resources/print-quality-troubleshooting/gaps-in-top-layers/)
7. [Stringing or Oozing](https://www.simplify3d.com/resources/print-quality-troubleshooting/stringing-or-oozing/)
8. [Overheating](https://www.simplify3d.com/resources/print-quality-troubleshooting/overheating/)
9. [Layer Shifting](https://www.simplify3d.com/resources/print-quality-troubleshooting/layer-shifting/)
10. [Layer Separation and Splitting](https://www.simplify3d.com/resources/print-quality-troubleshooting/layer-separation-and-splitting/)
11. [Blobs and Zits](https://www.simplify3d.com/resources/print-quality-troubleshooting/blobs-and-zits/)
12. [Gaps Between Infill and Outline](https://www.simplify3d.com/resources/print-quality-troubleshooting/gaps-between-infill-and-outline/)
13. [Curling or Rough Corners](https://www.simplify3d.com/resources/print-quality-troubleshooting/curling-or-rough-corners/)
14. [Vibrations and Ringing](https://www.simplify3d.com/resources/print-quality-troubleshooting/vibrations-and-ringing/)
15. [Gaps in Thin Walls](https://www.simplify3d.com/resources/print-quality-troubleshooting/gaps-in-thin-walls/)
16. [Inconsistent Extrusion](https://www.simplify3d.com/resources/print-quality-troubleshooting/inconsistent-extrusion/)
17. [Warping](https://www.simplify3d.com/resources/print-quality-troubleshooting/warping/)
18. [Poor Surface Above Supports](https://www.simplify3d.com/resources/print-quality-troubleshooting/poor-surface-above-supports/)
19. [Poor Bridging](https://www.simplify3d.com/resources/print-quality-troubleshooting/poor-bridging/)

