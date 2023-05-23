Implicit Neural Representations with Periodic Activation Functions [![[/snapshots/Q5g3p9Zwjrk/00-00-03.png]]](<https://youtu.be/Q5g3p9Zwjrk?t=0s>)
### Implicit Neural Representations with Periodic Activation Functions  [![[/snapshots/Q5g3p9Zwjrk/00-00-03.png]]](<https://youtu.be/Q5g3p9Zwjrk?t=0s>)
#### Introduction and Overview
SIREN (Sinusoidal Representation Networks) is a new model that can represent signals such as images, sound, waves or point clouds as functions by mapping their coordinates to their values. The authors introduce siren neural networks that use sine waves as their nonlinearities instead of ReLU or hyperbolic tangent functions. Initializing these networks carefully allows them to capture signals very well. [![[/snapshots/Q5g3p9Zwjrk/00-54-39.png]]](<https://youtu.be/Q5g3p9Zwjrk?t=3276s>)

#### SIREN Architecture and Initialization
SIREN is an MLP (Multi-Layer Perceptron) model. The only difference from classic MLPs is that they use sine wave as activation functions instead of ReLU or sigmoid functions. The initialization of the weights and biases in the siren networks plays an essential role as improper initialization may lead to poor performance. The authors propose an initialization scheme that bends the input to each of the sine activation functions to be normally distributed. [![[/snapshots/Q5g3p9Zwjrk/00-01-06.png]]](<https://youtu.be/Q5g3p9Zwjrk?t=62s>)

#### Fitting Image Gradients and Laplacian [![[/snapshots/Q5g3p9Zwjrk/00-27-20.png]]](<https://youtu.be/Q5g3p9Zwjrk?t=1638s>)
SIREN can match not only an image but also its derivatives. They showcase this property by training siren networks to match the image's first and second derivatives (gradients and Laplacian). By matching the gradients, the network is able to reproduce the image with high fidelity while only using the gradient information. Similarly, when matching the Laplacian, the reconstructed image is still of good quality, despite missing the constant luminosity in both the first and second derivative. [![[/snapshots/Q5g3p9Zwjrk/00-52-24.png]]](<https://youtu.be/Q5g3p9Zwjrk?t=3139s>)

#### Practical Applications and Conclusion
SIREN demonstrates that neural representations with periodic activation functions allow more faithful representation of images and signals than traditional neural networks. The ability to match not only the image but also its derivatives opens up new possibilities in image processing and signal understanding. The initialization is crucial for SIREN networks' performance, and researchers should keep this in mind when experimenting with sine wave activation functions in deep learning models. 

Source: [(167) SIREN: Implicit Neural Representations with Periodic Activation Functions [![[/snapshots/Q5g3p9Zwjrk/00-00-03.png]]](<https://youtu.be/Q5g3p9Zwjrk?t=0s>) (Paper Explained) - YouTube](https://www.youtube.com/watch?v=Q5g3p9Zwjrk)
