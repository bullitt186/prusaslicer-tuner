---
source_block: all3dp
entry: 4
title: "Print Head Misses the Bed"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Print Head Misses the Bed

There’s really no missing this one. At its most severe the noise will instantly alert you that something is very wrong. When the printhead misses the bed it will usually also have reached the limit of either the X or Y position. As the head tries to travel beyond its furthest point noise will be generated through slipping belts, grinding cogs, or the head simply trying to rip through the side of the printer. It’s very unlikely that your printer will succeed in producing a print in this state. And while it’s easy to fix, it’s not a problem that can be overlooked or dealt with at a later time.

Cause

Misconfiguration, wrong printer selection, or worn-out or broken end stops are all common issues. If the problem starts with a new printer then the likelihood is that something is amiss with the printer’s configuration. Run through the setup process again and ensure that you have the correct firmware version for your printer. Accidentally selecting the wrong printer from a dropdown list in your slicer program can be a common cause for this 3D printing problem. For example, trying to print using Ultimaker Go using print files configured for the Ultimaker 2. When you set up your printer ensure that you have specified the correct print volume, again either in the printer’s firmware or through software. If the printer thinks it has a bigger print platform than it has then it’s going to try to use it, even if it’s not there. If your printer is usually fine and then the problem occurs suddenly, start by double-checking your print preparation software. Something may have reset or been altered by an update! It’s not unusual for software to either revert to the default settings or to automatically select the latest printer version, even if that’s not the one you’re using. And if all else looks fine then it could be that one of your end stops in the printer has stopped working.

## 1\) CHECK SLICER FOR CORRECT PRINTER

Before trying anything else make sure that you have the correct printer selected in your printing software. All printers are different so even if the print beds of two printers are the same it’s highly unlikely the other dimensions and settings will match exactly.

## 2\) UPDATE FIRMWARE

If you’ve just purchased the printer and this issue is happening make sure you have the latest version of the firmware installed. Once updated run through the setup process and double-check all settings, especially around the size of the print area are correct.

## 3\) CHECK END STOPS

This will take a little more effort to diagnose. Watch the print head move. If it tries to push past the furthest point of one of its axes, check that an end stop hasn’t disconnected. If all looks fine (and none of the above steps fixed the issue for you) then replacing the end stops with new ones should be your next step.
