---
name: prusaslicer-tuner
description: Diagnose 3D print defects (from photos or descriptions) and read, explain, diff or change PrusaSlicer printer/print/filament profiles. Use for stringing, under/over-extrusion, warping, layer shifts, bad first layers, ringing, blobs or any "what should I change in my slicer settings" question, and when asked to tune, compare or edit PrusaSlicer profiles.
---

# PrusaSlicer tuner

- Profiles: PrusaSlicer's data dir (`print/`, `filament/`, `printer/`, `physical_printer/`, `vendor/`). The default is the OS default (macOS `~/Library/Application Support/PrusaSlicer`, Linux `~/.config/PrusaSlicer`, Windows `%APPDATA%\PrusaSlicer`). Override it with `PRUSASLICER_DIR`, e.g. for a synced folder.
- Tool: `python3 ~/.claude/skills/prusaslicer-tuner/profiles.py` (stdlib only; `-h` for help).
- Knowledge: `~/.claude/skills/prusaslicer-tuner/knowledge/`, an OKF v0.2 bundle compiled into a knowledge graph (`knowledge/graph.json`). Concepts: problems (`defects/`), causes (`causes/`), procedures (`tuning/`), materials, hardware, plus generated nodes for slicer keys (`key/<name>`) and firmware parameters (`klipper/…`, `prusa-fw/…`). Typed, qualified edges: problem `caused_by` cause (ranked, evidence A–D), cause `fixed_by` procedure with `sets` key↑/↓, material `prone_to` problem, procedure `calibrates` key, `key/filament_*` `overrides` `key/*`.
- **Navigate the graph, don't read whole docs:** MCP `lookup(term)` (English or German synonyms) → `card(id)` (labels, check, ranked relations; ~1k chars) → `read_knowledge(path)` only when you need the article's detail. Without MCP: `knowledge/graph.json`, or each doc's generated `## Relations` block. Raw source reports in `research/raw/` are not knowledge.
- **Test prints:** MCP `test_prints(match)` (CLI: `test_prints/`) lists the calibration STLs with absolute paths: first-layer patches, labeled EM cubes, Klipper PA tower. Which one to use when, and with which settings, is in the "Test prints" section of `tuning/first-layer-squish.md`, `tuning/extrusion-multiplier.md` and `tuning/pressure-advance.md`. Empty folder: run `test_prints/fetch.sh`.

## How profiles work (read this before reasoning about values)
- User profiles inherit from vendor presets: `inherits = Generic PETG` → `vendor/PrusaResearch.ini [filament:Generic PETG]` → `*PET*` → `*common*`. `profiles.py show` resolves the chain and tags each value with its source:
  - `[user]`: you changed it yourself (it differs from the parent).
  - `[Vendor:Section]`: inherited from a vendor preset.
  - `[default]`: PrusaSlicer's built-in default (`prusaslicer_defaults.ini`; regenerate it after PrusaSlicer upgrades, using the command in `profiles.py`).
- **Filament overrides printer:** `filament_retract_*` and `filament_wipe` take precedence over the printer's `retract_*` and `wipe` unless the value is `nil`. Always read both.
- Pressure advance is **not** a slicer setting. On Klipper printers it lives in `printer.cfg`, or per filament as `SET_PRESSURE_ADVANCE` in `start_filament_gcode`. On Prusa printers it is `M900 K` inside the vendor's `start_filament_gcode`.
- `printer.cfg` also overrides the slicer for firmware retraction (`use_firmware_retraction = 1`), acceleration limits and input shaper.

## Printers and firmware access
Run `profiles.py list` for the profiles and the active presets. `physical_printer/*.ini` holds each printer's host (`print_host`, `host_type`). This tool has **no access to printers or firmware config**. For `printer.cfg`, `pressure_advance`, `[firmware_retraction]`, input shaper, belts or Z offset, use whatever access the environment provides (SSH, Moonraker, a config backup repo), or ask the user.

## Integrating with your own printer context
Facts that live neither in the profiles nor in the knowledge library belong in **your own** skill, agent memory or notes, not in this repo. Examples: your printers' hardware (hardened nozzle, hotend, probe, `max_temp`), hosts and access paths, and your own calibration results per printer × filament. A personal "printer manager" skill can load those facts, configure this MCP server with `PRUSASLICER_DIR`, and send generally valid findings back here as knowledge contributions (see "Extending the knowledge library").

## Workflow: "here's a photo, what do I change?"
1. **Diagnose.** `lookup` the symptom in the user's words, then `card("defects/…")`. Name the defect and the visible evidence. If the photo is ambiguous, list the 2–3 candidate problems and say what would distinguish them. Its `caused_by` list is already ranked cheapest and most likely first; `affects` shows materials prone to it. `card("causes/…")` gives each cause's discriminating `check` and its fixes.
2. **Find the profiles used — from the gcode, not by asking.** If the printer keeps a job history (e.g. Moonraker `/server/history/list`, then `/server/files/gcodes/<file>`), download the gcode and grep the PrusaSlicer config block at the end (`; filament_settings_id =`, `; print_settings_id =`, `; temperature =`, `; extrusion_multiplier =`, `; filament_retract_* =`, …). Check the actual moves too (`G1 E-` retract lengths, Z-hop deltas, `M106` fan values) and the `PRINT_START` line. Ask only when no gcode is reachable; then offer the active presets from `profiles.py list` as the default.
3. **Map the diagnosis to profile keys.** The cause's `fixed_by … sets` edges name the exact keys and direction; `card("key/<name>")` gives the profile type (scope), where it is set (slicer vs `klipper`/`prusa-fw`), what overrides it and which other fixes touch it. `knowledge/slicer/profile-knowledge-map.md` has the precedence and authority rules. Do not recommend a number before the material, nozzle, layer height, speed/flow, temperature, cooling and moisture context is known or marked unknown.
   - **An inherited vendor template is not a reference for another brand.** A third-party filament that inherits `Prusament … @Template` carries Prusament's EM and temperatures. Before calling a user value too high or too low, check the brand-specific evidence (`materials/*.md`, `research/raw/`) or search for reports on that exact product. (Example: for a third-party PC-CF, comparing EM 0.90 with Prusament's 1.04 suggested "too little flow", while that brand's community range is 0.85–1.00.)
   - **Name trade-offs before recommending a change.** A fix for one defect can make another worse (for PC: a lower temperature reduces stringing but makes the surface more matte and the layers weaker). Read the material doc first.
4. **Read the effective values** for the mapped keys:
   `profiles.py show filament "<name>" --grep "retract|^temperature|wipe|start_filament_gcode"` and the same for `printer` and `print`. Use `--overrides` to see only what the user changed, and `diff` to compare against a profile that prints well.
5. **Check the firmware side if relevant** (PA, firmware retraction, accel, input shaping, Z offset) with the firmware access the environment provides (see "Printers and firmware access"). Don't change `printer.cfg` without asking. For Prusa firmware, inspect the generated start G-code and firmware flavor.
   - **Always check the temperature limits** for high-temperature materials: every nozzle and bed target (first layer included) must be 5–10 °C below Klipper `max_temp`. A target equal to `max_temp` shuts the printer down on the first overshoot.
   - Facts the config does not record (for example whether the nozzle is hardened, for abrasive filaments) belong in the user's own printer context (see "Integrating with your own printer context"). If one is missing, ask once and record it there.
6. **Propose** a table ordered cheapest and most likely first, following `tuning/tuning-order.md`. Non-setting causes such as wet filament or mechanics come first when they are more likely. Include the exact profile type/key, current effective value and source annotation, proposed test, expected observation and knowledge link.

   | # | Profile (type) | Key | Current [source] | Proposed | Why | Doc |
   |---|---|---|---|---|---|---|

   Recommend changing **one thing at a time** and suggest a quick test print (e.g. a retraction test or two towers for stringing).
6. **Apply only on request, and ask how for each change:**
   - **In place:** `profiles.py set filament "<name>" key=value …`. This makes a backup in `backups/<timestamp>/` first.
   - **As a copy:** `profiles.py set filament "<name>" key=value … --copy "<name> - tuned"`. This is the only option for vendor presets, since vendor files are never written.
   - **A filament used on several printers:** prefer a per-printer copy (`"<name> @<PRINTER>"` with a `compatible_printers_condition` such as `printer_model=~/.*Voron_v2.*/`) over editing the shared original. Put printer-specific retraction tweaks in its `filament_retract_*` overrides, so the printer profile stays unchanged for other filaments.
   - Afterwards, tell the user to restart PrusaSlicer (the script warns if it is running). If PrusaSlicer is open with that preset modified, saving it in the GUI would overwrite the change.
   - To undo, copy the file back from `backups/`.

## Key glossary (concept → key, profile type)
- Temperature: `temperature`, `first_layer_temperature`, `bed_temperature`, `first_layer_bed_temperature`, `chamber_temperature` (filament)
- Flow: `extrusion_multiplier`, `filament_max_volumetric_speed` (filament); `max_volumetric_speed` (print)
- Retraction: `retract_length`, `retract_speed`, `deretract_speed`, `retract_lift`, `retract_lift_above`/`_below`, `retract_before_travel`, `retract_layer_change`, `wipe`, `retract_restart_extra`, `travel_ramping_lift` (printer); `filament_retract_*`, `filament_wipe` (filament override); `use_firmware_retraction` (printer)
- Cooling: `cooling`, `min_fan_speed`, `max_fan_speed`, `bridge_fan_speed`, `disable_fan_first_layers`, `fan_below_layer_time`, `slowdown_below_layer_time`, `min_print_speed`, `enable_dynamic_fan_speeds`, `overhang_fan_speed_0..3` (filament)
- Speeds and accel: `perimeter_speed`, `external_perimeter_speed`, `small_perimeter_speed`, `infill_speed`, `solid_infill_speed`, `top_solid_infill_speed`, `bridge_speed`, `travel_speed`, `first_layer_speed`, `*_acceleration` (print); `machine_max_acceleration_*` (printer)
- Geometry and quality: `layer_height`, `first_layer_height`, `*_extrusion_width`, `external_perimeters_first`, `seam_position`, `infill_overlap`, `top_fill_pattern`, `elefant_foot_compensation`, `avoid_crossing_perimeters`, `only_retract_when_crossing_perimeters`, `brim_width`, `thick_bridges`, `bridge_flow_ratio` (print)
- PA and custom gcode: `start_filament_gcode` (filament); `start_gcode`, `gcode_flavor` (printer)

## Web research access
- **Reddit** blocks WebFetch, curl (403 or bot wall) and the Chrome extension. Ask the user to paste the thread text right away; don't retry.
- **Printables** model pages return 403, but the GraphQL API works: `curl -s https://api.printables.com/graphql/ -H 'content-type: application/json' -d '{"query":"{ searchPrints2(query: \"stringing test\", limit: 12) { items { id name likesCount downloadCount makesCount summary } } }"}'`, and `print(id: N) { name description likesCount makesCount }` for one model.

## Extending the knowledge library
Rules: `knowledge/maintenance.md`; schema and controlled vocabularies: `knowledge/schema.yaml`. For a new source, put one raw report per URL under `research/raw/` (or a deterministic split script, like `research/import_troubleshooting_guide.py`), record it in `research/coverage.md`, write a mapping table (entry → existing concept / alias / new concept), then consolidate: prefer adding an edge with a new `source`, or an `altLabel`, over a new file. New problems need ranked `caused_by`; new causes need `check` and `fixed_by`; keys in `sets` must exist (`uv run kg.py keys` after regenerating `prusaslicer_defaults.ini`). Run `uv run kg.py fix`: it regenerates `graph.json` and the viewer `build/graph.html`, and refuses to write anything while any error exists. Never hand-edit `<!-- generated:… -->` blocks; never commit knowledge with `--no-verify`.
