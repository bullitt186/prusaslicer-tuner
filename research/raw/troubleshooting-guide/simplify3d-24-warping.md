---
source_block: simplify3d
entry: 24
title: "Warping"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Warping

As you start printing larger models, you may start to notice that even though the first few layers of your part successfully adhered to the bed, later on the part begins to curl and deform. This curling can be so severe that it actually causes part of your model to separate from the bed, and may cause the entire print to eventually fail. This behavior is particular common when printing very large or very long parts with high temperature materials such as ABS. The main reason for this problem is the fact that plastic tends to shrink as it cools. For example, if you printed an ABS part at 230C and then allowed it to cool to room temperature, it will shrink by almost 1.5%. For many large parts, this could equate to several millimeters of shrinkage! As the print progresses, each successive layer will deform a bit more until the entire part curls and separates from the bed.

## 1\) Use a Heated Bed

Many machines come equipped with a heated bed that can help keep the bottom layers of your part warm throughout the print. For materials such as ABS, it is common to set the heated bed temperature to 100-120C, which will significantly reduce the amount of plastic shrinkage in these layers. To adjust your heated bed temperature, click on “Edit Process Settings”, select the Temperature tab, and then choose your Heated Bed from the list on the left-hand side. You can double-click on the temperature setpoint to edit the value.

## 2\) Disable Fan Cooling

By now, you probably realize that cooling can be a problem for parts that tend to warp. For this reason, many users prefer to disable any external cooling fans entirely when printing with materials such as ABS. This allows all of the layers to stay warm for a longer period of time, increasing your chance of success.

## 3\) Use a Heated Enclosure

While a heated bed can keep the bottom layers of your part warm, it may struggle to keep the upper layers of the part from contracting once you start printing taller and taller objects. In this situation, you may find it useful to place your printer inside of an enclosure that can help regulate the temperature of the entire build volume. Some machines may already include an external enclosure specifically for this reason. If your machine does include a heated enclosure, make sure to keep the doors closed during the print, which will keep the heat from escaping.

## 4\) Brims and Rafts

If you have already tried all of the other suggestions, but your parts are still curling later on in the print, then you can also try including a brim or a raft with your print. These features will help hold the edges down and may warp less, since they are typically only a few layers tall.

## 5\) Troubleshooting

● Use PrusaSlicer profiles – Make sure you are starting off by using corresponding default profiles in PrusaSlicer. You may save yourself a lot of hassle with figuring out the ideal settings yourself. Profiles are already refined for each material.

● Keep the surface free of grease – Before starting any of your prints, simply wipe the print surface clean with IPA 90%+. A complete guide on how to prepare the print surface can be found at First layer issues.

● Lower the Live Adjust Z slightly to increase bed adhesion. But not too much. Do not over-squish the first layer. Be aware the bed adhesion might be too high with PETG or PC and might result in a damaged PEI surface.

● Print cooling.  Some materials such as PLA or PETG need a lot of cooling. If corners of your print are lifting up, check if the print fan is enabled, try increasing the print fan speed. Check if the print fan actually works and the fan shroud isn´t obstructed or molten.

● If steep overhangs and small parts of your print are warping, you may try enabling the print fan at low speeds (10-20%) even for materials that do not require a lot of print-cooling such as ABS or PC-Blend. This may help for example if you have a printer in an enclosure or if the problematic part is drowned in between supports that are retaining heat. Be aware that too much print-fan speed may warp and lift up the whole object and may decrease layer-to-layer adhesion. Our goal is to cool the part neither too fast nor too slow.

● If you experience lower layer-to-layer adhesion or even print cracking after raising the print-fan speed, try increasing the nozzle temperature to restore the bonding of the individual layers together properly.

● Ambient temperature – For high-temperature filaments, try to maintain a stable ambient temperature. An open window or an AC unit nearby the printer will increase the occurrence of warps. High-temperature materials generally require higher ambient temperature not to warp during printing. If you print with these materials most of the time, you should consider having the printer in an enclosure. Printing PLA or PETG in an enclosure might not be a good idea. These materials need a lot of print cooling, which is harder to achieve with a higher ambient temperature. It is possible to either purchase an enclosure in our e-shop. You can purchase the Original Prusa Enclosure in our e-shop. It is also possible to make your own enclosure.

● Use a skirt and try to print more objects at once. For high-temperature materials such as PC-Blend, ASA, or ABS, try using a printed skirt (draft shield) to retain heat in and around the printed object. Printing more objects at once may also help with retaining heat. Try to orient the problematic parts of the objects towards the center of the heatbed.

● Decrease the print speed. This may help a lot with high-warping materials. Although Prusament PC-Blend is low-warping compared to other PC-Blend filaments, decreasing the print speed will help your part as a whole to settle down, melt individual layers together properly and warp less. It also increases the layer-to-layer adhesion and part strength.

● Use the brim – A brim is a good way how to increase the adhesion to the print surface.

● If the brim isn't enough, try adding a small geometry (like a tiny cylinder) specifically to the culprit area. The object should only be a few layers tall so it is also easy to remove.
