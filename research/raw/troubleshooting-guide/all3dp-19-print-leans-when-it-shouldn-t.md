---
source_block: all3dp
entry: 19
title: "Print Leans When it Shouldn't"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Print Leans When it Shouldn't

As the print forms it starts to lean. Instead of being straight and true, vertical edges are printed at an angle, and this angle isn’t consistent throughout the print. The severity could be increasing and decreasing at different stages.

Cause

The cause of the issue is generally very simple; one of the pulleys attached to a stepper motor is slightly loose, or one of the belts is rubbing against something and stopping the full travel of the head. All you need to do to correct the issue is to make sure that none of the pulleys are slipping and the grub screws that hold the pulleys in place are all tightened. Although this should be a quick and straightforward fix, one issue you may experience as you go to tighten the pulleys is that the small grub screws that tighten onto the shaft of the motor aren’t always that easy to access. Firstly diagnosing which pulley is causing the issue and then getting access to that pulley can be tricky and time-consuming.

## 1\) CHECK X- AND Y-AXIS

If your print is leaning to the left or right then you have an X-axis issue. Back to front and you have a Y-axis problem. Once you’ve diagnosed which it is you can then check the belts and pulleys. If you have a printer such as the Prusa i3 then the process is pretty straight forward, as the steppers are directly connected to the main drive belt. For the Ultimaker and other printers, the process can be a little more tricky.

## 2\) CHECK THE BELTS AREN’T RUBBING

Look around each of the belts and ensure that they’re not rubbing against the side of the machine or any other components. Also, check to see that the alignment of the belts is correct. If one is at a slight angle then this can cause issues.

## 3\) TIGHTEN THE STEPPER MOTOR COUPLER GRUB SCREW

Once you diagnose which axis is causing the issue, use an Allen key to tighten the corresponding coupler’s grub screw that attaches to the stepper motor.

## 4\) CHECK ROD PULLEYS

More complex machines such as the Ultimaker 2 have a series of belts and pulleys. The main X and Y rods at the top of the machine feature eight pulleys. Go around each of these on the affected axis and tighten the grub screws for each. It’s unlikely that these will cause any slip but if one is loose then a belt may misalign.
