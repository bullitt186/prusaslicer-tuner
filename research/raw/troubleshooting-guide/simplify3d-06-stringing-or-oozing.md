---
source_block: simplify3d
entry: 6
title: "Stringing or Oozing"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Stringing or Oozing

Stringing (otherwise known as oozing, whiskers, or “hairy” prints) occurs when small strings of plastic are left behind on a 3D printed model. This is typically due to plastic oozing out of the nozzle while the extruder is moving to a new location.

## 1\) Retraction distance

The most important retraction setting is the retraction distance. This determines how much plastic is pulled out of the nozzle. In general, the more plastic that is retracted from the nozzle, the less likely the nozzle is to ooze while moving. Most direct-drive extruders only require a retraction distance of 0.5-2.0mm, while some Bowden extruders may require a retraction distance as high as 15mm due to the longer distance between the extruder drive gear and the heated nozzle. If you encounter stringing with your prints, try increasing the retraction distance by 1mm and test again to see if the performance improves.

## 2\) Retraction speed

The next retraction setting that you should check is the retraction speed. This determines how fast the filament is retracted from the nozzle. If you retract too slowly, the plastic will slowly ooze down through the nozzle and may start leaking before the extruder is done moving to its new destination. If you retract too quickly, the filament may separate from the hot plastic inside the nozzle, or the quick movement of the drive gear may even grind away pieces of your filament. There is usually a sweet spot somewhere between 1200-6000 mm/min (20-100 mm/s) where retraction performs best. Thankfully, Simplify3D has already provided many pre-configured profiles that can give you a starting point for what retraction speed works best, but the ideal value can vary depending on the material that you are using, so you may want to experiment to see if different speeds decrease the amount of stringing that you see.

## 3\) Temperature is too high

Once you have checked your retraction settings, the next most common cause for excessive stringing is the extruder temperature. If the temperature is too high, the plastic inside the nozzle will become less viscous and will leak out of the nozzle much more easily. However, if the temperature is too low, the plastic will still be somewhat solid and will have difficulty extruding from the nozzle. If you feel you have the correct retraction settings, but you are still encountering these issues, try decreasing your extruder temperature by 5-10 degrees. This can have a significant impact on the final print quality. You can adjust these settings by clicking “Edit Process Settings” and selecting the Temperature tab. Select your extruder from the list on the left, and then double-click on the temperature setpoint you wish to edit.

## 4\) Long movements over open spaces

Stringing occurs when the extruder is moving between two different locations, and during that move, plastic starts to ooze out of the nozzle. The length of this movement can have a large impact on how much oozing takes place. Short moves may be quick enough that the plastic does not have time to ooze out of the nozzle. However, long movements are much more likely to create strings. Thankfully, Simplify3D includes an extremely useful feature that can help minimize the length of these movements. The software is smart enough that it can automatically adjust the travel path to make sure that nozzle has a very short distance to travel over an open space. In fact, in many cases, the software may be able to find a travel path that avoids crossing an open space all together! This means that there is no possibility to create a string, because the nozzle will always be on top of the solid plastic and will never travel outside the part. To use this feature, click on the Advanced tab and enable the “Avoid crossing outline for travel movement” option.

## 5\) Movement Speed

Finally, you may also find that increasing the movement speed of your machine can also reduce the amount of time that the extruder can ooze when moving between parts. You can verify what movement speeds your machine is using by clicking on the Speeds tab of your process settings. The X/Y Axis Movement Speed represents the side-to-side travel speed, and is frequently directly related to the amount of time your extruder spends moving over open air. If your machine can handle moving at higher speeds, you may find that increasing this settings can also reduce stringing between parts.

## Solution #2

Stringing or oozing, also known as "hairy prints", is the name given for when small strings of filament are left on a printed model. This usually happens when the filament keeps flowing from the nozzle while the extruder is moving to another object. You can see this as a marginal line of filament left between the objects. This issue is caused by very high printing temperatures and/or using incorrect retraction settings.

## 1\) Stringing from material left on the nozzle

If you print for a long time from a single type of filament, such as PET-G, the filament can create a thin layer in the nozzle. This can cause stringing as the strands of the filament stick to the surface of the print. Therefore, thoroughly clean the nozzle before printing and make sure that any dirt or remnants of previous filaments are removed from the nozzle.

## 2\) The retraction settings

● Retraction length: Amount that the filament is pulled back when a retraction is triggered. On the MK2.5/S and MK3/S/+, the retraction length should be a maximum of 2 mm.

● Lift z: lifts the extruder during movement. Having this setting lower will improve stringing. Note that disabling this feature may cause the nozzle to hit the printed part.

● Retraction Speed: Extruder motor speed on retraction. A higher value improves stringing, but if it is too high it may skip steps in the motor.

● Minimum travel after retraction: Amount of move that will trigger a retraction (mm). The preset number in PrusaSlicer is 1 mm, which is a low amount. Having this number higher will get lower printing times, but increase oozing and stringing.

● Retract on layer change: Activates retraction when the layer changes to the next one. It is recommended to leave this option on.

● Wipe while retracting: Moves the nozzle (wipe) while the retraction is happening. It is recommended to leave this option on.

● Retract amount before wiping: This option does a quick retract before doing the wiping movement. More suitable for the Original Prusa MINI/MINI+.

## 3\) Other settings that affect retraction:

● Only retract when crossing perimeters: (Print settings -> Infill -> Advanced): Disables retraction when the travel path does not exceed the upper layer's perimeter. Any oozing that happens will be within the walls and should be invisible.

● Avoid crossing perimeters: (Print settings -> Layers and perimeters -> Quality): Optimize travel moves in order to minimize the crossing of perimeters. This will lower the stringing amount, especially in the MINI/MINI+.

● Sequential printing: (Print settings -> Output options -> Sequential printing): Printing each object individually has a smaller chance of causing stringing between the parts. When using this feature, PrusaSlicer will warn you of any possibility of the extruder colliding with an already printed part, but follow the print closely.

● Nozzle temperature: (Filament settings -> Filament -> Nozzle): Lowering the temperature decreases the occurrence of strings. Try decreasing the nozzle temperature by 5 – 10°C and check whether there’s less stringing.

## 4\) Filament

Try using a different spool than the one that is causing the stringing. The filament might have gathered moisture, which will cause a lot of stringing.

## 5\) Hotend

Stringing in the nozzle might be caused by a heat dissipation issue in the nozzle. Try re-applying thermal paste on the threads between the heatbreak and the heatsink.
If you have recently changed any component in the hotend, it is also possible that some individual parts are not in place. Go over the assembly of the hotend and check for any parts that may be different from the instructions.

## 6\) Enough settings, pass me my heat-gun.

If you don’t feel like tweaking any of the settings, well, then there is an alternative. You can get rid of the strings with a heat gun (or often with a lighter – but be very careful). Set your heat-gun to around 200 °C and aim at the strings for one or two seconds. This will melt the strings, and the printed object should remain undamaged. Do not leave the heat source on the printed model for longer than one or two seconds, as this may deform the part.
