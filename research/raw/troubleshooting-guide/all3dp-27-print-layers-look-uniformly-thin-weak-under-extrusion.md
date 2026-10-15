---
source_block: all3dp
entry: 27
title: "Print Layers Look Uniformly Thin/Weak (Under-Extrusion)"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Print Layers Look Uniformly Thin/Weak (Under-Extrusion)

Under-extrusion is the term given to the printer not supplying sufficient material for the print. Under-extrusion has many telltale signs — most significantly thin layers, unwanted gaps and even missing layers entirely.

Cause

There are several possible causes. First, the diameter of the filament used does not match the diameter set in the slicing software. Secondly, the amount of material that is extruded is too low because of faulty slicer software settings. Alternatively, the flow of the material through the extruder is restricted by dirt in the nozzle.

## 1\) CHECK THE FILAMENT DIAMETER

Start with the simplest issue, have you set the correct filament diameter in the slicing software? If you’re unsure about the diameter the value along with the recommended temperature is usually printed on the box.

## 2\) MEASURE THE FILAMENT

If you’re still not getting the results you want and filament flow is the issue, then use a set of calipers to double-check the filament diameter. You should be able to tweak the filament diameter settings accurately in the slicer software settings.

## 3\) CHECK THE HOT END FOR DEBRIS

After printing, most printers will lift the printhead away from the print base. Quickly check that the nozzle is clear from a build-up of filament and dirt.

## 4\) SET THE EXTRUSION MULTIPLIER

If there is no mismatch between actual filament diameter and the software setting, then then the extrusion multiplier (also referred to as the flow rate or flow compensation) may be too low. Each slicer application will handle this slightly differently but the principle is to increase this value in steps of 5% until you see the problem is gone.
