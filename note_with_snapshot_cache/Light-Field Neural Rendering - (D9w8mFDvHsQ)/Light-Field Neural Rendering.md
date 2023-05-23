## Light-Field Neural Rendering
### Introduction to Light-Field Neural Rendering [![[/snapshots/D9w8mFDvHsQ/00-01-04.png]]](<https://youtu.be/D9w8mFDvHsQ?t=62s>)

Light-Field Neural Rendering is a new image-based rendering method for novel view synthesis. It is specifically designed to address complex view-dependent effects which challenges existing methods such as Neural Radiance Fields (NeRF) and follows up works like NEX. [![[/snapshots/D9w8mFDvHsQ/00-00-20.png]]](<https://youtu.be/D9w8mFDvHsQ?t=18s>)

### Limitations of Prior Methods

NERF and NEX have made significant progress in photorealistic view synthesis but struggle with severe non-Lambertian effects, such as refractions through liquid. Light-Field Neural Rendering outperforms them in rendering such complex effects. 

### Incorporating Geometric Bias

Light-Field Neural Rendering uses Light-Fields to represent a scene. Incorporating a geometric bias in the rendering framework using the epipolar constraint addresses the limitations of multi-view consistency in Light-Fields. 

### Epipolar Feature Transformer

This transformer is used to reason about correspondences in reference views and aggregate features of points along the epipolar line. It helps estimate attention weights between each epipolar point and the target ray. [![[/snapshots/D9w8mFDvHsQ/00-02-23.png]]](<https://youtu.be/D9w8mFDvHsQ?t=141s>)

### View Feature Transformer

This transformer is responsible for reasoning about occlusions and aggregating features from multiple reference views. It helps estimate pairwise attention weights for each view concerning the target ray. [![[/snapshots/D9w8mFDvHsQ/00-03-20.png]]](<https://youtu.be/D9w8mFDvHsQ?t=197s>)

### Experimental Results

Light-Field Neural Rendering outperforms state-of-the-art methods like NERF, NEX, and MIP-NERF on various datasets, including RFF, Blender, and Shiny datasets. Its ability to reconstruct complex view-dependent effects can be attributed to the attention-based aggregation mechanism. 

### Conclusion and Project Details

For more information on Light-Field Neural Rendering, including additional results and code, visit the project webpage. [![[/snapshots/D9w8mFDvHsQ/00-00-02.png]]](<https://youtu.be/D9w8mFDvHsQ?t=0s>)

Source: [CVPR 2022 Light Field Neural Rendering - YouTube](https://www.youtube.com/watch?v=D9w8mFDvHsQ)
