## Structured 3D Features (S3Fs)
### Introduction to Structured 3D Features (S3Fs) [![[/snapshots/mcZGcQ6L-2s/00-00-04.png]]](<https://youtu.be/mcZGcQ6L-2s?t=0s>)
Structured 3D Features (S3Fs) is a novel feature representation for 3D human reconstruction that enables a single model to perform various tasks such as 3D reconstruction, novel view synthesis, 3D human relighting, avatar animation, and 3D virtual try-on using just one monocular input image. 

### S3Fs Pipeline
The pipeline starts with extracting image features using the Feature Extractor Network, estimating 3D body pose and shape, sampling 3D points on the body surface, and pulling per point features from the image feature map. The network then moves the points freely to discover optimal 3D feature locations, resulting in structured 3D features that better cover the full body geometry. [![[/snapshots/mcZGcQ6L-2s/00-01-09.png]]](<https://youtu.be/mcZGcQ6L-2s?t=66s>)

### 3D Manipulation and Applications
S3Fs carry over semantic information from the body model and can be manipulated in 3D, enabling various applications such as animation and 3D virtual try-on. Using a transformer architecture, they can obtain sign distance and albedo, as well as model scene illumination for realistic lighting effects. [![[/snapshots/mcZGcQ6L-2s/00-01-45.png]]](<https://youtu.be/mcZGcQ6L-2s?t=102s>)

### Comparison to Previous Methods
S3Fs outperform previous state-of-the-art methods, such as ICON and FORUM, in monocular 3D human reconstruction by providing better coverage of loose clothing and more robust performance under challenging body poses. Additionally, they offer more accurate shading estimations that are consistent with input images. 

### Relighting and Avatar Animation
The proposed representation enables relighting of 3D reconstructions for more realistic placement in novel scenes and avatar animation using linear blend skinning. [![[/snapshots/mcZGcQ6L-2s/00-04-10.png]]](<https://youtu.be/mcZGcQ6L-2s?t=246s>)

### 3D Virtual Try-On
S3Fs enable virtual try-on by interpolating structured 3D features between target clothing and source images, resulting in smooth cloth texture interpolations even when there are significant differences in style, viewpoint, or body poses and shapes. This process requires only one image of the target person and one image of the piece of clothing, with no additional post-processing needed. [![[/snapshots/mcZGcQ6L-2s/00-05-01.png]]](<https://youtu.be/mcZGcQ6L-2s?t=298s>)

Source: [(195) CVPR 2023: Structured 3D Features for Reconstructing Relightable and Animatable Avatars - YouTube](https://www.youtube.com/watch?v=mcZGcQ6L-2s)
