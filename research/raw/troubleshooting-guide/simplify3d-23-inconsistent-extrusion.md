---
source_block: simplify3d
entry: 23
title: "Inconsistent Extrusion"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Inconsistent Extrusion

For your printer to be able to create accurate parts, it needs to be capable of extruding a very consistent amount of plastic. If this extrusion varies across different parts of your print, it is going to affect the final print quality. Inconsistent extrusion can usually be identified by watching your printer closely as it prints. For example, if the printer is printing a straight line that is 20mm long, but you notice that the extrusion seems rather bumpy or seems to vary in size, then you are likely experiencing this issue

## 1\) Filament is getting stuck or tangled

The first thing you should check is the spool of plastic that is feeding into your printer. You need to make sure that this spool is able to rotate freely and that the plastic is easily being unwound from the spool. If the filament becomes tangled, or the spool has too much resistance to spin freely, it will impact how evenly the evenly the filament is extruded through the nozzle. If your printer includes a Bowden tube (a small hollow tube that the filament is routed through), you should also check to make sure that the filament can easily move through this tube without too much resistance. If there is too much resistance in the tube, you may want to try cleaning the tube or applying some lubrication inside the tube.

## 2\) Clogged Extruder

If the filament is not tangled and can easily be pulled into the extruder, then the next thing to check is the nozzle itself. It is possible that there is some small debris or foreign plastic inside the nozzle that is preventing proper extrusion. An easy way to check this is to use Simplify3D’s machine control panel to manually extrude some plastic from the nozzle. Watch to make sure that the plastic is extruding evenly and consistently. If you notice problems, you may need to clean the nozzle. Please consult your manufacturer for instructions on how to properly clean the inside of the nozzle.

## 3\) Very low layer height

If the filament is spinning freely and the extruder is not clogged, it may be useful to check a few settings within Simplify3D. For example, if you are trying to print at an extremely low layer height, such as 0.01mm, there is very little room for the plastic to exit the nozzle. This gap below the nozzle is only 0.01mm tall, which means that the plastic may have a difficult time exiting the extruder. Double check to make sure you are using a reasonable layer height for your printer. You can view this setting by clicking “Edit Process Settings” and selecting the Layer tab. If you are printing at a very small layer height, try increasing the value to see if the problem goes away.

## 4\) Incorrect extrusion width

Another setting to check within Simplify3D is the extrusion width that you have specified for your extruder. You can find this setting by clicking “Edit Process Settings” and going to the Extruder tab. Each extruder can have its own unique extrusion width, so make sure you select the appropriate extruder from the list of the left to view the settings for that specific extruder. If you extrusion width is significantly smaller than your nozzle diameter, this may cause extrusion issues. As a general rule of thumb, the extrusion width should be within 100-150% of the nozzle diameter. If your extrusion width is far below the nozzle diameter (for example, a 0.2mm extrusion width for a 0.4mm nozzle), then your extruder won’t be able to push a consistent flow of filament.

## 5\) Poor quality filament

One of the most common causes of inconsistent extrusion that we have not mentioned yet is the quality of the filament that you are printing with. Low-quality filament may contain extra additives that impact the consistency of the plastic. Others may have an inconsistent filament diameter, which will also cause inconsistent extrusion. Finally, many plastics also have a tendency to degrade over time. For example, PLA tends to absorb moisture from the air, and over time, this will cause the print quality to degrade. This is why many spools of plastic include a desiccant in the packaging to help remove any moisture from the spool. If you think your filament may be at fault, try swapping the spool for a new, unopened, high-quality spool to see if the problem goes away.

## 6\) Mechanical extruder issues

If you have verified everything above and are still having problems with inconsistent extrusion, then you may want to check for mechanical issues with your extruder. For example, many extruders use a drive gear with sharp teeth that bite into the filament. This allows the extruder to move the filament back and forth easily. These extruders also typically include an adjustment that changes how hard the drive gear is pressed into the filament. If this setting is too loose, the drive gear teeth won’t cut far enough into the filament, which impacts the extruder’s ability to accurately control the position of the filament. Check with your manufacturer to see if your printer has a similar adjustment.
