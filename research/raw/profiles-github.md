# PrusaSlicer official settings/profile repository research

## SOURCE_METADATA

- **Requested source:** `https://github.com/prusa3d/PrusaSlicer-settings`
- **Inspection date:** 2026-10-13 (Europe/Berlin)
- **Method:** Cloned the requested repository and the four repositories linked by its current README; inspected the INI and IDX primary files directly at the checked-out commits. No search-result snippets were used.
- **Requested repository HEAD:** `a40f669e7c3ff4dfe05a937fc08fc57993dcf0d5` (2026-09-22, “Update PrusaSlicer.version”)
- **Current linked repositories inspected:**
  - `PrusaSlicer-settings-prusa-fff` HEAD `e11094507a9ed229fa1f93057bee4f1d303d877a` (2026-10-02)
  - `PrusaSlicer-settings-prusa-sla` HEAD `2076abb7afba885166b1213620d33e5de4e61625` (2026-09-14)
  - `PrusaSlicer-settings-non-prusa-fff` HEAD `a01e756eceadc4d7b47e56f7296f00e4dd6b85bf` (2026-07-15)
  - `PrusaSlicer-settings-non-prusa-sla` HEAD `fb1d0826d31152c5595dbf1b9a7ba467ed7abfc5` (2024-06-12)
- **Important source qualification:** The requested repository’s README states that it is no longer used for PrusaSlicer 2.8.0 and newer. It redirects Prusa FFF, Prusa SLA, non-Prusa FFF, and non-Prusa SLA profiles to the four repositories above. The current values below therefore come from the redirected repositories, while legacy metadata is reported separately.

## COVERAGE

Inspected:

- legacy `live/{vendor}/{bundle}.ini` layout, `index.idx`, and version metadata;
- current Prusa FFF vendor metadata, printer-model declarations, printer variants, nozzle/high-flow distinctions, print profile inheritance, filament/material inheritance, compatibility conditions, start G-code conditions, and recent changelog entries;
- current Prusa SLA bundle/index metadata and material-profile change history;
- non-Prusa FFF vendor/index structure and a representative current Voron bundle;
- representative numerical values for generic PLA, Prusament PETG, TPU 95A, high-temperature PPS-CF, Core One printer variants, Core One HT print profiles, and Voron common print settings.

Not attempted: exhaustive extraction of every vendor, printer, material, nozzle, or print preset; validation on physical hardware; or normalization of values across printers/materials.

## CLAIMS

### 1. The requested repository is a legacy distribution point, not the current profile data source

**Conditions:** Applies to PrusaSlicer 2.8.0 and newer; legacy `live/` content remains relevant only for older compatibility paths.

- **Evidence A — source:** The requested repository README explicitly says it is no longer used for PrusaSlicer 2.8.0+ and links four replacement repositories.
- **Evidence B — observed:** The legacy repository contains `live/PrusaSlicer.version` with release `2.9.6`, alpha `3.0.0-alpha12`, beta `2.9.6-beta1`, plus `live/PrusaSlicer.version2` containing `2.9.6`.
- **Evidence C — context:** The legacy README documents bundles as `live/{vendor name}/{bundle version}.ini` and vendor `index.idx` files as the compatibility index.
- **Evidence D — tuning implication:** A tuner should resolve current values from the redirected repository matching the technology/vendor; treating the legacy INIs as current can silently miss later printer, nozzle, material, and firmware changes.

### 2. Profile selection is conditional and inheritance-driven; a numeric value is not globally applicable

**Conditions:** The effective value depends on selected vendor, printer model, printer variant/nozzle, material profile, print preset, and compatibility predicates.

- **Evidence A — source:** `PrusaResearch/2.5.11.ini` declares reusable sections such as `[print:*common*]`, `[print:*0.20mm*]`, `[filament:*HT_common*]`, and named printer/material profiles.
- **Evidence B — observed:** Generic PLA high-flow inherits `Generic PLA @PG`, `*PLAHF*`, `*PLA225*`, and `*PA_GenericPLA*`; Core One HT PPS-CF inherits `*HT_common*` and `*C1_HT04*`; Core One HT print profiles inherit a regular Core One print profile plus `*C1_Shared04*` and `*C1_STR*`.
- **Evidence C — context:** Compatibility expressions constrain profiles with predicates such as `printer_model=="COREONE"`, `nozzle_diameter[0]==0.4`, `! nozzle_high_flow[0]`, and printer-note tokens such as `HT400` or `HT_HOTEND_HT`.
- **Evidence D — tuning implication:** Use the resolved profile chain for the exact printer/nozzle/material/print combination. Do not lift a value from a shared section or another nozzle/material variant as a universal recommendation.

### 3. Printer models expose nozzle and hardware variants explicitly

**Conditions:** Applies to the current Prusa FFF bundle, especially Core One, Core One L, MK4-family, and XL models.

- **Evidence A — source:** The Core One model declaration lists variants `HF0.4`, `HF0.5`, `HF0.6`, `HF0.8`, standard `0.25` through `0.8`, and `HT Hotend 0.4/0.6`.
- **Evidence B — observed:** The concrete printer profile `Prusa CORE One HF0.4 nozzle` sets `printer_variant = HF0.4`, `nozzle_diameter = 0.4`, and `nozzle_high_flow = 1`; the HT profile inherits the standard 0.4-nozzle profile but sets `printer_variant = HT Hotend 0.4` and `nozzle_high_flow = 0`.
- **Evidence C — context:** The high-flow profile has a 0.3 mm maximum layer height, while the HT profile has a 0.15–0.3 mm layer-height range, 0.8 mm retraction, 0.6 mm retract lift, and `HT400` printer-note gating.
- **Evidence D — tuning implication:** Nozzle diameter alone is insufficient. High-flow, regular, and HT hotends are separate hardware contexts with different compatible material and print profiles.

### 4. Material profiles are materially different by polymer, printer family, nozzle, and hotend

**Conditions:** Values below are only for the named profile contexts and are not generic material recommendations.

- **Evidence A — source:** `Prusament PETG @HF0.4` inherits the standard PETG profile plus `*PETHF`; its explicit temperature and volumetric-speed values are separate from the 0.6 and 0.8 high-flow variants.
- **Evidence B — observed:** PETG high-flow 0.4 uses 255 °C first-layer and nominal temperature and 24 mm³/s maximum volumetric speed; the 0.6 and 0.8 variants use 255 °C/30 mm³/s and 260 °C/37 mm³/s respectively.
- **Evidence C — context:** `Prusament TPU 95A @COREONE` inherits a MK4 TPU base plus `*FLEXPGC1*`, then overrides cooling, extrusion multiplier, volumetric speed, and temperature for that printer family.
- **Evidence D — tuning implication:** Temperature, cooling, extrusion multiplier, and volumetric speed must be treated as profile-and-hardware-specific. Even within one filament family, changing nozzle/hotend/printer can change the effective values.

### 5. The latest Prusa FFF bundle adds high-temperature Core One support with strong environmental constraints

**Conditions:** Applies to Core One/Core One L HT Hotend profiles and the named high-temperature materials in bundle `2.5.11`.

- **Evidence A — source:** The FFF `index.idx` changelog identifies `2.5.11` as adding HT Hotend support; the bundle declares HT printer and print sections and HT-compatible materials.
- **Evidence B — observed:** Shared HT material defaults include 120 °C bed, 320 °C nozzle, 45 °C minimum chamber, 55 °C nominal chamber, abrasive material flag, and 6.5 mm³/s maximum volumetric speed.
- **Evidence C — context:** The named `Fiberon PPS-CF @COREONE HT0.4` profile overrides those shared defaults to 330 °C nozzle, 110 °C bed, 40 °C minimum chamber, 55 °C chamber, 1.03 extrusion multiplier, 1.29 g/cm³ density, 5 mm³/s volumetric speed, and 10–20% fan limits. It is restricted to Core One HT 0.4 by the inherited compatibility condition.
- **Evidence D — tuning implication:** These are constrained process envelopes, not values to port to standard brass/high-flow profiles. The profile also emits conditional pressure-advance/heatbreak G-code and marks the filament abrasive.

### 6. Print profiles encode quality/speed/strength trade-offs and hardware-specific motion limits

**Conditions:** Applies to the selected named print profile and its inherited printer/nozzle context.

- **Evidence A — source:** The current INI contains nozzle-specific print families, printer-specific compatibility expressions, and separate Core One HT and Core One INDX print sections.
- **Evidence B — observed:** `0.20mm High Temperature @COREONE HT0.4` uses 35 mm/s perimeter, 30 mm/s external/small perimeter, 70 mm/s infill, 30 mm/s bridge and first layer, acceleration up to 2,500 mm/s² for infill, and 0.48 mm nominal/perimeter extrusion widths.
- **Evidence C — context:** The Core One INDX 0.20 mm Balanced HF0.4 profile uses 250 mm/s perimeter and solid-infill speeds, 7,000 mm/s² infill/solid acceleration, 6,000 mm/s² perimeter acceleration, and 5,000 mm/s² external-perimeter acceleration. It inherits an INDX-specific common section and is not a normal Core One HT profile.
- **Evidence D — tuning implication:** Print speed/acceleration values must be attached to the exact printer, firmware/hardware mode, nozzle, and quality/strength intent. Comparing one raw speed number across these profiles is misleading.

### 7. The bundle index is the compatibility and change-history control plane

**Conditions:** Applies when PrusaSlicer downloads or selects setting bundles.

- **Evidence A — source:** `PrusaResearch/index.idx` contains multiple `min_slic3r_version` blocks and ordered bundle changelog entries.
- **Evidence B — observed:** The newest block requires PrusaSlicer `2.9.6` and lists `2.5.11`; older blocks gate versions such as `2.9.4-rc0`, `2.9.3-alpha0`, and `2.8.1-rc0`.
- **Evidence C — context:** Recent entries document additions and targeted changes, including Core One INDX profiles, PETG cooling-threshold updates, support settings, PA changes, MMU3/nozzle additions, and firmware-version notifications.
- **Evidence D — tuning implication:** A profile comparison must record the bundle version and minimum slicer version. Otherwise a change in a tuning value may be confused with a machine-calibration difference.

### 8. Non-Prusa FFF profiles use the same layered model but are vendor-specific

**Conditions:** Applies to the non-Prusa FFF repository and its vendor subdirectories.

- **Evidence A — source:** The Voron `3.0.0.ini` has `[vendor]`, printer-model sections, hidden intermediate `*common*` sections, print sections, filament sections, and printer sections.
- **Evidence B — observed:** Voron V2/Trident/Zero/Switchwire model declarations expose HF and standard nozzle variants and default materials such as Generic ABS, Generic ASA, Generic PLA, and Generic PETG.
- **Evidence C — context:** The Voron common print section sets 0.2 mm layer height, 0.45 mm extrusion width, 15% fill density, 200 mm/s infill speed, 170 mm/s external-perimeter speed, and 4,000 mm/s² default/infill acceleration; these are Voron common-profile defaults, not Prusa machine defaults.
- **Evidence D — tuning implication:** Cross-vendor tuning can reuse the inheritance/condition method, but not the numeric values. Vendor, kinematics, hotend, frame, firmware, and bed-size context remain part of the profile meaning.

### 9. SLA profile data is a separate technology and repository lineage

**Conditions:** Applies to Prusa SLA profiles, not FFF nozzle/material/volumetric-speed tuning.

- **Evidence A — source:** The Prusa SLA repository contains `PrusaResearchSLA/index.idx` and versioned bundles through `1.0.10`.
- **Evidence B — observed:** The SLA index requires PrusaSlicer `2.8.0-alpha0` for the current block and records resin additions/updates, including Prusament Resin Model+ and Resin Basic.
- **Evidence C — context:** SLA material-profile changes concern resin exposure/profile reconstruction and configuration-wizard classification rather than FFF nozzle diameter, chamber, or volumetric flow.
- **Evidence D — tuning implication:** Do not mix FFF and SLA material semantics in a unified numerical tuning table without an explicit technology key.

## PROCEDURES

1. Identify technology (`FFF` or `SLA`) and source lineage. For FFF, select Prusa or non-Prusa repository, then vendor directory and bundle version.
2. Record repository commit, vendor `config_version`, and the applicable `index.idx` `min_slic3r_version` block.
3. Resolve the printer model declaration first: model ID, family, bed geometry, printer variants, default materials, and nozzle/high-flow/HT flags.
4. Resolve the concrete `[printer:...]` profile and collect printer notes. Treat notes as functional compatibility keys when conditions reference them.
5. Resolve the print profile inheritance chain from named profile to hidden `*...*` sections. Preserve later overrides over inherited values.
6. Resolve the filament/material inheritance chain, then apply `compatible_printers_condition` and `compatible_prints_condition` before using any numeric value.
7. Keep values keyed by at least `{vendor, bundle, printer_model, printer_variant, nozzle_diameter, hotend_mode, material_profile, print_profile}`.
8. Separate machine limits, print-profile targets, material targets, and start/end/toolchange G-code behavior. Do not collapse them into a single “recommended setting.”
9. When comparing revisions, diff both the INI and the corresponding `index.idx` changelog/compatibility block; note whether a change is explicit or inherited.
10. Validate any proposed tuning change on the actual printer and filament lot. Repository profiles are starting configurations, not a substitute for calibration or hardware verification.

## NUMERICAL_VALUES

All values below are context-bound observations from the named profiles.

| Context | Value | Interpretation |
|---|---:|---|
| Legacy requested repo `live/PrusaSlicer.version` | release `2.9.6`; alpha `3.0.0-alpha12`; beta `2.9.6-beta1`; rc `2.9.6-rc1` | Legacy distribution metadata |
| Current Prusa FFF `2.5.11` | min slicer `2.9.6` | Current FFF bundle compatibility block |
| Core One HF0.4 printer | nozzle `0.4 mm`; high-flow `1`; max layer `0.3 mm`; min layer `0.07 mm`; retract `0.7 mm`; retract speed `45 mm/s` | Core One standard/high-flow hardware profile |
| Core One HT Hotend 0.4 printer | high-flow `0`; retract `0.8 mm`; retract lift `0.6 mm`; layer range `0.15–0.3 mm`; note token `HT400` | Core One HT hardware profile |
| Prusament PETG @HF0.4 | first/nominal `255 °C`; max volumetric `24 mm³/s` | High-flow 0.4 material context |
| Prusament PETG @HF0.6 | first/nominal `255 °C`; max volumetric `30 mm³/s` | High-flow 0.6 material context |
| Prusament PETG @HF0.8 | first/nominal `260 °C`; max volumetric `37 mm³/s` | High-flow 0.8 material context |
| Prusament TPU 95A @COREONE | extrusion multiplier `1.09`; max volumetric `2.5 mm³/s`; first/nominal `225 °C`; fan min/max/bridge `65%` | Core One TPU profile |
| Shared HT material base | bed `120 °C`; nozzle `320 °C`; chamber min/nominal `45/55 °C`; max volumetric `6.5 mm³/s`; abrasive `1` | HT-family inherited defaults |
| Fiberon PPS-CF @COREONE HT0.4 | nozzle `330 °C`; bed `110 °C`; chamber min/nominal `40/55 °C`; multiplier `1.03`; density `1.29 g/cm³`; max volumetric `5 mm³/s`; fan `10–20%`; bridge `20%` | PPS-CF on Core One HT 0.4 only |
| Core One HT 0.20 High Temperature print | perimeter `35`; external/small perimeter `30`; infill `70`; bridge/first layer `30 mm/s`; default accel `2500`; nominal EW `0.48 mm`; top EW `0.42 mm` | HT print profile |
| Core One INDX HF0.4 0.20 Balanced | perimeter/solid infill `250 mm/s`; infill/solid accel `7000`; perimeter accel `6000`; external perimeter accel `5000` | INDX high-flow balanced profile |
| Voron common print | layer `0.20 mm`; EW `0.45 mm`; fill `15%`; infill `200 mm/s`; external perimeter `170 mm/s`; default/infill accel `4000 mm/s²` | Voron 3.0.0 common FFF profile |

## CONFLICTS_OR_LIMITS

- **Repository identity conflict:** The requested URL is still an active Git repository but its own README says it is obsolete for PrusaSlicer 2.8.0+. Current tuning work must use the redirected repositories.
- **Version-date anomaly:** The checked-out repository metadata contains dates after the research date’s surrounding release history; the report treats the checked-out Git commits and file contents as the authoritative inspected state, not inferred release chronology.
- **Bundle versus effective profile:** A bundle can contain multiple inherited and conditional sections with the same material family. The value visible in one section may not be the final effective value for a selected printer.
- **Nozzle/hotend ambiguity:** Labels such as `HF0.4`, `0.4`, and `HT Hotend 0.4` encode different hardware modes. They must not be reduced to nozzle diameter alone.
- **Firmware coupling:** Start G-code includes firmware checks and version notifications; copying profile values without matching firmware can produce incompatible or misleading behavior.
- **Raw numeric comparability:** Speeds and accelerations are not comparable across printers with different motion systems, hotends, nozzle diameters, input-shaper modes, or intended quality profiles.
- **Physical validation limit:** Repository content documents Prusa’s shipped defaults and compatibility logic; it does not establish that a particular machine, filament lot, environment, or modified printer will print optimally at those values.
- **SLA/FFF separation:** SLA resin exposure data and FFF extrusion/material data require separate schemas and should not be combined by field name alone.

## GAPS

- No exhaustive profile matrix was produced for every vendor, printer, nozzle, material, and print preset.
- No historical diff across every bundle revision was computed; the report uses current checked-out bundles and the changelog entries in `index.idx`.
- No physical print or firmware test was run.
- No independent confirmation was made of whether every profile in the repositories is currently exposed by a specific PrusaSlicer release beyond the repository compatibility metadata.
- The non-Prusa FFF review used Voron as a representative vendor; other vendors may encode different inheritance and condition patterns.
- The current non-Prusa SLA repository is older than the FFF repositories and was only used to confirm technology/repository separation, not to extract a full resin matrix.

## CITATIONS

- [Requested legacy repository README](https://github.com/prusa3d/PrusaSlicer-settings/blob/master/README.md) — deprecation notice, replacement repositories, legacy bundle layout.
- [Legacy `PrusaSlicer.version`](https://github.com/prusa3d/PrusaSlicer-settings/blob/master/live/PrusaSlicer.version) — release/alpha/beta/RC metadata.
- [Current Prusa FFF `index.idx`](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/master/PrusaResearch/index.idx) — bundle compatibility blocks and changelog.
- [Current Prusa FFF bundle `2.5.11.ini`](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/master/PrusaResearch/2.5.11.ini) — vendor, printer-model, printer, print, filament, inheritance, conditions, and numerical values.
- [Current Prusa SLA `index.idx`](https://github.com/prusa3d/PrusaSlicer-settings-prusa-sla/blob/master/PrusaResearchSLA/index.idx) — resin bundle compatibility and material-history entries.
- [Representative non-Prusa FFF Voron `3.0.0.ini`](https://github.com/prusa3d/PrusaSlicer-settings-non-prusa-fff/blob/master/Voron/3.0.0.ini) — vendor, printer-model, common print, filament, and printer-profile structure.
- [Current Prusa FFF repository](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff) — repository scope and current commit history.
- [Current non-Prusa FFF repository](https://github.com/prusa3d/PrusaSlicer-settings-non-prusa-fff) — vendor-directory scope and commit history.
