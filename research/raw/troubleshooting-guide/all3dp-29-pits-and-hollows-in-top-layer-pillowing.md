---
source_block: all3dp
entry: 29
title: "Pits and Hollows in Top Layer (Pillowing)"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Pits and Hollows in Top Layer (Pillowing)

The top surface of the print shows unsightly bumps or even holes.

Cause

The two most common causes are improper cooling of the top layer and that the top surface isn’t thick enough.

## 1\) FILAMENT SIZE

Pillowing is an issue that can affect all 3D printers, however, it’s far more common on those using 1.75 mm filament. If none of the other tips below help, try switching to 2.85mm filament if you can.

## 2\) CHECK THE FAN POSITION

Cooling can be a cause of pillowing. As the print starts your printer’s fans will typically be set to low or off and after the first few layers, they should kick into action. Check that the fans around your hot end start spinning, especially toward the end of the print. If they appear to be functioning fine, then the issue could be that they are not directing sufficient airflow over your print. There are a variety of 3D printable mods to alter your print airflow.

## 3\) SET FAN SPEED IN G-CODE

Another cooling issue happens when each successive top layer of molten plastic is applied. As it covers the inner support structure it needs to be cooled quickly to avoid falling into the holes between the supports. The speed of the fans can be adjusted in the G-Code. A common G-Code for Fan On is M106 and is M107 Fan Off. By those control lines, you just need to set the Fan speed to maximum for those top layers. For example, looking at the G-Code (generated in Cura for printing on a Prusa i3) for a 1cm x 1cm cube printed at 0.1mm layer height, we can see that there are 97 layers. Knowing that we have a ‘Bottom / Top Thickness setting’ of 0.6mm we can look back to ;LAYER:91, then in the subsequent line add M106 S255. M106 sets the fan going and S255 sets it to full blast.

## 4\) INCREASE TOP LAYER THICKNESS

The easiest solution is to increase the top layer thickness. Most applications will enable you to do this in the advanced section, under the ‘Bottom / Top Thickness setting’. You’re aiming for at least 6 layers of material normally and up to 8 for smaller nozzles and filaments. If your layer height is therefore set to 0.1mm then set the ‘Bottom / Top Thickness setting’ to 0.6mm. If the effect of pillowing still exists then bump it up to 0.8mm.
