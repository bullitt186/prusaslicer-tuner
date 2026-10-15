---
type: cause
title: Partial clog
description: A restricted nozzle or heatbreak limits flow; the extruder skips and extrusion is thin or stops.
altLabel: [clogged nozzle, blocked nozzle, Teilverstopfung, verstopfte Düse, clogged extruder]
facets: {phase: [extrusion]}
check: Manual extrusion at temperature is weak or deflected; a cold pull pulls debris.
fixed_by:
  - {action: 'cold pull, clean or replace nozzle, check heatbreak'}
sources:
  - id: ellis-extruder-skipping
    title: Ellis Print Tuning Guide — Extruder skipping
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/extruder_skipping.html
generated:
  by: process:kg-migration
  at: 2026-10-13 23:00:00+00:00
status: stable
---
# Partial clog

A restricted nozzle or heatbreak limits flow; the extruder skips and extrusion is thin or stops.

**Check:** Manual extrusion at temperature is weak or deflected; a cold pull pulls debris.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (cold pull, clean or replace nozzle, check heatbreak)
- **Causes:** [Extruder skipping / clicking](../defects/extruder-skipping.md) (#1; B) · [Extrusion stops mid-print](../defects/extrusion-stops.md) (#2; B) · [Inconsistent extrusion](../defects/inconsistent-extrusion.md) (#2; B) · [No extrusion at print start](../defects/no-extrusion-at-start.md) (#4; B) · [Under-extrusion](../defects/under-extrusion.md) (#4; C) · [Weak or messy infill](../defects/weak-infill.md) (#4; C)
<!-- /generated:relations -->
