---
source_block: simplify3d
entry: 9
title: "Layer Separation and Splitting"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Layer Separation and Splitting

3D printing works by building the object one layer at a time. Each successive layer is printed on top of the previous layer, and in the end this creates the desired 3D shape. However, for the final part to be strong and reliable, you need to make sure that each layer adequately bonds to the layer below it. If the layers do not bond together well enough, the final part may split or separate.

## 1\) Layer height is too large

Most 3D printing nozzles have a diameter between 0.3-0.5mm. The plastic squeezes through this tiny opening to create a very thin extrusion that can produce extremely detailed parts. However, these small nozzles also create some limitations for what layer heights can be used. When you print one layer of plastic on top of another, you want to make sure that the new layer is being pressed against the layer below it so that the two layers will bond together. As a general rule of thumb, you want to make sure that the layer height you select is 20% smaller than your nozzle diameter. For example, if you have a 0.4mm nozzle, you can’t go too far past a layer height of 0.32mm, or each layer of plastic will not be able to properly bond to the layer beneath it. So if you notice that your prints are separating and the layers are not sticking together, the first thing you should check is your layer height compared to the size of your nozzle. Try reducing the layer height to see if it helps the layers bond together better. You can do this by clicking “Edit Process Settings” and selecting the Layer tab.

## 2\) Print temperature is too low

Warm plastic will always bond together much better than cold plastic. If you notice that your layers aren’t bonding together and you are certain that your layer height isn’t too large, then it is possible that your filament needs to be printed at a higher temperature to create a strong bond. For example, if you tried to print ABS plastic at 190C, you would likely find that the layers of your part will easily break apart. This is because ABS typically needs to be printed around 220-235C to create a strong bond between the layers of your print. So if you feel this may be the problem, verify that you are using the correct temperature for the filament you have purchased. Try increasing the temperature by 10 degrees to see if the adhesion improves. You can do this by clicking “Edit Process Settings” and selecting the Temperature tab. Simply double-click the temperature setpoint you wish to change.

## Solution #2

This refers to the de-lamination of the printed layers. It is mostly caused by an incorrect preset/(custom)profile with wrong temperatures and/or too much cooling from either the print fan or the sorrounding environment. Layer-separation is more an issue from the "old days" of unheated print-beds and less accessible materials, past ABS. This is rarely an issue on the MK-series hardware with PrusaSlicer presets, especially with materials like PLA and PETG. It’s not difficult to tell the difference between cracking and missing layers. Best way to identify cracked layers are the clean cuts that show a bit of an upward bend or warp. Layer separation occurs when the object cracks due to forces exerted on the print when layers cool down at different rates. Warping forces exceed the layer adhesion strength and the layers separate.

## 1\) How to prevent Layer separation and Splitting

ABS is highly susceptible to layer separation when there’s any sort of cold air blowing on the print before it has cooled down fully. We suggest turning fans OFF for ABS prints completely. ABS is best printed in an enclosed chamber (even heated). Here we made one from an Ikea Lack table. Please remember that you may probably not be able to print objects covering the whole print area using ABS, so it is better to replace ABS with PETG filament. PETG has similar advantages ABS, but it’s much better for printing large objects and it does not have the same tendency to crack/de-laminate. ASA is also a great alternative but is still more dependent on a stable environment when printing than PETG. PLA may suffer from cracking and layer separation problems if you’re printing with insufficient temperature. Depending on the brand, PLA is printed at a range between 195-220. If you are having issues, try increasing the printing temperature in 5°C increments, until you get a good layer adhesion.

## 2\) Flow-rate / extrusion multiplier

Increase your printer’s flow rate (in PrusaSlicer called extrusion multiplier). More material extruded will create a stronger bond between layers. increase on 5% increments. Extrusion-multiplier is located where you set temperatures, but only accessible when PrusaSlicer is set to Advanced- or Expert-mode.
