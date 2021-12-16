---
layout: slide
title: ""
---

# The pothole detection problem
##### **our approach to automate the collection of masks for training**

<div markdown="1" style="font-size:2vw;ul{font-size:10vw};">

- Why did we choose semantic segmentation for road damage?
	- it's a difficult problem
	- in 2020 it was a problem that didn't seem so much addressed in the literature
	- semantic segmentation is the top in terms of information content extracted from the image
	- [video](http://deeplearning.ge.imati.cnr.it/genova-5G/video/crocetta-field-tests/wls-2021-06-08-17-44-28-libx265-short-fixed.html){: .pleaseletmeclickonthislink8px}
	- the semantic segmentation problem can somehow be mapped to a pothole depth problem!

</div>
<br>



<div markdown="1" style="font-size:1vw;ul{font-size:10vw};margin-left:15%;text-align:left;">
[1] “We Learn Better Road Pothole Detection: from Attention Aggregation to Adversarial Domain Adaptation”, Rui Fan, Hengli Wang, Mohammud J. Bocus, Ming Liu, In Proceedings of European Conference on Computer Vision (ECCV) Workshops, 2020 -<b>[Link to the project and to Pothole-600 dataset](https://sites.google.com/view/pothole-600){: .pleaseletmeclickonthislink}</b><br>
</div>

{:refdef: style="margin-left:5%;margin-top:-2%"}
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="200vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>

<div markdown="1" class="pic_with_text" style="float:left;left:25%;">
![classif](img/pothole-imgs/potholes-segmentation-sota-lowres-1-rgb.jpg){: .pic_with_text height="250vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">RGB</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:25%;">
![classif](img/pothole-imgs/potholes-segmentation-sota-lowres-2-rawdepth.jpg){: .pic_with_text height="250vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Raw Disparity</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:25%;">
![classif](img/pothole-imgs/potholes-segmentation-sota-lowres-3-postprocdepth.jpg){: .pic_with_text height="250vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Postproc. Disparity</p></div></div>
{:refdef}

<!--
{:refdef: style="margin-left:5%;margin-top:-2%"}
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="200vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="200vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>

<div markdown="1" class="pic_with_text" style="float:left;left:25%;">
![classif](img/pothole-imgs/pothole-classif.png){: .pic_with_text height="250vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Classification</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:15%;">
![objdet](img/pothole-imgs/pothole-object-detection.png){: .pic_with_text height="250vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Obj. Detection</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:15%;">
![segmentation](img/pothole-imgs/pothole-semantic-segmentation.png){: .pic_with_text height="250vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Sem. Segmentation</p></div></div>
{:refdef}
-->
