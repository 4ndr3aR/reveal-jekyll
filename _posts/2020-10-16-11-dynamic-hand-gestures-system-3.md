---
layout: slide
title: ""
---

# 3D Dynamic Hand Gestures Recognition
##### **training the network and results**

<div markdown="1" style="font-size:2vw">

- The network has been trained in Python using Jupyter Notebook and the Fast.ai v1 library
	- a little bit more high level than Pytorch
	- great community that keeps it up to date with literature
- ResNet-50 pretrained on ImageNet and on [our other 2k image hand gestures dataset](https://arxiv.org/abs/2003.01450){: .pleaseletmeclickonthislink}
	- [Progressive resizing technique](https://www.biorxiv.org/content/10.1101/740548v3.full){: .pleaseletmeclickonthislink5px} (192x108, 384x216, 576x324 and 960x540)
	- Standard augmentation (rotate, crop+pad, flip, warp, zoom, brightness, contrast)
	- Fit one cycle policy for training [(i.e. cyclical learning rate)](https://arxiv.org/pdf/1506.01186.pdf){: .pleaseletmeclickonthislink5px}

</div>

![view-based-method-classification-accuracy](assets/pics/old-imgs/3DOR-paper-graphs/viewClassification2.png){: .resultsimage height="30%" width="30%"}
![view-based-method-false-positives](assets/pics/old-imgs/3DOR-paper-graphs/FPview.png){: .resultsimage height="35.5%" width="35.5%"}

<figcaption class="figcaption" markdown="1">

Credits: [SFINGE 3D: A novel benchmark for online detection and recognition of heterogeneous hand gestures from 3D fingers’ trajectories](https://www.sciencedirect.com/science/article/pii/S0097849320301163){: .pleaseletmeclickonthislink}

</figcaption>

