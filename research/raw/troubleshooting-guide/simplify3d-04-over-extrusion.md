---
source_block: simplify3d
entry: 4
title: "Over-Extrusion"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Over-Extrusion

The software is constantly working together with your printer to make sure that your nozzle is extruding the correct amount of plastic. This precise extrusion is an important factor in achieving good print quality. However, most 3D printers have no way of monitoring how much plastic is actually extruded. If your extrusion settings are not configured properly, the printer may extrude more plastic than the software expects. This over-extrusion will result in excess plastic that can ruin the outer dimensions of your part. To resolve this issue, there are only a few settings you need to verify in Simplify3D. Please see the Under-extrusion section for a more detailed description. While those instructions are for under-extrusion, you will adjust the same settings for over-extrusion, just in the opposite direction. For example, if increasing the extrusion multiplier helps with under-extrusion, then you should decrease the extrusion multiplier for over-extrusion issues.
