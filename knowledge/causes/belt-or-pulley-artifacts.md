---
type: cause
title: "Belt or pulley tooth artifacts"
description: "Belt, pulley or idler teeth print as fine vertical lines at about the tooth pitch (≈2 mm)."
altLabel: [2 mm artifacts, belt teeth, Riemenzahn-Artefakte]
facets: {phase: [mechanics]}
check: "Measure artifact spacing on the wall; ≈2 mm points to belt-path parts."
fixed_by:
  - {action: "fix belt rubbing and pulley height, clean teeth, use quality belts/idlers"}
sources:
  - id: ellis-vfas
    title: "Ellis Print Tuning Guide — VFAs"
    resource: https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/vfas.html
generated:
  by: process:kg-migration
  at: 2026-10-13T23:00:00Z
status: stable
---
# Belt or pulley tooth artifacts

Belt, pulley or idler teeth print as fine vertical lines at about the tooth pitch (≈2 mm).[^ellis-vfas]

**Check:** Measure artifact spacing on the wall; ≈2 mm points to belt-path parts.[^ellis-vfas]

[^ellis-vfas]: Ellis Print Tuning Guide — VFAs

<!-- generated:relations -->
## Relations
- **Fixed by:** (settings only) (fix belt rubbing and pulley height, clean teeth, use quality belts/idlers)
- **Causes:** [VFAs (vertical fine artifacts)](../defects/vfas.md) (#1; B)
<!-- /generated:relations -->
