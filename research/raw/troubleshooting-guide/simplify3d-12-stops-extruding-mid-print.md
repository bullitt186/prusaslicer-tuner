---
source_block: simplify3d
entry: 12
title: "Stops Extruding Mid Print"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Stops Extruding Mid Print

## 1\) Out of filament

This one is pretty obvious, but before checking the other issues, first verify that you still have filament leading into the nozzle. If the spool has run out, you will need to load a new spool before continuing the print.

## 2\) The filament has stripped against the drive gear

During a print, the extruder motor is constantly spinning trying to push the filament into the nozzle so that your printer can keep extruding plastic. If you try to print too quickly or you try to extrude too much plastic, this motor may end up grinding away the filament until there is nothing left for the drive gear to grab onto. If your extruder motor is spinning, but the filament is not moving, then this is likely the cause. Please see the Grinding Filament section for more details on how to resolve the issue.

## 3\) The extruder is clogged

If none of the above causes apply to you, then it is very likely that the extruder is clogged. If this happens in the middle of the print, you may want to check and make sure that the filament is clean and that there is no dust on the spool. If enough dust is attached to the filament, it can cause a clog as it builds up inside the nozzle. There are several other possible causes for a clogged extruder, so please see the clogged extruder description in the Not Extruding at Start of Print section for more details.

## 4\) Overheated extruder motor driver

The extruder motor has to work incredibly hard during your print. It is constantly spinning back and forth, pushing and pulling plastic back and forth. This quick motion requires quite a bit of current, and if the printer’s electronics do not have sufficient cooling, it can cause the motor driver electronics to overheat. These motor drivers typically have a thermal cutoff that will cause the driver to stop working if the temperature gets too high. If this happens, the X and Y axis motors will be spinning and moving the extruder toolhead, but the extruder motor will not be moving at all. The only way to resolve this issue is to turn off the printer and allow the electronics to cool down. You may also want to add an extra cooling fan if the problem continues.
