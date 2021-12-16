---
layout: slide
title: ""
---

# The pothole detection problem
##### **training and data augmentation**

<div markdown="1" style="font-size:2vw;ul{font-size:10vw};">

- The training of the latest model was carried out with images of segmented cracks and potholes available online
	- approximately 4300 image/mask pairs (a balanced dataset this time)
- Training recipe:
	- [strong data augmentation](img/pothole-imgs/training-and-data-aug.png){: .pleaseletmeclickonthislink8px}
	- low learning rate
	- transfer learning + fine-tuning for many epochs
	- "meaningful" metrics: DiceMulti and "net" pixel accuracy (not considering intact asphalt)
- Progressive resizing during training
	- 360x360 -> 540x540
	- automatic reload of the "best" model between rounds

<!--
</div>
<div markdown="1" class="pic_with_text" style="float:right;left:25%;top:500px">
![classif](img/pothole-imgs/training-and-data-aug.png){: .pic_with_text height="500vw" float="right" top="500px"}
</div>
-->

<!--
{:refdef: style="margin-left:5%;margin-top:-2%"}
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="120vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="120vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="120vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="120vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>

<div markdown="1" class="pic_with_text" style="float:left;left:25%;">
![classif](img/pothole-imgs/training-and-data-aug.png){: .pic_with_text height="750vw" top="-50%"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Data Augmentation</p></div></div>
{:refdef}
-->
