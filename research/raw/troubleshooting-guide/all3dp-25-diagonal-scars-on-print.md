---
source_block: all3dp
entry: 25
title: "Diagonal Scars on Print"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Diagonal Scars on Print

Horizontal lines appear across the top layer of your print, usually diagonally from one side to another.

Cause

A 3D print is created by laying down successive layers, one after the other. As each layer is set the print head moves through the X and Y axis. Once the layer is complete the head lifts through the Z-axis and returns to the start point to set down the next layer. It is at this point that visible lines or scaring can occur. These can be caused by a number of printer settings, but in essence, the problem is due to filament oozing or the nozzle physically scratching the surface. Combing is one of the major offenders. Combing confines the print head to the printed area of the model. If there is any excess filament, it oozes across the rest of the print. Alternatively, the head doesn’t lift high enough and the hot nozzle drags across the surface, leaving a scar. Over extrusion is another less common cause, as the head lifts excess drags across the surface leaving a trace of filament. On larger flat surfaces you may see the diagonal line fade across the surface. Too high a temperature is a less likely cause but with some cheaper or older filaments the residual heat of the nozzle can lead to filament oozing from the nozzle, again leaving a trail as the nozzle shifts.

## 1\) COMBING

Combing keeps the print head over the already printed areas of the model and therefore reduces the need for retractions. Whilst this increases print speeds it can cause the scaring. Switch combing off and in most cases, this will clear the problem but expect longer print times.

## 2\) RETRACTION

If you’ve switched off combing and the issue remains, try increasing the retraction amount. If the problem still persists then take a look at over-extrusion or the nozzle temperature.

## 3\) CHECK THE EXTRUSION

How you adjust the flow rate of the filament will vary depending on your printer. Using Cura and the Ultimaker series you’ll find the flow details on the machine in the material settings for the Ultimaker 2, on the Ultimaker 3 you’ll find them in the Custom settings in the Cura software. Reduce the flow rate by 5% and print a calibration cube to check if the filament is extruding correctly and eliminating the issue.

## 4\) NOZZLE TEMPERATURE

The tolerance of good quality filaments should negate the issue in principle, but if your filament has been sitting around for a while, exposed to moisture or sunlight, you may find that the filament’s tolerances to temperature has reduced. Decrease the hot end temperature by 5 ºC and try again.

## 5\)  Z-LIFT

Filament isn’t the only issue; if the head doesn’t lift high enough from the surface of the print then the nozzle itself can cause the scarring as it travels from one layer to another. On older printers you’ll need to re-calibrate if there are no Z-lift or Z-hop settings, otherwise increase Z-Hop or Z-Lift in 0.25mm increments.
