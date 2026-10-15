# Klipper GitHub source-research report

## SOURCE_METADATA

- **Repository:** [Klipper3d/klipper](https://github.com/Klipper3d/klipper)
- **Inspected ref:** `master`
- **Inspected HEAD:** `c7d572441f7d6d6d7f887df5c0fa8cec69d14980`
- **HEAD date:** 2026-10-04 00:13:05 +03:00
- **HEAD subject:** `temperature_probe: Store tap params only after calibration starts`
- **Latest tagged release found:** `v0.13.0`, commit `61c0c8d2ef40340781835dd53fb04cc7a454e37a`, dated 2025-04-09; [release page](https://github.com/Klipper3d/klipper/releases/tag/v0.13.0)
- **Release status:** the inspected `master` is unreleased relative to `v0.13.0`; findings below are source-tree findings, not necessarily release guarantees.
- **Method:** shallow Git clone of the primary repository, direct inspection of docs, Python/C-adjacent implementation, tests, and `git log`/`git show` from `v0.13.0..HEAD`. Search-result snippets were not used.
- **Scope:** pressure advance, resonance/input shaping, calibration, extrusion, retraction, and motion limits; emphasis on changes and implementation details likely to be missed when treating public docs or the last release as the baseline.

## COVERAGE

| Area | Current-tree result | Change since `v0.13.0` |
|---|---|---|
| Pressure advance | Current implementation, tuning procedure, limits, and interaction with retraction reviewed | No matching change to `docs/Pressure_Advance.md` or `klippy/kinematics/extruder.py` since `v0.13.0`; implementation still matters for slicer tuning |
| Resonance/input shaping | Z-axis measurement/shaping; parameterized shapers; damping validation; calibration scripts; multi-file processing | Major changes in 2025–2026 |
| Calibration | Eddy-current tap-threshold workflow and unit change; resonance calibration; runtime calibration commands | Major Eddy/tap changes; resonance changes |
| Extrusion | Rotation distance, pressure-advance queueing, extruder-only limits, synchronized extruder steppers | No user-facing PA/rotation-distance change since `v0.13.0`; motion-queue internals changed |
| Retraction | Firmware retraction defaults, runtime commands, G10/G11 semantics, PA interaction | No substantive change since `v0.13.0` |
| Motion limits | `minimum_cruise_ratio`, square-corner velocity, Z-axis test-limit enforcement, manual-stepper limits | `minimum_cruise_ratio` remains current; Z resonance testing now explicitly consumes Z limits |

## CLAIMS

### 1. `master` has a new Z-axis resonance/input-shaping path

**Conditions:** A printer must define an accelerometer usable for Z (`accel_chip_z`), have reachable probe points/clearance, and run `TEST_RESONANCES AXIS=Z` or `SHAPER_CALIBRATE AXIS=Z`. Z cannot be measured in the same test as non-Z axes.

**Evidence A — source/docs:** `resonance_tester.py` adds Z parsing, separate `max_freq_z`, `accel_per_hz_z`, `sweeping_accel_z`, and Z-limit lookup; it rejects a mixed Z/non-Z test. The config reference adds `shaper_freq_z`, `shaper_type_z`, `damping_ratio_z`, `accel_chip_z`, and Z-specific resonance-test settings. See [current resonance implementation](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/klippy/extras/resonance_tester.py) and [config reference](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/Config_Reference.md#resonance_tester).

**Evidence B — change:** commit [`47080385`](https://github.com/Klipper3d/klipper/commit/470803853e4d6b547e933a979ff3736cb95c7c2a) adds Z-axis docs/config/G-code support; [`caf7accf`](https://github.com/Klipper3d/klipper/commit/caf7accf2d7b4d3c810bbb16f4ff7d4be80b043c) adds the Z-axis input-shaper implementation; [`ec82cee7`](https://github.com/Klipper3d/klipper/commit/ec82cee7fc6653304b766b15d4d31dbd59698e21) adds Z resonance testing.

**Evidence C — operational behavior:** Default Z test values are less aggressive: `max_freq_z=100 Hz`, `accel_per_hz_z=15 mm/s`, `sweeping_accel_z=50 mm/s²`. The guide gives temporary example printer limits `max_z_velocity: 20` and `max_z_accel: 1550`, and suggests `accel_per_hz_z` in the 20–30 range only if results are bogus.

**Evidence D — impact:** A slicer-tuning tool must not assume input shaping is X/Y-only. Z can have its own frequency, shaper type, damping ratio, accelerometer, frequency ceiling, and test acceleration. The code also reports required Z limits and refuses unsafe/inadequate test motion rather than silently running the XY test profile.

### 2. Input-shaper types now accept parameterized forms

**Conditions:** The parameter syntax is accepted in `[input_shaper]`, `SET_INPUT_SHAPER`, `calibrate_shaper.py --shapers`, and `graph_shaper.py --shaper`; the selected shaper’s own validation still applies.

**Evidence A — source/docs:** `shaper_defs.py` parses shaper names with optional parameters. MZV supports generalized `n`/`t` forms; EI supports `v_tol`. Invalid/negative-valued or mathematically ill-formed shapers raise a `ShaperError`; each shaper has a maximum damping ratio. See [shaper definitions](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/klippy/extras/shaper_defs.py) and [input-shaper implementation](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/klippy/extras/input_shaper.py).

**Evidence B — change:** [`db10e92e`](https://github.com/Klipper3d/klipper/commit/db10e92e9b3a4112e7f8fdafffbdb0969e94bcfd) introduces parameterized initialization; [`530cd051`](https://github.com/Klipper3d/klipper/commit/530cd051221056bdd93121da52da759908571ef8) documents and tests it.

**Evidence C — operational behavior:** Examples in the current docs include `mzv(n=4,t=0.9)`, `mzv(n=3,t=0.8)`, `mzv(n=5,t=1.1)`, and `ei(v_tol=0.1)`. The default MZV remains `n=3`, `t=0.75` of the damped period; the new form is not a new default.

**Evidence D — impact:** A configuration parser or tuner that treats `shaper_type` as a fixed enum will reject valid current configurations. Preserve the complete parameterized string when generating `SET_INPUT_SHAPER` or config output.

### 3. Shaper calibration can constrain residual vibration score, smoothing, damping, and frequency

**Conditions:** These controls apply to `SHAPER_CALIBRATE`/`calibrate_shaper.py`; a constraint can eliminate every candidate, producing no recommendation. `--max_vibrs_pcnt` is a percentage input, converted internally to a fraction.

**Evidence A — source/scripts:** `scripts/calibrate_shaper.py` accepts `--max_smoothing`, `--max_vibrs_pcnt`, `--scv`, `--shaper_freq`, `--shapers`, `--damping_ratio`, and `--test_damping_ratios`; it supports comma-separated frequencies or `[start]:end[:step]` ranges. See [calibrate_shaper.py](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/scripts/calibrate_shaper.py).

**Evidence B — change:** [`ef8edf3a`](https://github.com/Klipper3d/klipper/commit/ef8edf3aef7fe8c4e886f20eef3d68dd15e61465) adds the remaining-vibrations limit; [`2239041d`](https://github.com/Klipper3d/klipper/commit/2239041df6a289acce54c4e88eddfdf76bcba7f0) fixes processing of `max_vibrs_pcnt`; [`2aff840f`](https://github.com/Klipper3d/klipper/commit/2aff840f68e31acc0c2e470211291671e44a7b3a) reworks multi-file calibration.

**Evidence C — numerical/validation behavior:** The standalone script rejects `max_smoothing < 0.05` and `max_vibrs_pcnt < 0.1`; `--scv` defaults to `5.0`. When several logs are supplied, their calibration datasets are combined before recommendation. Raw logs and already-normalized shaper CSV are both accepted.

**Evidence D — impact:** A tuner should expose these as optional calibration constraints rather than hard-coding the first recommendation. It should distinguish “no valid shaper under constraints” from a parser failure.

### 4. Eddy-current tap calibration changed units and requires recalibration

**Conditions:** This applies to `[probe_eddy_current] tap_threshold`, the runtime `TAP_THRESHOLD`, and `METHOD=tap`. Existing values from before the change are not portable without recalibration.

**Evidence A — primary change/config:** Current docs define `tap_threshold` in **Hz/mm**, not Hz. The implementation scales the threshold by probe speed and sensor samples-per-second before configuring the analog trigger, and compares the pullback slope delta directly in Hz/mm. See [current Eddy implementation](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/klippy/extras/probe_eddy_current.py) and [Eddy config reference](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/Config_Reference.md#probe_eddy_current).

**Evidence B — change/compatibility notice:** [`460ee783`](https://github.com/Klipper3d/klipper/commit/460ee78340a57f51493bf4568ced0a89e26eb063) changes the handling and adds a `Config_Changes.md` warning that the value must be recalibrated.

**Evidence C — procedure:** The current automated sequence is `PROBE_EDDY_CURRENT_TAP_CALIBRATE TAP=guess`, then `TAP=refine`, then `TAP=verify`; the verify stage probes five times. Save the resulting `tap_threshold` with `SAVE_CONFIG`. Manual fallback is `PROBE METHOD=tap TAP_THRESHOLD=<value>`; too-early stops imply increasing the value about 10%, while failure to stop after contact implies reducing it, roughly by half.

**Evidence D — impact:** This is a high-risk migration for printer configs: wrong direction or stale units can cause premature stops or uncontrolled descent. Any prusaSlicer-tuner firmware profile must mark old Eddy thresholds as invalid after the change, not merely preserve the numeric value.

### 5. The new Eddy tap calibration command is distinct from the main Eddy height calibration

**Conditions:** `PROBE_EDDY_CURRENT_CALIBRATE` maps sensor frequency to Z height; `PROBE_EDDY_CURRENT_TAP_CALIBRATE` tunes contact-detection threshold. The latter assumes the main calibration has already been completed.

**Evidence A — command reference:** The current G-Code reference lists `PROBE_EDDY_CURRENT_CALIBRATE CHIP=... [MANUAL_METHOD=manual]` separately from `PROBE_EDDY_CURRENT_TAP_CALIBRATE [TAP=guess|refine|verify]` ([G-Codes](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/G-Codes.md#probe_eddy_current_tap_calibrate)).

**Evidence B — change:** [`ef7b13b1`](https://github.com/Klipper3d/klipper/commit/ef7b13b1f2d45dc82a9d3ba37500756145cb527) adds the command and the multi-stage documented workflow.

**Evidence C — conditions:** The guide requires a clean nozzle/bed, homing, a near-center position, and a starting nozzle gap of 3–10 mm; it explicitly recommends being ready to issue `M112` during the contact descent.

**Evidence D — impact:** A calibration UI should present these as separate jobs and should not label tap-threshold calibration as a replacement for the frequency-to-height calibration.

### 6. Pressure advance remains bounded by implementation validation, but not by an extruder-movement cap

**Conditions:** `[extruder] pressure_advance` must be non-negative; `pressure_advance_smooth_time` and `SET_PRESSURE_ADVANCE SMOOTH_TIME` are limited to 0–0.200 s. A zero PA value disables smoothing in the implementation.

**Evidence A — source:** `ExtruderStepper` validates `pressure_advance >= 0`, defaults smoothing to `0.040`, and limits smoothing to `0.200`; changing smoothing flushes step generation, while a same-smoothing update is scheduled through a lookahead callback. See [extruder.py](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/klippy/kinematics/extruder.py).

**Evidence B — history:** `git log v0.13.0..HEAD` shows no pressure-advance doc or extruder-kinematics change; the current behavior is carried forward from the release line, while motion-queue infrastructure around synchronized extruder steppers did change.

**Evidence C — documented tuning:** The pressure-advance tower uses `SQUARE_CORNER_VELOCITY=1 ACCEL=500`; direct-drive uses `START=0 FACTOR=.005`, long Bowden uses `.020`; the guide gives typical PA values of 0.050–1.000 and warns that values over roughly 0.200 can cause extruder skipping at high acceleration ([Pressure Advance](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/Pressure_Advance.md)).

**Evidence D — source-only nuance:** The docs explicitly say no config setting caps PA-induced extra extruder movement. PA changes extruder motion during acceleration/deceleration, but not toolhead path, print timing, or total filament. A tuner must therefore treat PA and extruder acceleration/torque as coupled constraints, not as a simple flow multiplier.

### 7. Extrusion-only and retraction moves have separate safety/kinematic treatment

**Conditions:** Extrusion-only moves and retract moves are detected in `PrinterExtruder.check_move`; they are limited by `max_extrude_only_velocity`, `max_extrude_only_accel`, and `max_extrude_only_distance` as configured. Firmware retraction uses separate retract/unretract lengths and speeds.

**Evidence A — source/config:** `firmware_retraction.py` defaults are `retract_length=0`, `retract_speed=20 mm/s`, `unretract_extra_length=0`, `unretract_speed=10 mm/s`; G10/G11 emit relative E-only moves while preserving/restoring G-Code state. The config reference exposes runtime `SET_RETRACTION` and `GET_RETRACTION` ([firmware retraction](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/klippy/extras/firmware_retraction.py)).

**Evidence B — history:** No substantive firmware-retraction change appears after `v0.13.0`; this is a current baseline rather than a new feature.

**Evidence C — documented interaction:** The PA guide still recommends a small slicer retract, e.g. 0.75 mm, possibly wipe-on-retract, and recommends disabling Z-lift-on-retract. PA and retraction are therefore complementary and should not be collapsed into one setting.

**Evidence D — impact:** Slicer output should not assume E-only moves inherit XY motion limits. Firmware retraction can be changed per filament at runtime, but its values are not persisted by `SET_RETRACTION` unless separately written to config.

### 8. `minimum_cruise_ratio` is a live motion limit and is intentionally disabled during resonance tests

**Conditions:** `[printer] minimum_cruise_ratio` accepts 0–less-than-1, defaults to 0.5, and can be changed with `SET_VELOCITY_LIMIT MINIMUM_CRUISE_RATIO=...`. Set it to zero before ringing/input-shaper tests.

**Evidence A — source/docs:** The toolhead computes a pseudo-acceleration from `max_accel * (1 - minimum_cruise_ratio)` and reports the value in status; the config reference explains that 0.5 forces a minimum cruising distance of 0.75 mm on a standalone 1.5 mm move. See [toolhead.py](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/klippy/toolhead.py) and [printer config reference](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/Config_Reference.md#printer).

**Evidence B — procedure:** `Resonance_Compensation.md` now explicitly says to issue `SET_VELOCITY_LIMIT MINIMUM_CRUISE_RATIO=0` before measurement and shaper test prints ([guide](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/Resonance_Compensation.md)).

**Evidence C — related change:** [`3ef760c1`](https://github.com/Klipper3d/klipper/commit/3ef760c1) removes obsolete `max_accel_to_decel`; [`20d9c84a`](https://github.com/Klipper3d/klipper/commit/20d9c84a) fixes the `SET_VELOCITY_LIMIT` response field ordering.

**Evidence D — impact:** A calibration generator that leaves the printer’s configured cruise ratio enabled will measure a different motion profile from ordinary tuning assumptions and can bias ringing/shaper selection.

### 9. Manual-stepper axes now have explicit motion-limit controls

**Conditions:** These parameters apply when `manual_stepper` is used with a G-Code axis registration. They do not replace the main toolhead’s `[printer]` limits.

**Evidence A — change/docs:** [`6c1d5d91`](https://github.com/Klipper3d/klipper/commit/6c1d5d912ae34991dbe866d2bbf9dc75a6345a0c) adds `LIMIT_VELOCITY` and `LIMIT_ACCEL`; [`64e01f03`](https://github.com/Klipper3d/klipper/commit/64e01f03a20f4d895f4baa5d5f72870f800f5830) adds `INSTANTANEOUS_CORNER_VELOCITY` for G-Code axes.

**Evidence B — source:** The command/config path is in the current `manual_stepper` implementation and G-Code reference; limits are applied to that stepper’s generated motion rather than silently changing global toolhead limits.

**Evidence C — condition:** These are relevant to tool-changing, auxiliary, or calibration axes registered as G-Code axes, not ordinary E retraction or standard XYZ moves.

**Evidence D — impact:** Config generation should preserve these as per-axis controls and avoid mapping them onto global `max_velocity`/`max_accel` fields.

## PROCEDURES

### Pressure advance

1. Calibrate extruder `rotation_distance`, nozzle temperature, and flow first.
2. Run the tower with `SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500`.
3. Use factor `.005` for direct drive or `.020` for long Bowden as starting points.
4. Calculate `pressure_advance = START + measured_height * FACTOR`; verify at normal acceleration because high PA can overload the extruder.
5. Keep a small slicer retraction only if ooze remains; do not use PA as a retraction substitute.

### Resonance/input shaping

1. Disable dynamic slicer acceleration, PA, and `minimum_cruise_ratio`; return square-corner velocity to 5.0 unless the test explicitly calls for another value.
2. For XY, use accelerometer measurement or the ringing tower; for Z, configure `accel_chip_z` and run Z alone.
3. Run `TEST_RESONANCES` for raw data or `SHAPER_CALIBRATE` for an in-firmware recommendation.
4. Use `calibrate_shaper.py` for multi-file data, optional smoothing/vibration/frequency constraints, or custom shaper parameters.
5. Validate max acceleration from both ringing and smoothing; choose the lower safe value.
6. Persist per-axis settings, including `shaper_type_z`/`shaper_freq_z` where applicable.

### Eddy-current tap calibration

1. Complete the main `PROBE_EDDY_CURRENT_CALIBRATE` first.
2. Home, clean nozzle/bed, move near center, and position 3–10 mm above the bed.
3. Run `PROBE_EDDY_CURRENT_TAP_CALIBRATE TAP=guess`, then `refine`, then `verify`.
4. Be prepared to abort with `M112`; the tool intentionally drives the nozzle into contact.
5. Save the verified threshold with `SAVE_CONFIG`.
6. Treat pre-2026 values as needing recalibration because the unit/algorithm changed to Hz/mm.

## NUMERICAL_VALUES

| Parameter/operation | Current value or range | Meaning |
|---|---:|---|
| PA smooth time | default 0.040 s; valid 0–0.200 s | Extruder pressure-advance smoothing |
| PA tuning | direct drive factor .005; long Bowden .020 | PA tower increment per layer height |
| Typical PA | 0.050–1.000 | Guide range; not a hard validator |
| High-PA warning | roughly >0.200 | Possible extruder skipping at high acceleration |
| Input-shaper damping | default 0.1 | Per-axis default; shaper-specific maximums apply |
| MZV default | `n=3`, `t=0.75` of damped period | Parameterized generalized MZV |
| `calibrate_shaper.py --scv` | default 5.0 mm/s | Square-corner velocity used in analysis |
| `--max_smoothing` | must be at least 0.05 | Standalone-script validation |
| `--max_vibrs_pcnt` | must be at least 0.1 percent | Remaining-vibration constraint |
| XY resonance defaults | max 135 Hz; 60 mm/s per Hz; sweep accel 400 mm/s² | Current resonance-test defaults |
| Z resonance defaults | max 100 Hz; 15 mm/s per Hz; sweep accel 50 mm/s² | Less aggressive Z defaults |
| Z guide example | `max_z_velocity=20`, `max_z_accel=1550` | Temporary minimum-ish example for Z testing, not universal printer defaults |
| Eddy tap threshold | Hz/mm | New unit after `460ee783`; recalibrate |
| Eddy tap starting gap | 3–10 mm | Automated tap-calibration precondition |
| Firmware retraction | length 0 mm; retract 20 mm/s; extra 0 mm; unretract 10 mm/s | Current defaults |
| Minimum cruise ratio | default 0.5; disable at 0.0; valid below 1.0 | Short-move cruise enforcement |
| Square-corner velocity | default 5 mm/s | Runtime-adjustable corner velocity |

## CONFLICTS_OR_LIMITS

- **Docs typo:** current `docs/G-Codes.md` renders the third frequency argument for `SET_INPUT_SHAPER` as `SHAPER_FREQ_Y=<shaper_freq_z>`; implementation and config reference clearly use `SHAPER_FREQ_Z`. Treat the source/config spelling as authoritative and consider this a documentation defect. See [current G-Codes.md](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/G-Codes.md#input_shaper).
- **Unreleased-source risk:** Z shaping, parameterized shapers, and tap-threshold behavior are present on `master` but are not part of `v0.13.0`. A production profile should record the Klipper commit, not only the nominal release.
- **Eddy migration risk:** the threshold unit change is explicitly breaking for existing values; do not auto-convert by copying numbers without calibration.
- **Shaper recommendation is conditional:** smoothing, residual vibration, damping ratio, SCV, maximum frequency, and selected shaper parameters can change the recommendation. “Best shaper” is not a universal fixed table entry.
- **Z measurement is constrained:** Z and XY cannot be tested together; Z test settings and kinematic limits differ. A generic XY-only calibration procedure is invalid for Z.
- **Pressure advance has no movement cap:** high PA can create large extra E motion. The 0.200 s smoothing ceiling is not a cap on PA-induced extrusion distance.
- **Firmware retraction is runtime state:** `SET_RETRACTION` changes active settings but is not itself a persistent config write; `SAVE_CONFIG` is a separate operation where applicable.
- **`minimum_cruise_ratio` changes the actual short-move profile:** leaving it at 0.5 during resonance testing conflicts with the documented test method.

## GAPS

- No current post-`v0.13.0` user-facing changes were found for the core pressure-advance tuning document, rotation-distance calibration, or firmware-retraction implementation; this report therefore records their current behavior but does not claim new tuning guidance.
- The source tree does not provide a universal conversion from old Eddy tap thresholds to the new Hz/mm values; calibration is the supported migration path.
- Resonance calibration still depends on accelerometer mounting, electrical/mechanical noise, and printer-specific mechanics; source defaults cannot determine a safe final `max_accel` for a particular machine.
- The repository does not define a slicer-specific contract for how to combine PA, firmware retraction, wipe, and Z-hop. The PA guide only gives interaction guidance.
- No binary release artifact was inspected; findings are tied to the Git revision above.
- The final HEAD commit concerns temperature-probe calibration state and does not materially change the requested PA/resonance/extrusion/retraction/motion-limit areas; it is included in metadata because it identifies the exact inspected revision.

## CITATIONS

1. [Klipper repository](https://github.com/Klipper3d/klipper)
2. [Latest tagged release: v0.13.0](https://github.com/Klipper3d/klipper/releases/tag/v0.13.0)
3. [Inspected HEAD commit](https://github.com/Klipper3d/klipper/commit/c7d572441f7d6d6d7f887df5c0fa8cec69d14980)
4. [Z-axis resonance/input-shaper docs commit](https://github.com/Klipper3d/klipper/commit/470803853e4d6b547e933a979ff3736cb95c7c2a)
5. [Parameterized shaper implementation commit](https://github.com/Klipper3d/klipper/commit/db10e92e9b3a4112e7f8fdafffbdb0969e94bcfd)
6. [Parameterized shaper docs/tests commit](https://github.com/Klipper3d/klipper/commit/530cd051221056bdd93121da52da759908571ef8)
7. [Remaining-vibration limit commit](https://github.com/Klipper3d/klipper/commit/ef8edf3aef7fe8c4e886f20eef3d68dd15e61465)
8. [Multi-file shaper calibration commit](https://github.com/Klipper3d/klipper/commit/2aff840f68e31acc0c2e470211291671e44a7b3a)
9. [Eddy tap calibration command commit](https://github.com/Klipper3d/klipper/commit/ef7b13b1f2d45dc82a9d3ba37500756145cb527)
10. [Eddy threshold unit-change commit](https://github.com/Klipper3d/klipper/commit/460ee78340a57f51493bf4568ced0a89e26eb063)
11. [Manual-stepper velocity/acceleration-limit commit](https://github.com/Klipper3d/klipper/commit/6c1d5d912ae34991dbe866d2bbf9dc75a6345a0c)
12. [Manual-stepper corner-velocity commit](https://github.com/Klipper3d/klipper/commit/64e01f03a20f4d895f4baa5d5f72870f800f5830)
13. [Klipper source: Pressure Advance](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/Pressure_Advance.md)
14. [Klipper source: Resonance Compensation](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/Resonance_Compensation.md)
15. [Klipper source: Measuring Resonances](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/Measuring_Resonances.md)
16. [Klipper source: Config Reference](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/Config_Reference.md)
17. [Klipper source: G-Code Reference](https://github.com/Klipper3d/klipper/blob/c7d572441f7d6d6d7f887df5c0fa8cec69d14980/docs/G-Codes.md)
