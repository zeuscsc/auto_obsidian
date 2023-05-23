## NERF -  Neural Radiance Fields [![[/snapshots/CRlN-cYFxTk/00-01-40.png]]](<https://youtu.be/CRlN-cYFxTk?t=97s>)
### NERF: Neural Radiance Fields for View Synthesis 

#### Overview
The paper, "Representing Scenes as Neural Radiance Fields for View Synthesis", introduces a method for synthesizing novel views of complex scenes by overfitting a neural network to a single scene, instead of using traditional datasets. The method, called NERF - Neural Radiance Fields, optimizes a continuous volumetric scene function using a sparse set of input views. 

#### Method
The input of the neural network is a 3D position and a 2D viewing direction. The output is a color and volume density at that location. The network is trained by shooting rays through every pixel in a given set of images, sampling positions along the ray, and calculating the difference between what is seen and what the network predicts to be seen. [![[/snapshots/CRlN-cYFxTk/00-09-27.png]]](<https://youtu.be/CRlN-cYFxTk?t=564s>)

#### Benefits & Results
1. A compact and accurate representation of the scene is stored in the neural network weights. [![[/snapshots/CRlN-cYFxTk/00-07-50.png]]](<https://youtu.be/CRlN-cYFxTk?t=468s>)
2. The method can handle fine-grained structure, reflections, and transparency. [![[/snapshots/CRlN-cYFxTk/00-13-57.png]]](<https://youtu.be/CRlN-cYFxTk?t=833s>)
3. The optimized network can generate new views quickly (once training is complete) [![[/snapshots/CRlN-cYFxTk/00-30-05.png]]](<https://youtu.be/CRlN-cYFxTk?t=1803s>)
4. The model can provide depth maps, AR, and actual meshes for complex scenes. [![[/snapshots/CRlN-cYFxTk/00-03-10.png]]](<https://youtu.be/CRlN-cYFxTk?t=188s>)

#### Limitations
Training a single neural network for a scene can take 1-2 days on a single GPU, but it only needs to be done once. Once trained, the network can render new views as needed. [![[/snapshots/CRlN-cYFxTk/00-30-42.png]]](<https://youtu.be/CRlN-cYFxTk?t=1840s>)

#### Conclusion
NERF is a novel method for view synthesis that overfits a neural network to a specific scene, optimizing a continuous volumetric scene function. This method is highly efficient and can handle complex information, such as fine-grained structure, reflections, and transparency. 

Source: [(167) NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis (ML Research Paper Explained) - YouTube](https://www.youtube.com/watch?v=CRlN-cYFxTk&list=WL&index=24&t=524s)
