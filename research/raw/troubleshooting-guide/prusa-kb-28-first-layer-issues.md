---
source_block: prusa-kb
entry: 28
title: "First Layer Issues"
origin: https://help.prusa3d.com/category/print-quality-troubleshooting_225
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# First Layer Issues

This is by far the most common 3D printing problem, and probably the first one you may encounter. The first layer is the essential one because it is the base of the printed object. Therefore, if it isn’t perfect, the chance of print failure increases. Many common 3D printing problems stem from a poor first layer.

## 1\) How to prepare your print surface

If you don't touch the print surface with your hands or dirty tools, then you don't have to clean it before every print. Clean your tools the same way you would the bed, and you will be able to start your next print right away.

\- Isopropyl alcohol

To achieve the best adhesion of the print surface, it is vital to keep it clean. The best option when printing with ABS, PLA, and many other materials is 90% Isopropyl alcohol, which can usually be sourced locally at drugstores or hardware stores. Denatured alcohol is also an option. We recommend always using 90% IPA. Solutions with lower percentages may contain unsuitable chemicals and oils.

PETG, ABS, ASA, XT, and CPH filaments are an exception - the adhesion may be too strong, and you can damage your Smooth PEI sheet. We recommend using a separating agent (e.g. a glue stick).

\- Dish soap and water

If the adhesion seems to decrease over time even when using IPA, you can clean the steel sheet with a few drops of dish soap and warm water (not hot!). This should not be done often, and do not submerge the sheet completely in hot water, but it will dissolve some oils and sugars that gather over time and that IPA does not remove. Make sure to use only dish soap and dry the sheet well before using it.

\- Acetone

PEI can lose its adhesive powers after a couple of hundred hours. When you see models coming loose regularly, wipe the surface thoroughly with acetone to restore the adhesion. This should only be used in the smooth PEI sheet and only around once per month. Do not overuse acetone. Extended use makes PEI surface brittle. Also, do not use acetone before printing with PETG.

\- Glue

Glue is a great, easy-to-use tool to increase adhesion. It also creates a protective separation layer. No need for glue specially made for 3D printing. You can use a basic (PVA-based) glue stick. From our experience, it is not needed when printing PLA, but may it be advisable when printing:

● Polyamide (Nylon)

● PETG

● Polycarbonate (PC)

● PET-based materials

● ABS

● ASA

● Other more exotic materials

● Flexible materials

## 2\) Resurface it

It can happen that you will leave some small marks on the print surface with your nozzle or tools. Typically, they will be shinier than the rest of the pad. It does not affect functionality or adhesion. However, if you want to have the same surface look on the whole print bed, you can resurface it. The easiest way is to take the hard side of a dry kitchen sponge and gently wipe the affected area in a circular motion a few times. Another option is to use fine-grit sandpaper (400-600) and lightly give the sheet a rub. Wipe over with IPA after doing so.

## 3\) The nozzle is too close/far from the sheet (MK2/MK2.5/MK3/MK3.5)

If the nozzle is too close to the printing bed, there won’t be enough room for the plastic to come out of the extruder. By having the nozzle too close to the print surface, you will essentially block its opening, so that no plastic can be extruded. You can easily recognize this issue when the printer does not extrude plastic for the first layer or two. Use the Live Adjust Z function and First Layer Calibration (i3) options to tweak the height of the nozzle. You perform the calibration from LCD Menu –> Calibration –> First layer calibration.

## 4\) Speed and temperature

\- Decrease the printing speed

If the steps described above didn’t help, then try decreasing the printing speed. The easiest way how to do it is by rotating the knob during the printing process, lowering the percentage. Counterclockwise = decrease speed, Clockwise = increase speed. We suggest decreasing the speed to about 75% for the first three layers, and then returning it to normal.

\- Use recommended printing temperatures

Make sure to use the recommended nozzle and heatbed temperatures. PrusaSlicer will configure them correctly based on the selected material, so you don’t need to adjust the temperatures manually on the printer itself. If you are experimenting with new materials that don’t adhere well, you can try to increase the heatbed temperature by 5-10 °C. This way the plastic will stick a bit better.

## 5\) A full or partial clog

The extruder could be clogged. This can happen either when excessive debris gets stuck inside the nozzle, when hot plastic is kept inside the extruder for too long, or when the thermal cooling for the extruder is not sufficient and the filament begins to soften outside of the desired melt zone.

## 6\) Uneven surface

If your print surface is not flat and the alignment of the mesh does not help, to achieve a flat print surface, a temporary solution is to add a piece of paper under the uneven area of the steel sheet. A more permanent solution would be to perform the firmware Bed Level Correction.

\- Correctly placed sheet

Before printing, make sure that you have the print plate properly installed, and that there are no leftovers from the previous print or a piece of loose filament that could affect the sheet position. Also, make sure that the sheet is straight and not bent or damaged.

## 7\) Brim

Before you consider applying extra adhesion materials onto the bed, consider using the Brim option in PrusaSlicer, which increases the surface area of the first layer.

## 8\) Expansion joints (MK4, MK3.9, MK3.5)

On the Original Prusa MK4, having the Magiboxes in the wrong orientation can cause an uneven first layer. Make sure that all of them have the full side facing the center of the carriage.

## 9\) Nozzle conditions (MK4, MK3.9, XL)

The nozzle on the Nextruder has to be at the correct height. If you are not sure if the height is correct, open the thumb screws on the side of the heatbreak, and push the nozzle up. Tighten the thumb screws just by hand, do not use any tools. If you have a Nozzle Adapter, check the installation again to make sure that the nozzle has not been lowered with the installation of the adapter.

## 10\) LoadCell check (MK4, MK3.9, XL)

If the filament is loaded while the printer is doing the leveling at the start of a print, check if the extruder is not pulling the filament down by loosening the filament spool a little. If you have the filament being fed by a PTFE tube, make sure that the tube is not short. After the previous checks, go into the printer menu to Control -> Calibrations \& tests -> 4. Loadcell test, and make the LoadCell test per screen instructions.

## 11\) Mechanical checks (XL)

\- Core XY

If your first layer is showing one side higher than the others on the Original Prusa XL, check the assembly of the Core for any loose screws which hold the Core to the four extrusions. Also, use the torque indicator to make sure the screws are tightened correctly.

\- Heatbed Tiles

Check if any of the screws under each heatbed tiles are loose.

\- Z-axis bearing housing

Re-print the two Z axis bearing housing parts, and replace them in the printer.
