---
layout: slide
title: ""
---

# 3D Dynamic Hand Gestures Recognition
##### **problem outline**

<div markdown="1" style="font-size:2vw">

- Dynamic Hand Gestures Recognition can be split into two subproblems:
	- acquisition of the skeletons of the hands (hard)
		- through hardware like gloves or Leap Motion
		- through software with other NN models like Google MediaPipe
		- (we're using the Leap Motion sensor now because it's convenient, but our approach is versatile)
	- actual understanding of the dynamic gesture using "its whole history" (also hard)
		- training "traditional" tabular data classifiers (SVMs, feed-forward NN, LSTMs)
		- training CNN classifiers to leverage 2D image structure -> powerful (learned) features extractors + transfer learning

</div>

<!-- | <figcaption class="figcaption" markdown="1"> Grab </figcaption> | <figcaption class="figcaption" markdown="1"> Pinch </figcaption> | -->

![grab](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/grab.gif){: .slideimage height="15%" width="15%"}
![pinch](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/pinch.gif){: .slideimage height="15%" width="15%"}
![tap](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/tap.gif){: .slideimage height="15%" width="15%"}
![swipe-left](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/swipe-left.gif){: .slideimage height="15%" width="15%"}
![swipe-right](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/swipe-right.gif){: .slideimage height="15%" width="15%"}
![swipe-O](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/swipe-O.gif){: .slideimage height="15%" width="15%"}
![swipe-V](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/swipe-V.gif){: .slideimage height="15%" width="15%"}
![OK](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/OK.gif){: .slideimage height="15%" width="15%"}
![expand](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/expand.gif){: .slideimage height="15%" width="15%"}
![three](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/three.gif){: .slideimage height="15%" width="15%"}

<!--
![one](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/one.gif){: .slideimage height="15%" width="15%"}
![two](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/two.gif){: .slideimage height="15%" width="15%"}
![four](assets/pics/old-imgs/dynamic-hands-gestures-animated-gifs/four.gif){: .slideimage height="15%" width="15%"}
-->


<!-- figcaption class="figcaption" markdown="1">

Credits: [Visualizing the Loss Landscape of Neural Nets](https://arxiv.org/pdf/1712.09913.pdf){: .pleaseletmeclickonthislink}

</figcaption -->

