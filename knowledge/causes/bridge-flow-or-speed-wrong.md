---
type: cause
title: "Bridge flow or speed wrong"
description: "Bridge flow above 100 % sags and bulges the layers above; too fast bridges droop."
altLabel: [bridge flow ratio, Brückenfluss]
facets: {phase: [supports-bridges]}
check: "Problems only above bridges; preview shows bridge detection and direction."
fixed_by:
  - {action: "bridge flow back to 1, slow bridges", sets: [{key: bridge_flow_ratio, direction: down}, {key: bridge_speed, direction: down}]}
sources:
  - id: ellis-bulging
    title: "Ellis Print Tuning Guide — Bulging"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/bulging.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Bridge flow or speed wrong

Bridge flow above 100 % sags and bulges the layers above; too fast bridges droop.

**Check:** Problems only above bridges; preview shows bridge detection and direction.

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (bridge flow back to 1, slow bridges) `bridge_flow_ratio` ↓ `bridge_speed` ↓
- **Causes:** [Poor bridges & overhangs](../defects/bridging-overhangs.md) (#2; B) · [Bulging](../defects/bulging.md) (#5; B)
<!-- /generated:relations -->
