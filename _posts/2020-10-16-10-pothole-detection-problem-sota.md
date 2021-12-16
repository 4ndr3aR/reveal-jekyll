---
layout: slide
title: ""
---

# The pothole detection problem
##### **state of the art**

<div markdown="1" style="font-size:2vw;ul{font-size:10vw};">

- Early attempts of pothole detection in the pre-Deep Learning era
	- using a wide range of sensors (RGB/infrared/depth cameras, LIDAR, accelerometers, etc.) \[[1](https://ieeexplore.ieee.org/document/5978573){: .pleaseletmeclickonthislink8px}\]
	- and conventional Computer Vision (thresholding, denoising, background subtraction, segmentation, shape estimation, etc.) \[[2](https://www.researchgate.net/profile/Ioannis-Brilakis/publication/220371471_Pothole_detection_in_asphalt_pavement_images/links/59f4b2a9aca272607e2a84b6/Pothole-detection-in-asphalt-pavement-images.pdf){: .pleaseletmeclickonthislink8px}\]

- The deep learning era boosted research in this area
	- Classification \[[3](https://link.springer.com/chapter/10.1007%2F978-3-030-00220-6_72){: .pleaseletmeclickonthislink8px}\]
	- Object detection \[[4](https://ieeexplore.ieee.org/document/9112424){: .pleaseletmeclickonthislink8px}\]
	- <span style="color:#e8103f"><b>Semantic segmentation</b></span> \[[5](https://arxiv.org/abs/2008.06840){: .pleaseletmeclickonthislink8px}\]
</div>



<div markdown="1" style="font-size:1vw;ul{font-size:10vw};margin-left:15%;text-align:left;">
[1] Pavement Pothole Detection and Severity Measurement Using Laser Imaging, Yu et al., 2011<br>
[2] Pothole detection in asphalt pavement images, Koch et al., 2011<br>
[3] Computer Vision and Deep Learning for Real-Time Pavement Distress Detection, Doycheva et al., 2019<br>
[4] Deep Learning based Detection of potholes in Indian roads using YOLO, Dharneeshkar et al., 2020<br>
[5] We Learn Better Road Pothole Detection: from Attention Aggregation to Adversarial Domain Adaptation, Fan et al., 2020<br>
</div>

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
![segmentation](img/pothole-imgs/pothole-semantic-segmentation-example.png){: .pic_with_text height="250vw"}
<div markdown="1" class="text_anim_over_pic"><p class="text_anim_over_pic_content">Sem. Segmentation</p></div></div>
{:refdef}

