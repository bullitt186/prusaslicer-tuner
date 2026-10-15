---
source_block: all3dp
entry: 17
title: "Layers Don't Line Up Well"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Layers Don't Line Up Well

As the print is forming, there appear to be a few issues with the quality. Look closer and you see that the layers aren’t aligning quite as they should. Look at the internal support structure and again the pattern looks slightly out. The outer wall, rather than being smooth, features slight misalignments that cause an uneven face. It’s highly likely that the issue only affects the print in one direction; front to back or left to right.

Cause

Over time the parts of your 3D printer — such as nuts, bolts, and belts — will become loose and require a tightening. The effect of misaligned layers is similar to the cause of the more pronounced effects of shifting layers and there is no doubt that there is a crossover. If left unchecked, this problem will eventually result in shifting layers, but as the issue starts the visual effect on the prints is far less pronounced and can look very different. The cause is usually linked directly to a loose belt.

## 1\) CHECK THE BELTS PART I

Start by checking each of the belts is tight but not overly tight. You should feel a little resistance from the two belts as you pinch them together. If you find that the top section of the belt is tighter than the bottom then this is a sure-fire sign that they need a tweak and tighten. Some printers, such as the Original Prusa i3, come with belt tensioners built into them. Others can be retrofitted with 3D printed ones. If neither of these is an option for you, you may have to get your hands dirty and manually tighten the belt.

## 2\) CHECK THE BELTS PART II

The printer belts are normally just one continuous loop hooked around two pulleys. A common issue is that over time the belt can slip on one pulley and gradually gets tighter on the top compared to the bottom — or visa versa — and again this can cause misaligned layers.

## 3\) CHECK THE RODS ARE CLEAN AND OILED

Over time debris can build up on the rods, causing odd patches of higher friction which in turn can affect the free movement of the head and again cause layer shifting. A quick wipe and re-oil of the rods usually solves the issue.

## 4\) CHECK FOR BENT OR MISALIGNED RODS PART I

If you see the print head falter at certain points then it could be that one of the rods has become slightly bent. You can usually tell by switching off the machine so there’s no power going through the steppers and then moving the print head through the X- and Y-axis. If you feel resistance then you know something is amiss. Start by seeing if the rods are aligned. If they are, remove them and roll them on a flat surface. If any are bent then it will be quite obvious.

## 5\) CHECK FOR BENT OR MISALIGNED RODS PART II

Many printers use threaded rods rather than lead screws and although these do the job, they do have a tendency to bend over time. Don’t worry about dismantling your printer to see if they’re straight, simply use control software such as ‘Printrun’ to move the print head up or down. If one of the Z-axis rods is bent you’ll instantly see. Unfortunately, it’s almost impossible to accurately straighten a rod once it’s bent, but on the upside, it’s a good excuse to replace the old threaded rods for lead screws.

## 6\) CHECK THE DRIVE PULLEYS

These are usually connected directly to a stepper motor or to one of the main rods that drive the print head. If you carefully rotate the pulley you’ll see a small grub screw. Holding both the rod and the attached belt, give the belt a tug to force the pulley to turn. You should find that there is no slip between the pulley and stepper or rod. If there is tighten the grub screw and try again.
