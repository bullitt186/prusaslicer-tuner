# Klipper Discourse source research

## SOURCE_METADATA

- **Source:** [Klipper Discourse](https://klipper.discourse.group/)
- **Collection date:** 2026-10-13
- **Scope:** Representative thread corpus, not an exhaustive history of the forum. Threads were selected for direct relevance to pressure advance, input shaping/resonance, rotation distance, firmware retraction, macros, motion limits, and hardware/failure diagnosis.
- **Evidence labels used below:**
  - **B — maintainer / Knowledge Base / Developers:** official Klipper explanation, release note, or maintainer/Knowledge Base answer. Strongest evidence for intended semantics and supported procedure.
  - **C — experienced community guidance:** recurring or technically reasoned guidance from established forum participants, often consistent with Klipper docs. Useful, but not equivalent to a specification.
  - **D — individual report / experiment:** printer-specific observation, workaround, or unverified claim. Preserve context; do not generalize without corroboration.
- **Version caveat:** Forum guidance spans roughly 2021–2025 and Klipper behavior changed during that period. In particular, `max_accel_to_decel` was deprecated/replaced by `minimum_cruise_ratio` by the 0.13.0 era, and resonance testing gained a sweeping-vibrations mechanism in 2025. Always reconcile older advice with the current Klipper documentation and installed version.

## CORPUS_SELECTION

The corpus contains 31 threads, distributed as follows:

| Area | Threads | Selection rationale |
|---|---:|---|
| Pressure advance / extruder dynamics | 9 | Calibration method, slicer-vs-firmware precedence, tuning failures, multi-extruder syntax, speed/acceleration context, PA/input-shaper interaction |
| Input shaping / resonance | 8 | Graph interpretation, accelerometer/test procedure, shaper smoothing, mechanical diagnosis, dynamic/axis questions, maintainer implementation detail |
| Rotation distance | 5 | Formula semantics, calibration boundaries, hardware-vs-flow distinction, configuration errors, unsafe values |
| Firmware retraction | 3 | Z-hop macro behavior, observed retraction, travel-speed semantics |
| Macros | 2 | Macro parameterization and pause/resume state handling |
| Motion limits | 4 | `max_velocity`, `max_accel`, `square_corner_velocity`, MCU/step-rate bottlenecks |
| Hardware / failure diagnosis | 7 | MCU timeout, timer-too-close, grounding, host load, ADC, spontaneous MCU reset |

Some threads intentionally count in more than one topical bucket because the cross-topic interaction is useful for tuning workflows.

## COVERAGE

### Pressure advance

- [Pressure advance tuning model slicing](https://klipper.discourse.group/t/pressure-advance-tuning-model-slicing/1183) — 2021-10-26; community guidance on test height and interpretation.
- [Rotation Distance calibration](https://klipper.discourse.group/t/rotation-distance-calibration/1280) — 2021-11-08; separates extruder mechanics from slicer flow.
- [Start end extrusion problems](https://klipper.discourse.group/t/start-end-extrusion-problems/6159) — 2023-01-24; experienced guidance on intended speed/acceleration and disabling slicer optimizations.
- [Pressure advance issues - not making a difference](https://klipper.discourse.group/t/pressure-advance-issues-not-making-a-difference/10068) — 2023-08-23; printer-specific diagnosis of an apparently ineffective PA test.
- [Why am I getting “Unable to infer active extruder stepper” ...](https://klipper.discourse.group/t/why-am-i-getting-unable-to-infer-active-extruder-stepper-when-trying-a-pressure-advance-tuning-tower/10740) — 2023-09-29; multi-extruder `TUNING_TOWER` syntax.
- [Pressure Advance Custom Start and Factor](https://klipper.discourse.group/t/pressure-advance-custom-start-and-factor/13025) — 2024-01-11; common confusion between the PA value and tower start value.
- [Regarding the issue of setting pressure advantage](https://klipper.discourse.group/t/regarding-the-issue-of-setting-pressure-advantage/15845) — 2024-04-18; runtime slicer commands versus config defaults.
- [Questions related to Tuning pressure advance](https://klipper.discourse.group/t/questions-related-to-tuning-pressure-advance/23369) — 2025-05-10; normal-speed/acceleration test context and slicer settings.
- [Extruder PA synchronization with input shaping](https://klipper.discourse.group/t/extruder-pa-synchronization-with-input-shaping/3843) — 2022-08-14; developer discussion of PA smoothing and input-shaper timing.

### Input shaping and resonance

- [New resonance testing method](https://klipper.discourse.group/t/new-resonance-testing-method/3215) — 2022-era feature discussion; test isolation and accelerometer procedure.
- [Is the input shaper lying?!](https://klipper.discourse.group/t/is-the-input-shaper-lying/1955) — 2022-02-03; distinguishes software smoothing recommendation from physical acceleration capability.
- [Input Shaper - Why do low frequencies equal low accelerations?](https://klipper.discourse.group/t/input-shaper-why-do-low-frequencies-equal-low-accelerations/9025) — 2023-06-18; maintainer explanation of smoothing and acceleration implications.
- [Interpreting the Input Shaper Graphs](https://klipper.discourse.group/t/interpreting-the-input-shaper-graphs/9879) — 2023-08-11; Knowledge Base article on PSD, shaper score, smoothing, and mechanical clues.
- [Dynamic input shaper](https://klipper.discourse.group/t/dynamic-input-shaper/9110) — 2023-06-23; maintainer explanation of why changing shapers while moving is difficult.
- [How to interpret this resonance graph?](https://klipper.discourse.group/t/how-to-interpret-this-resonance-graph/17290) — 2024-06-26; bed-slinger interpretation and per-axis configuration.
- [Is input shaping implemented as a FIR-filter?](https://klipper.discourse.group/t/is-input-shaping-implemented-as-a-fir-filter/20788) — 2024-12-20; Kevin O’Connor explains the continuous-motion implementation analogy.
- [Klipper v0.13.0 Release!](https://klipper.discourse.group/t/klipper-v0-13-0-release/22958) — 2025-04-12; release context for sweeping-vibrations testing and motion-limit changes.

### Rotation distance

- [Rotation_distance clarification](https://klipper.discourse.group/t/rotation-distance-clarification/138) — 2021-04-15; formula direction and why a larger value produces less movement.
- [How to change Rotation distance in the Gcode ...](https://klipper.discourse.group/t/how-to-change-rotation-distance-in-the-gcode-on-the-x-on-y-axis/1476) — 2021-12-05; experienced guidance not to use hardware calibration for shrinkage compensation.
- [MCU ... shutdown: Rescheduled timer in the past — maybe a rotation_distance problem](https://klipper.discourse.group/t/mcu-mcu-shutdown-rescheduled-timer-in-the-past-maybe-a-rotation-distance-problem/1849/2) — 2022-01-21; dangerous Z value / homing-speed interaction.
- [Rotational distance changes not working](https://klipper.discourse.group/t/rotational-distance-changes-not-working/10694) — 2023-09-26; hardware-derived belt distance versus dimensional-print measurements.
- [Repeating Error “rotation_distance”](https://klipper.discourse.group/t/repeating-error-rotation-distance/658) — 2021-08-04; case-sensitive section naming and configuration diagnosis.

### Firmware retraction and macros

- [Firmware retraction Z-HOP](https://klipper.discourse.group/t/firmware-retraction-z-hop/2662) — 2022-04-21; community macro, explicit alpha status, dependencies, and failure risks.
- [Why is the filament being retracted?](https://klipper.discourse.group/t/why-is-the-filament-being-retracted/16830) — 2024-06-04; PA can create reverse extruder motion even with monotonically increasing E values.
- [Non-print moves?](https://klipper.discourse.group/t/non-print-moves/9232) — 2023-07-01; distinction between firmware retraction speed and toolhead travel speed.
- [Macro Creation Tutorial](https://klipper.discourse.group/t/macro-creation-tutorial/30) — early forum tutorial; parameterized start macro and PA example.
- [Save/restore gcode state in updated pause/resume macros](https://klipper.discourse.group/t/save-restore-gcode-state-in-updated-pause-resume-macros/1995) — 2022-02-08; base pause/resume already saves/restores state.

### Motion limits

- [Need set max_velocity low or high for speed up?](https://klipper.discourse.group/t/need-set-max-velocity-low-or-hight-for-speed-up/1874) — 2022-01-24; definitions and practical interaction of velocity and acceleration.
- [Macro to change M220 automatically](https://klipper.discourse.group/t/macro-to-change-m220-automatically/8387) — 2023-05-14; acceleration often matters more than speed for short segments.
- [Finding out max velocity cpu/bandwidth limits](https://klipper.discourse.group/t/finding-out-max-velocity-cpu-bandwith-limits/19368) — 2024-10-13; measured MCU step-rate bottleneck on an ATmega2560 system.
- [Acceleration control after gcode start](https://klipper.discourse.group/t/acceleration-control-after-gcode-start/22611) — 2025-03-22; current config-reference context including `minimum_cruise_ratio`.

### Hardware and failure diagnosis

- [Mcu shutdown when homing](https://klipper.discourse.group/t/mcu-shutdown-when-homing/2254) — 2022-03-08; `Timer too close` and host-load possibilities.
- [Timeout with MCU / Lost communication with MCU](https://klipper.discourse.group/t/timeout-with-mcu-lost-communication-with-mcu/6639) — 2023-02-13; Knowledge Base troubleshooting framework.
- [Failed print ... Timer too close](https://klipper.discourse.group/t/failed-print-due-to-following-error-message-transition-to-shutdown-state-previous-mcu-mcu-shutdown-timer-too-close/9225) — 2023-07-01; log-level interpretation of delayed MCU scheduling.
- [MCU shutdown: Timer too close - OctoEverywhere Triggered](https://klipper.discourse.group/t/mcu-mcu-shutdown-timer-too-close-octoeverywhere-triggered/9901) — 2023-08-12; community report linking remote webcam load with intermittent failure.
- [Klipper state: Disconnect, Ready, Shutdown](https://klipper.discourse.group/t/klipper-state-disconnect-ready-shutdown/14716) — 2024-03-06; ADC/MCU temperature diagnosis.
- [Klipper Starts up and then gives error ... Invalid oid type](https://klipper.discourse.group/t/klipper-starts-up-and-then-gives-error-klipper-mcu-mcu-shutdown-invalid-oid-type/20387) — 2024-12-01; maintainer says spontaneous MCU reset is likely hardware instability; reflash/update as diagnostic.
- [Mcu losing connection mid print after fresh install?](https://klipper.discourse.group/t/mcu-losing-connection-mid-print-after-fresh-install/24856) — 2025-09-14; individual report ultimately implicating mains grounding.

## CLAIMS

### Pressure advance

1. **PA is a dynamic extrusion correction, not a substitute for fixing a bad extruder path.** Under-extrusion at starts/ends or a very high PA value should trigger checks for Bowden length/quality, couplings, extruder condition, temperature, and achievable speed. **Condition:** interpret a PA result only after the hotend/extruder path is mechanically sound and the test is printed at a meaningful speed. **Evidence B/C:** developer PA discussion and experienced diagnosis in [Extruder PA synchronization](https://klipper.discourse.group/t/extruder-pa-synchronization-with-input-shaping/3843) and [Start end extrusion problems](https://klipper.discourse.group/t/start-end-extrusion-problems/6159). **Evidence D:** a 2024 user saw apparent reverse filament motion with PA=1.04; the reply listed long/poor Bowden and couplings as likely contributors ([thread](https://klipper.discourse.group/t/why-is-the-filament-being-retracted/16830)).

2. **Calibrate PA with the motion conditions that expose it.** Use a test speed around 100 mm/s or the intended production speed/acceleration, disable slicer-side extrusion optimizations, and avoid mixing firmware PA and slicer PA during the same experiment. **Condition:** the test object must contain sufficiently rapid flow changes; a slow test can hide the effect. **Evidence C:** [Start end extrusion problems](https://klipper.discourse.group/t/start-end-extrusion-problems/6159), [Questions related to Tuning pressure advance](https://klipper.discourse.group/t/questions-related-to-tuning-pressure-advance/23369). This is guidance, not a universal required speed.

3. **`TUNING_TOWER`’s `START` is a PA value, not a measured height.** The calculated result is `pressure_advance = start + measured_height * factor`; setting `START=20` means PA starts at 20, which is normally nonsensical. **Condition:** when narrowing a range, convert the desired PA interval into a valid start and factor rather than reusing the visual height as the PA value. **Evidence C:** [Pressure Advance Custom Start and Factor](https://klipper.discourse.group/t/pressure-advance-custom-start-and-factor/13025).

4. **A slicer-issued PA command overrides the runtime value from `printer.cfg`, but does not rewrite the config default.** **Condition:** after a print/restart, the configured value returns unless the slicer emits another command. Decide whether the slicer should own per-filament PA or the firmware should provide a fallback, and avoid two competing owners. **Evidence C:** [Regarding the issue of setting pressure advantage](https://klipper.discourse.group/t/regarding-the-issue-of-setting-pressure-advantage/15845).

5. **For multiple extruders, quote the embedded `SET_PRESSURE_ADVANCE` command and specify `EXTRUDER=`.** **Condition:** otherwise `TUNING_TOWER` can parse the command boundary incorrectly or fail to infer the active extruder stepper. **Evidence C:** [Unable to infer active extruder stepper](https://klipper.discourse.group/t/why-am-i-getting-unable-to-infer-active-extruder-stepper-when-trying-to-do-a-pressure-advance-tuning-tower/10740).

6. **PA and input shaping are separate filters but can interact through timing/smoothing.** **Condition:** especially when X and Y resonances differ materially or PA smooth time differs from shaper duration, artifacts may not match a simple “PA only” expectation. **Evidence B:** developer discussion in [Extruder PA synchronization with input shaping](https://klipper.discourse.group/t/extruder-pa-synchronization-with-input-shaping/3843).

### Input shaping and resonance

7. **The shaper report’s acceleration number is a smoothing-related recommendation, not proof that the printer can physically run that acceleration.** **Condition:** choose final acceleration from the mechanical system, thermal/current limits, motion quality, and print results; do not simply copy a 20,000 mm/s² report into a bedslinger. **Evidence B/C:** [Is the input shaper lying?!](https://klipper.discourse.group/t/is-the-input-shaper-lying/1955), [Interpreting the Input Shaper Graphs](https://klipper.discourse.group/t/interpreting-the-input-shaper-graphs/9879).

8. **Lower resonances are more costly than higher resonances because they require more aggressive, more smoothing shapers.** **Condition:** mechanical work should aim to move low peaks upward or eliminate them before accepting a heavily smoothing shaper. **Evidence B:** [Interpreting the Input Shaper Graphs](https://klipper.discourse.group/t/interpreting-the-input-shaper-graphs/9879).

9. **A clean resonance graph is not required to have one giant peak, and high PSD is not automatically bad.** Broad spectra, unusually low PSD, or strong auxiliary-axis content can indicate binding or other mechanical problems, but the graph alone cannot identify the root cause. **Condition:** use the graph as a screening signal, then inspect belts, rails, wheels, frame, toolhead, bed, and wiring. **Evidence B:** Knowledge Base guidance in [Interpreting the Input Shaper Graphs](https://klipper.discourse.group/t/interpreting-the-input-shaper-graphs/9879).

10. **Measure and configure both X and Y even on a bed-slinger.** **Condition:** Y-bed motion can excite measured X/Z components, but the practical configuration still uses per-axis X/Y shaper settings; do not substitute a single visual peak for Klipper’s recommended shaper without understanding the score/smoothing trade-off. **Evidence C:** [How to interpret this resonance graph?](https://klipper.discourse.group/t/how-to-interpret-this-resonance-graph/17290) and the Knowledge Base article above.

11. **Do not change the input shaper dynamically during arbitrary motion.** **Condition:** changing the filtered command while the step generator is active can require a flush/stop and create artifacts; if resonances vary across the volume, measure multiple representative toolhead positions and calibrate against the combined data. **Evidence B:** [Dynamic input shaper](https://klipper.discourse.group/t/dynamic-input-shaper/9110).

12. **Resonance-test setup matters.** Turn off PA and input shaping for the test, remove avoidable noise sources, use the documented resonance-test mechanism, and mount the accelerometer rigidly and consistently. **Condition:** older forum procedures may describe raw accelerometer collection; current releases include sweeping-vibrations testing, so match the procedure to the installed Klipper version. **Evidence B/C:** [New resonance testing method](https://klipper.discourse.group/t/new-resonance-testing-method/3215), [Klipper v0.13.0 Release](https://klipper.discourse.group/t/klipper-v0-13-0-release/22958).

### Rotation distance, retraction, macros, and limits

13. **`rotation_distance` describes hardware kinematics, not filament flow or shrinkage compensation.** For a belt axis, belt pitch × pulley teeth is the mechanical basis; for an extruder, calibrate the actual drive system. Use slicer flow/material settings for filament-dependent flow and slicer scaling for shrinkage. **Evidence C:** [How to change Rotation distance ...](https://klipper.discourse.group/t/how-to-change-rotation-distance-in-the-gcode-on-the-x-on-y-axis/1476), [Rotational distance changes not working](https://klipper.discourse.group/t/rotational-distance-changes-not-working/10694), [Rotation Distance calibration](https://klipper.discourse.group/t/rotation-distance-calibration/1280).

14. **The correction formula has inverse direction:** `new_rotation_distance = old_rotation_distance * actual_extrude_distance / requested_extrude_distance`. A larger rotation distance commands fewer motor steps for a given requested distance. **Evidence C:** [Rotation_distance clarification](https://klipper.discourse.group/t/rotation-distance-clarification/138).

15. **Extreme rotation-distance values can create implausible motor speeds and secondary MCU errors.** **Condition:** verify the mechanical calculation before compensating with lower homing speed or arbitrary distances, especially on Z. **Evidence C:** [Rescheduled timer in the past — maybe a rotation_distance problem](https://klipper.discourse.group/t/mcu-mcu-shutdown-rescheduled-timer-in-the-past-maybe-a-rotation-distance-problem/1849/2).

16. **Firmware retraction controls extrusion retraction; it does not automatically make travel moves fast.** **Condition:** travel velocity remains governed by the travel G-code and printer/slicer limits. **Evidence C:** [Non-print moves?](https://klipper.discourse.group/t/non-print-moves/9232).

17. **Community firmware-retraction Z-hop macros are not equivalent to core Klipper support.** **Condition:** review dependencies such as `[save_variables]` and `[respond]`, test close to the printer, and treat macros that override G0/G1/G2/G3 as risky; the author explicitly reported bugs and alpha-level status. **Evidence D:** [Firmware retraction Z-HOP](https://klipper.discourse.group/t/firmware-retraction-z-hop/2662).

18. **Do not duplicate base pause/resume state handling blindly.** Klipper’s built-in pause/resume already saves/restores state; custom macros should use `rename_existing` and `BASE_PAUSE`/`BASE_RESUME` deliberately, or they can introduce double-saving, unsafe moves, or stale state. **Evidence C:** [Save/restore gcode state ...](https://klipper.discourse.group/t/save-restore-gcode-state-in-updated-pause-resume-macros/1995).

19. **`max_velocity` and `max_accel` are ceilings, not promises.** The slicer requests motion up to those ceilings, but short segments often never reach nominal velocity; acceleration can dominate print time. **Condition:** tune them against mechanics and the actual move-length distribution, not just a long straight-line test. **Evidence C:** [Need set max_velocity ...](https://klipper.discourse.group/t/need-set-max-velocity-low-or-hight-for-speed-up/1874), [Macro to change M220 automatically](https://klipper.discourse.group/t/macro-to-change-m220-automatically/8387).

20. **Input-shaper recommendations, MCU step rate, and physical limits are independent constraints.** **Condition:** a printer can be limited by mechanical ringing, shaper smoothing, motor/driver current, or MCU bandwidth; raising one limit does not solve the others. **Evidence B/C:** [Finding out max velocity cpu/bandwidth limits](https://klipper.discourse.group/t/finding-out-max-velocity-cpu-bandwith-limits/19368), [Acceleration control after gcode start](https://klipper.discourse.group/t/acceleration-control-after-gcode-start/22611).

### Hardware and failure diagnosis

21. **“MCU shutdown” is a symptom class, not a diagnosis.** Start with the exact preceding error in `klippy.log`; then separate host scheduling, serial/USB/CAN communication, power/grounding, thermals, configuration, and firmware/MCU reset hypotheses. **Evidence B:** [Timeout with MCU / Lost communication with MCU](https://klipper.discourse.group/t/timeout-with-mcu-lost-communication-with-mcu/6639).

22. **`Timer too close` can be host overload, but the forum evidence does not justify assuming the SBC is always at fault.** Check CPU pressure, swap/storage faults, thermal/voltage stability, cameras/remote streaming, and log timing; also consider board step-rate limits and electrical noise. **Evidence B/C:** [Mcu shutdown when homing](https://klipper.discourse.group/t/mcu-shutdown-when-homing/2254), [Failed print ... Timer too close](https://klipper.discourse.group/t/failed-print-due-to-following-error-message-transition-to-shutdown-state-previous-mcu-mcu-shutdown-timer-too-close/9225), [Finding out max velocity cpu/bandwidth limits](https://klipper.discourse.group/t/finding-out-max-velocity-cpu-bandwith-limits/19368).

23. **Grounding, connectors, cable routing, power supply, and USB/CAN integrity are first-class suspects for intermittent communication faults.** **Condition:** verify mechanically and electrically before repeatedly reflashing firmware. **Evidence B/C:** [Timeout with MCU / Lost communication with MCU](https://klipper.discourse.group/t/timeout-with-mcu-lost-communication-with-mcu/6639); **Evidence D:** a 2025 user reported the fault stopped after replacing an ungrounded mains cable ([Mcu losing connection mid print](https://klipper.discourse.group/t/mcu-losing-connection-mid-print-after-fresh-install/24856)).

24. **A spontaneous MCU reset or invalid OID should be treated as hardware/firmware instability until proven otherwise.** Update host Klipper, rebuild/reflash the MCU as a diagnostic, inspect wiring and power, and collect a fresh full log. **Evidence B:** Kevin O’Connor’s response in [Invalid oid type](https://klipper.discourse.group/t/klipper-starts-up-and-then-gives-error-klipper-mcu-mcu-shutdown-invalid-oid-type/20387).

25. **ADC out-of-range errors require checking the exact sensor/MCU reading, not just replacing motion hardware.** **Condition:** inspect the startup log and thermistor/MCU-temperature configuration; false or spurious MCU temperature readings can produce a shutdown. **Evidence C:** [Klipper state: Disconnect, Ready, Shutdown](https://klipper.discourse.group/t/klipper-state-disconnect-ready-shutdown/14716).

## PROCEDURES

### Recommended evidence-aware tuning sequence

1. Record printer model/kinematics, Klipper commit or release, host/SBC, MCU(s), extruder type, nozzle, filament, slicer, and the exact config sections relevant to the test.
2. Establish mechanical baseline: belt/rail/wheel condition, gantry squareness, toolhead/bed rigidity, extruder and Bowden path, hotend temperature control, and wiring/grounds.
3. Set hardware-derived `rotation_distance`; do not use it to encode material flow, shrinkage, or visual dimensional compensation.
4. Calibrate extrusion/flow and temperature before interpreting PA. Select one PA owner for the test: firmware `TUNING_TOWER` or slicer-emitted PA, not both.
5. Run PA at intended production speed/acceleration or above, with coasting/pressure equalizer/dynamic acceleration and similar extrusion optimizations disabled. Use a meaningful test speed; 100 mm/s is a commonly cited example, not a universal requirement.
6. Convert the selected tower height to PA using the formula and store per-filament values in the chosen owner (slicer profile or firmware fallback).
7. Run resonance testing with PA/input shaping disabled, a rigidly mounted accelerometer, and a version-appropriate resonance procedure. Measure both X and Y and more than one representative position if resonance changes across the volume.
8. Inspect the report for shaper type/frequency, residual vibration, smoothing, recommended acceleration, and mechanical warning patterns. Treat the acceleration figure as a shaping/smoothing constraint, then validate a lower physical acceleration with prints.
9. Set `max_velocity`, `max_accel`, `square_corner_velocity`, and current-version motion parameters. Remember that short moves may be acceleration-limited and that the MCU may be step-rate-limited before the host appears busy.
10. Add firmware retraction only after basic extrusion and PA behavior is understood. Treat custom Z-hop/retraction macros as untrusted code: validate dependencies, test with low Z risk, and keep a recovery path.
11. For failures, save the full `klippy.log`, exact error text, current config, version, and reproduction conditions before changing several variables at once. Work from the earliest causal-looking log event, not the final generic shutdown state.

### PA tower sanity checks

- Confirm `START` is a PA value and `FACTOR` has the intended units/range.
- For multiple extruders, use a quoted `SET_PRESSURE_ADVANCE EXTRUDER=...` command inside `TUNING_TOWER`.
- Ensure the tower is not being overridden by slicer PA commands or vice versa.
- If PA appears ineffective, verify the test is actually changing PA, the configured nozzle/extruder context is correct, and the print speed/acceleration is sufficient.

### Resonance sanity checks

- Disable PA and input shaping during measurement.
- Mount the accelerometer rigidly on the moving assembly appropriate to the axis being measured.
- Measure both X and Y on bed-slingers; do not infer the whole machine from one graph.
- Treat broad/low/auxiliary-axis-heavy spectra as prompts for mechanical inspection, not as proof of one specific fault.
- Prefer current release tooling; 2025 release notes mention sweeping-vibrations testing.

### Failure triage

1. Capture the first MCU/host error and timestamp.
2. Check whether the failure correlates with heating, homing, high step rate, webcam/remote access, or a specific G-code region.
3. Inspect cables, connectors, grounding, PSU, USB/CAN routing, and board temperature.
4. Check host CPU, storage, swap, thermal and voltage state.
5. Check configuration extremes: implausible rotation distance, aggressive Z speed, excessive acceleration, unsupported macro overrides.
6. Update/rebuild/reflash only after preserving logs, and verify that the new failure mode is compared against the old one.

## NUMERICAL_VALUES

These values are preserved as context from the corpus, not recommended defaults:

| Value | Context | Interpretation |
|---|---|---|
| 100 mm/s | PA calibration examples | Common minimum/example speed to make PA effects visible; use intended production conditions where possible. |
| 0.020 factor | Official-style PA tower examples | Example tower increment factor, not a universal material value. |
| `PA=1.04` | Bowden printer report | Very high in that printer context; prompted checks of Bowden/extruder mechanics. |
| 0.4 mm / 0.3 mm | PA test discussion | 0.3 mm cited as 75% of a 0.4 mm nozzle; forum guidance says a thicker first layer does not necessarily invalidate the test. |
| 50–70 Hz | Input-shaper Knowledge Base | An idealized high single-peak region; not a target that every printer can achieve. |
| 20,000 mm/s² | Input-shaper report example | Software report’s smoothing-related acceleration example; explicitly not a physical-machine guarantee. |
| `max_velocity: 350` mm/s | RF2000/ATmega2560 report | Demonstrated setting before systematic testing; combined XYZ failed around 375 mm/s, and the response identified the MCU as the bottleneck. |
| 450 / 375 mm/s | Same report | X-only versus combined-axis observed limits on that specific ATmega2560 setup. |
| `square_corner_velocity: 5` mm/s | Current/reference config discussions | Common default/reference; setting 1 can make 90° corners nearly stop. Not a universal tuning target. |
| `max_accel: 1600` mm/s² | Bedslinger discussion | Described as reasonable but conservative for that printer; context-specific. |
| 2 mm belt pitch × 20 teeth = 40 mm | CR10S/Voron-related rotation discussion | Mechanical belt-axis calculation example; do not replace with dimensional-shrinkage compensation. |
| `z_homing_speed: 2–5` mm/s | Extreme rotation-distance diagnosis | Suggested temporary mitigation while correcting an implausible Z rotation distance; not a general Z homing recommendation. |
| `retract_length: 1.5` mm, `retract_speed: 45` mm/s | Community Z-hop macro | Macro example only; not core Klipper defaults. |
| `retract_length: 2.6` mm, `retract_speed: 60` mm/s | FLSUN user report | Printer-specific firmware-retraction configuration accompanying a PA observation. |
| `max_z_velocity: 20`, `max_z_accel: 1300` | 2025 Z-axis input-shaper feature test | Temporary minimums stated for that experimental Z resonance test with default parameters. |

## CONFLICTS_OR_LIMITS

- **Official docs versus forum shorthand:** The forum often says “use 100 mm/s” for PA, while the more defensible rule is to use intended production speed/acceleration or a speed high enough to expose the effect. Treat 100 mm/s as an example.
- **Input-shaper acceleration:** Reports can recommend very high acceleration based on smoothing, while real prints ring at much lower values. This is not a contradiction once software smoothing and physical capability are separated.
- **Graph interpretation:** A broad or low PSD spectrum can indicate binding, but the Knowledge Base explicitly warns that the graph cannot identify the cause by itself.
- **Firmware retraction Z-hop:** The corpus contains a user-authored macro with useful field experience but explicit bugs, dependencies, and risk. It must not be treated as maintainer-supported core behavior.
- **Old motion parameters:** Older threads discuss `max_accel_to_decel`; current Klipper release context identifies it as deprecated/replaced by `minimum_cruise_ratio`. Do not copy old config blocks unchanged.
- **MCU shutdown diagnosis:** “Timer too close”, “lost communication”, “missed scheduling”, “invalid OID”, and “ADC out of range” have overlapping symptoms but different causal paths. The earliest log event and reproduction condition matter more than the UI’s final state label.
- **Community sample bias:** Many threads are troubleshooting cases, so the corpus over-represents failures and confusion. Successful printers and unreported edge cases are not visible.
- **Version drift:** A 2021 procedure may predate current resonance tools, macro behavior, release defaults, or slicer integration. Preserve date/version context when applying it.
- **Search/index limitation:** The corpus was assembled from indexed Discourse results and representative direct threads; it is not a complete scrape of categories, deleted posts, or every maintainer answer.

## GAPS

- No systematic coverage of every kinematics family (delta, CoreXZ, toolchangers, multi-MCU synchronization).
- Limited direct evidence on modern CAN-FD, USB-to-CAN adapters, and EBB toolhead failure patterns beyond general communication guidance.
- Limited quantitative comparison of PA values by filament, nozzle diameter, drive gear, and Bowden/direct-drive geometry; forum anecdotes are too printer-specific for a reliable table.
- Limited current (post-0.13.0) discussion of the sweeping-vibrations method; the release note establishes availability, but the corpus does not validate it across printer types.
- No controlled comparison of slicer-generated PA versus firmware `TUNING_TOWER` under identical G-code and acceleration conditions.
- No exhaustive treatment of motor current, stealthChop/spreadCycle, resonance coupling from fans, or electrical noise spectra.
- No claim that any cited numerical value is a safe default for this project’s target printers.

## CITATIONS

All citations above are permanent Discourse topic URLs where available. Key maintainer/Knowledge Base sources:

- [Interpreting the Input Shaper Graphs](https://klipper.discourse.group/t/interpreting-the-input-shaper-graphs/9879) — Sineos, 2023-08-11.
- [Input Shaper - Why do low frequencies equal low accelerations?](https://klipper.discourse.group/t/input-shaper-why-do-low-frequencies-equal-low-accelerations/9025) — maintainer discussion, 2023-06-18.
- [Dynamic input shaper](https://klipper.discourse.group/t/dynamic-input-shaper/9110) — 2023-06-23.
- [Extruder PA synchronization with input shaping](https://klipper.discourse.group/t/extruder-pa-synchronization-with-input-shaping/3843) — dmbutyugin, 2022-08-14.
- [Timeout with MCU / Lost communication with MCU](https://klipper.discourse.group/t/timeout-with-mcu-lost-communication-with-mcu/6639) — Knowledge Base, 2023-02-13.
- [Klipper v0.13.0 Release!](https://klipper.discourse.group/t/klipper-v0-13-0-release/22958) — koconnor, 2025-04-12.
- [Klipper Starts up and then gives error “Invalid oid type”](https://klipper.discourse.group/t/klipper-starts-up-and-then-gives-error-klipper-mcu-mcu-shutdown-invalid-oid-type/20387) — Kevin O’Connor response, 2024-12-02.

