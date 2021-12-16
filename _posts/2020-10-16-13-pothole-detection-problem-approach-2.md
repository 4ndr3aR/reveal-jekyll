---
layout: slide
title: ""
---

# The pothole detection problem
##### **our approach to automate the collection of masks for training**

<div markdown="1" style="font-size:2vw;ul{font-size:10vw};">

- idea: automatically label the images acquired using RGB-D technology
- train the convolutional neural network with RGB and D pairs
- the network learns to produce the segmentation information related to the depth from standard RGB images

- after the training phase, when fully operational, the neural network model works with RGB images only (a normal camera) and outputs segmentation masks of potholes.

</div>
<br>


{:refdef: style="margin-left:5%;margin-top:-2%"}
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="120vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:25%;opacity:0;">
![classif](img/transparent-100x100.png){: .pic_with_text height="120vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Transparent</p></div></div>

<div markdown="1" class="pic_with_text" style="float:left;left:25%;">
![classif](img/pothole-imgs/rectright-2021-06-08-17-14-35.jpg){: .pic_with_text height="350vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Rectified Right</p></div></div>
<div markdown="1" class="pic_with_text" style="float:left;left:25%;">
![classif](img/pothole-imgs/depth-2021-06-08-17-14-35.png){: .pic_with_text height="350vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Raw Disparity</p></div></div>
{:refdef}



<!--
<div markdown="1" style="font-size:1vw;ul{font-size:10vw};margin-left:15%;text-align:left;">
[1] “We Learn Better Road Pothole Detection: from Attention Aggregation to Adversarial Domain Adaptation”, Rui Fan, Hengli Wang, Mohammud J. Bocus, Ming Liu, In Proceedings of European Conference on Computer Vision (ECCV) Workshops, 2020 -<b>[Link to the project and to Pothole-600 dataset](https://sites.google.com/view/pothole-600){: .pleaseletmeclickonthislink}</b><br>
</div>


-->
