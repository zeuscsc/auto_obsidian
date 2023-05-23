## Denoising Diffusion Probabilistic Models
### Introduction to Denoising Diffusion Probabilistic Models (DDPM) [![[/snapshots/_d-san8W1Js/00-03-16.png]]](<https://youtu.be/_d-san8W1Js?t=194s>)

Denoising Diffusion Probabilistic Models (DDPM) are generative models that take an image and iteratively denoise it by adding small amounts of noise. These models can generate semantically meaningful images, making them particularly useful in domains such as healthcare where supervised data may be scarce. Diffusion models fall into the broader category of generative models, alongside Variational Auto-encoders (VAEs) and Generative Adversarial Networks (GANs). 

#### Overview of DDPM

DDPM involves training a Markov chain using variational inference to produce samples matching the input data after a finite time. The model aims to reverse the diffusion process by gradually adding noise and then reversing the information destruction process. The Gaussian conditional assumption allows for efficient neural network parameterization and training. [![[/snapshots/_d-san8W1Js/00-08-59.png]]](<https://youtu.be/_d-san8W1Js?t=537s>)

#### Information Theoretical Analysis and Connection to Compression [![[/snapshots/_d-san8W1Js/00-05-06.png]]](<https://youtu.be/_d-san8W1Js?t=304s>)

DDPM's high-quality image generation capabilities can be seen as a progressive decoding process resembling autoregressive decoding. The majority of the model's lossless code lengths describe imperceptible image details, making the model similar to a lossy compression scheme. [![[/snapshots/_d-san8W1Js/00-59-55.png]]](<https://youtu.be/_d-san8W1Js?t=3593s>)

#### ELBO: Evidence Lower Bound

The evidence lower bound (ELBO) is used to optimize parameterized models that describe the joint distribution of data points and their latent variables. ELBO is a variational bound on the log likelihood of the data, making it easier to compute than the original likelihood. The ELBO is calculated by finding the expected value of the log likelihood function over the generation process. [![[/snapshots/_d-san8W1Js/00-09-08.png]]](<https://youtu.be/_d-san8W1Js?t=545s>)

#### Defining and Parameterizing Diffusion Models [![[/snapshots/_d-san8W1Js/00-07-00.png]]](<https://youtu.be/_d-san8W1Js?t=419s>)

Diffusion models are defined as a Markov chain comprising a sequence of random variables from X0 (a semantically nice image) to XT (a noise from a prior distribution). The model parameters are optimized to represent this distribution, learning the true distribution of the images in the process. The variational bound can be computed using the forward and reverse processes and the Gaussian conditionals. Variance schedules (beta T's) can be defined as either learnable or fixed hyperparameters. [![[/snapshots/_d-san8W1Js/00-05-31.png]]](<https://youtu.be/_d-san8W1Js?t=329s>)

---
The video notes above provide an overview of denoising diffusion probabilistic models, their applications, and the mathematics behind their optimization. The video also discusses the information theoretical analysis of the diffusion models and how they relate to compression schemes in the context of lossy compression. Additionally, the video covers the concept of the evidence lower bound (ELBO) and how it is used in optimizing the models. Finally, the video explains how diffusion models are defined and parameterized, touching upon concepts such as Markov chains, Gaussian conditionals, and variance schedules. 

Source: [(162) PaperView: Denoising diffusion probabilistic models - YouTube](https://www.youtube.com/watch?v=_d-san8W1Js)
