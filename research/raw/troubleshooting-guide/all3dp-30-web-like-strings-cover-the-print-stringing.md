---
source_block: all3dp
entry: 30
title: "Web-like Strings Cover the Print (Stringing)"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Web-like Strings Cover the Print (Stringing)

There are unsightly strings of plastic between parts of the model.

Cause

When the print head moves over an open area (also known as travel move), some filament has dripped from the nozzle.

## 1\) ENABLE RETRACTION

Retraction is an important factor when it comes to quality of finish and can be enabled through most slicing software. Its function is pretty simple and works by retracting the filament back into the nozzle before the head moves. The idea is that it avoids molten filament from trailing behind the head creating thin strings in its wake. Most applications such as Cura offer a one-click activation option. This uses a set of default parameters and is perfectly adequate for the most part, but for fine-tuning there are customizable options that give greater control. Adjusting the minimum travel of the head before retraction is activated, for example.

## 2\) MINIMUM TRAVEL (MM)

Reducing the minimum travel is usually the quickest fix for stringing if the standard retraction isn’t doing the job. Drop the value in 0.5mm increments until the stringing has stopped.

## 3\) JUST CUT THEM OFF

This isn’t the most elegant of solutions but simply taking a scalpel to the strings is quite often the quickest and easiest solution.
