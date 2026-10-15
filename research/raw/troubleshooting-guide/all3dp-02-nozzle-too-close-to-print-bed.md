---
source_block: all3dp
entry: 2
title: "Nozzle Too Close to Print Bed"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Nozzle Too Close to Print Bed

Inexplicably, despite loading the filament and the print head moving without a hitch, no filament is depositing on the print bed.

Cause

Quite simply, your nozzle may be too close to the print bed. If you’ve somehow tuned your print bed to mere microns from your nozzle opening, it’s unlikely the melted filament has room to escape. At best your print will be missing its first layers, and have a higher chance of not sticking once the filament does extrude. At worst, you’ll cause a backup of melted filament in your hot end, possibly leading to a blockage.

## 1\) Z-AXIS OFFSET

Just raising the height of the nozzle slightly can often help. Most 3D printers in their system settings will allow you to set a Z-axis offset. To raise your nozzle away from the print bed you’ll need to increase the offset into the positive value. This also works for the reverse, with a negative offset helping to address your prints not sticking to your bed.

## 2\) LOWER THE PRINT BED

Alternatively if your printer allows for it, you can achieve the same effect by lowering your print bed. This is the more troublesome fix though, as it requires you to re-calibrate and level the bed for even prints.
