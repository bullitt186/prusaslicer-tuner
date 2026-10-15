---
source_block: prusa-kb
entry: 29
title: "Layer Shifting"
origin: https://help.prusa3d.com/category/print-quality-troubleshooting_225
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Layer Shifting

Layer shifting is a printing issue, which causes the layers of the printed object to shift from their intended positions.  It is usually associated with an abnormal movement of the X-axis and/or the Y-axis, leading the extruder head to be misaligned mid-printing.

## 1\) Check your printer’s power mode

Run the printer in Normal mode rather than in the Stealth mode. You can change Power mode in the LCD Menu -> Settings -> Mode. The stealth mode is perfect for small and simple objects. For bigger or more complex prints, the Normal mode is recommended. Also, note that in Stealth mode, the Crash detection feature is not available.

## 2\) Make sure the extruder and the heatbed can move freely

Make sure there are no obstructions in the path of the extruder or heatbed and their bearings. For example, there might be a piece of filament stuck around the belt (usually around the Y-axis pulley) from your previous prints. Another instance of obstruction is when the zip ties or another part of the extruder cable bundle are not arranged according to 5. E-axis assembly. If the cables hit the frame before the extruder assembly does (if it's an MK3) or before the X end-stop does (if it's an MK2/S or an MK2.5) the printer detects an inaccurate end position. See the photo below and make sure the cables are arranged accordingly. Also, verify if the smooth rods don't bear any deep scratches and if the bearings are properly lubricated. According to our testers, the best lubricant is a homogeneous, soft grease with lithium additives, such as the GLEIT-µ HF 400. Another good lubricant is the Mogul LV 2-EP. In general, Super-lube or any other multi-purpose grease will do as well.

## 3\) Check your X/Y axis motors and pulleys

Make sure the X and Y motor is tightened in the motor mount, that the pulley (orange arrows in the picture below) is secured on the motor shaft and aligned with the pulley on the opposite end, and that the pulley can move freely. Both grub screws need to be tight, one of them has to be tightened against the flat part of the motor shaft. A loose pulley is usually the main cause of staircase layer shifts. Both pulleys on both axes also have to be aligned, meaning the motor pulley has to be well centered and the belt has to be moving in a straight line, not traveling from right to left while the pulley is turning.

## 4\) Check the tension of your belts

Check your belt-tension. If you have an MK3 or MK3S, check the Belt Status numbers via LCD menu -> Support -> Belt Status. The values should not be under 240 and above 300, but there is no single ideal value. The number does not represent any quantity.

● If your value is under (or close to) 240, you need to loosen the belt

● If your value over (or close to) 300, you need to tighten the belt

● The values are updated every time you run the Selftest or run the belt test in LCD menu -> Calibration -> Belt test.

The MK2.5S, MK2.5, and lower models do not have the belt status option. The clue we can give you is that the belt should sound roughly like a low bass string when plucked. It should be possible to pinch the two sides together with your thumb and index finger, but you should feel a little bit of resistance.

## 5\) Print geometry and settings

Objects with overhangs are generally harder to print. Some overhangs might even warp upwards during the print, and the nozzle might crash into them. The same can happen in some cases if you choose too small infill percentage when slicing the 3D model. To prevent printing overhangs, you can cut the object (check out our article on the Cut tool). You can also try to increase the print fan speed or increase the Z-hop distance in PrusaSlicer. Print fan speed is found in Filament settings -> Cooling and Z-hop distance in Printer Settings -> Extruder 1.
