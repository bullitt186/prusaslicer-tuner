---
source_block: all3dp
entry: 24
title: "Ripples and "Echoes" in Print (Ringing)"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Ripples and "Echoes" in Print (Ringing)

The effect of visual waves or rippling on the print surface is one of those minor and annoying problems that many of us simply overlook. It has a habit of coming and going, and there really does seem to be no consistent reason for the issue. The effect is normally very subtle and appears as a wave or ripple through the surface of the print, it’s position and severity can also change. Most people will simply overlook the problem. Other than a slight visual effect on the surface the effect of these ripples has little other effect on the quality of the final 3D print, except of course in the most severe of cases.

Cause

The issue of waves in your 3D prints is usually down to one of two things, and more commonly a combination of the two. Vibrations and speed. 3D print manufacturers do an awful lot to their machines to make sure that the small vibrations created by the motors are kept to an absolute minimum. Lift up a printer like the Ultimaker 3 and you’ll see exactly what we mean, even the small Cel Robox Dual packs in some significant weight. This weight helps to minimize vibrations through the machine but doesn’t completely eliminate it. Those small vibrations can travel through the furniture, floor boards or any surface you’ve seen fit to adorn with your printer. The next time you start your 3D printer up take a look at the surface that it’s on, then as the printer prints check to see if the table is sturdy enough to properly support the machine. Vibrations can also be amplified by poor maintenance and worn linear bearings. Regularly check that your printer is clean, free of fluff, grit and dirt, and remember to keep the rails oiled. When the printer’s off check the quality of the linear bearings and make sure that the movement of the print head is smooth, you can do this by moving the head with your fingers. Make sure everything is cool before you start. As you’re checking the maintenance make sure that all the bolts and bits within the machine are good and tight, especially if you built the machine yourself. Waves will also be an issue if you try to print too fast, the simple solution here is to simply drop the print speed, this will solve the problem in the majority of cases. If you still need to print fast then try increasing the flow and extrusion temperature. Finally, and this is one for the more advanced users, and that’s firmware acceleration. This adjusts the speed of the head as it prints and changes direction, it’s function is to help prevent ringing. Here there are two functions that you should look at and this will change depending on the machine. Look for acceleration and jerk, there are several values listed, start by lowering the jerk and then the acceleration during printing.

## 1\) REDUCE VIBRATIONS

Make sure that the surface you use for your 3D printer is solid and as the printer prints there are no visual vibrations.

## 2\) CHECK THE BEARINGS

Linear bearings wear over time, with the printer off check that all are still running smooth.

## 3\) MAKE SURE EVERYTHING IS TIGHT

It’s amazing how one loose bolt can affect print quality, as part of your maintenance routine make sure everything is bolted and tight.

## 4\) ADD OIL

Check all the rods are clear of dust and dirt and then add a drop of oil to ensure everything is well lubricated.

## 5\) SLOW DOWN THE PRINT

Reduce the print speed.

## 6\) ADJUST THE FIRMWARE ACCELERATION

One for advanced users only, check the printer’s firmware and adjust the values in the code for the acceleration and jerk, you’ll then need to upload the firmware back to your machine.
