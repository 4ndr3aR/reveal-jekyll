---
layout: slide
title: ""
---

# The pothole detection problem
##### **conclusions and next steps**

<div markdown="1" style="font-size:2vw;ul{font-size:10vw};">

- Permanent or semi-permanent installation of the RGB-D camera on the bus provided by AMT
	- integration of our image acquisition system with the software of the on-board unit by Leonardo
- Enrichment of the training dataset
	- with images and videos (both RGB and depth) acquired from the bus
	- with images and masks obtained performing inference on the field test videos with the current model
- Re-training of the neural network model with the new enriched dataset
- Porting of the model on the Vodafone infrastructure for real-time inference with 5G connectivity 
</div>

<br>

{:refdef: style="margin-left:5%;margin-top:-2%"}

<div markdown="1" class="pic_with_text" style="float:left;left:25%;">
[![classif](img/pothole-imgs/bus-installation-gallery-horiz.jpg){: .pic_with_text height="220vw"}](img/pothole-imgs/bus-installation-gallery-vert.png){: .pleaseletmeclickonthislink}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">AMT bus installation</p></div></div>
{:refdef}
