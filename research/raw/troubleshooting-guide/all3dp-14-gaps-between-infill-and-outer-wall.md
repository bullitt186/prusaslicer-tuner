---
source_block: all3dp
entry: 14
title: "Gaps Between Infill and Outer Wall"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Gaps Between Infill and Outer Wall

When you look at the top or bottom of the print, you can see a slight gap between the infill and the outer perimeter walls.

Cause

Gaps between the perimeter and top layers used to be a common problem, but as printer accuracy has improved and the support for different materials extends, it’s now less of an issue than it was. However the new wave of advanced materials is far less forgiving than the likes of PLA and ABS, and we’re starting to see a slight resurgence of the problem. Gaps are caused by the filament used for the infill and outer walls not quite meeting and bonding. Handily, it’s one of the easiest things on this list to fix. The most obvious cause of the problem is that the infill overlap is not set, or it’s set to zero. This means that the slicing software is actually telling the printer not to allow the two parts of the print to meet. Another issue could be the order in which you have set the infill and outer walls to be printed. If you’re printing the perimeter first, then there is generally little or no overlap which can again cause the problem.

## 1\) CHECK THE INFILL OVERLAP

This is by far the most common issue and is really easy to resolve. In your slicing software locate the ‘Infill Overlap’ option and increase the value.

● In Cura, this is set to 15% by default. Raise it to 30%.

● In Simplify3D you’ll find the option in ‘Edit Process Settings > Infill > Outline Overlap’. Again increase the value. This setting is directly linked to the extrusion width, so the % value will be a % of whatever you’re extrusion width is. When adjusting this setting always keep it below 50% or you’ll start to see the effects of the overlap in the outer perimeters of your print.

## 2\) PRINT INFILL BEFORE THE PERIMETER SHELL

If you’re printing with a relatively thin outer wall the structure of the infill can show through. If this happens then you can switch the order by which the printer lays down the infill and perimeter layers. For example, in Cura check to see if you have ‘Infill prints after perimeters’ ticked.

## 3\) INCREASE HOT END TEMPERATURE

Some of the latest advanced materials such as XT-CF20 are a little less forgiving when it comes to spreading due to the carbon fibers that make up part of their structure. When printing with these materials you may find that a slight 5-10º increase in hot end temperature makes all the difference.

## 4\) LOWER PRINT SPEED

Okay, so you may be in a rush to get the printout, but printing at higher speeds can cause all sorts of issues if the printer isn’t perfectly calibrated. If you need to print quickly you can still avoid gaps by decreasing the speed of the top layer.
