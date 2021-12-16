---
layout: slide
title: ""
---

# The pothole detection problem
##### **training results**

<div markdown="1" style="font-size:2vw;ul{font-size:10vw};">

- Neural network training is progressing very well (beyond our expectations)
	- the metrics on the validation set are more than good as well
	- train/valid loss: 0.037/0.04 
	- net pixel acc/Dice Multi: 0.625/0.798
- What really matters is the "quality" of the segmentation on a real (and large) test set

<br>

{:refdef: style="margin-left:5%;margin-top:-2%"}
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="200vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="200vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>

<div markdown="1" class="pic_with_text" style="float:left;left:25%;">
[![classif](img/pothole-imgs/training-results.jpg){: .pic_with_text height="450vw"}](img/pothole-imgs/training-results.jpg){: .pleaseletmeclickonthislink}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Training Results</p></div></div>
{:refdef}

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
