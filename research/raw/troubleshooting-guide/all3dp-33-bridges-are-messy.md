---
source_block: all3dp
entry: 33
title: "Bridges are Messy"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Bridges are Messy

Bridges are essentially a stretch of plastic that is extruded between two raised points. If you have two columns with a 5 cm gap, then the beam that sits on top between those two points with nothing below is the bridge. Most filament is surprisingly resilient to bridging, and with a finely tuned printer the distance achievable when bridging can be surprising. However, you know something isn’t quite right when your printer starts to fail to bridge even the smallest gap. The most obvious sign is when the printer fails to successfully bridge gaps between 1 and 3 cm. The extrusion may be too thin, filament sags, or simply flows down the height of the bridge rather than across.

Cause

Getting to the bottom of bridging issues is usually pretty easy and much of the diagnosis comes through the look of the failed bridge. It’s also worth noting that the way that different slicer applications handle bridging is very different, with applications such as Simplify3D having a special Bridge option that will adjust extrusion and cooling for the best results. The most common related issue is that the gap you’re trying to bridge is just too big, this distance will vary with each printer and material. You can usually tell if the gap is too great as the filament will start to sag in the middle or collapse. Cooling is another major issue, the filament needs to be cooled quickly in order for it to be able to support itself between the two columns. Extrusion speed is equally important, if the print head moves too quickly then the speed and vibrations will inevitably cause instability before the filament has set. Too high extrusion temperature will often result in bridging, again showing sagging of the filament. If the extruded filament is of different thicknesses then you know this is the issue.

## 1\) CHECK THE BRIDGING CAPABILITIES

You can make a test print with columns and bridges of different distances to check how far your printer will go, start with a 5cm gap and then increase, anything between 5 and 10 is good, 15 would be exceptional.

## 2\) ADD SUPPORTS

A quick and easy fix is to simply add supports below the structure

## 3\) INCREASE FAN SPEEDS

Boost the extrusion fan speed to ensure that the filament cools quickly, the faster the filament sets the larger the bridge it will be able to create.

## 4\) DECREASE EXTRUSION SPEED

Fast extrusion is an absolute no when it comes to bridging, you need slow and steady as the filament needs to have time to set as the distance is bridged.

## 5\) USE SIMPLIFY3D

This dedicated 3D print software features a bridging option and will automatically recognize any areas of your print that require greater cooling and slower extrusion speeds.
