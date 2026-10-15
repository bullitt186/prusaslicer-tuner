---
source_block: all3dp
entry: 8
title: "Print Doesn't Stick to Print Bed"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Print Doesn't Stick to Print Bed

Losing a print due to it not sticking to the print platform is a common issue and one that’s usually relatively easy to resolve. Unfortunately, a 3D print can break free at almost any time, from the first layer through to the last, which is especially infuriating. Of course, it’s not always the printer’s fault and if you’ve tried to print a model that only has a small amount of contact with the platform then undoubtedly that’s going to be the issue. Imagine you’re trying to print a plane and the only contact the model has with the print platform is the wheels. It’s therefore unlikely to print without some type of build plate adhesion and brim, and that’s before you even start to look at supports.

Cause

The most common cause is simply that the print just doesn’t bond to the surface of the print platform. The filament needs a textured base in order to adhere, so to solve the issue you’ll need to create a better bonding surface. An unlevel print platform can be another major issue. If the platform is uneven then for some parts of the print the nozzle won’t be close enough to the platform to correctly extrude and bond the first layer. Calibration can also be a major issue, over time the distance between the nozzle and platform can increase to the point where the initial layer is dragged rather than pushed into the print platform. In all of these cases you’re likely to see a spaghetti of filament appear above your half-formed model, just filament spaghetti or parts of your model dotted around the print platform.

## 1\) ADD TEXTURE

To increase the chances that filament will bond to the platform you need to add another material to add texture. The most common solution is to apply a thin layer of stick glue to the print platform, which can then be easily washed away with hot water. Another alternative for PLA is to add decorator’s tape. For filaments that require a heated platform of 40º and above, there is a variety of special tapes now available that are a little more heat resistant.

## 2)LEVEL THE PRINT BED

Every printer has a different process for print platform leveling, some like the latest Prusa models utilize an extremely reliable auto leveling system, others such as the Ultimaker have a handy step-by-step approach that guides you through the adjustment process. Refer to your printer’s manual for how to level your print bed.

## 3\) ADJUST THE NOZZLE HEIGHT

If the nozzle is too high then the filament won’t stick to the platform, too low and the nozzle will actually start to scrape the print off. Find the Z-axis offset option in your printer’s settings and make small adjustments — into the positive to raise the nozzle away from the bed, and negative to lower it closer.

## 4\) CLEAN THE PRINT PLATFORM

If you’re printing on a material such as glass, every so often it’s a good idea to give it a good clean, especially if you frequently apply glue. The grease from your fingerprints and the excessive build up of glue deposits can all contribute to the non-stickiness of the print platform.

## 5\) APPLY BUILD PLATE ADHESION

Some models will print fine without a brim, but smaller items and those with only a small footprint in contact with the platform will require some type of Build Plate Adhesion. These can be added in your slicer software- — look for “Brim” and “Raft”. Brim will add a single layer of a specified number of perimeter lines radiating out from where your print makes contact with the print bed; it’s the least wasteful of the two, and in our experience is the better option, provided you don’t mind taking a knife to your print to trim the brim away. Raft adds just that to your print. Depending on the parameters you specify, you will get a shadow of your print’s footprint, printed in a thicker, better-adhering layer. Your print is then printed as usual on top of this. Rafts tend to create a rough, unpleasant surface where it touches your print, and use up more material than a brim. The benefit of a raft though lies in being able to simply snap the part off.

## 6\) ADD SUPPORTS

As well as adding build plate adhesion, if your model has complex overhangs or extremities be sure to add supports to hold the print together during the process.
