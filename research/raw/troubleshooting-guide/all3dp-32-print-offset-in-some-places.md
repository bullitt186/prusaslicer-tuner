---
source_block: all3dp
entry: 32
title: "Print Offset in Some Places"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Print Offset in Some Places

The lower and top layers shift so that you get a stepping effect through the print. Usually, it’s quite subtle, but the above image shows a print with a more pronounced effect.

Cause

There’s a variety of reasons for shifting layers, and these can be as simple as someone knocking against the printer during the print process. More complex causes can be bent or misaligned rods, or even the nozzle catching on the print and causing a slight shift in platform position

## 1\) CHECK THE PRINTER HAS A STABLE BASE

Place the printer on a stable base and in a location where it will avoid being knocked, poked and generally fiddled with. Even a small nudge of the printer can shift the print base and cause issues.

## 2\) CHECK THE PRINT BED IS SECURE

Many 3D printers use some form of detachable print bed. Although this is handy when it comes to removing prints and avoids damage to the printer, it also means that over time clips and screws can work loose. Make sure that when you reinstall the print platform it’s clipped or bolted tightly in place to avoid any slip or movement.

## 3\) WATCH FOR WARPED UPPER LAYERS

A print’s upper layers can easily warp if cooled too quickly. As the layers warp they rise and can cause an obstruction to the nozzle as it moves. In most cases the print will release from the platform, but if it doesn’t the powerful stepper motors can push the print and platform around. If your prints are suffering from warping in the upper layers try reducing the speed of the fans slightly.

## 4\) REDUCE PRINT SPEED

It is possible to speed up the print times for your machine by increasing temperature and flow. However whilst this may result in the filament flowing in the correct quality the rest of the machine may struggle to keep up. If you hear a clicking during printing this could be a sign that the printer is going to fast. If you do hear a click the first port of call is to check that the filament isn’t slipping, before you take a look at the actual printer speed. You can adjust your printer’s speed easily enough in any good slicing software.

## 5\) CHECK THE BELTS

If layers are still shifting then it’s time to check the belts. A quick check is to just go around all belts and pinch the two together. The tension in each belt should be the same, if not then you’ll need to adjust the belt position to even out the belt tension. Over time the rubber belts will stretch (You can often tell if they do as they’ll start to slip on the drive pulleys), if there is quite a bit of play in the belts then it’s time to replace them with new ones. Over tight belts can also be an issue but this is usually only a problem if you’ve built the machine yourself. Some printers such as the Prusa i3 have belt tensioning screws that enable you to easily adjust the belt tensions.

## 6\) CHECK THE DRIVE COUPLERS

These are usually connected directly to a stepper motor, and one of the main rods that drives the print head. If you carefully rotate the coupler you’ll see a small grub screw. Hold onto the rod and taking hold of the attached belt and then tug the belt and try to force the pulley to turn. You should find that there is no slip between the coupler and stepper or rod. If there is, tighten the grub screw and try again.

## 7\) CLEAN AND OIL THE RODS

Over time debris can build up on the rods which means that at some points along their length they encounter an increase in friction. This can affect the free movement of the head and cause layer shifting. A quick wipe and re-oil of the rods usually solves the issue.

## 8\) CHECK FOR DEFORMED RODS

If you see the print head falter at certain points then it could be that one of the rods has become slightly bent. You can usually tell by switching off the machine so there’s no power going through the steppers and then move the print head through the X- and Y- axes. If you feel resistance then you know something is amiss. Start by seeing if the rods are aligned, if they are then remove the rods and roll them on a flat surface. If any are bent then it will be quite obvious.
