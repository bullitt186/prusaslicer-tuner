---
type: concept
title: Slicer flow, width and firmware output
description: PrusaSlicer and OrcaSlicer derive extrusion geometry and firmware commands from nozzle, layer, width, material and firmware context; profile values are not portable defaults.
tags: [slicer, prusaslicer, orcaslicer, flow, extrusion-width, gcode, profiles]
generated:
  by: process:source-consolidation-2026-10-13
  at: 2026-10-13T12:00:00Z
status: stable
sources:
  - id: prusaslicer-source
    title: PrusaSlicer source and preset schemas
    resource: https://github.com/prusa3d/PrusaSlicer
  - id: prusa-kb-layers
    title: Prusa Knowledge Base — Layers and perimeters
    resource: https://help.prusa3d.com/article/layers-and-perimeters_1748
  - id: profiles-source
    title: PrusaSlicer settings repositories
    resource: https://github.com/prusa3d/PrusaSlicer-settings
  - id: orca-source
    title: OrcaSlicer source
    resource: https://github.com/SoftFever/OrcaSlicer
  - id: ellis-flow
    title: Ellis Print Tuning Guide — Maximum volumetric flow
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/determining_maximum_volumetric_flow_rate.html
related: [tuning/extrusion-multiplier, fundamentals/layer-height-extrusion-width, slicer/profile-knowledge-map]
---
# Slicer flow, width and firmware output

PrusaSlicer and OrcaSlicer do not treat “flow” as one universal knob. A generated line depends on layer height, requested width, nozzle diameter, filament diameter/flow ratio, speed and the active extrusion mode. The effective result also depends on the selected firmware flavor and custom start G-code. [^prusaslicer-source]

## Geometry and machine limits

PrusaSlicer models a rounded-rectangle extrusion cross-section. In current source, most automatic roles derive a width near `1.125 × nozzle diameter`, while support, support-interface and top-solid roles use different defaults. The percentage base is option-specific; it is not safe to interpret every percentage as “percent of nozzle diameter.” [^prusaslicer-source] [^prusa-kb-layers]

Layer height is constrained by the nozzle and profile limits. Prusa's guidance of roughly 70–80% of nozzle diameter is a starting rule, not a physical universal. Larger nozzles improve throughput and robust wall deposition but reduce detail and may increase warping because more material must cool. [^prusa-kb-layers]

The volumetric relation is:

```text
volumetric_flow = layer_height × extrusion_width × speed
```

The Ellis procedure measures the hotend/material limit empirically and recommends setting a conservative cap below the measured drop-off. [^ellis-flow]

## Profile inheritance and portability

The requested `PrusaSlicer-settings` repository is a legacy distribution point for PrusaSlicer 2.8+; current values live in redirected vendor repositories. Profile inheritance, printer variants, nozzle/HF conditions and material compatibility are part of the profile identity. Do not copy a numeric value between printers or materials without retaining those conditions. [^profiles-source]

## Firmware boundary

The slicer may emit `M572`, `M900 K`, `SET_PRESSURE_ADVANCE`, `G10/G11`, acceleration and fan commands depending on firmware flavor. Klipper, the printer firmware and custom start G-code can override or reinterpret these values. Inspect generated G-code when a profile comparison disagrees with observed behavior. [^prusaslicer-source] [^orca-source]

PrusaSlicer machine limits may be used only for estimates or emitted as commands depending on firmware configuration; firmware remains authoritative. Cooling can also slow moves after nominal toolpaths are generated. [^prusaslicer-source]

## Diagnostic procedure

1. Record slicer, version, printer, nozzle diameter/type, filament product, temperature, layer height, width and firmware.
2. Inspect effective printer, print and filament profile values, including inheritance and overrides.
3. Check generated G-code for extrusion mode, flow/ratio, PA, retraction, acceleration, fan and temperature commands.
4. Measure hotend flow at the intended temperature and nozzle before raising speeds.
5. Change one variable and re-test with the same geometry.

## PrusaSlicer keys

`nozzle_diameter`, `layer_height`, `first_layer_height`, `extrusion_width`, `perimeter_extrusion_width`, `first_layer_extrusion_width`, `extrusion_multiplier`, `filament_diameter`, `filament_max_volumetric_speed`, `max_volumetric_speed`, `use_firmware_retraction`, `retract_length`, `temperature`, `cooling`, `*_acceleration`.

## Conflicts and limits

- PrusaSlicer 3.0 alpha source behavior is not identical to stable 2.9 profiles.
- Ellis flow tables are approximate hardware examples, not transferable hotend specifications.
- OrcaSlicer calibration names such as Flow Ratio do not automatically equal PrusaSlicer Extrusion Multiplier; verify the slicer's implementation and profile field.
- A lower slicer flow cap cannot fix a partial clog, wet filament or incorrect rotation distance.

[^prusaslicer-source]: PrusaSlicer source, preset schemas and G-code writer
[^prusa-kb-layers]: Prusa Knowledge Base — Layers and perimeters
[^profiles-source]: PrusaSlicer settings repository and redirected current profile repositories
[^orca-source]: OrcaSlicer source and calibration/profile implementation
[^ellis-flow]: Ellis Print Tuning Guide — Maximum volumetric flow

<!-- generated:relations -->
## Relations
- **Related:** [Layer height and extrusion width](../fundamentals/layer-height-extrusion-width.md) · [PrusaSlicer profile to knowledge map](profile-knowledge-map.md) · [Extrusion multiplier (flow)](../tuning/extrusion-multiplier.md)
<!-- /generated:relations -->
