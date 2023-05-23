## Event NERF
### Introduction to Event Cameras

Event cameras record asynchronous events, which are per-pixel changes in brightness. This results in high dynamic range, lack of motion blur, low latency, improved data bandwidth, and less power consumption. They have been applied to numerous computer vision problems, such as optical flow estimation, video interpolation, and 3D pose estimation. [![[/snapshots/AjtljRfIn68/00-00-06.png]]](<https://youtu.be/AjtljRfIn68?t=0s>)

### 3D Reconstruction with Event Cameras [![[/snapshots/AjtljRfIn68/00-00-47.png]]](<https://youtu.be/AjtljRfIn68?t=44s>)

Current event-based 3D reconstruction approaches can only recover sparse, colorless point clouds of the scene. The research question addressed in this work is if just an event stream from an event camera moving around a scene is sufficient to reconstruct a dense volumetric 3D representation of that static scene in the absence of RGB images. The proposed approach is called Event NERF. 

### Neural Radiance Fields (NERF) 

Neural Radiance Fields (NERF) is a state-of-the-art coordinate-based volumetric 3D scene representation. The researchers adopt NERF to connect the event stream and volumetric scene model. [![[/snapshots/AjtljRfIn68/00-01-41.png]]](<https://youtu.be/AjtljRfIn68?t=98s>)

### Ray Sampling Strategy for Event NERF [![[/snapshots/AjtljRfIn68/00-03-17.png]]](<https://youtu.be/AjtljRfIn68?t=193s>)

The ray sampling strategy involves splitting the event stream into intervals, picking random window ends and lengths, and applying positive and negative sampling. This strategy allows for efficient and consistent training. [![[/snapshots/AjtljRfIn68/00-02-39.png]]](<https://youtu.be/AjtljRfIn68?t=155s>)

### Experiments and Results

Event NERF shows improved performance over the baseline method (E2VID + NERF) on both synthetic and real data. This includes handling high dynamic range, reconstructing sharp color details, fuzzy materials, and view-dependent effects. [![[/snapshots/AjtljRfIn68/00-06-51.png]]](<https://youtu.be/AjtljRfIn68?t=408s>)

### Ablation Study

Using fixed long windows instead of randomized window lengths results in loss of fine detail and minor artifacts. Disabling negative sampling results in significant artifacts. However, the model demonstrates data efficiency by reconstructing scenes using as little as 3% of the data. [![[/snapshots/AjtljRfIn68/00-07-11.png]]](<https://youtu.be/AjtljRfIn68?t=429s>)

### Mesh extraction and Torch NGP integration [![[/snapshots/AjtljRfIn68/00-08-24.png]]](<https://youtu.be/AjtljRfIn68?t=500s>)

Event NERF can be used to reconstruct detailed textured 3D meshes using marching cubes. The method can also be integrated with Torch NGP for real-time rendering on a single consumer GPU. [![[/snapshots/AjtljRfIn68/00-08-02.png]]](<https://youtu.be/AjtljRfIn68?t=478s>)

### Conclusion and Future Applications

Event NERF shows promise in various applications, such as fast object scanning and reconstruction on factory floors. The code and data will be publicly released in the future. [![[/snapshots/AjtljRfIn68/00-08-16.png]]](<https://youtu.be/AjtljRfIn68?t=492s>)

Source: [(167) CVPR 2023 EventNeRF: Neural Radiance Fields from a Single Colour Event Camera - YouTube](https://www.youtube.com/watch?v=AjtljRfIn68)
