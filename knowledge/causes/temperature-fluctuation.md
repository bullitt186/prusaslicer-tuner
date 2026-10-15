---
type: cause
title: Hotend temperature fluctuation
description: A poorly tuned PID loop swings the nozzle temperature cyclically, changing flow layer by layer.
altLabel: [PID not tuned, Temperaturschwankung]
facets: {phase: [thermal]}
check: Temperature graph varies by more than about ±2 °C during printing.
fixed_by:
  - {action: run PID tuning (Klipper PID_CALIBRATE / Prusa firmware)}
sources:
  - id: tsg-s3d
    title: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)
    resource: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - id: tsg-dataset
    title: 'Kang, Ahn, Kim (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, commit cedd5fb'
    resource: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
generated:
  by: process:kg-migration
  at: '2026-10-13T23:30:00Z'
status: stable
---
# Hotend temperature fluctuation

A poorly tuned PID loop swings the nozzle temperature cyclically, changing flow layer by layer.

**Check:** Temperature graph varies by more than about ±2 °C during printing.[^tsg-s3d]

[^tsg-s3d]: Simplify3D Print Quality Troubleshooting Guide (retrieved via the Kang/Ahn/Kim dataset)

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (run PID tuning (Klipper PID_CALIBRATE / Prusa firmware))
- **Causes:** [Lines or ridges on the sides (Z banding)](../defects/z-banding.md) (#2; B)
<!-- /generated:relations -->
