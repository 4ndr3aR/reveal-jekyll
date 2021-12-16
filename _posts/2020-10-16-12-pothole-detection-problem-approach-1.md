---
layout: slide
title: ""
---

# The pothole detection problem
##### **our approach to automate the collection of masks for training**

<div markdown="1" style="font-size:2vw;ul{font-size:10vw};">

- Basically, to install a depth cam on "some vehicle"
	- also called RGB-D camera (or simply stereo camera)
	- capable of extracting depth information as well as the normal RGB stream ([video](http://deeplearning.ge.imati.cnr.it/genova-5G/video/crocetta-field-tests/wls-2021-06-08-17-44-28-libx265-short-fixed.html){: .pleaseletmeclickonthislink8px})

</div>
<br>


<video height="50%" controls autoplay muted loop>
  <source src="http://deeplearning.ge.imati.cnr.it/genova-5G/video/crocetta-field-tests/wls-2021-06-08-17-44-28-libx265-short-fixed.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>



<!--
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

-->
