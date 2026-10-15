---
source_block: all3dp
entry: 31
title: "Print Has Lost Dimensional Accuracy"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Print Has Lost Dimensional Accuracy

When you’re designing a product in your CAD application, the dimensions you’ve painstakingly planned need to be perfectly reproduced by your 3D Printer. However, when it comes to bolting your product together, you find that all that accurate measurement and design has gone to pot. Nothing aligns, the holes are the wrong size and nothing fits. Print dimension accuracy is actually one of the few areas of 3D printing where it’s highly likely that your printer is absolutely fine. Before checking the printer for faults, double-check that the dimensions of the 3D model are correct.

Cause

Let’s start with the measurements and the most common problem. First of all, check that you’re working in real-world measurements; cm and mm are probably best, although inches are also a workable unit for 3D printing. Mix the two up between your 3D model and slicing engine, and you’ll quickly spot the error. If all is fine with the unit selection, then double-check the physical measurements of the parts. When it comes to measuring, always measure twice! Now if you have separate prints that need to fit together, such as a male-to-female connector, or screw and hole, then make sure the insert is slightly smaller than the hole you’ve created for it. For example, if you have an M5 screw and you’ve created a 5mm diameter hole for it to go in, then it’s not going to fit (at least not without some muscle and determination). In order to solve this, increase the hole size by 0.1mm for a fine print and possibly 0.2mm for a low quality print. Print and try again. If it still doesn’t fit enlarge it a little more. If the hole looks oval, the issue is not necessarily the hole’s size. If you’ve created a low polygon shape, then the likelihood is that your hole is no longer round and instead has slightly straightened edges. When printing an object with holes, always ensure you keep a moderate polygon count to keep those smooth round holes for things to fit in. The same goes for custom shapes that need to fit together. Reducing the polygon count of one object can cause all sorts of issues if the two sections have rounded edges that need to interconnect. Once you’ve finished checking everything with the model’s dimensions, it’s time to turn your attention to the printer. The first few layers are all important when it comes to print accuracy. Print out a test cube 50mm x 50mm and use digital calipers to check the measurements; make sure you print the cube at the same layer height you’ll be printing your final model. Firstly check the overall height to see if it equals 50mm, if it does then all is fine on the Z-axis. If not, then carefully measure the top 20 layers — these should equal 20mm. If this is correct but the overall height is wrong, then it’s likely that the first few layers are causing the issue. To resolve this, check the height of the nozzle from the print platform and that it’s within the margin of error for your printer in relation to the layer height. If your nozzle height is 1mm from the print platform and your layer height is 2mm, you may find too much filament is being laid down in that first layer and causing the issue. If this is the case, either recalibrate your printer and ensure the nozzle to platform distance is increased or reduce the layer height. Now check the X and Y dimensions. If they’re approximately 1mm smaller than they should be but all proportions look correct, it could be due to filament thermal contraction. This is relatively common with ABS; in order to correct this, work out the percentage of error and increase the scale of the print to compensate. Using high-quality filaments is the best way to avoid this. Back to the hole and have a look inside; if the walls look smooth then everything is ok. If you see the layers protruding slightly then this could be a sign that the nozzle is too hot and the filament is oozing after it’s been laid down. If the hole looks oval, then it could be that one of your belts is loose or there is a slight misalignment of the X- and Y- axes. Check all are tight and everything screwed into place as should be.

## 1\) CHECK WORKING UNIT OF MEASUREMENT

In your 3D printing application make sure you have the correct real-world dimensions selected.

## 2\) DOUBLE-CHECK THE MEASUREMENTS

If you’re designing a part that needs to connect with other objects, double-check your measurements and use a digital caliper.

## 3\) OVER-SCALE SCREW HOLES

If you’re making a screw hole, create a virtual 3D M5 screw with a diameter slightly larger than it should be and use this to extract/create a boolean subtraction from the model you need the hole to appear in.

## 4\) INCREASE POLYGON COUNT

Reducing the polygon count of your models can cause issues with the slightly flattened edges. Make sure you keep polygons within a reasonable count for smoother gradients and better fits.

## 5\) TEST PRINTER ACCURACY WITH TEST CUBE

Use a 3D Print Calibration Cube to check the X, Y, and Z dimensions of your print.

## 6\) CHECK NOZZLE TEMPERATURE

Try reducing your print temperature if there are blobs and other stray extrusions on the inside of your print’s holes.

## 7\) CHECK BELTS AND RAILS

Check over the belt tension and make sure all axes are straight and correctly aligned.
