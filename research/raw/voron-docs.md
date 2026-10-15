# Voron Documentation — printer-specific FDM considerations

## SOURCE_METADATA

- **Source set:** Official Voron Documentation at <https://docs.vorondesign.com/>; primary HTML pages and the official model/configuration links exposed by that site. Community how-to pages are identified separately where used.
- **Research date:** 2026-10-13 (Europe/Berlin).
- **Saved report:** `research/raw/voron-docs.md`.
- **Scope:** Mechanical preparation; frame/gantry squaring; belt selection and tension; hotend/extruder; chamber and thermal behavior; calibration; Klipper integration; input shaping; pressure advance; materials; electrical/fire safety.
- **Models covered:** V0/Voron Zero (current V0.2r1), Trident (V1 successor), V2/V2.4 (current V2.4r2 documentation), Switchwire, and Legacy where the official page explicitly distinguishes it. V1/V1.8 is mostly historical, but retained where the docs group it with V2/Legacy or provide V1 wiring/configuration.
- **Evidence grades used below:** **A** = direct statement or executable procedure on an official Voron page; **B** = direct official page that points to another primary technical source/config; **C** = official Voron community how-to, video, or linked community guide; **D** = bounded synthesis/inference from A–C, not a direct Voron specification.
- **Method limit:** I inspected page content rather than search-result snippets. The documentation site links some detail to GitHub manuals, Klipper documentation, YouTube, and community guides; those are not silently treated as equivalent to the official core guidance.

## COVERAGE

| Topic | Official pages inspected | Model scope |
|---|---|---|
| Mechanical assembly, frame, belts, bed | `build/mechanical/` | Universal guidance; explicit V0, Trident, V1, V2, Legacy, Switchwire distinctions |
| V2 gantry squaring | `build/mechanical/v2_gantry_squaring.html` | V2/V2.4 architecture |
| Startup and calibration | `build/startup/startup.html` | Interactive guide branches for V0, Trident, V2, Switchwire, probes, Mainsail/Fluidd/OctoPrint |
| Secondary tuning, belts, mesh, input shaping | `tuning/secondary_printer_tuning.html` | All printers, with Switchwire and Legacy/Trident/V2 branches |
| Filament tuning | `tuning/filament_tuning.html` | General filament workflow; enclosure/PLA caveat |
| Materials | `materials.html` | Printed structural parts; all models, with V2 AB-drive caveat |
| Hardware/extruders | `hardware.html` | V0, Trident, V2 plus Stealthburner/Clockwork2/Galileo/Nightwatch context |
| Klipper/configuration | `build/software/`, `build/software/configuration.html` | All stock Vorons; model-specific config templates |
| Slicer and start sequence | `build/slicer/`, `community/howto/EricZimmerman/SlicerAndPrintStart.html` | General; examples use V2.4/SuperSlicer but principles apply broadly |
| Electrical safety | `build/electrical/` | All printers; extra relevance to mains-powered beds |
| Chamber/exhaust | `sourcing.html`, `community/howto/alchemyEngine/chamber_temperature_exhaust_fan.html` | Enclosed Vorons; community how-to for added chamber sensing/control |

## CLAIMS

### Mechanical preparation and squareness

1. **Build the frame on a genuinely flat reference and verify diagonals.** Voron recommends a granite or similarly flat surface; frame diagonals should differ by less than 2 mm. The docs explicitly reject unnecessary 0.001 mm-level precision. **Conditions:** applies to the general mechanical build, not a substitute for model-specific dimensional checks. **Evidence A:** official mechanical assembly page.
2. **Use correct belt/pulley geometry.** Toothed pulleys should be GT2/2GT; pulleys should not wobble. Genuine Gates GT2/2GT open-loop belts are recommended because generic belts are often wider than 6 mm and can ride up on idler flanges. **Conditions:** open-loop belt systems; exact belt width remains model/configuration dependent. **Evidence A.**
3. **Match belt lengths before tensioning.** A/B belts, or X/Z belts on Switchwire, should be equal length; all V2 Z belts should also match. Leave roughly 1–2 inches of belt for later adjustment/reassembly. **Conditions:** assembly-stage guidance. **Evidence A.**
4. **Square gantries with matched belt tension.** The universal guide explicitly groups V1, V2, and Legacy; it also directs users to measure both diagonals. Trident is not included in that exact sentence because it has a fixed gantry and 3-point moving bed. **Evidence A; model-scope inference D.**
5. **V2 gantry squaring is a mechanical procedure, not merely a QGL command.** Poor squaring can produce first-layer issues, Z-belt rubbing, and front/rear racking. The V2 method disables only A/B motors, fully releases A/B tension, drops lower Z joints, partially loosens extrusion joints, seats the gantry on the lower Z joints, removes racking, retensions, heat-soaks, repeats QGL, then tightens Z-joint M5 hardware hot. **Conditions:** V2/V2.4 four-point moving gantry. **Evidence A.**
6. **Thermally lock the V2 geometry.** After 1.5–2 hours of full heat soak, run QGL 3–5 times, then fully tighten Z-joint M5 bolts while hot; the docs say this helps lock in QGL at expansion and improve stability, ringing, and layer consistency. **Conditions:** V2 procedure; not a universal tightening instruction. **Evidence A.**

### Belts and motion

7. **Nominal tension targets are frequency-based, not torque-based.** For A/B belts, measure a 150 mm span and target approximately 110 Hz; the docs relate this to roughly 2 lb and call it a low-end starting point. For V2 Z belts, 140 Hz is a starting point over the same measurement geometry. Recheck after moving the gantry because belt tensions interact and position affects the reading. **Conditions:** app/frequency method, geometry as specified; not a universal value for every belt or aftermarket design. **Evidence A.**
8. **Over- and under-tension both matter.** The tuning page associates either condition with mechanical issues, premature wear, and print-quality problems. Equalize A/B belts by alternating adjustments. **Evidence A.**
9. **Motion architecture drives the thermal/mechanical advice.** Vorons use CoreXY or CoreXZ, with linear rails or rods depending on model, and 6/9 mm Gates belts. V0 uses 1515 Makerbeam XL; V1/V2/Legacy use 2020 extrusions; Switchwire uses 6030/3030. **Conditions:** family-level architecture, not a substitute for the selected BOM. **Evidence A.**

### Hotend, extruder, and cooling

10. **Keep the heatsink fan active during hotend operation.** Startup verification expects the hotend/heatsink fan to run whenever the hotend is active or above 50 °C; the docs call this essential to avoid clogs. On Stealthburner, the bottom fan is the hotend fan and the top fan is part cooling. **Conditions:** fan placement is toolhead-specific; Stealthburner mapping is explicit. **Evidence A.**
11. **Calibrate extrusion with the hotend at temperature.** Mark filament 120–150 mm from the extruder entrance, extrude 50 mm twice, calculate `rotation_distance` from actual versus target extrusion, and iterate until 100 mm is within 0.5% (99.5–100.5 mm). **Conditions:** Klipper-based direct/bowden extruder calibration; do not confuse this with filament flow/extrusion multiplier. **Evidence A.**
12. **Voron’s current modular toolhead vocabulary matters.** Stealthburner is the interchangeable toolhead system, not the extruder itself; the extruder, hotend-holding toolhead, and cooling assembly are separable. Clockwork2 is the BMG-derived Stealthburner extruder; Mini Stealthburner is the V0.2 integrated direct-drive toolhead; Nightwatch is the smaller Clockwork2 packaging for V0. **Evidence A.**
13. **The official docs provide nominal rotation-distance references for common extruders.** Clockwork1 50:17 and Clockwork2 50:10 are both listed as 22.6789511; Galileo2 9:1 is 47.088; Mobius 3/4 80:20 is 22.6789511. These are starting/configuration references, not permission to skip measured calibration. **Evidence A.**

### Chamber and thermal behavior

14. **Enclosed Vorons commonly reach 55–60 °C chamber temperature.** Printed-part material should therefore have a thermal deformation/glass-transition temperature of at least 80 °C. The docs also state a chamber heater is not necessary for ABS/common materials. **Conditions:** common enclosed operation; actual temperature depends on enclosure, bed, ambient, and exhaust. **Evidence A.**
15. **Heat soak changes geometry enough to affect first layers and meshes.** The slicer guide recommends at least 10 minutes of preheat/soak for thermal equilibrium and reports a 350³ V2 growing 0.2 mm in height after one hour. The tuning guide explains that Legacy, Trident, and V2 gantries/frames expand and rail-bearing extrusions bend slightly, so a mesh can change with bed/chamber/frame temperature. **Evidence A.**
16. **Mesh strategy differs by model.** Switchwire commonly needs a mesh because of its thinner bed and must not use `relative_reference_index` because its probe is a virtual endstop. Legacy, Trident, and V2 commonly benefit from a mesh because of thermal deformation; current guidance recommends generating it before every print after homing/leveling rather than relying on a saved mesh. **Evidence A.**
17. **Exotic high-chamber materials are outside the stock design envelope.** Voron states typical chambers do not exceed 50–60 °C and warns that PEEK/PEI-class 100–130 °C chambers can fail printed parts, steppers, belts, bearings, probes, panels, fans, and other components. **Conditions:** stock Voron architecture; modified industrial-style systems are outside scope. **Evidence A.**

### Calibration and Klipper integration

18. **All stock Vorons use Klipper with a Raspberry Pi-class host and one or more controller boards.** The official recommendation is Mainsail or Fluidd; OctoPrint is supported but less specific to Klipper, and Pi Zero users are directed to Mainsail/Fluidd. **Evidence A.**
19. **Model-specific `printer.cfg` templates are the starting point, not the finished configuration.** Required edits include MCU paths, thermistor types, stepper/endstop/max-position settings, bed-screw/tilt/QGL coordinates, and Z-endstop location. Klipper is case-sensitive. **Conditions:** hardware and probe variants must be reconciled against the chosen model template. **Evidence A.**
20. **The standard startup sequence validates sensors, heaters, fans, motors, homing, probes, thermal leveling, PID, Z offset, and extrusion.** The page insists on `RESTART` after config changes and `STATUS` checks; it also calls for emergency-stop readiness during motion/homing checks. **Evidence A.**
21. **V2 uses `QUAD_GANTRY_LEVEL`; Trident uses `Z_TILT_ADJUST`.** Each probes multiple points and iterates motor positions; the V2 guidance says adjustment values should converge toward zero, and divergence suggests wiring/driver mapping problems. **Evidence A.**
22. **Probe accuracy is a gate for thermal leveling.** The startup guide uses 10 probes and considers standard deviation above 0.003 mm or a trend over the ten samples unstable; wait another five minutes and retry. For hot V2 QGL, use bed 100 °C and nozzle 150 °C, then record stabilization time (often 10–20 minutes from cold). **Conditions:** explicit startup examples, not a universal physical accuracy guarantee. **Evidence A.**
23. **Input shaping is officially recommended as a Klipper technique for reducing ringing.** The Voron tuning page points to Klipper for the complete measurement/configuration process rather than prescribing one fixed shaper or frequency. **Conditions:** values are printer/toolhead-specific and must be measured or otherwise tuned. **Evidence A/B.**
24. **Pressure Advance is part of filament tuning, not a one-time printer constant.** Voron places it alongside temperature, extrusion rate, and cooling, and says filament tuning should be repeated for each brand/type and potentially each color because pigment can affect behavior. The concise official page links/labels the topic but does not publish a universal PA value or complete test recipe. **Evidence A; limit noted under GAPS.**
25. **The slicer must hand thermal and material parameters into the Klipper start macro correctly.** Official examples pass bed, extruder, chamber, size, and material values to `PRINT_START`; some slicers may emit duplicate `M190`/`M109` heating before the macro if they do not recognize it. **Conditions:** exact placeholder syntax varies by slicer; example page uses SuperSlicer and V2.4. **Evidence A/C.**

### Materials and safety

26. **ABS is the primary recommended structural print material; ASA is supported.** PLA and PETG are discouraged for structural Voron parts due to temperature tolerance and/or cracking risk, though both are acceptable for skirts and panel clips. PA6 is discouraged for creep; PA12 is viable but expensive; PC/PC blends are generally discouraged for sudden cracking, with limited toolhead exceptions. Resin is strongly discouraged. **Evidence A.**
27. **V2 AB drive parts need material that tolerates some flex.** Four-point gantry misalignment can flex those units; a very stiff material is not automatically safer. **Conditions:** V2-specific. **Evidence A.**
28. **Electrical work is a fire and shock hazard.** Disconnect mains power and allow PSU capacitors to discharge; never plug/unplug powered devices, especially stepper motors. Use appropriately sized AC wiring (at least 18 AWG/0.75 mm²; 16 AWG/1.25 mm² preferred), a quality SSR, a 115–125 °C bed thermal fuse, bed/frame grounding, and do not run the bed above 110 °C. **Conditions:** mains-bed and general electrical recommendations; local electrical code still governs. **Evidence A.**
29. **Keep heated/electrical risk out of the print chamber where possible.** The official About page calls for a deck plate or electronics separate from the chamber and managed cabling. The wiring guide specifies flexible, heat-tolerant cable and warns that motor/probe leads not rated for repeated cable-chain bending should be terminated before the chain. **Evidence A.**

## PROCEDURES

### Recommended build-to-first-print sequence

1. Select the exact model/revision and use its official BOM/configuration; do not use the non-customized sourcing guide as a quantity authority.
2. Print structural parts in ABS/ASA with the official part settings; reserve PLA/PETG for low-load, cooler parts such as skirts/clips.
3. Square the frame on a flat surface; compare diagonals (<2 mm difference). Verify pulleys, belt paths, equal belt lengths, and leave belt tails for adjustment.
4. Assemble the model-specific motion system. For V2, leave Z-joint hardware sufficiently loose for QGL until the dedicated squaring procedure is complete.
5. Wire with power removed; verify thermistors read plausibly before energizing heaters, then test each heater, fan, motor, endstop, and probe. Keep an emergency stop available for all first motions.
6. Load the matching Klipper template and correct MCU paths, sensors, motor/endstop geometry, bed leveling coordinates, and Z-endstop/probe choice. `RESTART`, then `STATUS` after every config change.
7. Home and level using the model’s mechanism: QGL for V2; Z tilt for Trident; follow the model branch for V0, Switchwire, and Legacy.
8. Heat soak before final thermal leveling/mesh. Use probe-accuracy checks; retry if readings trend or exceed the official 0.003 mm standard-deviation criterion.
9. PID-tune bed and hotend for the actual hardware: the startup examples use bed 100 °C and hotend 245 °C with part cooling at 25%.
10. Calibrate Z offset/probe, then extruder rotation distance with hot filament and a 100 mm target; require 0.5% or better before moving on.
11. Tune belt tension: A/B approximately 110 Hz over 150 mm; V2 Z approximately 140 Hz. For V2, complete the hot squaring/retightening sequence and repeat QGL.
12. Configure/generate a thermally appropriate bed mesh. For Legacy/Trident/V2, prefer a fresh mesh after the start sequence’s homing/leveling and heat-up; for Switchwire do not use `relative_reference_index`.
13. Tune filament temperature, extrusion rate, cooling, pressure advance, and retraction per filament brand/type/color as applicable. Tune input shaping for the actual toolhead/frame.
14. Use a known-good slicer profile and ensure only one coherent heating/start sequence is active. First-print starting example for ABS: 240 °C hotend, 100 °C bed, 92% flow; treat these as a starting point, not a final profile.

### V2 gantry-squaring procedure (official order)

1. Set `SET_IDLE_TIMEOUT TIMEOUT=99999`; home with `G28`; run `QUAD_GANTRY_LEVEL`.
2. Move the gantry to the center; disable only `stepper_x` and `stepper_y`; fully release A/B belt tension.
3. Remove side panels; drop the lower Z joints; work on a reasonably level surface.
4. Partially loosen X/Y joints, A/B joints, and front idlers—never loosen Z-belt clamps enough to release belts.
5. Seat the gantry flush on the lower Z joints and ensure the joint bolts slide cleanly without side interference; avoid rotating A/B joints.
6. Retighten extrusion bolts except X/Y joints; reinstall lower Z joints only lightly; derack the gantry.
7. Retension A/B belts to approximately 110 Hz over 150 mm.
8. Reinstall panels; heat soak 1.5–2 hours; run QGL 3–5 times; then fully tighten Z-joint M5 bolts while hot; `RESTART` to restore the idle timeout.

## NUMERICAL_VALUES

| Value | Use | Scope/qualification |
|---|---|---|
| <2 mm diagonal difference | Frame squareness check | General mechanical build |
| 6 mm / 9 mm belts | Motion-system family sizes | Model/configuration dependent |
| ~110 Hz over 150 mm | A/B belt tension | General A/B guidance; V2 squaring explicitly uses it |
| ~2 lb | Approximate tension corresponding to 110 Hz | Lower-end starting point, not a torque spec |
| ~140 Hz over 150 mm | V2 Z-belt starting tension | V2 only |
| 55–60 °C | Common enclosed chamber temperature | Enclosure/ambient/bed dependent |
| ≥80 °C | Minimum recommended printed-part thermal deformation/glass temperature | Structural printed parts |
| 90–100 °C | ABS glass-transition range | Material guide estimate |
| 70–80 °C | PETG and PA6/PA12 glass-transition range | Material guide estimate |
| 110–130 °C | PC/PC-blend glass-temperature range | Material guide estimate |
| 1.5–2 h | Full V2 heat soak during gantry squaring | V2 procedure |
| ≥10 min | Recommended general preheat/heat-soak minimum | Slicer/startup guidance; larger rigs may need longer |
| 0.2 mm | Height expansion observed on a 350³ V2 after 1 h heating | Reported test observation, not universal constant |
| 100 °C bed / 150 °C nozzle | Hot V2 probe/QGL stabilization example | Startup guide |
| 0.003 mm | Probe-accuracy standard-deviation threshold | Startup guide criterion |
| 10 probes | Probe-accuracy sample count | Startup guide |
| 10–20 min | Typical cold-to-stable time noted for hot leveling | Printer/environment dependent |
| 100 °C bed PID target | Example bed PID calibration | Startup guide |
| 245 °C hotend PID target | Example hotend PID calibration | Startup guide |
| 25% / `M106 S64` | Part-cooling setting during hotend PID | Startup guide |
| 120–150 mm | Filament mark distance for extrusion calibration | Startup guide |
| 100 mm | Extrusion calibration target, in two 50 mm moves | Klipper extrusion limit in guide |
| ±0.5% | Acceptable extrusion calibration result | 99.5–100.5 mm |
| 240 °C / 100 °C / 92% | ABS first-print starting example | First print page; not a universal final profile |
| 115–125 °C | Recommended bed thermal-fuse range | Electrical safety |
| 110 °C maximum | Bed operating ceiling in safety guidance | Adhesive-lifespan warning |
| ≥18 AWG (0.75 mm²), preferably 16 AWG (1.25 mm²) | AC wiring size | Electrical safety; follow local code |
| 5 A | MicroFit 3.0 connector rating stated | Connector recommendation |
| 22.6789511 / 47.088 | Listed extruder rotation distances | Starting references for named extruders |

## CONFLICTS_OR_LIMITS

- **Heat-soak duration is context-dependent:** the general slicer page says at least 10 minutes is highly recommended; V2 gantry squaring requires 1.5–2 hours; startup notes cold printers often need 10–20 minutes to stabilize for leveling. These are different procedures, not contradictory universal timers.
- **Chamber-temperature ceiling varies by wording:** materials guidance says enclosed printers commonly reach 55–60 °C; sourcing guidance says typical chambers generally do not exceed 50–60 °C. Treat both as an approximate stock-design range, not a controlled chamber specification.
- **Mesh reference method changed:** current tuning guidance assumes modern Klipper and `ZERO_REFERENCE_POSITION`; the separate `relative_reference_index.html` page is explicitly obsolete. Switchwire remains the exception that should not use relative reference indexing.
- **Model names/revisions are uneven:** current mechanical links identify V0.2r1 and V2.4r2, while configuration links label V2.4 and retain historical V1.8. Always align the manual, CAD/STLs, and config revision to the physical build.
- **Official versus community material:** the core docs are official Voron pages. The `PRINT_START` deep-dive, chamber thermistor/exhaust implementation, and some linked video procedures are official-site community documentation; they should be treated as implementation examples, not universal Voron specifications.
- **Frequency tension is a starting target:** belt construction, span geometry, temperature, measurement app, and printer modifications can change the relation between Hz and force. The docs provide a practical start point, not a precision-certified tension standard.
- **Slicer examples are not a complete PrusaSlicer profile:** official docs list PrusaSlicer as supported, but the detailed macro example uses SuperSlicer/V2.4 syntax. Placeholder names and duplicate-heating behavior must be checked in the actual generated G-code.

## GAPS

- The official Voron `Filament Tuning` page labels Pressure Advance but does not expose a complete PA test procedure or a universal starting range; it points users toward broader tuning resources.
- The official Voron tuning page identifies Input Shaper and links to Klipper for the complete process but does not publish a self-contained accelerometer wiring, resonance-sweep, shaper-selection, or frequency table.
- No universal hotend/nozzle/heater-cartridge specification is given in the inspected core pages; hardware choice is delegated to the selected model/toolhead manual and BOM.
- No universal chamber-control policy exists for PLA/PETG beyond the warning that some enclosed setups need doors open, exhaust running, or panels removed; actual exhaust thresholds and sensor placement are configuration-specific.
- Mechanical maintenance intervals, lubrication choices, and belt replacement intervals were not detailed in the inspected pages; the site has a separate Maintenance Guide that would need a dedicated pass.
- Safety guidance is practical rather than a substitute for local electrical code, enclosure ventilation requirements, material SDS review, or fire-detection policy.

## CITATIONS

1. [Voron Documentation home](https://docs.vorondesign.com/)
2. [Mechanical Assembly](https://docs.vorondesign.com/build/mechanical/)
3. [V2 Gantry Squaring](https://docs.vorondesign.com/build/mechanical/v2_gantry_squaring.html)
4. [Initial Startup Guide](https://docs.vorondesign.com/build/startup/startup.html)
5. [Secondary Printer Tuning](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html)
6. [Filament Tuning](https://docs.vorondesign.com/tuning/filament_tuning.html)
7. [Materials Selection](https://docs.vorondesign.com/materials.html)
8. [Choosing a Printer / Extruder](https://docs.vorondesign.com/hardware.html)
9. [Electrical Wiring](https://docs.vorondesign.com/build/electrical/)
10. [Software Installation](https://docs.vorondesign.com/build/software/)
11. [Software Configuration](https://docs.vorondesign.com/build/software/configuration.html)
12. [Slicer Setup](https://docs.vorondesign.com/build/slicer/)
13. [First Print](https://docs.vorondesign.com/build/slicer/first_print.html)
14. [About Voron](https://docs.vorondesign.com/about.html)
15. [Sourcing Information](https://docs.vorondesign.com/sourcing.html)
16. [Using Slicers and PRINT_START macros](https://docs.vorondesign.com/community/howto/EricZimmerman/SlicerAndPrintStart.html)
17. [Chamber Temperature & Exhaust Fan](https://docs.vorondesign.com/community/howto/alchemyEngine/chamber_temperature_exhaust_fan.html)
18. [Obsolete Bed Mesh with Relative Reference Index](https://docs.vorondesign.com/tuning/relative_reference_index.html)

