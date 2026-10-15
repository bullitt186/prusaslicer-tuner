---
source_block: simplify3d
entry: 13
title: "Weak Infill"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Weak Infill

The infill inside your 3D printed part plays a very important role in the overall strength of your model. The infill is responsible for connecting the outer shells of your 3D print, and must also support the upper surfaces that will be printed on top of the infill.

## 1\) Try alternate infill patterns

One of the first settings you should investigate is the infill pattern that is used for your print. You can find this setting by clicking “Edit Process Settings” and going to the Infill tab. The “Internal Fill Pattern” determines what pattern is used for the interior of your part. Some patterns tend to be more solid than others. For example, Grid, Triangular, and Solid Honeycomb are all strong infill patterns. Other patterns like Rectilinear and Fast Honeycomb may sacrifice some strength for faster printing speeds. If you are having trouble producing strong reliable infill, try a different pattern to see if it makes a difference.

## 2\) Lower the print speed

The infill is typically printed faster than any other portion of your 3D print. If you try to print the infill too fast, the extruder won’t be able to keep up and you will start to notice under-extrusion on the inside of your part. This under-extrusion will tend to create weak, stringy infill since the nozzle is not able to extrude as much plastic as the software would like. If you have tried several infill patterns, but continue to have problems with weak infill, try reducing the print speed. To do this, click “Edit Process Settings” and select the Speeds tab. Adjust the “Default Printing Speed”, which directly controls the speed that is used for the infill. For example, if you were previously printing at 3600 mm/min (60 mm/s), try decreasing that value by 50% to see if the infill starts to become stronger and more solid.

## 3\) Increase the infill extrusion width

Another very powerful feature within Simplify3D is the ability to modify the extrusion width that is used for the infill of your part. For example, you could print the outline perimeters with a very fine 0.4mm extrusion width, but transition to a 0.8mm extrusion width for the infill. This will create thicker, stronger infill walls that greatly improve the strength of your 3D printed part. To adjust this setting, click “Edit Process Settings” and select the Infill tab. The “Infill Extrusion Width” is set as a percentage of the normal extrusion width. For example, if you enter a value of 200%, the infill extrusions will be twice as thick as the outline perimeters. One thing to keep in mind when adjusting this setting is that the software must also maintain the infill percentage that you specify. So if you set the infill extrusion width to 200%, the infill will use twice as much plastic for each line. To maintain the same infill percentage, the infill lines must be spaced further apart.
