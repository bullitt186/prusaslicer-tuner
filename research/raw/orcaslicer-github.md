# OrcaSlicer GitHub source research

## SOURCE_METADATA

- **Source:** [SoftFever/OrcaSlicer](https://github.com/SoftFever/OrcaSlicer)
- **Branch/revision inspected:** `main` at commit `869e450981bb8bece1622ef3fd55381962af11b3` (HEAD observed 2026-10-13; commit subject: “Keep Per-Nozzle Values When a User Preset Syncs Through the Cloud (#16355)”).
- **Revision link:** [869e450 full commit](https://github.com/SoftFever/OrcaSlicer/commit/869e450981bb8bece1622ef3fd55381962af11b3)
- **Primary material inspected:** `src/slic3r/GUI/calib_dlg.cpp`, `src/slic3r/GUI/NativeCommands.cpp`, `src/libslic3r/PrintConfig.cpp`, `src/libslic3r/GCodeWriter.cpp`, `src/libslic3r/calib.cpp`, `src/libslic3r/GCode.cpp`, `src/libslic3r/GCode/AdaptivePAProcessor.cpp`, and bundled JSON under `resources/profiles/`.
- **Method:** shallow clone at the pinned commit; source and profile inspection; no reliance on search-result snippets. Wiki URLs were checked where the application exposes them, but the repository source was treated as authoritative for behavior and defaults.
- **Interpretation:** “OrcaSlicer supports X” means the inspected revision has a config key, generator, emitter, or bundled profile for X. It does not mean every printer/firmware combination supports it safely.

## COVERAGE

| Area | Finding | Primary evidence |
|---|---|---|
| Calibration workflows | Dedicated GUI actions and generators for temperature, max volumetric speed, pressure advance, flow ratio, retraction, cornering, VFA, and input-shaping frequency/damping | `NativeCommands.cpp`; `calib_dlg.cpp`; `calib.cpp` |
| Pressure advance | Static PA/Linear Advance, per-filament/per-extruder values, adaptive PA model, feature-specific overhang/bridge handling, visualization | `PrintConfig.cpp`; `GCodeWriter.cpp`; `AdaptivePAProcessor.cpp`; `GCodeViewer.cpp` |
| Flow ratio | Filament flow ratio plus print flow ratio; calibration has coarse/fine/YOLO modes and Archimedean/monotonic patterns | `PrintConfig.cpp`; `calib_dlg.cpp` |
| Max volumetric speed | Filament-level melt/extrusion ceiling; calibration tower with configurable start/end/step | `PrintConfig.cpp`; `calib_dlg.cpp` |
| Temperature | Material-family selector, start/end/step tower, nozzle-diameter model scaling, belt-printer overhang model | `calib_dlg.cpp` |
| Retraction | Retraction tower, independent length sweep, normal slicer retraction, wipe and firmware-retraction controls | `calib_dlg.cpp`; `PrintConfig.cpp` |
| Input shaping | Frequency and damping towers; Klipper, RepRapFirmware, Marlin 2 emission; explicit firmware-version notes | `calib_dlg.cpp`; `GCodeWriter.cpp`; `PrintConfig.cpp` |
| Overhang/cooling | Overhang detection/speed tiers, curl slowdown, overhang fan threshold/speed, bridge/internal-bridge fan controls, layer-cooling slowdown | `PrintConfig.cpp`; process/filament profiles |
| Supports | Normal/tree auto/manual modes, build-plate-only and critical-region filters, small-overhang suppression, top/bottom Z gaps, support filament selection | `PrintConfig.cpp` |
| Seams | Nearest/aligned/aligned-back/back/random, seam gap, staggered inner seams, scarf seam beta controls | `PrintConfig.cpp`; bundled process profiles |
| Profiles/printer-specific features | Inheritance-based machine/process/filament JSON, explicit Klipper/Marlin/RRF/Repetier flavors, per-nozzle/per-extruder values, Bambu/AMS and other vendor-specific extensions | `resources/profiles/`; `PrintConfig.cpp`; current commit |

## CLAIMS

### 1. OrcaSlicer has a first-class, menu-addressable calibration suite

**Condition:** A user runs a calibration from the OrcaSlicer Calibration menu/native command layer.

**Claim:** The current source exposes temperature, max volumetric speed, pressure advance, flow ratio, retraction, cornering, VFA, and two input-shaping tests. These are not merely profile fields: each action dispatches to a calibration mode and a dedicated test generator.

- **Evidence A — UI dispatch:** `src/slic3r/GUI/NativeCommands.cpp` registers all named calibration actions; `MainFrame.cpp` adds them to the calibration menu.
- **Evidence B — dialog parameters:** `src/slic3r/GUI/calib_dlg.cpp` defines the input ranges/defaults and maps each dialog to `m_plater->calib_*`.
- **Evidence C — generators:** `src/libslic3r/calib.cpp` contains PA line/pattern generation and related calibration geometry; `GCode.cpp` integrates calibration modes into output.
- **Evidence D — application links:** dialogs expose Orca’s first-party wiki guides for temperature, volumetric speed, retraction, flow ratio, and input shaping, e.g. [temperature calibration](https://www.orcaslicer.com/wiki/temp_calib/) and [input-shaping calibration](https://www.orcaslicer.com/wiki/input_shaping_calib/).

### 2. Pressure advance is firmware-flavor aware and materially broader than a single static value

**Condition:** `enable_pressure_advance` is enabled for the relevant filament/extruder column.

**Claim:** OrcaSlicer treats the configured factor as Klipper Pressure Advance or Marlin Linear Advance, emits firmware-specific commands, and can replace the static value with an adaptive model keyed by volumetric flow and acceleration. Adaptive PA can also react to overhang/feature flow changes and use a bridge-specific fallback.

- **Evidence A — config semantics:** `PrintConfig.cpp` defines `enable_pressure_advance`, `pressure_advance` (default `0.02`, max `2`), `adaptive_pressure_advance`, a multiline triplet model, `adaptive_pressure_advance_overhangs`, and bridge PA.
- **Evidence B — emitter:** `GCodeWriter.cpp::set_pressure_advance()` emits Klipper `SET_PRESSURE_ADVANCE ADVANCE=...`, Marlin `M900 K...`, RRF `M572 D... S...`, and Repetier `M233 X... Y...`; Bambu-specific output uses `M900 ... L1000 M10`.
- **Evidence C — processor:** `AdaptivePAProcessor.cpp` interpolates PA from flow/acceleration and falls back to the static value when the model is absent/invalid; `GCode.cpp` applies PA at filament/extruder changes and layer/feature transitions.
- **Evidence D — explicit warning:** the config tooltip says adaptive PA within features is experimental and “not compatible with Prusa printers” because their PA changes pause for processing; the same source recommends a reasonable static fallback for tool changes.

### 3. Orca’s flow-ratio model has two multiplicative layers

**Condition:** A filament and print preset both contain flow-ratio values.

**Claim:** `filament_flow_ratio` applies a filament-wide extrusion multiplier and `print_flow_ratio` is a quality/print-level multiplier; the final object flow ratio is their product. The filament setting’s source guidance calls `0.95–1.05` a recommended range, not a hard limit.

- **Evidence A:** `PrintConfig.cpp` defines filament flow ratio with range `0–2`, nullable storage, and the recommended `0.95–1.05` interval.
- **Evidence B:** the same file defines `print_flow_ratio` with `0.01–2` and explicitly documents multiplication with filament flow ratio.
- **Evidence C:** `FlowRateCalibrationDialog` offers Pass 1 coarse, Pass 2 fine, YOLO recommended, and YOLO perfectionist; generated tests can use Archimedean Chords or Monotonic top-surface patterns.
- **Evidence D:** bundled filament JSON files serialize flow-ratio values per material and often per nozzle/extruder variant, demonstrating that profile inheritance/variant expansion is part of the operational model.

### 4. Max volumetric speed is a filament melt-cap and can clamp requested speed

**Condition:** The requested line speed would exceed the active filament’s `filament_max_volumetric_speed`.

**Claim:** Orca limits print speed to the filament volumetric ceiling. The calibration dialog creates a tower over a volumetric-speed range; other calibration logic explicitly accounts for the ceiling when a requested tower speed would otherwise be clamped.

- **Evidence A:** `PrintConfig.cpp` defines the setting in `mm³/s`, with default `2`, minimum `0`, and a tooltip describing it as the volume melted/extruded per second.
- **Evidence B:** `calib_dlg.cpp` defaults the test to start `5`, end `20`, step `0.5 mm³/s`, and rejects non-positive start/step or an end not greater than start plus step.
- **Evidence C:** VFA calibration code reads the active filament max volumetric speed and can auto-adjust layer height or lower the requested end speed to stay within the ceiling.
- **Evidence D:** Orca’s app links a dedicated [volumetric-speed calibration guide](https://www.orcaslicer.com/wiki/volumetric_speed_calib/); profile JSONs store the cap as a filament property rather than a universal printer constant.

### 5. Temperature calibration is material-family and printer-model aware

**Condition:** The user chooses a filament family and optionally a belt printer.

**Claim:** The temperature tower supports PLA, ABS/ASA, PETG, PCTG, TPU, PA-CF, PET-CF, and Custom. Defaults are a `230→190 °C` sweep in `5 °C` increments; inputs are normalized in `5 °C` increments and validated against the supported range. Belt printers additionally expose Standard versus Overhang tower geometry.

- **Evidence A:** `Temp_Calibration_Dlg` in `calib_dlg.cpp` defines the material-family radio group and the belt-only model selector.
- **Evidence B:** the dialog defaults start `230 °C`, end `190 °C`, step `5 °C`, and has a “resize model to nozzle diameter” option.
- **Evidence C:** validation clamps input to the source’s stated supported range (`170–500 °C` in the message) and rounds to `5 °C`; source-level code also rejects values below its internal lower guard.
- **Evidence D:** the dialog links the [temperature calibration guide](https://www.orcaslicer.com/wiki/temp_calib/). This is a calibration generator, not a material safety guarantee; actual ranges remain printer/filament dependent.

### 6. Retraction is a tower workflow, but firmware retraction is a separate advanced mode

**Condition:** The printer uses slicer-generated retraction or explicitly supports firmware retraction.

**Claim:** The retraction tower defaults to `0→2 mm` in `0.1 mm` steps and produces a retraction calibration mode. Normal retraction is a per-extruder distance setting; Orca also exposes wipe sequencing, layer-change retraction, long cut retractions, and an experimental Marlin-only firmware retraction switch.

- **Evidence A:** `Retraction_Test_Dlg` defines start `0`, end `2`, step `0.1 mm`, validates the sweep, and invokes `Calib_Retraction_tower`.
- **Evidence B:** `PrintConfig.cpp` defines `retraction_length` default `0.8 mm`, wipe-before/after percentages, `retract_when_changing_layer`, and long-retraction/cut options.
- **Evidence C:** `use_firmware_retraction` explicitly says it uses G10/G11 and is only supported in recent Marlin.
- **Evidence D:** the dialog links Orca’s [retraction calibration guide](https://www.orcaslicer.com/wiki/retraction_calib/); no source evidence says the tower automatically writes the selected value back to every affected filament variant.

### 7. Input shaping combines calibration towers with firmware command emission

**Condition:** The printer firmware supports the selected input-shaping command family and the user enables emission.

**Claim:** Orca has frequency and damping tests. Frequency defaults are `15→110 Hz`; frequency is bounded below `0` and above `500 Hz` for the calibration dialog. Damping is tested over a `0–1` ratio range. The slicer can emit Klipper `SET_INPUT_SHAPER`, RRF/Marlin 2 `M593`, or reject legacy Marlin/unsupported flavors.

- **Evidence A:** `Input_Shaping_Freq_Test_Dlg` and `Input_Shaping_Damp_Test_Dlg` define tower models, shaper type selection, frequency and damping inputs.
- **Evidence B:** frequency calibration defaults to X/Y `15–110 Hz` and damping `0.15`; damping calibration validates start/end within `0–1`. RRF uses one frequency range for both axes.
- **Evidence C:** `GCodeWriter.cpp::set_input_shaping()` emits firmware-specific commands; `PrintConfig.cpp` defines shaper types including MZV, ZV, ZVD, EI variants, DAA, and Disable, with X/Y frequency max `1000 Hz` and damping max `1` for normal config fields.
- **Evidence D:** the dialog warns about firmware versions: Klipper `0.9.0`, Marlin `2.1.2`, and RRF `3.4.0` in the UI text. Legacy Marlin below 2.1.2 is explicitly rejected by the emitter.

### 8. Overhang and cooling are separate but interacting controls

**Condition:** Overhang detection/speed and cooling controls are enabled in the active process/filament profiles.

**Claim:** Orca can detect overhang walls, slow overhang perimeters through four percentage tiers, force overhang cooling above a threshold, slow curled perimeters, slow short layers, and separately control support-interface, internal-bridge, ironing, auxiliary, and minimum non-zero fan behavior.

- **Evidence A:** `PrintConfig.cpp` defines `enable_overhang_speed`, four overhang speed fields, `overhang_fan_speed`, and `overhang_fan_threshold`.
- **Evidence B:** the same source documents curl slowdown and its interaction with PA smooth time, minimum speeds, and extrusion-rate smoothing; it notes that bridge-like overhangs may receive overhang slowdown when curl protection is enabled.
- **Evidence C:** filament profiles serialize `overhang_fan_speed`, `overhang_fan_threshold`, `fan_cooling_layer_time`, `slow_down_for_layer_cooling`, and auxiliary cooling values; process profiles serialize overhang speed tiers and detection.
- **Evidence D:** this is richer than a single “fan speed” knob, but a profile may override/disable each branch; inspect the resolved inherited preset before assuming a field is active.

### 9. Supports and seams have Orca-specific policy knobs beyond the basic PrusaSlicer model

**Condition:** The active process preset enables supports or seam controls.

**Claim:** Supports include normal/tree and auto/manual modes, build-plate-only generation, critical-region-only generation, small-overhang suppression, independent top/bottom Z gaps, and support-material assignment. Seams include five base positions, seam gap, staggered inner seams, and scarf-joint beta options.

- **Evidence A:** `PrintConfig.cpp` defines support mode enum values `normal(auto)`, `tree(auto)`, `normal(manual)`, `tree(manual)` and explains auto/manual semantics.
- **Evidence B:** support fields include `support_on_build_plate_only`, `support_critical_regions_only`, `support_remove_small_overhang` (default true), `support_top_z_distance` and `support_bottom_z_distance` (both default `0.2 mm`), and `support_filament`.
- **Evidence C:** seam fields include `nearest`, `aligned`, `aligned_back`, `back`, and `random`, plus `seam_gap` default `10%`, staggered inner seams, and scarf-joint beta settings.
- **Evidence D:** bundled process JSON confirms these are used in real vendor presets rather than only declared in the schema; values vary by printer/material profile.

### 10. Profiles are inheritance- and variant-driven, with printer-specific behavior encoded in JSON

**Condition:** A user selects a vendor machine/process/filament preset or a custom profile inheriting from a common base.

**Claim:** Orca’s bundled profiles separate machine, process, and filament data, use `inherits`, encode nozzle/extruder variants, and set firmware flavor explicitly. The repository includes common Klipper bases plus Marlin, RepRapFirmware, Repetier, belt, toolchanger, and vendor-specific profiles.

- **Evidence A:** `resources/profiles/*/machine`, `process`, and `filament` contain layered JSON; examples include `Custom/machine/fdm_klipper_common.json`, `Creality/process/fdm_process_common_klipper.json`, and vendor-specific machine/process bases.
- **Evidence B:** common Klipper profiles set `gcode_flavor: klipper`; other common profiles set `marlin`, `reprapfirmware`, or `repetier`, which drives command generation.
- **Evidence C:** current commit code specifically addresses preserving per-nozzle values during cloud preset sync, confirming that nozzle/variant scoping is operationally significant.
- **Evidence D:** source lists many Orca/Bambu extensions and fields in addition to the Prusa-origin baseline; a direct INI key-for-key import is therefore unsafe without resolving inheritance and firmware semantics.

## PROCEDURES

1. **Identify the resolved machine, process, and filament preset.** Record firmware flavor, nozzle diameter, extruder index, active filament variant, max volumetric speed, PA enable/value, input-shaper emission, and support/seam/cooling overrides. Do not infer these from a parent JSON alone; resolve `inherits` and variant columns.
2. **Temperature:** choose the material family; start from the default `230→190 °C`, `5 °C` step, then adjust to the filament’s safe range. For belt printers choose Standard or Overhang geometry. Select the coolest region that still gives adhesion, surface quality, and overhang strength; update the filament preset manually.
3. **Flow ratio:** run the default YOLO Recommended first; use coarse/fine passes when the result is ambiguous. Keep the print-level flow ratio separate from the filament flow ratio. Apply the selected result to the correct filament/nozzle variant and validate with a flat-top or dimensional part.
4. **Max volumetric speed:** run a tower over a range appropriate to the hotend/nozzle, starting from the UI default `5–20 mm³/s` at `0.5 mm³/s` steps only when that range is plausible. Choose the highest region without under-extrusion, then leave headroom and ensure process speeds do not conceal the cap.
5. **Pressure advance:** calibrate with the active firmware flavor and correct tool. For static PA, choose the cleanest corner/line transition and set `enable_pressure_advance` plus `pressure_advance`. For adaptive PA, collect at least three flow speeds per acceleration value, covering external, internal, and fastest infill speeds; keep the acceleration range within the input-shaper-recommended maximum. Validate bridges/overhangs separately before enabling feature-adaptive PA.
6. **Retraction:** run the tower with the actual hotend path, temperature, and travel settings. Start with `0–2 mm`/`0.1 mm` only for a direct-drive-like range; Bowden or unusual paths need a different range. If using firmware retraction, confirm firmware support and avoid mixing slicer and firmware distance ownership.
7. **Input shaping:** run frequency first, then damping if the firmware requires it. Use the firmware-specific shaper set and confirm emitted commands are accepted. Store X/Y frequencies and damping in the printer profile; do not enable slicer emission when firmware is already authoritative unless the override is intentional.
8. **Overhang/cooling:** tune overhang speeds and overhang fan threshold together. Check short-layer slowdown and curl protection after PA and volumetric limits are stable, because speed changes alter extrusion dynamics.
9. **Supports/seams:** choose auto/manual and normal/tree based on geometry; validate top/bottom Z gaps and support-interface fan with the actual material. Tune seam position/gap/scarf only after wall flow and PA are stable.
10. **Cross-slicer export:** map concepts, not names. Validate generated G-code on a short test object, especially PA, input shaping, firmware retraction, adaptive PA, and vendor-specific start/end/tool-change code.

## NUMERICAL_VALUES

| Feature | Source value / constraint | Meaning |
|---|---:|---|
| Flow ratio | Filament default `1.0`; hard `0–2`; recommended `0.95–1.05` | Filament extrusion multiplier |
| Print flow ratio | Default `1.0`; `0.01–2` | Multiplies filament flow ratio |
| Static PA | Default `0.02`; max `2` | Klipper PA / Marlin LA factor |
| Max volumetric speed | Default `2 mm³/s`; calibration defaults `5→20` by `0.5 mm³/s` | Filament melt/extrusion ceiling |
| Temperature tower | Default `230→190 °C`, `5 °C` step | UI defaults; safe range remains material/printer-specific |
| Retraction tower | Default `0→2 mm`, `0.1 mm` step | UI defaults, not universal Bowden/direct-drive limits |
| Input-shaping frequency tower | Default `15→110 Hz`; calibration upper bound `500 Hz` | X/Y sweep; RRF uses one range |
| Input-shaping damping | Frequency-test default `0.15`; valid `0–1` | Damping/zeta ratio |
| Config input-shaper frequencies | `0–1000 Hz` | Normal profile-field bounds |
| Config input-shaper damping | `0–1`; default `0.1` per axis | Normal profile-field bounds/default |
| Support Z gaps | Top and bottom default `0.2 mm` | Object/support separation |
| Seam gap | Default `10%` | Closed-loop seam interruption; may also be mm |
| Overhang reversal threshold | Default `50%`; max literal `20 mm` | Overhang reversal trigger |
| Extrusion-rate smoothing | Default `0`; example high-flow recommendation `300–350 mm³/s²`; slower direct drive `10–15`, Bowden `5–10` | Rate-change limiter; not the same as max volumetric speed |

## CONFLICTS_OR_LIMITS

### OrcaSlicer versus PrusaSlicer

- **Naming/semantics:** Orca calls the filament multiplier `filament_flow_ratio` and also has `print_flow_ratio`; do not blindly map either to a single PrusaSlicer extrusion multiplier.
- **Pressure advance:** Orca’s PA field explicitly unifies Klipper PA and Marlin Linear Advance and adds adaptive PA. PrusaSlicer’s closest related concept is Pressure Equalizer/extrusion-rate smoothing, not an equivalent adaptive PA model. Orca’s own tooltip says feature-adaptive PA is not compatible with Prusa printers because PA changes can cause processing pauses/defects.
- **Extrusion-rate smoothing:** Orca names the feature `max_volumetric_extrusion_rate_slope` and explicitly calls it “Pressure Equalizer in Prusa slicer”; transfer requires unit/value review and arc-fitting review.
- **Input shaping:** Orca emits firmware commands and has a broad shaper enum; Prusa profiles/firmware may already own shaping. Enabling both can cause command precedence or duplicated control.
- **Supports/seams/overhangs:** Orca adds tree/manual variants, critical-region and small-overhang filters, seam scarf controls, overhang reversal, curl slowdown, and multiple cooling branches. These are not guaranteed to exist under the same names or with the same defaults in PrusaSlicer.
- **Profiles:** Orca’s machine/process/filament inheritance and per-nozzle/per-extruder columns are not equivalent to a flat PrusaSlicer INI export. Resolve the profile first, then map only supported keys.

### OrcaSlicer versus Klipper

- **PA command ownership:** Orca emits `SET_PRESSURE_ADVANCE`; Klipper must support the command and the selected extruder name. Orca maps tool `0` to `extruder` and later tools to `extruder1`, etc.; custom Klipper extruder names or macros need review.
- **Input shaper ownership:** Orca emits `SET_INPUT_SHAPER` only when input-shaping emission is enabled. Klipper’s saved/configured shaper can otherwise remain authoritative; “Default” and zero frequency intentionally defer to firmware values.
- **Firmware version/type:** The UI notes Klipper `0.9.0` for the calibration workflow and offers shaper types that may not exist on every deployed Klipper build. Confirm supported `SHAPER_TYPE`/parameters before printing.
- **Adaptive PA:** Orca’s adaptive processor injects changing PA commands based on its own model. This is distinct from Klipper’s firmware-side behavior/macros; do not enable competing PA automation without understanding which layer owns the value.
- **Pressure-advance smooth time:** Orca’s overhang/curl guidance refers to Klipper PA smooth time and suggests `0.015–0.02` when aggressive slowdown creates artifacts, but this is advice in a tooltip, not an enforced Klipper setting.
- **Retraction:** Orca’s normal slicer retraction is not Klipper firmware retraction. If Klipper macros handle retraction, avoid double application and check start/end/tool-change G-code.
- **Max volumetric speed:** Orca limits requested G-code speed before Klipper; Klipper does not make an Orca filament melt limit physically true. The value still needs empirical validation for hotend, nozzle, temperature, and material.

### General limits

- Calibration dialogs mostly generate test G-code; source does not prove automatic, safe write-back to every affected preset variant.
- Defaults are UI defaults, not material recommendations. They can be inappropriate for high-flow hotends, Bowden paths, belt printers, high-temperature polymers, or unusual nozzles.
- Vendor profiles contain device-specific start/end/tool-change code and may rely on proprietary commands or hardware. A generic Klipper mapping is not sufficient for Bambu/vendor profiles.
- The inspected revision is a moving `main` snapshot. Pin the commit above when reproducing findings.

## GAPS

- The repository delegates detailed operator-facing explanations to hosted Orca wiki pages; the inspected GitHub tree contains the links and implementation, but not a complete, versioned calibration manual.
- No exhaustive machine-by-machine inventory was attempted; bundled profiles are numerous and continuously changing. The report establishes the schema and representative Klipper/Marlin/RRF/Repetier patterns.
- No hardware print tests were performed, so recommended operating values remain source defaults/constraints, not validated settings for the prusaslicer-tuner target printer.
- Exact resolved values depend on preset inheritance, extruder/nozzle column, and selected vendor profile. A future integration should parse the effective profile graph rather than scrape one JSON file.
- Conflict statements compare Orca source semantics with the PrusaSlicer terminology explicitly referenced by Orca. A full PrusaSlicer revision-by-revision diff would require pinning and inspecting a separate PrusaSlicer commit.

## CITATIONS

- [OrcaSlicer pinned commit](https://github.com/SoftFever/OrcaSlicer/commit/869e450981bb8bece1622ef3fd55381962af11b3)
- [Calibration command registration](https://github.com/SoftFever/OrcaSlicer/blob/869e450981bb8bece1622ef3fd55381962af11b3/src/slic3r/GUI/NativeCommands.cpp)
- [Calibration dialogs and UI defaults](https://github.com/SoftFever/OrcaSlicer/blob/869e450981bb8bece1622ef3fd55381962af11b3/src/slic3r/GUI/calib_dlg.cpp)
- [Configuration definitions and tooltips](https://github.com/SoftFever/OrcaSlicer/blob/869e450981bb8bece1622ef3fd55381962af11b3/src/libslic3r/PrintConfig.cpp)
- [Firmware-specific PA and input-shaping emitters](https://github.com/SoftFever/OrcaSlicer/blob/869e450981bb8bece1622ef3fd55381962af11b3/src/libslic3r/GCodeWriter.cpp)
- [PA calibration geometry](https://github.com/SoftFever/OrcaSlicer/blob/869e450981bb8bece1622ef3fd55381962af11b3/src/libslic3r/calib.cpp)
- [G-code integration and adaptive PA](https://github.com/SoftFever/OrcaSlicer/blob/869e450981bb8bece1622ef3fd55381962af11b3/src/libslic3r/GCode.cpp)
- [Adaptive PA processor](https://github.com/SoftFever/OrcaSlicer/blob/869e450981bb8bece1622ef3fd55381962af11b3/src/libslic3r/GCode/AdaptivePAProcessor.cpp)
- [Bundled printer/process/filament profiles](https://github.com/SoftFever/OrcaSlicer/tree/869e450981bb8bece1622ef3fd55381962af11b3/resources/profiles)
- [Orca temperature calibration guide](https://www.orcaslicer.com/wiki/temp_calib/)
- [Orca flow-ratio calibration guide](https://www.orcaslicer.com/wiki/flow_ratio_calib/)
- [Orca max-volumetric-speed calibration guide](https://www.orcaslicer.com/wiki/volumetric_speed_calib/)
- [Orca retraction calibration guide](https://www.orcaslicer.com/wiki/retraction_calib/)
- [Orca input-shaping calibration guide](https://www.orcaslicer.com/wiki/input_shaping_calib/)
