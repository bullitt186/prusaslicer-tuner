---
source_block: simplify3d
entry: 22
title: "Small Features Not Printed"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Small Features Not Printed

Most 3D printers have a fixed nozzle size that determines the part resolution in the XY direction. Popular nozzle sizes are 0.4mm or 0.5mm in diameter. While this works well for most parts, you may start to encounter issues when trying to print extremely thin features that are smaller than the nozzle size. For example, if you were trying to print a 0.2mm thick wall with a 0.4mm diameter nozzle, you may notice that this thin wall does not show up in the Simplify3D preview.

## 1\) Enable single extrusion walls

Simplify3D includes a specialty printing mode specifically for very thin walls and exterior features. To enable this special mode, click “Edit Process Settings”, go to the Advanced tab, and change the External Thin Wall Type to “Allow single extrusion walls”. After you save these settings, if you return to the Simplify3D preview, you will notice that many of these thin features are now printed using these specialty single extrusions.

## 2\) Redesign the part to have thicker features

If you are still having issues printing these thin features, another option is to redesign the part so that it only includes features that are larger than your nozzle diameter. This typically involves editing the 3D model in the original CAD package to modify the size of the small features. Once you have thickened the small features, you can re-import the model into Simplify3D to verify that your printer is capable of reproducing the 3D shape you created.

## 3\) Install a nozzle with a smaller tip size

In many cases, you are not able to modify the original 3D model. For example, it may be a part that someone else designed or one that you downloaded from the internet. In this case, you may want to consider obtaining a second nozzle for your 3D printer that allows it to print smaller features. Many printers have a removable nozzle tip, which makes these aftermarket adjustments quite easy. For example, many users purchase a 0.3mm nozzle as well as a 0.5mm nozzle to provide two options. Consult your printer manufacturer for exact instructions on how to install a smaller nozzle tip size.
