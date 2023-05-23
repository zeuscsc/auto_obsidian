## Denoising Diffusion Model
### Introduction
This tutorial covers the implementation of a denoising diffusion model in PyTorch for image generation. Denoising diffusion models belong to the domain of generative deep learning, alongside variations like generative adversarial networks (GANs) and variational autoencoders (VAEs). Diffusion models work by incrementally adding noise to the input until pure noise is left over and then recovering the input from the noise using a neural network. [![[/snapshots/a4Yfz2FxXiY/00-00-03.png]]](<https://youtu.be/a4Yfz2FxXiY?t=0s>)

### Dataset and Implementation Overview
We will be fitting a diffusion model on the Stanford Cars dataset. This dataset is comprised of around 16,000 images of cars in various poses and backgrounds. Our implementation involves four main components: a scheduler to sequentially add noise, a U-Net model to predict the noise in an image, and encoding the current time step. [![[/snapshots/a4Yfz2FxXiY/00-02-49.png]]](<https://youtu.be/a4Yfz2FxXiY?t=167s>)

### Scheduler and Forward Process
The scheduler sequentially adds noise and is dependent on a variance schedule. By calculating the cumulative product of the alpha terms, we can specify a new distribution that allows us to sample for a specific time step. The forward process adds noise gradually to an image, with the noise level controlled by the variance schedule. [![[/snapshots/a4Yfz2FxXiY/00-07-36.png]]](<https://youtu.be/a4Yfz2FxXiY?t=453s>)

### U-Net and Backward Process
The U-Net is a type of neural network architecture that is suitable for image segmentation tasks. It shares some structural similarities with autoencoders, featuring a series of convolutional layers, down/up-sampling, and residual connections. The U-Net takes a noisy image with three colored channels as input and predicts the noise in the image. The backward process is formulated by learning the probability density of an earlier time step given the current time step and using the predicted Gaussian noise distribution in the image. [![[/snapshots/a4Yfz2FxXiY/00-16-31.png]]](<https://youtu.be/a4Yfz2FxXiY?t=988s>)

### Time Steps and Positional Embeddings [![[/snapshots/a4Yfz2FxXiY/00-05-21.png]]](<https://youtu.be/a4Yfz2FxXiY?t=320s>)
To accommodate varying time steps, we use positional embeddings, a component found in transformer models. Positional embeddings assign different vectors to each index, usually calculated using sine and cosine functions. These embeddings are added as additional input to the model. [![[/snapshots/a4Yfz2FxXiY/00-19-56.png]]](<https://youtu.be/a4Yfz2FxXiY?t=1193s>)

### Loss Function and Training
The loss function used to optimize the diffusion models is the L2 distance of the predicted noise and the actual noise in the image. Finally, we train the model and optimize it using this loss function.  

### Conclusion
The diffusion models show great promise in generating high-quality images, even though the sampling speed is slower compared to GANs and VAEs. By training the model longer, and refining the model architecture, higher-resolution images can be achieved. Future applications of diffusion models involve molecule graphs, audio, and other domains. [![[/snapshots/a4Yfz2FxXiY/00-03-05.png]]](<https://youtu.be/a4Yfz2FxXiY?t=183s>)

Source: [(97) Diffusion models from scratch in PyTorch - YouTube](https://www.youtube.com/watch?v=a4Yfz2FxXiY)
