## Diffusion Models
### Introduction to Diffusion Models

#### Diffusion Models for Image Generation [![[/snapshots/HoKDTa5jHvg/00-01-21.png]]](<https://youtu.be/HoKDTa5jHvg?t=79s>)
- Diffusion models are popular for image generation tasks and competitive with state-of-the-art GANs. [![[/snapshots/HoKDTa5jHvg/00-31-08.png]]](<https://youtu.be/HoKDTa5jHvg?t=1865s>)
- They can generate highly accurate and realistic images based on text prompts and have applications in generating variations of images, inpainting, and creating animations. [![[/snapshots/HoKDTa5jHvg/00-00-14.png]]](<https://youtu.be/HoKDTa5jHvg?t=12s>)
- Four fundamental papers on diffusion models introduce and develop various improvements to the technique. [![[/snapshots/HoKDTa5jHvg/00-02-53.png]]](<https://youtu.be/HoKDTa5jHvg?t=171s>)

#### Overview of Diffusion Models
- The main idea behind diffusion models is that they consist of two processes, forward and reverse diffusion processes. [![[/snapshots/HoKDTa5jHvg/00-31-56.png]]](<https://youtu.be/HoKDTa5jHvg?t=1914s>)
- Forward diffusion process involves iteratively applying noise to an image, turning it into complete noise. [![[/snapshots/HoKDTa5jHvg/00-03-40.png]]](<https://youtu.be/HoKDTa5jHvg?t=218s>)
- Reverse diffusion process uses a neural network to iteratively remove noise from the noisy image, eventually producing a clear image. 

#### Architecture and Training Process
- The architecture follows a U-Net-like structure, which takes an image and the current time step as inputs, and predicts the image at the previous time step. [![[/snapshots/HoKDTa5jHvg/00-32-25.png]]](<https://youtu.be/HoKDTa5jHvg?t=1943s>)
- Neural network predicts noise in the image rather than predicting the mean or the original image directly. [![[/snapshots/HoKDTa5jHvg/00-14-30.png]]](<https://youtu.be/HoKDTa5jHvg?t=868s>)
- A schedule for noise application controls the amount of noise applied to the image, with the cosine schedule outperforming the linear schedule in the image-to-noise transformation. [![[/snapshots/HoKDTa5jHvg/00-06-22.png]]](<https://youtu.be/HoKDTa5jHvg?t=379s>)
- Various architecture improvements are done over time, such as adaptive group normalization and classifier guidance. [![[/snapshots/HoKDTa5jHvg/00-08-34.png]]](<https://youtu.be/HoKDTa5jHvg?t=512s>)

#### Math Behind Diffusion Models
- The forward process can be expressed analytically as a series of formulas involving normal distributions, schedules for noise application, and probability distributions. [![[/snapshots/HoKDTa5jHvg/00-21-06.png]]](<https://youtu.be/HoKDTa5jHvg?t=1264s>)
- The reverse process is based on variational lower bound optimization and also involves a series of mathematical manipulations, resulting in a relatively simple final objective. [![[/snapshots/HoKDTa5jHvg/00-15-01.png]]](<https://youtu.be/HoKDTa5jHvg?t=898s>)
- Several improvements have been made in the learning process, including learning the variance of the noise, a better noise schedule, and approximating certain terms in the loss calculation. [![[/snapshots/HoKDTa5jHvg/00-32-59.png]]](<https://youtu.be/HoKDTa5jHvg?t=1978s>)

#### Results and Comparison
- Diffusion models have shown competitive results in image generation tasks, with some models outperforming GANs. 
- OpenAI's improvements to diffusion models have notably improved performance and enabled better image synthesis capabilities. 
- Diffusion models show potential for further improvements and surpassing GANs in the future. 

Source: [Diffusion Models | Paper Explanation | Math Explained - YouTube](https://www.youtube.com/watch?v=HoKDTa5jHvg)
