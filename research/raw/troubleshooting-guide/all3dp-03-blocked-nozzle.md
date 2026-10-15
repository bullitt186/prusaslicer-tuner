---
source_block: all3dp
entry: 3
title: "Blocked Nozzle"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Blocked Nozzle

You initiate a print job but whatever you try, nothing comes out of the nozzle. Extracting the filament and reinserting doesn’t work.

Cause

A small piece of filament has been left behind in the nozzle after changing spools, often because the filament has snapped off at the end. When the new filament is loaded, the piece of old filament that is left in the nozzle doesn’t allow the new filament to be pushed through. A little printer maintenance can go a long way to reducing the chance of problems like a blocked nozzle affecting your extrusions. In fact you’ll often find that before a clog even appears, there is old carbonized filament sitting inside your nozzle. It can and will sit there for weeks or even months without you realizing, but there will be small signs in the quality of your prints. The effects are often overlooked; such as small nicks in the outer walls, small flecks of dark filament, or small changes in print quality between models. These defects are often simply put down to the slight variations we come to expect from 3D printers, but really there could be something a little more sinister going on. A cleaning method known as the Atomic Pull or Cold Pull (which we detail below) can clear this up. You’ll commonly see this if you frequently switch from a PLA to ABS, for example. A small amount of PLA is left in the nozzle, and it is heated beyond its normal melting point. That can mean it will carbonize and burn. Likewise, switch between ABS and Nylon and again you’ll witness something similar. It’s not uncommon to see a wisp of smoke appear briefly as the new filament is fed through.

## 1\) UNBLOCK WITH A NEEDLE

If you’re lucky then unblocking can be a quick and easy process. Start by removing the filament. Then using your printer’s control panel (if it has one) select the “heat up nozzle” setting and increase it to the melting point of the stuck filament. Alternatively, hook your printer up to a computer running compatible control software and heat the nozzle using that. For PLA set the temperature to 220 °C. Once the nozzle reaches the correct temperature, use a small pin to clear the hole (being careful not to burn your fingers). If your nozzle is 0.4mm then you need a pin that is smaller; an airbrush cleaning kit works perfectly.

## 2\) PUSH OLD FILAMENT THROUGH

If you find that the nozzle is still blocked then you may be able to push the filament through with another bit of filament. Start by removing the filament as before and then remove the feeder tube from the print head. Heat up the hot end to 220 °C for PLA and then use another piece of filament to push this through from the top to try to force the stuck filament in the nozzle out. Usually, if the new filament hasn’t succeeded in unblocking then the extra pressure you can exert by hand might just do the job. However, don’t push too hard as you’ll risk bending the horizontal printer rods.

## 3\) DISMANTLE AND REBUILD THE HOT END

In extreme cases when the nozzle remains blocked, you’ll need to do a little surgery and dismantle the hot end. If you’ve never done this before then it’s a good idea to make notes and take photographs so you know where everything fits when you reassemble. Start by removing the filament, then check your printer’s manual to see exactly how to dismantle the hot end.

\+ The Atomic Pull

1\) ATOMIC PULL PART I – CHOOSE A MATERIAL

You can use ABS or Nylon for this, but over time we’ve found that the most consistent results come from Nylon due to its higher melting point. The filament also holds its shape far better. ABS is more common however, so we’ll use it here.

2\) ATOMIC PULL PART II – REMOVE FILAMENT

Start by removing the filament that’s already in the print head in the usual way for your printer. Then remove the Bowden tube or release the direct drive, so that when the time comes you can manually feed the filament through.

3\) ATOMIC PULL PART III – INCREASE THE NOZZLE TEMPERATURE

Increase the nozzle temperature to 240 degrees. We’re using ABS, but if using Nylon check the melting point temperature on the packaging. Leave it at this temperature for 5 minutes without pushing the filament through.

4\) ATOMIC PULL PART IV – PUSH THE FILAMENT THROUGH

Slowly apply pressure to the filament until it starts to come out of the nozzle. Pull it back slightly and push it back through again until it starts to flow from the nozzle.

5\) ATOMIC PULL PART V – REDUCE THE NOZZLE TEMPERATURE

Reduce the temperature to 180 degrees for ABS or 140 degrees for Nylon (you’ll need to experiment a little for your filament). Leave the printer at this temperature for 5 minutes.

6\) ATOMIC PULL PART VI – EXTRACT THE FILAMENT

Pull out the filament from the head. When you look at the end you should see some black carbonized material at the end. Repeat the process until clean. If the filament won’t pull from the nozzle, increase the hot end temperature slightly.
