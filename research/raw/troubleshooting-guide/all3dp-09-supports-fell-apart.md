---
source_block: all3dp
entry: 9
title: "Supports Fell Apart"
origin: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
dataset: https://github.com/hyungjungkim/3D-printing-troubleshooting-guide/blob/cedd5fb/3D-Printer-Troubleshooting-Guide-Markdown.md
citation: "Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp"
---
# Supports Fell Apart

Printing complex models will require a support or two, and whilst supports can be a pain to remove, they’re unfortunately an essential part of modeling. The job of support is simple, it supports, but occasionally they fail, leaving your model unsupported. You’ll notice that as your print is extruded parts of the support structure will look uneven, cracks may appear or they’ll just start to look stingy. Not only are the supports failing but the additional filament is ruining your model rather than ensuring it prints correctly.

Cause

Support structures are complex things and most slicer applications will provide you with several options. It’s all too easy to stick with the default settings, but this doesn’t guarantee success with your 3D printed overhangs. An important consideration is the type of support that will keep your model steady and supported throughout the print. Lines and zig zags are generally easy to remove after the print has finished, but offer less rigidity during the print process. Triangles and grids offer more support but can be a pain to remove. Take a simple bridge structure with thin uprights and then think about the supports. They will have a great deal of work to do keeping the model rigid, if you’ve opted for lines or zig zags then the likelihood is the model will move during the print process, breaking the delicate supports as it goes.

## 1\) SELECT THE CORRECT SUPPORTS

Look at the type of model you’re about to print. If there are large overhangs that connect sections of the model and these have good contact with the platform, try using lines or zig zag supports. If the model has less bed contact or needs much stronger supports, use grid or triangle supports.

## 2\) ADD PLATFORM ADHESION

Make sure you have added some type of platform adhesion, such as a brim, so that the mounts have plenty of foundation to bond to.

## 3\) INCREASE THE SUPPORT DENSITY

Try this as a last resort. Increasing the support density will offer your model a denser structure to rest on and will be less affected by any model movement, but will be much tougher to remove.

## 4\) CREATE IN-MODEL SUPPORTS

Supports that are overly tall can be susceptible to weakness. By adding a tall block as part of your print that ends just below where the supports are required, the supports are given a solid base without the need to print tall and weak.

## 5\) CHANGE FILAMENT

Filament can become brittle as it reaches the end of its usable life span, and this usually shows in the quality of the supports. Swap the filament for a fresh reel and see if the problem improves

## 6\) CHECK EVERYTHING IS TIGHT

Printer shakes and wobble can be a real issue. Give your machine the once over and make sure that everything is tight and re-calibrate if needed.
