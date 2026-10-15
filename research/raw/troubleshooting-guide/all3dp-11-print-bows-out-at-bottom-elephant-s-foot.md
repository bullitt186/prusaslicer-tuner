---
source_block: all3dp
entry: 11
title: "Print Bows Out at Bottom (Elephant's Foot)"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Print Bows Out at Bottom (Elephant's Foot)

The base of the model is slightly bulging outwards, an effect otherwise known as “elephant foot”.

Cause

This ungainly print defect can be caused by the weight of the rest of the model pressing down on the lower before they have properly cooled back into a solid – this is particularly an issue when your printer has a heated bed.

## 1\) BALANCE BED TEMP \& COOLING

To stop elephant foot from appearing in your 3D prints the base layers of the model need to be cooled sufficiently so that they can support the structure above. Apply too much cooling however, and you risk the base layers warping. Getting the balance right can be tricky, start by lowering the temperature of the print platform by intervals of 5 degrees, (to within +/- 20 degrees of the recommended temperature). If your Bottom / Top Thickness is set to 0.6mm then start the fan at a slightly lower height.

## 2\) LEVEL PRINT BED

More often than not the majority of print issues can be traced back to the level of the print platform. Each printer has a slightly different technique for print platform leveling. Start by calibrating yours according to your printer manufacturer’s recommended procedure. Try printing a calibration cube and watch how the printer lays the filament on the bed. From printing the cube you should easily be able to see if your bed is level from how evenly (or not) your layers are on the bed. Similarly, you will be able to see if the nozzle is too close to the print platform and scraping through the molten filament, or too high and causing the filament to build up and blob.

## 3\) RAISE THE NOZZLE

Just raising the height of the nozzle slightly can often help, but be careful too high and it won’t stick to the platform.

## 4\) CHAMFER THE BASE

Another option is to chamfer the base of your model. Of course, this is only possible if you have either designed the model yourself or you have access to the original file. Start with a 5mm and 45º chamfer, but experiment a little to get the best result.
