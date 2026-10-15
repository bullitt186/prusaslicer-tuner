---
source_block: all3dp
entry: 15
title: "Infill is Visible from the Outside"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Infill is Visible from the Outside

The final print looks fine but an outline of the internal support structure can be seen through the walls of the print. This is also often referred to as ghosting.

Cause

The issue with ghosting happens due to the infill encroaching into the path of the perimeter. This effect is most visible when your print has thin walls. The problem is caused by the infill structure overlapping with the perimeter line as it’s being laid down. Although this ghosting is an issue it’s actually an important part of the printing process, as it helps the internal structure bond effectively to the external walls. Luckily it’s very easy to overcome. Another cause of ghosting can be that you have set an incorrect wall thickness in relation to the nozzle size that you’re using. In normal printing conditions, wall thickness should be directly related to the nozzle size, so if you have a 0.4mm nozzle the wall thickness should be a multiple of this: 0.4, 0.8, 1.2, and so forth.

## 1\) CHECK THE SHELL THICKNESS

Make sure that the value you have selected for the shell thickness is a multiple of the nozzle size.

## 2\) INCREASE THE SHELL THICKNESS

The easiest solution is to increase the shell thickness. By doubling the size it should cover any overlap caused by the infill.

## 3\)  USE INFILL AFTER PERIMETERS

Most slicing software will enable you to activate Infill prints after perimeters.

● In Cura open up the ‘Expert Settings’ and under the Infill section tick the box next to ‘Infill prints after perimeters’

● In Simply3D Click ‘Edit Process Settings’ then select ‘Layer’ and under ‘Layer Settings’ select ‘Outside-in’ next to the ‘Outline Direction’.

## 4\) CHECK PRINT PLATFORM

Check around the model and if you see that the effect is more prevalent on one side than the other, the effect could be due to calibration. If so run through the usual calibration process.

## 5\) PRINT SHELLS TO YOUR ADVANTAGE

Depending on the type of model that you’re printing you can use the internal and shell printing order to your advantage. When you want a high-quality print with a good surface finish where the actual strength of the model isn’t important, select print from the Outside-in. If however the strength of the print is paramount then select Print from Inside-Out and double the wall thickness. The reason for the difference in strength is that when you print from the Outside-in you eliminate the small amount of overlap that causes the ghosting issue, but this also means that the actual structure won’t create the same bonding strength between the internal and external structure due to the lack of overlap.
