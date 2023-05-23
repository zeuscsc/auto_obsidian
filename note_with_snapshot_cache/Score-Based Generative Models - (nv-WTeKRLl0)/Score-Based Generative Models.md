## Score-Based Generative Models
### Score-Based Generative Models: Definition and Advantages [![[/snapshots/nv-WTeKRLl0/00-50-46.png]]](<https://youtu.be/nv-WTeKRLl0?t=3043s>)

Score-based generative models are a new framework for generative modeling that work with score functions to represent probability distributions. They satisfy three main goals: 

1. They allow for very flexible models as the score function bypasses the intractable normalizing constants. This enables the use of flexible deep neural networks (referred to as score models) to model the score function, which can then be learned from data using principled statistical methods. [![[/snapshots/nv-WTeKRLl0/00-22-54.png]]](<https://youtu.be/nv-WTeKRLl0?t=1371s>)
2. These models can generate high-quality new data samples comparable to GANs and control the data generation process for important applications in inverse problem solving. [![[/snapshots/nv-WTeKRLl0/00-23-23.png]]](<https://youtu.be/nv-WTeKRLl0?t=1401s>)
3. Score-based generative modeling can be used to compute accurate probability values, demonstrating better empirical performance than other methods. [![[/snapshots/nv-WTeKRLl0/00-41-18.png]]](<https://youtu.be/nv-WTeKRLl0?t=2473s>)

### Estimating the Score Function

Score functions can be estimated from data using a method called score matching, which compares two vector fields of score functions (one representing the ground truth score function of the data distribution and the other given by the score model). By minimizing the feature divergence of the two vector fields, the score function can be accurately estimated. The score matching loss function aims to address the difficulty of estimating score functions in low data density regions by incorporating the right amount of Gaussian noise to perturb the dataset. This results in learned score models being accurate across different noise levels. [![[/snapshots/nv-WTeKRLl0/00-23-35.png]]](<https://youtu.be/nv-WTeKRLl0?t=1412s>)

### Generating Samples with Score-Based Generative Models 

To generate new samples, the Langevin dynamics algorithm is used to move data samples, following the noisy score functions while injecting the right amount of Gaussian noise. In practice, a large number of different noise levels are used to jointly perturb the training dataset, and the noise conditional score model is trained to estimate the score function for each noise level. Langevin dynamics is then run iteratively over these noise levels to generate new samples from the learned score functions. [![[/snapshots/nv-WTeKRLl0/00-24-29.png]]](<https://youtu.be/nv-WTeKRLl0?t=1465s>)

Score-based generative models have been shown to generate high-quality samples, making them a promising framework for various applications, such as medical image reconstruction, outlier detection, and lossless compression. [![[/snapshots/nv-WTeKRLl0/00-50-29.png]]](<https://youtu.be/nv-WTeKRLl0?t=3027s>)

Source: [(188) Learning to Generate Data by Estimating Gradients of the Data Distribution (Yang Song, Stanford) - YouTube](https://www.youtube.com/watch?v=nv-WTeKRLl0)
