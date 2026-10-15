---
source_block: all3dp
entry: 21
title: "Surface Areas Beneath Supports are Rough"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Surface Areas Beneath Supports are Rough

You’ve printed a complex model with supports created with your chosen software. But when it comes to removing the structure, small remnants of material are left on the surface. When you try to sand or remove the remaining material, it ruins the overall effect of the model.

Cause

Supports are an essential part of 3D modelling and a subject that can divide opinion. Many models can actually avoid the need for supports completely with a little adjustment of the model to angle verticals, or with the addition of design integral support structures to the model. You may also be surprised by the full capabilities of your printer, with most being able to bridge 50 mm gaps and print angles of 50º without any support at all. Software solutions such as Cura and Simplify3D are capable of producing outstanding support structures, and for the most part these automatically generated supports will far exceed the quality of any home grown solution. But although auto-generated supports do the job, they can be difficult to remove. Applying your own support structures is a neater solution, but you’ll need to delve into the settings of your software to tailor the supports to your models. Depending on your slicing software, enabling supports will require the activation of a checkbox. There are plenty of associated options that enable you to fine tune the support structure, and minimize the effect that the structures will have on the surface of your models. However, as careful as you are with the support settings, the supports themselves will be bonded to your model, so will always leave some sort of trace mark. The issue of surface finish when supports are used is a big one and the severity of the effect will change depending on the material types you use. A more brittle filament such as PLA is often harder to work and finish than a decent ABS.

## 1\) CHECK SUPPORT PLACEMENT

Most slicing software will allow you choose whether your support structure is touching the build plate or “everywhere”. For most models “Touching the Build Plate” is sufficient. Choosing Everywhere will result in supports… well, everywhere. Which then means, in the context of this 3D printing troubleshooting tip, a rough surface finish all over your print.

## 2\) CHECK THE CAPABILITY OF YOUR PRINTER

Quite often people use supports without realizing that their printer can bridge gaps and print relatively steep angles with ease. Most printers are capable of bridging gaps of 50 mm and printing angles of 50º without error. Create or download a test print to familiarize yourself with the true capability of your printer.

## 3\) ADJUST THE SUPPORT PATTERN

Depending on the model type, a change in the support pattern could be all it takes for a better support-model interface; try switching from “Grid” to “Zig Zag”.

## 4\) REDUCE SUPPORT DENSITY

In your slicer software switch the view to “Layers” and take a look through the support structure. Default software will usually apply a dense support structure. If you reduce this density the support will become weaker, but as long as your printer is finely tuned this shouldn’t be an issue. In Cura a support density of 5 can be used successfully and vastly reduces the effect of the structure on the model’s surface.

## 5\) REDUCE PRINT TEMPERATURE

Double-check the filament temperature range and adjust the hot end temperature to the minimum for the material. This may result in a weaker bond between the layers, but will also make it easier to remove the support structure.

## 6\) DUAL EXTRUSION \& SOLUBLE SUPPORT MATERIALS

An expensive solution, but if the majority of your prints use complex support structures then a dual extrusion printer such as the Ultimaker 3 or the Cel RoboxDual is really the only way to go. Water soluble support materials such as PVA have come into their own, and provide a convenient way to achieve complex prints without completely sacrificing surface finish. Best of all, you can add supports to cavities that previously would have been impossible to remove standard print material supports from, meaning more complex prints are also within your grasp.
