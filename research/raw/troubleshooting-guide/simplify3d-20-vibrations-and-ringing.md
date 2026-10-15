---
source_block: simplify3d
entry: 20
title: "Vibrations and Ringing"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Vibrations and Ringing

Ringing is a wavy pattern that may appear on the surface of your print due to printer vibrations or wobbling. Typically, you will notice this pattern when the extruder is making a sudden direction change, such as near a sharp corner. For example, if you were printing a 20mm cube, each time the extruder changes to printing a different face of the cube, it would need to change directions. The inertia of the extruder can create vibrations when these sudden direction changes occur, which will be visible of the print itself.

## 1\) Printing too fast

The most common cause for ringing is that your printer is trying to move too fast. When the printer suddenly changes direction, these quick movements will create additional force that can cause the lingering vibrations. If you feel that your printer may be moving too fast, try to reduce the printing speed. To do this, click “Edit Process Settings” and select the Speeds tab. You will want to make adjustments to the “Default Printing Speed” and the “X/Y Axis Movement Speed”. The first controls the speed of any movements where the extruder is actively extruding plastic, while the second controls the speed of rapid movements where no plastic is being extruded. You may need to adjust both settings to see an effect.

## 2\) Firmware acceleration

The firmware that runs on your 3D printer’s electronics typically implements acceleration controls to help prevent sudden direction changes. The acceleration settings will cause the printer to slowly ramp up in speed and then to slowly decelerate before changing directions. This functionality is vital for preventing ringing. If you are comfortable working with your printer’s firmware, you may even want to try decreasing the acceleration settings so that the speed changes more gradually. This can help reduce ringing even further.

## 3\) Mechanical issues

If nothing else has been able to resolving the ringing issues, then you may want to look for mechanical issues that could be causing the excessive vibrations. For example, there could be a loose screw or a broken bracket that is allowing excessive vibrations to occur. Watch your printer closely while it is running and try to identify where the vibrations are coming from. We’ve had many users that eventually traced these issues back to mechanical problems with the printer, so it’s worth checking if none of the suggestions above were able to help.
