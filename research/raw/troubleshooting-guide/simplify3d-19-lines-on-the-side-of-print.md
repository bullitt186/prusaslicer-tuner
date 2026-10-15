---
source_block: simplify3d
entry: 19
title: "Lines on the Side of Print"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Lines on the Side of Print

The sides of your 3D printed part are composed of hundreds of individual layers. If things are working properly, these layers will appear to be a single, smooth surface. However, if something goes wrong with just one of these layers, it is usually clearly visible from the outside of the print. These improper layers may appear to look like lines or ridges on the sides of your part. Many times the defects will appear to be cyclical, meaning that the lines appear in a repeating pattern (i.e. once every 15 layers).

## 1\) Inconsistent extrusion

The most common cause for this issue is poor filament quality. If the filament does not have very tight tolerances, then you will notice this variation on the side walls of your print. For example, if your filament diameter varied by just 5% over the length of the spool, the width of the plastic extruded from the nozzle could change by as much as 0.05mm. This extra extrusion will create a layer that is wider than all the others, which will end up looking like a line on the side of the print. To create a perfectly smooth side wall, your printer needs to be able to produce a very consistent extrusion which requires high-quality plastic.

## 2\) Temperature variation

Most 3D printers use a PID controller to regulate the temperature of the extruder. If this PID controller is not tuned properly, the temperature of the extruder may fluctuate over time. Due to the nature of how PID controllers work, this fluctuation is frequently cyclical, meaning that the temperature will vary with a sine wave pattern. As the temperature gets hotter, the plastic may flow differently than when it is cooler. This will cause the layers of the print to extrude differently, creating visible ridges on the sides of your print. A properly tuned printer should be able to maintain the extruder temperature within +/-2 degrees. During your print, you can use Simplify3D’s machine control panel to monitor the temperature of your extruder. If it is varying by more than 2 degrees, you may need to recalibrate your PID controller. Please consult your printer manufacturer for exact instructions on how to do this.

## 3\) Mechanical issues

If you know that inconsistent extrusion and temperature variation are not to blame, then there may be a mechanical issue that is causing lines and ridges on the sides of your print. For example, if the print bed wobbles or vibrates while printing, this can cause the nozzle position to vary. This means that some layers may be slightly thicker than others. These thicker layers will produce ridges on the sides of your print. Another common issue is a Z-axis threaded rod that is not being positioned properly. For example, due to backlash issues or poor motor controller micro-stepping settings. Even a small change in the bed position can have a major impact on the quality of each layer that is printed.
