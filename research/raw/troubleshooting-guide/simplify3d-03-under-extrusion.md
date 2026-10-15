---
source_block: simplify3d
entry: 3
title: "Under-Extrusion"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Under-Extrusion

## 1\) Incorrect filament diameter

The first thing you want to verify is that the software knows the filament diameter that you are using. You can find this setting by clicking “Edit Process Settings” and going to the Other tab. Check to make sure that this value matches the filament that you purchased. You may even want to measure your filament yourself using a pair of calipers to make sure that you truly have the correct diameter specified in the software. The most common values for the filament diameter are 1.75mm and 2.85mm. Many spools of plastic also include the correct diameter on the packaging.

## 2\) Increase the extrusion multiplier

If your filament diameter is correct, but you are still seeing under-extrusion issues, then you need to adjust your extrusion multiplier. This is a very useful setting in Simplify3D that allows you to easily modify the amount of plastic that is extruded (otherwise known as the flow rate). You can find this setting by clicking “Edit Process Settings” and going to the Extruder tab. Each extruder on your printer can have a unique extrusion multiplier, so if you are trying to modify the flow rate for a specific extruder, make sure to select it from the list on the left to load the settings for that extruder. As an example, if your extrusion multiplier was 1.0 previously and you change it to 1.05, it means you will be extruding 5% more plastic than you were previously. It is typical for PLA to print with an extrusion multiplier near 0.9, while ABS tends to have extrusion multipliers closer to 1.0. Try increasing your extrusion multiplier by 5%, and then reprint the test cube to see if you still have gaps between your perimeters.

## 3)First layer calibration too close

Make sure you have performed the First Layer Calibration correctly. Avoid compensating for a lack of adhesion by squishing the first layer too much. If the nozzle is too close to the build plate, the filament can be obstructed from pushing through. We recommend running the first layer calibration every time you move the printer to a different location or do maintenance on the hotend, like changing the nozzle. Moreover, when you swap the steel sheet from the textured one to the smooth one you must recalibrate due to the sheet's different thickness.

## 4\) Slicer settings

Each profile in the PrusaSlicer contains settings that determine temperature, speeds, and how much filament the 3D printer should extrude. The printer does not provide any feedback on how much filament actually leaves the nozzle. It can be that less filament is extruded than the firmware expects. If that happens, you may notice gaps in and/or in between printed layers.

## 5\) Nozzle

If you had the nozzle removed from the hotend at some point, make sure it has been correctly reinstalled. Please see the dedicated guide for your hotend:
● Changing or replacing the nozzle (MK2.5S/MK3S/MK3S+/MK3.5)
● Changing/replacing the nozzle (MINI)
Incorrect installation can cause both clogging and leaks. The nozzle must be tightened when heated and there must be a gap between the nozzle and the heater block. Also, inspect the extruder and hotend for any damage, like the heater element or thermistor's wires or a bent heatbreak (only on V6 hotend).
If the installation of the nozzle is correct, then performing a Cold pull will often resolve a clog.

## 6\) Using specialty nozzles

If you are using specialty nozzles like hardened steel or stainless steel, etc., you may have to increase the nozzle temperature when printing, usually within a range of 5-10 °C. Steel has different thermal properties compared to a brass nozzle, which can affect print results, mainly the inter-layer adhesion. But remember that higher temperatures can also lead to increased stringing. If the issue persists, try replacing the nozzle with the original 0.4mm brass nozzle and see if it makes a difference.
Furthermore, not all nozzle sizes will be suitable for all filaments. Filament that contains particles of wood or metal will most often be unsuitable for nozzles with a diameter below 0.4, and some will require an even larger nozzle, like 0.6 mm or 0.8 mm.
A 0.1 mm nozzle can be considered experimental; Its small diameter will not work with all filaments, the tolerances required in its manufacturing are hard to guarantee and the excessive printing time it requires can be beyond reasonable. For these fine resolutions, you may want to consider SLA printing.

## 7\) Extruder gears

Check both Bondtech gears for any dirt or misalignment so they are able to push filament through. Please see Checking/re-aligning the Bondtech gear (MK3S/MK2.5S) for details.
Additionally, make sure that your printer’s extruder idler is at the correct tension. Having the idler screw too loose or too tight can cause under extrusion.

## 8\) Insufficient hotend cooling

Controlling the "melt-zone" of the filament is very important. With insufficient cooling, the filament can start melting too far away from the nozzle. Check that your extruder fan is installed in the correct orientation and whether the fan is blocked by a piece of filament or some other debris.
Unless you have turned off "Fan check", the printer will give an error if it detects if either fan is not spinning when it should (hotend fan or print fan).
If you are using your printer in an enclosure, make sure the temperature inside is not too hot, as overheating can result in Heat creep, where the filament will start melting before it reaches the nozzle The hotend fan will always spin if the nozzle is heated above 50 °C.

## 9\) Filament

Too low or too high printing temperature can cause print issues as well. If your filament brand and type is not listed in PrusaSlicer, you can try to adjust the print temperature by +/- 5-15°C to see if this resolves the issue. Some specialty materials, like Flexible materials, may require many adjustments and tweaks to print them successfully. Composite materials, like Woodfill filament, may require at minimum a 0.6 mm nozzle, and 0.2 mm layer height to prevent clogging. If there are composite materials like kevlar or carbon fiber, a hardened nozzle is required. Be sure to see our extensive material table, where most types of filament and their considerations are covered. Some filaments can also have a varying thickness, due to quality or infused materials like wood, which will cause unexpected changes in the volume of extruded filament. The industry standard of variations in diameter is +/- 0.05 mm. Keep your filament dry, free of moisture because damp filaments have a negative impact on printing, especially soluble filament, PETG, and ABS. We highly recommend putting spools back inside their original bag when it’s not in use, along with a silica gel. We recommend storing your filaments in a dry area or ideally in a “dry box”.
