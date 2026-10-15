# PrusaSlicer upstream source research

## SOURCE_METADATA

- **Source:** [prusa3d/PrusaSlicer](https://github.com/prusa3d/PrusaSlicer)
- **Inspected revision:** `30ef59195e0f3ee6f270b185bb5f9fb5f349f81f`
- **Upstream label:** `version_3.0.0-alpha12`
- **Commit date:** 2026-09-21; repository checkout inspected 2026-10-13.
- **Version file:** [`version.inc`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/version.inc)
- **Method:** shallow, blob-filtered checkout of the upstream Git repository; source and bundled preset files were read directly. No search snippets were used. This working repository has no `.codegraph/` directory, so CodeGraph was not applicable.
- **Scope:** FFF configuration schema/definitions, flow and layer-height implementation, speeds/acceleration/cooling, supports, seams, retraction, variable layer height, firmware/G-code emission, preset formats, and recent upstream history relevant to those areas.

## COVERAGE

| Area | Primary source paths inspected | Result |
|---|---|---|
| Config options | `src/slic3r-shared/src/Slic3r/Biz/Config/Legacy/PrintConfig.cpp` | Definitions, types, defaults, ranges, aliases, tooltips, inheritance/override groupings |
| Flow/width | `src/libslic3r/src/libslic3r/Flow.cpp`, `Flow.hpp` | Width fallback, percentage conversion, spacing and cross-section math |
| Layer height | `src/slic3r-biz-algorithms/src/Slic3r/Biz/Algorithms/LayerHeight.cpp`, `src/libslic3r/src/libslic3r/PrintObjectSlice.cpp` | Profile interpolation, bounds, adaptive layer generation |
| Speeds/acceleration | `PrintConfig.cpp`, `GCodeWriterConfig.cpp`, `GCodeWriter.cpp` | Role speeds, acceleration commands, machine-limit gating |
| Cooling | `PrintConfig.cpp`, `GCode/CoolingBuffer.cpp` | Minimum-layer-time slowdown, fan ramping/clamping, per-feature adjustment |
| Supports | `Support/SupportMaterial.cpp`, `Support/SupportCommon.cpp`, `Support/TreeSupport*.cpp` | Mode, angle/overhang detection, contact/interface and style paths |
| Seams | `GCode/SeamPlacer.cpp`, `Seam*` sources, `PrintConfig.cpp` | Four seam modes, visibility/rear/random selection, staggering/scarf conditions |
| Retraction/G-code | `GCodeWriter.cpp`, `GCodeWriterConfig.cpp`, `PrintConfig.cpp` | E-axis, volumetric/relative modes, firmware retraction, fan/pressure advance |
| Presets | `specs/presets/*.json`, `resources/presets/**` | YAML fragment model, vendor/printer/tool/material structure and inheritance |
| Release history | Git tags and `git log` touching the paths above | Relevant post-2.9.6 changes and 3.0 alpha state |

## CLAIMS

### C1 — Config is a typed option registry, while current bundled profiles are YAML fragments

**Condition:** A setting is accepted only if it is registered in the config definition layer; a bundled preset then supplies values/fragments for printer, print, tool-print, material, or filament contexts.

**Evidence A — primary definition:** [`PrintConfig.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/slic3r-shared/src/Slic3r/Biz/Config/Legacy/PrintConfig.cpp) registers each key with a config type (`coFloat`, `coFloatOrPercent`, `coEnum`, `coBools`, etc.), GUI metadata, limits, defaults, aliases, and `ratio_over` dependencies.

**Evidence B — schema:** [`preset-schema.json`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/specs/presets/preset-schema.json) defines fragments with `id`, `name`, `values`, optional `features`, `variants`, `inherits`, `unconditional_inherits`, and `match_mode`; top-level fragments are typed as `printer`, `print`, `tool_print`, `material`, or `filament`.

**Evidence C — vendor model:** [`vendor-schema.json`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/specs/presets/vendor-schema.json) models vendor, printer, tool, feeder, and related definitions; [`vendor.yaml`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/resources/presets/prusa-research-fff/PrusaResearch/vendor.yaml) demonstrates feature defaults and printer-family ordering.

**Evidence D — operational implication:** Values in a preset are not a complete independent schema. They are interpreted against the registered option definitions and can be selected conditionally by hardware features. Treat profile YAML and the C++ config registry as a coupled contract.

### C2 — Default extrusion width is role- and nozzle-dependent; percentages are resolved against nozzle diameter or layer height according to the option

**Condition:** A width is zero, absolute, or percentage. `Flow::new_from_config_width()` resolves the value before constructing the extrusion model.

**Evidence A:** [`Flow.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/Flow.cpp) uses `1.125 × nozzle_diameter` for external/perimeter/solid/infill fallback roles, and `1.0 × nozzle_diameter` for support, support interface, and top solid infill.

**Evidence B:** `Flow::new_from_config_width()` treats a zero non-percentage width as automatic; otherwise it uses `FloatOrPercentage::get_abs_value(nozzle_diameter)`. The config tooltips separately define percentage widths for most extrusion-width options as percentages of layer height, with `first_layer_extrusion_width` tied to `first_layer_height` through `ratio_over`.

**Evidence C:** The rounded-rectangle model computes spacing as `width - height × (1 - π/4)` and volume per head length as `height × (width - height × (1 - π/4))`; bridge flow uses circular area and bridge-specific spacing.

**Evidence D:** The result is not a single universal “extrusion multiplier”: geometry width/height/spacing, filament diameter, extrusion multiplier, bridge flow, and feature-specific widths can all affect final E.

### C3 — Layer height is represented as a profile and constrained by minimum/maximum values

**Condition:** Variable/adaptive layer height is enabled and a profile exists; otherwise the fixed `layer_height` and `first_layer_height` path is used.

**Evidence A:** [`LayerHeight.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/slic3r-biz-algorithms/src/Slic3r/Biz/Algorithms/LayerHeight.cpp) stores `(z, layer_height)` pairs, linearly interpolates between profile points, and clamps edits to `min_layer_height`/`max_layer_height`.

**Evidence B:** `generate_object_layers()` emits a fixed first layer when configured, then advances by interpolated heights until the object height is reached. It asserts generated heights remain inside the min/max bounds and notes that the final layer is not necessarily re-adjusted to exactly align with the top.

**Evidence C:** Adaptive generation derives a candidate height from mesh-face cusp geometry, caps it at `max_layer_height`, and clamps a final remaining gap to the min/max range.

**Evidence D:** [`PrintConfig.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/slic3r-shared/src/Slic3r/Biz/Config/Legacy/PrintConfig.cpp) marks `variable_layer_height` enabled by default and describes `min_layer_height` as the resolution floor; printer capability and motion/Z constraints still determine whether a profile is practically usable.

### C4 — Speeds are feature-specific, while acceleration is emitted dynamically and firmware-flavor dependent

**Condition:** A nonzero role-specific acceleration is selected during G-code generation and machine-limit emission is enabled.

**Evidence A:** Config definitions provide separate speeds/accelerations for perimeters, external perimeters, infill, solid/top infill, bridges, supports, travel, first layer, and wipe tower. Percent settings such as external perimeter speed are expressed relative to a named base option via `ratio_over`.

**Evidence B:** [`GCodeWriter.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/GCode/GCodeWriter.cpp) clamps print/travel acceleration to configured machine maxima, suppresses redundant/zero updates, and emits `M201`, `M202`, `M204 P/T`, or `M204 S` depending on firmware flavor.

**Evidence C:** [`GCodeWriterConfig.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/GCode/GCodeWriterConfig.cpp) only enables machine-limit emission for legacy Marlin, Marlin firmware, Prusa Firmware Buddy, and RepRapFirmware; the default `machine_limits_usage` is time-estimate-only.

**Evidence D:** Junction deviation is emitted as `M205 J` only for Marlin/Prusa Buddy when positive and within the configured maximum. Thus slicer acceleration settings do not guarantee equivalent physical motion on every firmware.

### C5 — Cooling is a post-slicing speed/fan adjustment constrained by minimum speeds and fan limits

**Condition:** Auto cooling is enabled and estimated layer time falls below the configured target/slowdown threshold.

**Evidence A:** [`PrintConfig.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/slic3r-shared/src/Slic3r/Biz/Config/Legacy/PrintConfig.cpp) defaults `cooling` on, exposes `fan_below_layer_time`, minimum/maximum fan speeds, first-layer fan disable, full-fan ramp layer, and a choice between uniform cooling and consistent-surface cooling.

**Evidence B:** [`CoolingBuffer.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/GCode/CoolingBuffer.cpp) parses movement durations, identifies adjustable lines, and iteratively stretches adjustable feed rates while respecting per-extruder minimum print speed.

**Evidence C:** The consistent-surface mode first preserves the first two perimeters where possible, while uniform cooling slows all print features. Fan speed is ramped between `disable_fan_first_layers` and `full_fan_speed_layer`, then clamped to the filament's min/max range.

**Evidence D:** Cooling changes output feed rates/fan commands after toolpaths are formed; it is not equivalent to changing the nominal feature speed. Short layers can therefore print slower than their configured feature speed, but never below the configured minimum print speed used by the cooling solver.

### C6 — Support generation combines an explicit mode, auto overhang detection, contact/interface geometry, and style-specific engines

**Condition:** `support_material` is not `none`, or enforced support layers are requested.

**Evidence A:** The option is now a `SupportMode` enum: `none`, `enforcers_only`, or `everywhere`; `support_material_auto` remains represented in legacy/config migration areas but the active support logic checks the mode.

**Evidence B:** [`SupportMaterial.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/Support/SupportMaterial.cpp) converts a positive overhang threshold to radians with an inclusive `+1` degree adjustment; zero selects automatic detection. Build-plate-only, enforcer, raft, and lower-layer geometry are applied during area generation.

**Evidence C:** Config defaults include top contact distance `0.2 mm`, bottom contact distance `0` meaning reuse top distance, interface layers `3`, interface spacing `0` for solid interface, support spacing `2.5 mm`, support speed `60 mm/s`, grid style, and a sheath enabled.

**Evidence D:** `SupportMaterial.cpp` and `TreeSupport.cpp` dispatch separate grid/snug/organic/tree-style paths; “build plate only” constrains support rests, while contact distance and interface-layer settings determine separation and roof/floor construction. These are not interchangeable with a simple overhang-angle threshold.

### C7 — Seams are selected by mode, then optionally transformed by staggering and scarf-joint rules

**Condition:** The object has closed perimeters and a seam mode is selected.

**Evidence A:** [`SeamPlacer.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/GCode/SeamPlacer.cpp) dispatches `aligned`, `rear`, `random`, and `nearest`; aligned uses visibility and shell analysis, rear uses rear-tolerance geometry, random uses a seed, and nearest is chosen later rather than precomputed.

**Evidence B:** `staggered_inner_seams` offsets inner-perimeter starts according to seam depth and stops at blockers/overhang classifications.

**Evidence C:** Scarf seams are disabled on layer 0, on non-smooth perimeters when `scarf_seam_only_on_smooth` is true, for zero length, and for thick bridge overhang cases. Otherwise length, start height, entire-loop, inner-perimeter, and maximum segment-length settings shape the scarf.

**Evidence D:** Config defaults are aligned seams, seam gap `15%` (or absolute), scarf placement nowhere, scarf length `20 mm`, maximum segment length `1 mm`, and inner-perimeter scarf disabled. Seam visibility is geometry/model dependent, so changing mode does not guarantee a fixed XY coordinate.

### C8 — Retraction can be slicer-generated E motion or delegated to firmware; E semantics are independently configurable

**Condition:** Retraction is triggered by travel/layer/toolchange rules and the relevant length is nonzero, unless firmware retraction is enabled.

**Evidence A:** Config exposes `retract_before_travel` (default `2 mm`), normal length (`2 mm`), toolchange length (`10 mm`), retract speed (`40 mm/s`), deretract speed (`0` means reuse retract speed), layer-change retraction, wipe, lift, and “only retract when crossing perimeters.”

**Evidence B:** [`GCodeWriter.cpp`](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/GCode/GCodeWriter.cpp) emits E-axis `G1` with feed rate for slicer-managed retraction; with firmware retraction it emits `G10`/`G11` (or Machinekit `G22`/`G23`) and resets E after unretract.

**Evidence C:** `use_relative_e_distances` selects relative-vs-absolute E handling, `use_volumetric_e` converts raw filament lengths to volume using filament diameter, and `use_firmware_retraction` deliberately substitutes a fake internal length so configured raw length does not control the firmware command path.

**Evidence D:** Firmware support is a hard condition: enabling firmware retraction, volumetric E, pressure advance, or flavor-specific acceleration without matching firmware behavior can produce incorrect extrusion or motion even when the G-code is syntactically valid.

### C9 — G-code flavor affects extrusion axis, fans, acceleration, retraction, pressure advance, and machine limits

**Condition:** The selected `gcode_flavor` matches the printer firmware, and custom start/end/toolchange G-code does not contradict slicer state.

**Evidence A:** Config enumerates RepRap/Sprinter, RepRapFirmware, Repetier, Teacup, MakerWare, legacy Marlin, Marlin 2, Klipper, Sailfish, Mach3/LinuxCNC, Machinekit, Smoothie, and no-extrusion.

**Evidence B:** `GCodeWriterConfig.cpp` maps Mach3/Machinekit to axis `A`, no-extrusion to no extrusion axis, and other flavors to `E`; it also controls which machine-limit features are available.

**Evidence C:** `GCodeWriter.cpp` emits flavor-specific fan commands (`M106`, `M107`, `M126`, `M127`), pressure advance (`M572`, `M900 K`, `SET_PRESSURE_ADVANCE`, or `M572 D0 S`), and acceleration commands.

**Evidence D:** The config tooltip explicitly warns that temperature and other commands are not universal. Custom G-code can change fan/temperature/E state outside the slicer's model; CoolingBuffer contains a recovery path that re-emits fan state after custom toolchange code.

## PROCEDURES

1. Pin any research or profile change to the full revision above; do not rely on the moving `master` URL.
2. Identify the owning config key in `PrintConfig.cpp`, including its type, default, limits, `ratio_over`, aliases, and whether it is printer/print/tool/filament scoped.
3. Trace the key into the consumer implementation. For geometry, inspect `Flow.cpp`; for layer height, `LayerHeight.cpp`; for output behavior, `GCodeWriter*` and `CoolingBuffer.cpp`; for supports/seams, their dedicated modules.
4. Resolve percentage values using the declared dependency. A percentage may be relative to nozzle diameter, layer height, first-layer height, or another named speed/width setting.
5. For firmware-facing conclusions, inspect both `GCodeWriterConfig.cpp` flavor gating and the emitted command branch in `GCodeWriter.cpp`.
6. For presets, validate the YAML fragment against `preset-schema.json`/`vendor-schema.json`, then inspect inheritance/conditional variants and the vendor feature set before assuming a value applies to a printer.
7. When diagnosing a print symptom, compare nominal settings with generated G-code: cooling can rewrite feed rates, firmware can clamp motion, and custom G-code can change state that the slicer does not fully observe.

## NUMERICAL_VALUES

| Setting/constant | Upstream value or behavior | Source |
|---|---:|---|
| Fixed `layer_height` default | `0.3 mm` | `PrintConfig.cpp` |
| First-layer height default | `0.35` absolute, with `ratio_over: layer_height` | `PrintConfig.cpp` |
| Auto width, most FFF roles | `1.125 × nozzle diameter` | `Flow.cpp` |
| Auto width, support/interface/top solid | `1.0 × nozzle diameter` | `Flow.cpp` |
| Flow spacing | `w - h × (1 - π/4)` | `Flow.cpp` |
| Default perimeter speed | `60 mm/s` | `PrintConfig.cpp` |
| External perimeter speed | `50%` of perimeter speed | `PrintConfig.cpp` |
| Retraction length / speed | `2 mm` / `40 mm/s` | `PrintConfig.cpp` |
| Toolchange retraction length | `10 mm` | `PrintConfig.cpp` |
| Travel threshold before retract | `2 mm` | `PrintConfig.cpp` |
| Top support contact distance | `0.2 mm` | `PrintConfig.cpp` |
| Support interface layers | `3` | `PrintConfig.cpp` |
| Support spacing / speed | `2.5 mm` / `60 mm/s` | `PrintConfig.cpp` |
| Seam gap default | `15%` | `PrintConfig.cpp` |
| Scarf length / max segment | `20 mm` / `1 mm` | `PrintConfig.cpp` |
| Cooling tube retraction / length | `91.5 mm` / `5 mm` | `PrintConfig.cpp` |
| Fan-below-layer-time default | `60 s` | `PrintConfig.cpp` |
| Default machine limits usage | time-estimate-only | `PrintConfig.cpp` |
| Default XY max feedrate values | `500`, `200 mm/s` profile slots | `PrintConfig.cpp` |
| Default XY max acceleration values | `9000`, `1000 mm/s²` profile slots | `PrintConfig.cpp` |
| Default Z max feedrate / acceleration | `12 mm/s` / `500, 200 mm/s²` slots | `PrintConfig.cpp` |

## CONFLICTS_OR_LIMITS

- The inspected upstream HEAD is a future-dated 3.0 alpha snapshot relative to many stable PrusaSlicer deployments. Stable 2.9.x behavior and shipped profiles may differ.
- The repository contains a legacy config namespace and a newer `slic3r-domain`/business-layer split. A key’s name alone is insufficient; follow the active consumer at the pinned revision.
- Some historical option names remain for migration/backward compatibility. In particular, support behavior is now centered on `SupportMode`, so old documentation describing a boolean `support_material` plus `support_material_auto` pair can be stale.
- Machine limits can be used only for time estimation, emitted to G-code, or ignored. Even when emitted, the printer firmware remains authoritative and may apply additional limits.
- Cooling uses estimated movement times and can modify feed rates after nominal toolpaths are generated. A profile speed value is therefore not necessarily the feed rate seen on every line.
- Percent widths and percent speeds have different bases. Do not generalize “percentage” across options without reading `ratio_over` and `FloatOrPercentage` conversion.
- `first_layer_height` is a ratio-capable value, while some width percentages are interpreted against layer height and some profile values are absolute. Unit labels and the option definition must be checked together.
- Custom start/end/toolchange G-code can alter temperature, fan, E mode, pressure advance, or firmware state. The slicer cannot guarantee that external commands preserve its internal state model.
- The adaptive layer algorithm includes an explicit FIXME about exact top alignment; small final-layer differences are therefore expected in edge cases.

Relevant upstream changes visible in history include: replacement of the support boolean pair with `SupportMode` (`dd5c33e`), addition of the consistent-surface cooling logic (`df2de843a`, `d1b4c390a`, `4c22ddf9b`), pressure-advance flavor/parameter work (`c96269d`, `99c4436`, `6f564ea`), dynamic fan clamping (`093dd0`), machine-limit junction deviation (`3f084c`), and the preset/G-code metadata schemas (`e881062`). These commit messages are evidence of change history, not substitutes for the current source behavior.

## GAPS

- This report did not build PrusaSlicer or run a full end-to-end slice, so emitted command examples are derived from source branches rather than a generated file.
- It did not exhaustively enumerate every one of the thousands of preset YAML files or every vendor conditional; the schema and representative PrusaResearch vendor/profile files were inspected.
- SLA-only support and exposure settings were not covered beyond identifying the FFF scope.
- Firmware-specific semantics were inferred from PrusaSlicer’s flavor branches; printer firmware documentation was not independently audited.
- Release-note coverage is repository history/commit-based. No separate prose changelog is present at the pinned checkout; GitHub release UI text was not treated as primary evidence.

## CITATIONS

All citations below are pinned to the inspected revision unless a tag/commit is explicitly named.

1. [Version and build label](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/version.inc)
2. [Config option registry](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/slic3r-shared/src/Slic3r/Biz/Config/Legacy/PrintConfig.cpp)
3. [Flow construction and cross-section math](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/Flow.cpp)
4. [Layer-height algorithms](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/slic3r-biz-algorithms/src/Slic3r/Biz/Algorithms/LayerHeight.cpp)
5. [G-code writer config and firmware gating](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/GCode/GCodeWriterConfig.cpp)
6. [G-code emission](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/GCode/GCodeWriter.cpp)
7. [Cooling solver and fan control](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/GCode/CoolingBuffer.cpp)
8. [FFF support generation](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/Support/SupportMaterial.cpp)
9. [Tree support generation](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/Support/TreeSupport.cpp)
10. [Seam placement](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/src/libslic3r/src/libslic3r/GCode/SeamPlacer.cpp)
11. [Preset fragment schema](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/specs/presets/preset-schema.json)
12. [Vendor/profile schema](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/specs/presets/vendor-schema.json)
13. [Bundled PrusaResearch vendor definition](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/resources/presets/prusa-research-fff/PrusaResearch/vendor.yaml)
14. [Support mode change](https://github.com/prusa3d/PrusaSlicer/commit/dd5c33e)
15. [Cooling logic introduction](https://github.com/prusa3d/PrusaSlicer/commit/df2de843a)
16. [Pressure-advance flavor support](https://github.com/prusa3d/PrusaSlicer/commit/99c443624)
17. [Preset/G-code metadata schemas](https://github.com/prusa3d/PrusaSlicer/commit/e88106282)
