---
source_block: simplify3d
entry: 21
title: "Gaps in Thin Walls"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Gaps in Thin Walls

Because your 3D printer includes a fixed size nozzle, you may encounter issues when printing very thin walls that are only a few times larger than the nozzle diameter. For example, if you were trying to print a 1.0mm thick wall with a 0.4mm extrusion width, you may need to make some adjustments to ensure your printer creates a completely solid wall and does not leave a gap in the middle.

## 1\) Adjust the thin wall behavior

The first settings that you need to verify are the dedicated thin wall settings that Simplify3D includes. To view these settings, click “Edit Process Settings” and select the Advanced tab. The software includes several different options for the Internal Thin Wall Type. The default option typically uses something called “gap fill” to fill the small gaps between your thin walls. This will create a back-and-forth infill pattern that adjusts to fill the space between these thin gaps. However, the software also includes another useful option that can fill these thin walls with a single pass. To enable this option, change the Internal Thin Wall Type to “Allow single extrusion fill”. This will use a dynamic single extrusion that will adjust in size to perfectly fill the gap between these walls.

## 2\) Change the extrusion width to fit better

In some cases, you may find that you have better luck changing the size of the plastic that is extruded from the nozzle. For example, if you were printing a 1.0mm thick wall, you could achieve a fast and strong print if your nozzle was setup to create a 0.5mm extrusion. This works best for parts that have fairly consistent wall thicknesses. You can adjust the extrusion width that the software creates by clicking “Edit Process Settings” and selecting the Extruders tab. Choose a manual extrusion width and enter a value of your choosing.
