---
source_block: all3dp
entry: 22
title: "Print is Unusually Weak/Looks Wrong (Non-Manifold Edges)"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Print is Unusually Weak/Looks Wrong (Non-Manifold Edges)

Parts of your print are missing or the final print is weak and falls apart despite the exterior quality of the print looking fine. Sections of the print look completely different from the print preview or the final print has geometry errors that make no sense.

Cause

Non-manifold edges are a common cause of misshapen or odd prints. Non-manifold edges are the edges of models that can only exist in the 3D space and not the physical world. For example, if you have two cubes in the real world and try to overlap them directly, it’s physically impossible as the solid outer walls prevent the two objects from intersecting. In the 3D world you can simply intersect the two, they still exist as individual objects, but the software we use distinguishes between them regardless of the perceived oneness as we look at them. In order to get the two to print correctly, the objects need to be merged so that any inner walls are removed and an object with a single undivided inner cavity is left. Another common cause is if you have an object such as a cube and delete one of the surfaces. You essentially have an object with a hole, it might look like a shape with five sides, but it only exists in the virtual 3D space, this is geometry with no physical form. Although you can see the outer walls in the software, the walls that meet the hole only have dimensions on two axes. The third dimension which we see as the thickness of the wall is only illustrative and has no real physical dimension. When it comes to slicing the model the software does its best and in many cases will repair the hole. However, in more complex models, the effects can be interesting to say the least.

## 1\) USE LATEST SLICER SOFTWARE

Most of the latest slicer engines all support the automatic fixing of non-manifold edges but it’s still good practice to ensure that your models are correctly formed and print ready.

## 2\) FIX USING STL FILE REPAIR SOFTWARE

If you’re already using the latest slicer software then you might have noticed a notification telling you that your STL file features some non-manifold edges. Some software can fix this for you of course, and if you’re slicer can’t then there’s a good selection of STL file repair software that can be used on both desktop and the web. It’s a simple and easy task, just upload your file to your chosen software, let it identify any broken sections, then follow the instructions. If you didn’t get a notification on your slicer but your prints are coming out as a weird, messy blob this suggests you have some non-manifold edges in there. Try STL file repair software. It might not fix the problem, but it’s certainly something to try.

## 3\) FIX ‘NON-MANIFOLD’ IN SIMPLIFY3D

In edit ‘Process settings’ click the ‘Advanced’ tab and select ‘Heal’ next to ‘Non-manifold segments.

## 4\) USE THE LAYER VIEW

In your slicer software use the layer view to check through the model so you can see where the issues appear. A quick slide through the layers will often highlight an easy to fix problem.

## 5\) USE MODELING SOFTWARE TO FIX ISSUES

One of the easiest ways to fix models with non-manifold edges is to use software; Programs such as Blender and Meshmixer both have features built in that will quickly enable you to highlight problems with your models and fix them prior to slicing.

## 6\) MERGE OBJECTS

Really it’s better to fix your 3D models prior to importing them into your slicing software. To do this, make sure that when you have two objects that do intersect or overlap you choose the appropriate Boolean function to either intersect, merge or subtract.
