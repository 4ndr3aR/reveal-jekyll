---
layout: slide
title: ""
---

# 3D Dynamic Hand Gestures Recognition
##### **our approach**

<div markdown="1" style="font-size:2vw">

- Acquire hands skeleton data via the Leap Motion sensor (138 floats + label)
- Reinterpret the data to match the Leap Motion connection map to obtain both nodes and edges
- Draw the skeleton into a custom 3D visualizer made with VisPy (PyQt5 backend)
- Draw only the nodes representing the fingertips
- As the gesture progresses, keep the fingertips history and draw it with decreasing alpha values
	- The history of the gesture fades away with time
- Add variable amounts of 3D noise as further data augmentation
- Capture the canvas of the 3D visualizer as the gesture progresses to create the dataset
	- With different amounts of fingertips history and noise
	- 4.6 Gb, ~77k images (starting from 468 training sequences)

</div>



![swipe-O-hst-050](assets/pics/old-imgs/swipe-O-variable-history-lenght-and-noise/swipe-O-75-datafile-swipe-o-4.csv-hst-050.png){: .slideimage height="22%" width="22%"}
![swipe-O-hst-200](assets/pics/old-imgs/swipe-O-variable-history-lenght-and-noise/swipe-O-75-datafile-swipe-o-4.csv-hst-200.png){: .slideimage height="22%" width="22%"}
![swipe-O-hst-400](assets/pics/old-imgs/swipe-O-variable-history-lenght-and-noise/swipe-O-75-datafile-swipe-o-4.csv-hst-400.png){: .slideimage height="22%" width="22%"}
![swipe-O-hst-400-noise](assets/pics/old-imgs/swipe-O-variable-history-lenght-and-noise/swipe-O-75-datafile-swipe-o-4.csv-hst-400-noise.png){: .slideimage height="22%" width="22%"}
