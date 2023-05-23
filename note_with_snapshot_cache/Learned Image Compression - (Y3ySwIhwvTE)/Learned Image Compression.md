## Learned Image Compression
#### Learned Image Compression Recap
- Learned image compression models use neural networks to encode and decode images [![[/snapshots/Y3ySwIhwvTE/00-00-40.png]]](<https://youtu.be/Y3ySwIhwvTE?t=37s>)
- They are optimized via stochastic gradient descent on a loss function that balances rate and distortion [![[/snapshots/Y3ySwIhwvTE/00-08-22.png]]](<https://youtu.be/Y3ySwIhwvTE?t=500s>)
- MSE and MS-SSIM as optimization targets affect the rate allocation decisions within encoded images [![[/snapshots/Y3ySwIhwvTE/00-18-46.png]]](<https://youtu.be/Y3ySwIhwvTE?t=1121s>)

#### Improved Performance over Time
- Many new approaches experimenting with improved entropy coding and non-linear transforms [![[/snapshots/Y3ySwIhwvTE/00-17-25.png]]](<https://youtu.be/Y3ySwIhwvTE?t=1042s>)
- Computational complexity remains an open and actively researched question [![[/snapshots/Y3ySwIhwvTE/00-16-04.png]]](<https://youtu.be/Y3ySwIhwvTE?t=962s>)

#### Distortion Metrics for Image Composition [![[/snapshots/Y3ySwIhwvTE/00-25-27.png]]](<https://youtu.be/Y3ySwIhwvTE?t=1525s>)
- Good distortion metrics predict human ratings, are differentiable, and generalize across images and distorted types [![[/snapshots/Y3ySwIhwvTE/00-20-42.png]]](<https://youtu.be/Y3ySwIhwvTE?t=1239s>)
- Many popular distortion metrics have blind spots and may not optimize well for neural networks [![[/snapshots/Y3ySwIhwvTE/00-23-11.png]]](<https://youtu.be/Y3ySwIhwvTE?t=1388s>)

#### Realism vs Distortion
- Realism focuses on no-reference metrics, which evaluate an image without comparing it to a reference image [![[/snapshots/Y3ySwIhwvTE/00-28-03.png]]](<https://youtu.be/Y3ySwIhwvTE?t=1681s>)
- Data sets with a wider variety of distortion types are needed for evaluating distortion metrics [![[/snapshots/Y3ySwIhwvTE/00-26-18.png]]](<https://youtu.be/Y3ySwIhwvTE?t=1575s>)
- Neural networks may cheat by exploiting blind spots in distortion metrics, so better metrics and understanding of realism are needed [![[/snapshots/Y3ySwIhwvTE/00-53-05.png]]](<https://youtu.be/Y3ySwIhwvTE?t=3184s>)

#### Perceptual Spaces
- Concept that can be applied to both distortion and realism 
- Can encompass various approaches such as generalized convolutional neural networks, learned perceptual image patch similarity (LPIPS), and more [![[/snapshots/Y3ySwIhwvTE/00-44-18.png]]](<https://youtu.be/Y3ySwIhwvTE?t=2652s>)
- Realism, distortion, and perceptual spaces are interconnected, and improved understanding of these aspects can benefit image compression models [![[/snapshots/Y3ySwIhwvTE/00-31-13.png]]](<https://youtu.be/Y3ySwIhwvTE?t=1867s>)

Source: [(188) DCC 2023 - Perception: the Next Milestone in Learned Image Compression - YouTube](https://www.youtube.com/watch?v=Y3ySwIhwvTE)
