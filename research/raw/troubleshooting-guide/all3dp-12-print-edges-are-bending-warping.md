---
source_block: all3dp
entry: 12
title: "Print Edges are Bending (Warping)"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Print Edges are Bending (Warping)

At the base of the model, the print bends upwards until it’s no longer level with the print platform. This can also result in horizontal cracks in upper parts and cause your print to come unstuck from the print bed.

Cause

Warping is common as it’s caused by the natural characteristics of plastics. As the ABS or PLA filament cools it starts to contract very slightly; the problem of warping arises if the plastic is cooled too quickly.

## 1\) USE A HEATED PRINT PLATFORM

The easiest solution is to use a heated print platform and set the temperature to a point just below the plastics melting point. This is called the “glass transition temperature”. If you get that temperature right then the first layer will stay flat on the print platform. The print platform temperature is often set by the slicer software. You’ll normally find the recommended temperature for your filament printed on the side of the packaging or on the spool.

## 2\) APPLY AN ADHESIVE TO THE PRINT BED

If you still find your print lifting at the edges then apply a tiny amount of stick glue evenly on the bed to increase adhesion.

## 3\) TRY A DIFFERENT PLATFORM TYPE

Change your print bed to one that offers better adhesion. Manufacturers such as Prusa use a PEI (Polyetherimide) print surface that offers excellent adhesion without glue. XYZPrinting supply textured tape in the box with some of their printers, basically a large sheet of masking tape, and again adding this works excellently, although only with nonheated print platforms. Zortrax 3D printers have a perforated print bed, models weld themselves to this surface eliminating the issue completely.

## 4\) LEVEL THE PRINT PLATFORM

Print platform calibration can be another cause, run through the calibration process to check that the bed is level and nozzle height is correct.

## 5\) INCREASE CONTACT

Increasing the contact between the model and bed is an easy fix and most print software has the option to add rafts or platforms.

## 6\) ADJUST ADVANCED TEMPERATURE SETTINGS

If all else fails then you’ll need to take a look at your advanced print settings both on your printer and in your printer software. Try increasing the print bed temperature by increments of 5 degrees. In the slicer software take a look at the fan cooling, this is usually set so the cooling fans switch to full power at a height of around 0.5mm, try extending this to 0.75 to give the base layers a little more time to cool naturally. Even if your printer has a heated print platform, it’s always recommended that you use glue and regularly calibrate the bed level.
