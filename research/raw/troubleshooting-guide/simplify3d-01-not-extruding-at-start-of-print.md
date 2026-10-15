---
source_block: simplify3d
entry: 1
title: "Not Extruding at Start of Print"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Not Extruding at Start of Print

## 1\) Extruder was not primed before beginning the print

Most extruders have a bad habit of leaking plastic when they are sitting idle at a high temperature. The hot plastic inside the nozzle tends to ooze out of the tip, which creates a void inside the nozzle where the plastic has drained out. This idle oozing can occur at the beginning of a print when you are first preheating your extruder, and also at the end of the print while the extruder is slowly cooling. If your extruder has lost some plastic due to oozing, the next time you try to extrude, it is likely that it will take a few seconds before plastic starts to come out of the nozzle again. If you are trying to start a print after you nozzle has been oozing, you may notice the same delayed extrusion. To solve this issue, make sure that you prime your extruder right before beginning a print so that the nozzle is full of plastic and ready to extrude. A common way to do this in Simplify3D is by including something called a skirt. The skirt will draw a circle around your part, and in the process, it will prime the extruder with plastic. If you need extra priming, you can increase the number of skirt outlines on the Additions tab in Simplify3D. Some users may also prefer to manually extrude filament from their printer using the Jog Controls in Simplify3D’s Machine Control Panel prior to beginning the print.

## 2\) Nozzle starts too close to the bed

If the nozzle is too close to the build table surface, there will not be enough room for plastic to come out of the extruder. The hole in the top of the nozzle is essentially blocked so that no plastic can escape. An easy way to recognize this issue is if the print does not extrude plastic for the first layer or two, but begins to extrude normally around the 3rd or 4th layers as the bed continues to lower along the Z-axis. To solve this problem, you can use the very handy G-Code offsets which can be found on the G-Code tab of Simplify3D’s process settings. This allows you to make very fine adjustments to the Z-axis position without needing to change the hardware. For example, if you enter a value of 0.05mm for the Z-axis G-Code offset, this will move the nozzle 0.05mm further away from the print bed. Keep increasing this value by small increments until there is enough room between the nozzle and the build platform for the plastic to escape.

## 3\) The filament has stripped against the drive gear

Most 3D printers use a small gear to push the filament back and forth. The teeth on this gear bite into the filament and allow it to accurately control the position of the filament. However, if you notice lots of plastic shavings or it looks like there is a section missing from your filament, then it’s possible that the drive gear has removed too much plastic. Once this happens, the drive gear won’t have anything left to grab onto when it tries to move the filament back and forth. Please see the Grinding Filament section for instructions on how to fix this issue.

## 4\) The extruder is clogged

If none of the above solutions of the topic are able to resolve the issue, then it is likely that your extruder is clogged. This can happen if foreign debris is trapped inside the nozzle, when hot plastic sits inside the extruder too long, or if the thermal cooling for the extruder is not sufficient and the filament begins to soften outside of the desired melt zone. Fixing a clogged extruder may require disassembling the extruder, so please contact your printer manufacturer before you proceed. We have had great success using the “E” string on a guitar to unclog extruders by feeding it into the nozzle tip, however, your manufacturer should also be able to provide recommendations.
