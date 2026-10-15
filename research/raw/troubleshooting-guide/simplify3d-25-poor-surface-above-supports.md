---
source_block: simplify3d
entry: 25
title: "Poor Surface Above Supports"
origin: https://www.simplify3d.com/resources/print-quality-troubleshooting/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Poor Surface Above Supports

One of the major benefits of Simplify3D is the ability to create innovative support structures which allow you to create incredibly complex parts that would be hard to manufacture otherwise. For example, if you have a steep overhang or part of your model with nothing below it, then a support structure can provide a foundation for these layers. The support structures created by Simplify3D are disposable and can be easily separated from the final part. However, depending on your settings, you may find that some adjustments are needed to perfect the surface quality on the underside of your parts, right above the support structure foundation.

## 1\) Lower Your Layer Height

The overhang performance of your printer can be greatly improved by lowering your layer height. For example, if you reduced your layer height from 0.2mm to 0.1mm, your printer will create twice as many layers, which allows your printer to take smaller steps when creating an overhang. For this reason, your may find that you need support structures for any overhang above 45 degrees when using a 0.2mm layer height, but your overhang performance may improve to 60 degrees if you lower your layer height to 0.1mm. This has the obvious advantage of decreasing your print time and reducing the amount of support structures required for the print, but it will also allow you to create a smoother surface on the underside of your parts. If you find that you need to increase the print quality in this area, this is one of the first settings you will want to adjust.

## 2\) Support Infill Percentage

Just like the interior of your part, you can also adjust the density of your support structures by changing the Support Infill Percentage. It is common to use a value around 20-40%, but you may find that you need to increase this value if the bottom layers of your part are drooping too much. Many users also prefer to use Dense Support Structures for this task, as they allow you to use a lower density for the majority of your supports, and only use a higher infill percentage near the very top of the support structures.

## 3\) Vertical Separation Layers

Creating removable support structures involves a fine balance between the amount of support provided to the model, and how easy the supports are to remove. If you provide too much support to the model, the support structures may start to bond to the part, making them difficult to separate. If you provide very little support, the disposable support structures will be easy to remove, but the part may not have enough of a foundation to print successfully. Simplify3D allows your to customize the separation settings, so that you can choose the correct balance between these different factors. The first setting you will want to check is the Upper Vertical Separation Layers. This setting determines how many empty layers are left between the support structures and the part. For example, if you are printing your support structures with the same material as your part, it is common to use at least 1-2 vertical separation layers. Otherwise, if you used 0 separation layers and you are printing everything with the same material, the supports may bond to the part and can become difficult to remove. So this is one of the first settings you want to adjust as you try to perfect your print quality.

## 4\) Horizontal Part Offset

The next separation setting you should check is the Horizontal Offset from your part. This setting controls the side-to-side distance between your part and the support structures. So while the Vertical Separation Layers can help keep the top of your supports from bonding to the bottom of your part, the Horizontal Offset will keep the sides of your supports from bonding to the side of your model. It is common to use a value between 0.2-0.4mm for this setting, but you may need to experiment and see what works best for your specific extruder and filament.

## 5\) Use a Second Extruder

If your machine comes with 2 or more extruders, you can achieve a significant improvement by using a different material for your support structures. For example, it is quite common to print parts in PLA using water dissolvable PVA for the supports. Because the model and support structures are printed with different materials, they won’t bond together as easily, which allows you to do a better job of supporting the part. If you are using a different material for the support structures, you can frequently decrease your Upper Vertical Separation Layers to zero, and reduce your Horizontal Offset from the part to around 0.1mm.
