---
type: index
title: 3D printing tuning knowledge library
description: OKF v0.2 bundle — topic-oriented FDM/FFF knowledge, procedures, defects and materials mapped to PrusaSlicer and Klipper concepts.
okf_version: "0.2"
tags: [index, 3d-printing, prusaslicer, klipper]
generated:
  by: process:prusaslicer-tuner-maintenance
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: okf-spec
    title: Google Open Knowledge Format specification
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
---
# 3D printing knowledge library (OKF v0.2)

Each doc is one topic-oriented concept. New and maintained documents use OKF v0.2 provenance (`sources`, `generated`, and `status`); older v0.1 documents remain readable and are reported by the validator for later migration. Inline footnotes map substantive claims to source IDs. Evidence labels are repository conventions in prose: A = specification or reproducible measurement, B = official technical documentation/engineering analysis, C = repeated community observation, D = anecdote or unverified recommendation. A label is not a substitute for inspecting the cited source.

Read this index, then open only the docs you need.

Entry points: a visible problem → [diagnostic matrix](troubleshooting/diagnostic-matrix.md); setting up a printer or filament → [tuning order](tuning/tuning-order.md); a profile key → [profile knowledge map](slicer/profile-knowledge-map.md). Every topic ends with a generated **Relations** block (typed edges in both directions: caused by / causes, fixed by / fixes, prone to / affects, calibrates). Agents with MCP should use `lookup` and `card` instead of reading docs; the model is described in [knowledge maintenance](maintenance.md).

The catalog below is generated from each doc's frontmatter by `uv run kg.py fix`. Do not edit it by hand.

<!-- generated:catalog -->
## Diagnosis (start here for a symptom)
- [FDM print defect diagnostic matrix](troubleshooting/diagnostic-matrix.md): A symptom-first diagnostic workflow that separates material, hardware, slicer and firmware hypotheses before changing settings.

## Problems (defects)
- [Bulging](defects/bulging.md): Plastic pushed outward from perimeters — layers, sharp corners, around features, above overhangs.
- [Dimensional inaccuracy](defects/dimensional-inaccuracy.md): Printed parts are larger or smaller than designed.
- [Elephant foot](defects/elephant-foot.md): Bottom layers flare outward beyond the wall line.
- [Extruder skipping / clicking](defects/extruder-skipping.md): Wide periodic gaps, clicking extruder; clogs, heat creep, tension, flow above limit, current.
- [Extrusion patterns ("wood grain")](defects/extrusion-patterns.md): Repeating innie-outie texture along lines, often from extruder gear backlash.
- [Extrusion stops mid-print](defects/extrusion-stops.md): The print continues moving but no plastic comes out.
- [First layer inconsistency](defects/first-layer-inconsistency.md): Squish varies across the bed or between prints.
- [Gaps between infill and walls](defects/infill-wall-gaps.md): Infill does not fuse to the innermost perimeter.
- [Gaps or pillowing in top layers](defects/top-surface-gaps.md): Top surfaces show holes, bumps or gaps where solid layers sag into the infill.
- [Inconsistent extrusion](defects/inconsistent-extrusion.md): Line width varies along a single straight extrusion.
- [Infill visible through walls](defects/infill-visible-through-walls.md): The infill pattern shows through the outer walls.
- [Layer shifting](defects/layer-shift.md): Horizontal offset between layers — belts, nozzle strikes on curled parts, current, drivers, too much accel.
- [Lines or ridges on the sides (Z banding)](defects/z-banding.md): Individual layers stand out as lines, often in a repeating pattern.
- [Model errors (non-manifold geometry)](defects/model-errors.md): Sections are missing or the print differs from the model although the printer works.
- [No extrusion at print start](defects/no-extrusion-at-start.md): Nothing or too little comes out during the first moves or layers.
- [Over-extrusion](defects/over-extrusion.md): Rough/ridged top surfaces, blobby small areas, dimensional oversize, nozzle dragging through top layers.
- [Overheating (esp. PLA in enclosures)](defects/overheating.md): Droopy/melted small features, curled overhangs, heat creep jams with PLA in a closed printer.
- [Perimeter separation](defects/perimeter-separation.md): Walls not bonding to each other or layer below — lower layers (elephant foot comp) or everywhere (width, speed, temp).
- [Pockmarks](defects/pockmarks.md): Small pits on walls — random seam, wet filament, bad nozzle.
- [Poor bed adhesion](defects/poor-bed-adhesion.md): Prints don't stick, corners lift, parts pop off mid-print.
- [Poor bridges & overhangs](defects/bridging-overhangs.md): Sagging bridges, curled/droopy overhangs.
- [Poor layer adhesion](defects/poor-layer-adhesion.md): Layers split under modest force because interlayer bonding is weaker than the applied load or because the process is inconsistent.
- [Poor surface above or below supports](defects/support-surface-quality.md): Surfaces resting on supports droop, or supports leave scars when removed.
- [Print stuck to the bed](defects/part-stuck-to-bed.md): The finished part will not release from the build plate.
- [Ringing / ghosting](defects/ringing.md): Echo ripples after sharp corners or features on walls.
- [Scars on top surfaces](defects/top-surface-scars.md): Travel moves leave marks across top layers.
- [Small infill areas look overextruded](defects/small-infill-overextruded.md): Blobby short top-infill segments in small islands; partly normal.
- [Stringing / oozing](defects/stringing.md): Thin strings or wisps between separate parts of a print. Usually moisture, temperature, PA or retraction — in that rough order.
- [Supports fail during the print](defects/supports-fail.md): Support structures crack, wobble or detach before the overhang is printed.
- [Thin walls and small features missing](defects/thin-walls-and-small-features.md): Thin walls get gaps in the middle or small features do not print.
- [Under-extrusion](defects/under-extrusion.md): Gaps between lines, thin/weak walls, missing layers, holes in top surfaces.
- [VFAs (vertical fine artifacts)](defects/vfas.md): Fine vertical lines on walls — belts/pulleys/idlers (2 mm spacing) or bearings/rails/motor drivers.
- [Warping / corner lifting](defects/warping.md): Corners curl up during print, mainly ABS/ASA/PC/nylon; shrinkage stress beats adhesion.
- [Weak or messy infill](defects/weak-infill.md): Infill is stringy, incomplete or fails to support the surfaces above.
- [Zits, blobs & visible seam](defects/zits-blobs.md): Small bumps on walls, usually at layer starts/seams or retraction points.

## Causes
- [Acceleration or corner velocity too high](causes/acceleration-too-high.md): High accelerations excite resonances, cause bulging at corners and can skip steps.
- [Adhesion too strong](causes/adhesion-too-strong.md): Large contact areas, glue build-up or materials like PETG on smooth PEI bond too well.
- [Bed not level or mesh missing](causes/bed-not-level-or-unmeshed.md): Nozzle height varies across the bed when the gantry is racked or no heat-soaked mesh is used.
- [Bed temperature too high](causes/bed-temp-too-high.md): Lower layers stay soft and sag under the weight of the part.
- [Bed temperature too low](causes/bed-temp-too-low.md): The first layer does not stay soft enough to bond and contracts early.
- [Belt or pulley tooth artifacts](causes/belt-or-pulley-artifacts.md): Belt, pulley or idler teeth print as fine vertical lines at about the tooth pitch (≈2 mm).
- [Binding or worn bearings, rails or motors](causes/worn-or-binding-motion-parts.md): Rough bearings, rails or motors add periodic artifacts and resistance that can skip steps.
- [Bridge flow or speed wrong](causes/bridge-flow-or-speed-wrong.md): Bridge flow above 100 % sags and bulges the layers above; too fast bridges droop.
- [Brittle filament snaps](causes/brittle-filament.md): Old, sun-exposed or cheap filament becomes brittle and snaps in the feed path, often unseen in a Bowden tube.
- [Broken (non-manifold) model](causes/non-manifold-mesh.md): Intersecting or open meshes slice into missing or wrong regions.
- [Chamber too cold for the material](causes/chamber-too-cold.md): Shrinking materials (ABS, ASA, PC, PA) build stress against a cool chamber and lift or crack.
- [Chamber too hot for the material](causes/chamber-too-hot-for-material.md): Low-temperature materials like PLA soften and heat-creep in a closed, warm chamber.
- [Contaminated build surface](causes/contaminated-build-surface.md): Skin oils and residue block adhesion.
- [Elephant-foot compensation too high](causes/elephant-foot-compensation-too-high.md): Over-compensation pulls bottom perimeters apart.
- [External perimeter too narrow](causes/external-perimeter-too-narrow.md): With layer heights above about half the nozzle size, a narrow outer line cannot reach the neighbouring perimeter.
- [Extruder gear backlash, play or wear](causes/extruder-gear-backlash-or-wear.md): A dead zone on reversal or worn/eccentric gears makes extrusion uneven: repeating texture, inconsistent PA and stringing.
- [Extruder motor current wrong](causes/extruder-motor-current.md): Too little current loses steps under load; too much overheats the motor and softens the filament.
- [Extruder not calibrated](causes/extruder-not-calibrated.md): The extruder moves a different length than commanded, so every flow value is scaled wrong.
- [Extruder not primed](causes/extruder-not-primed.md): During heat-up the nozzle oozes empty, so the first moves extrude nothing until pressure rebuilds.
- [Extrusion multiplier too high](causes/em-too-high.md): More plastic than the line volume: ridged top surfaces, oversize parts, pushed-out perimeters and extra ooze.
- [Extrusion multiplier too low](causes/em-too-low.md): Less plastic than the line volume: gaps between lines, thin walls and weak bonding everywhere at all speeds.
- [Filament tension or path drag](causes/filament-tension-or-drag.md): Too much or too little idler tension, a tangled or binding spool or a tight PTFE path makes feeding inconsistent.
- [First layer printed too fast](causes/first-layer-too-fast.md): A fast first layer gets too little time to bond to the build surface.
- [First-layer lines too thin](causes/first-layer-lines-too-thin.md): Narrow first-layer lines have little contact area.
- [Frame thermal drift](causes/frame-thermal-drift.md): Frame and gantry expand during the first hour of chamber heating and shift Z.
- [Heat creep](causes/heat-creep.md): Heat rises past the heatbreak, filament softens early and jams; typical for PLA in a warm enclosure or a weak hotend fan.
- [Hotend temperature fluctuation](causes/temperature-fluctuation.md): A poorly tuned PID loop swings the nozzle temperature cyclically, changing flow layer by layer.
- [Infill lines too thin](causes/infill-line-too-thin.md): Thin infill lines make weak infill walls; wider lines are stronger at the same density.
- [Infill printed too fast](causes/infill-too-fast.md): Infill usually runs fastest; when the extruder cannot keep up it under-extrudes and fails to bond.
- [Infill too sparse](causes/infill-too-sparse.md): Low infill density leaves wide air gaps for top layers and corners to span.
- [Infill/perimeter overlap wrong](causes/infill-overlap-wrong.md): Too much overlap pushes walls out; too little leaves pinholes where infill meets perimeters.
- [Insufficient part cooling](causes/insufficient-cooling.md): Plastic stays soft: sagging bridges, curled overhangs, melted small features.
- [Layer height too large for the nozzle](causes/layer-height-too-large.md): Each layer must be pressed onto the one below; above about 80 % of the nozzle diameter it is not.
- [Layer height too small](causes/layer-height-too-small.md): A tiny gap under the nozzle restricts flow and makes extrusion uneven.
- [Layer time too short](causes/layer-time-too-short.md): Small layers are printed before the previous one has solidified.
- [Load along layer lines (orientation)](causes/load-along-layer-lines.md): FDM parts are weakest across layers; loads that pull layers apart fail regardless of tuning.
- [Loose belts, pulleys or toolhead parts](causes/loose-mechanics.md): Slack belts, loose pulley grub screws or loose toolhead parts let the toolhead lag or slip.
- [Material shrinkage stress](causes/material-shrinkage.md): Cooling plastic contracts; in high-shrink materials the stress beats bed adhesion at sharp corners.
- [No elephant-foot compensation](causes/elephant-foot-compensation-missing.md): Some first-layer flare is inherent; without compensation the bottom stays wider than the wall.
- [No z-hop over printed surfaces](causes/no-z-hop.md): Without a small lift the nozzle drags across finished top layers during travel.
- [Nozzle hits curled print](causes/nozzle-strike-on-curled-part.md): Curled overhangs or warped corners catch the nozzle, knocking the toolhead or part.
- [Nozzle temperature too high](causes/nozzle-temp-too-high.md): Low melt viscosity lets plastic ooze during travel and small features stay soft.
- [Nozzle temperature too low](causes/nozzle-temp-too-low.md): Plastic that is too cold flows poorly and bonds weakly to the previous layer or perimeter; at high flow it can make the extruder skip.
- [Nozzle too close to the bed](causes/z-offset-too-low.md): Over-squished first layer: flare, rough surface, the extruder struggles on the first layer.
- [Nozzle too far from the bed](causes/z-offset-too-high.md): First-layer lines are round and barely touch: poor adhesion, gaps in the second layer, separated bottom perimeters.
- [Nozzle too large for the detail](causes/nozzle-too-large-for-detail.md): Features smaller than the nozzle cannot be reproduced in XY.
- [Out of filament](causes/out-of-filament.md): The spool ran out or the filament end left the extruder.
- [Overhangs printed too fast](causes/overhang-too-fast.md): Fast overhangs do not get enough time to cool.
- [Partial clog](causes/partial-clog.md): A restricted nozzle or heatbreak limits flow; the extruder skips and extrusion is thin or stops.
- [Perimeter order pushes walls out](causes/perimeter-order.md): Printing inner walls first lets them push the outer wall outward.
- [Poor or degraded filament](causes/poor-filament-quality.md): Diameter variation, additives or aged material change the extruded volume from layer to layer.
- [Pressure advance smoothing too long](causes/pa-smooth-time-too-high.md): Klipper smooths PA over a time window; on short top-infill segments a long window leaves excess pressure.
- [Pressure advance too high](causes/pa-too-high.md): Pressure is pulled too early: gaps at line starts, thin corners and under-extruded starts.
- [Pressure advance too low](causes/pa-too-low.md): Nozzle pressure lags the toolhead: corners bulge, line ends blob and residual pressure oozes on travel.
- [Print speed too high](causes/print-speed-too-high.md): High feature speeds raise flow demand, vibration and bonding time pressure.
- [Random seam placement](causes/seam-random.md): Each layer starts at a new spot, leaving start/stop pits all over the walls.
- [Resonance not compensated](causes/resonance-uncompensated.md): Frame and toolhead resonances echo after sharp features when input shaping is missing or stale.
- [Retraction too long or too fast](causes/retraction-excessive.md): Long or fast retractions grind filament, pull molten plastic into the cold zone and jam soft filaments like TPU.
- [Retraction too short or too slow](causes/retraction-insufficient.md): Pressure is not relieved before travel, so the nozzle oozes between islands.
- [Seam start/stop pressure](causes/seam-start-stop-pressure.md): Pressure at loop starts and ends leaves a zit; extra restart or no wipe makes it worse.
- [Sheet not seated flat](causes/sheet-not-seated.md): Debris under the flex sheet creates a local bump.
- [Shrinkage not compensated](causes/shrinkage-uncompensated.md): Constant errors need an XY offset; errors that grow with part size are shrinkage and need scaling.
- [Small contact area](causes/small-contact-area.md): Small or sharp-cornered footprints have too little area to resist lifting forces.
- [Small top islands (inherent)](causes/small-island-geometry.md): Short top-infill segments always look slightly overextruded; partly normal.
- [Stepper driver or wiring fault](causes/stepper-driver-or-wiring.md): Intermittent wiring, poor crimps or overheating drivers lose steps on motion axes or the extruder.
- [Stepper driver tuning artifacts](causes/stepper-driver-tuning.md): Driver chopper settings can add fine periodic wall artifacts on X/Y. Community values are experimental.
- [Support interface or gap wrong](causes/support-interface-settings.md): Too little gap welds supports to the part; too much or too sparse a top lets the surface droop.
- [Supports too weak](causes/support-too-weak.md): Sparse or tall supports wobble, crack or detach mid-print.
- [Too few perimeters](causes/too-few-perimeters.md): Thin shells let infill show through and give step-downs a weak foundation.
- [Too few top solid layers](causes/top-layers-insufficient.md): Top solid layers must bridge the infill gaps; a thin top sags into them.
- [Too much part cooling](causes/excessive-cooling.md): Strong cooling freezes the line before it fuses: weak layers, perimeter separation and warping in shrinking materials.
- [Travel crosses open air](causes/travel-over-open-space.md): Every travel over empty space is a chance to ooze. Avoiding it only works inside one island; between separate islands the nozzle must cross air.
- [Travel moves too slow](causes/travel-too-slow.md): Slow travel gives the nozzle more time to ooze over open space.
- [Unnecessary retractions](causes/too-many-retractions.md): Every retract/prime cycle risks a zit; retracting on moves that never cross open space adds defects for nothing.
- [Unsuitable build surface](causes/unsuitable-build-surface.md): Fake or worn PEI, the wrong side of the sheet or a surface that does not suit the material.
- [Unsupported overhang or bridge](causes/missing-supports.md): Overhangs and long bridges beyond the printer's ability need support or redesign.
- [Volumetric flow above the hotend limit](causes/volumetric-flow-exceeded.md): Speed asks for more mm³/s than the hotend can melt: under-extrusion on fast sections, skipping and weak layers.
- [Wall thinner than the extrusion width](causes/wall-thinner-than-line-width.md): Walls only a few line widths thick leave gaps, or vanish below one line width.
- [Wet filament](causes/wet-filament.md): Absorbed water boils in the nozzle: popping, steam, ooze, rough walls and weak layers. Common with PETG, nylon, TPU and PC; new spools can be wet too.
- [Worn, dirty or leaking nozzle](causes/nozzle-worn-or-leaking.md): A worn bore, debris or a nozzle that is not hot-tightened changes flow and leaks plastic.
- [Wrong filament diameter setting](causes/wrong-filament-diameter.md): The slicer computes volume from the configured diameter; a mismatch scales all extrusion.
- [Z-hop too high](causes/zhop-too-high.md): A high lift gives the nozzle time and height to drag a string on every travel.

## Procedures (tuning)
- [Build surface prep & handling](tuning/build-surface.md): Wash plates with dish soap, air dry, don't touch; scuff smooth PEI.
- [Calibration matrix and dependency order](tuning/calibration-matrix.md): A context-preserving calibration sequence that separates machine, firmware, material and slicer variables.
- [Cooling and layer times](tuning/cooling-layer-times.md): Enough part cooling plus a minimum layer time so each layer solidifies before the next.
- [Extruder calibration (rotation_distance / e-steps)](tuning/extruder-calibration.md): Make 100 mm commanded equal 100 mm extruded; per-printer firmware value, not a slicer setting.
- [Extrusion multiplier (flow)](tuning/extrusion-multiplier.md): Per-filament flow tuned visually on top surfaces of 30x30x3 cubes; 2% then 0.5% steps.
- [First layer squish (Z offset)](tuning/first-layer-squish.md): Fine-tune nozzle-to-bed distance live with 0.01 mm babysteps using scattered test patches.
- [Infill/perimeter overlap](tuning/infill-perimeter-overlap.md): Pinholes where top infill meets perimeters after EM/PA are tuned — adjust overlap.
- [Input shaping](tuning/input-shaping.md): Reduce ringing by measuring printer resonances and selecting a shaper while controlling smoothing and acceleration.
- [Max volumetric flow](tuning/max-volumetric-flow.md): Find how many mm³/s the hotend can melt; cap it per filament so speed never outruns the hotend.
- [Pressure advance / Linear advance](tuning/pressure-advance.md): Compensates extruder pressure lag on accel/decel; fixes corner bulges and line-start gaps. Per filament and per printer.
- [Retraction](tuning/retraction.md): Tune retraction length/speed only after PA, EM, moisture and mechanics are ruled out; small values for direct drive.
- [Temperature tuning](tuning/temperature-tuning.md): Establish a material- and hardware-specific temperature window before optimizing cooling, flow or retraction.
- [Thermal drift (enclosed Klipper printers)](tuning/thermal-drift.md): Frame/gantry expansion shifts Z during the first ~hour of chamber heating; heat soak or compensate.
- [Tuning order](tuning/tuning-order.md): The order in which to calibrate a printer/filament so later steps aren't invalidated by earlier ones.

## Materials
- [ABS / ASA](materials/asa-abs.md): Needs enclosure & heat soak; warps; surprisingly high fan OK in a hot chamber.
- [Engineering materials and reinforced filaments](materials/engineering-materials.md): Engineering polymers and fiber-filled filaments require product-specific drying, thermal, nozzle and chamber conditions; datasheet values are test-condition values.
- [Filament drying and moisture](materials/filament-moisture.md): Moisture changes extrusion behavior and surface quality; drying must follow the polymer and product's validated limits.
- [Nylon (PA)](materials/nylon.md): Extremely hygroscopic, warps, needs dry box during printing.
- [PC / PC-CF](materials/pc-cf.md): High temp, abrasive (CF → hardened nozzle), enclosure, warps; temperature trades stringing against surface and layer bonding; brand-specific EM.
- [PETG](materials/petg.md): Stringy, hygroscopic, sticks too well to smooth PEI; moderate cooling.
- [PLA](materials/pla.md): Easy, low-temp, loves cooling; overheats in enclosures.
- [TPU (flexible)](materials/tpu.md): Slow, low retraction, very hygroscopic; direct drive strongly preferred.

## Slicer
- [PrusaSlicer profile to knowledge map](slicer/profile-knowledge-map.md): Map observable print symptoms and tuning concepts to effective PrusaSlicer profile keys, authority boundaries and diagnostic knowledge topics.
- [Slicer flow, width and firmware output](slicer/flow-width-and-gcode.md): PrusaSlicer and OrcaSlicer derive extrusion geometry and firmware commands from nozzle, layer, width, material and firmware context; profile values are not portable defaults.

## Fundamentals
- [Layer height and extrusion width](fundamentals/layer-height-extrusion-width.md): Layer height and line width trade vertical detail, XY resolution, bonding, throughput and machine limits.

## Hardware
- [Nozzle selection](hardware/nozzle-selection.md): Select nozzle diameter, geometry and material for the required detail, throughput, wear resistance and polymer.
- [Voron thermal and motion mechanics](hardware/voron-thermal-mechanics.md): Voron calibration must account for model-specific gantry architecture, belt tension, heat soak, chamber temperature and Klipper procedures.

## Firmware
- [Current Klipper calibration and compatibility notes](firmware/klipper-current.md): Klipper firmware state is versioned and authoritative for pressure advance, input shaping, extrusion calibration, retraction and motion limits.
- [Klipper operating boundaries](firmware/klipper-operating-boundaries.md): Keep Klipper motion, extrusion and calibration limits consistent with slicer output and distinguish firmware state from profile settings.

## Mechanical properties
- [Mechanical strength and test interpretation](mechanical-properties/strength-and-testing.md): FDM mechanical performance depends on orientation, process history, geometry and conditioning; strength claims need reproducible test context.
- [Part orientation and anisotropy](mechanical-properties/part-orientation.md): FDM parts are direction-dependent because layer interfaces and raster paths create anisotropic strength and failure modes.

## Bundle maintenance
- [Knowledge maintenance](maintenance.md): Repository rules for evidence, provenance, context, cross-links and validation of the FDM/FFF knowledge bundle.
<!-- /generated:catalog -->

## Adding or changing a topic
See [knowledge maintenance](maintenance.md) for the full rules and `schema.yaml` for the vocabulary. In short:
1. Prefer enriching an existing concept: a new `caused_by`/`fixed_by` edge with a `source`, or an `altLabel` (English and German), before creating a file.
2. A new problem needs ranked `caused_by` edges; a new cause needs a `check` and `fixed_by` (procedure, `sets` keys with direction, or a physical `action`).
3. Cite with `sources` + footnotes; put evidence (A–D) on edges.
4. Run `uv run kg.py fix`: it regenerates this catalog, Relations blocks, views and `graph.json`, and refuses to write anything while errors exist. The pre-commit hook runs the check.
5. Append a line to [log.md](log.md).

Candidate sources: Prusa Knowledge Base (help.prusa3d.com), Klipper docs (klipper3d.org), Teaching Tech calibration, PrusaSlicer config reference.
