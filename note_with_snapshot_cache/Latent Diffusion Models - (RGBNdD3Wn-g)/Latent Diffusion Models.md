## Latent Diffusion Models
### Latent Diffusion Models: An Overview [![[/snapshots/RGBNdD3Wn-g/00-06-16.png]]](<https://youtu.be/RGBNdD3Wn-g?t=374s>)
Diffusion models, including Dolly, Imogen, and Midjourney, have achieved state-of-the-art results in various image tasks. However, their training and inference times are computationally expensive, generally requiring hundreds of GPUs. Latent diffusion models transform the image into a compressed latent representation, making the process more efficient and allowing for different modalities, like text, to be used as input. [![[/snapshots/RGBNdD3Wn-g/00-00-16.png]]](<https://youtu.be/RGBNdD3Wn-g?t=14s>)

#### Diffusion Models: The Basics
Diffusion models iteratively learn to remove noise from random inputs, conditioned with text or an image. They apply further noise to the image iteratively until it becomes unrecognizable. Once the noise from all images is similar, the model is ready to generate new images from similar noise in reverse order. [![[/snapshots/RGBNdD3Wn-g/00-01-12.png]]](<https://youtu.be/RGBNdD3Wn-g?t=70s>)

#### Transforming into Latent Diffusion Models [![[/snapshots/RGBNdD3Wn-g/00-03-29.png]]](<https://youtu.be/RGBNdD3Wn-g?t=207s>)
Latent diffusion models work within a compressed image representation, reconstructing the image with the same quality as other diffusion models but at a fraction of the computation cost. They can also work with different input types, like text or images. 

#### The Overall Model
The model takes an initial image and encodes it into a latent space, a compressed representation of the information in the image. Conditioning inputs (such as text or other images) are merged with the image representation in latent space, creating the initial noise for the diffusion process. A diffusion model is then applied in this latent space, and finally, a decoder reconstructs the image by upsampling the results. [![[/snapshots/RGBNdD3Wn-g/00-05-03.png]]](<https://youtu.be/RGBNdD3Wn-g?t=300s>)

#### Applications and Availability
Latent diffusion models can be used for super-resolution, inpainting, text-to-image generation, and more. The authors of the research have provided open-source pre-trained models for developers to run on their own GPUs. [![[/snapshots/RGBNdD3Wn-g/00-05-43.png]]](<https://youtu.be/RGBNdD3Wn-g?t=340s>)

Source: [(156) What is Stable Diffusion? (Latent Diffusion Models Explained) - YouTube](https://www.youtube.com/watch?v=RGBNdD3Wn-g)
