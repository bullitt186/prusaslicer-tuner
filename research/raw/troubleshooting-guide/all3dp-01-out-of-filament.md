---
source_block: all3dp
entry: 1
title: "Out of Filament"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Out of Filament

Nothing is printing even though the model has been set and configured correctly in the slicing software. However, try as you might when repeatedly sending the print to the printer still nothing happens bar the odd spit of filament emerging from the nozzle. Alternatively a model is part way through the print and the filament extrusion stops but the nozzle continues to print into air.

Cause

It’s an obvious problem that’s unmissable in many printers such as the Prusa i3 style machines where the filament reel is in full view, but on other printers such as XYZ DaVinci, Cel Robox and Ultimaker machines, the issue isn’t always immediately obvious. These and many other printers either encase the filament within the design of the printer, or the filament is hidden round the back. Of course, some printers feature smart spools that feed back data to the software and highlight if the filament reel is close to, or out of material. However we all like to tinker and use our own tweaked firmware or third party software, and these sometimes work around such failsafes. And then there are other printers that simply don’t feature any type of failsafe at all. In all cases, especially with Bowden style extrusion systems, you’re going to have to extract some remaining filament and then feed in fresh material.

## 1\) Check the filament reel

Look at the filament reel and see if there’s any filament left. If not load a new reel. Easy.
