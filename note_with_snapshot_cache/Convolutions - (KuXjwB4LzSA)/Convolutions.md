## Convolutions
### Introduction to Convolutions
A convolution is a fundamental operation combining two lists of numbers or functions, ubiquitous in areas such as image processing, probability theory, and solving differential equations. Multiplying two polynomials together is also an instance of convolution. [![[/snapshots/KuXjwB4LzSA/00-21-28.png]]](<https://youtu.be/KuXjwB4LzSA?t=1286s>)

### Convolution in Probability
The convolution process can help compute the probability of various sums when rolling a pair of dice with distinct probabilities for each face. It involves mixing two sequences of numbers (probabilities for each face) to generate a new sequence. Alternatively, the process can be viewed as creating a table of pairwise products and summing its diagonals. [![[/snapshots/KuXjwB4LzSA/00-02-19.png]]](<https://youtu.be/KuXjwB4LzSA?t=136s>)

### Moving Averages
Convolutions can perform moving averages by choosing a list of numbers that add up to 1 and aligning smaller windows of values with the larger list, then multiplying corresponding terms and summing the results. In image processing, this produces a smoothed or blurred version of the original data. Modifying the list can change the average's weighting. [![[/snapshots/KuXjwB4LzSA/00-15-47.png]]](<https://youtu.be/KuXjwB4LzSA?t=943s>)

### Image Processing Examples
In image processing, the convolution of an original image with a grid of values results in a new image with different effects like blurring, edge detection, or sharpening. Choosing the grid of values (kernel) and multiplying corresponding terms allows these effects. [![[/snapshots/KuXjwB4LzSA/00-09-48.png]]](<https://youtu.be/KuXjwB4LzSA?t=586s>)

### Convolutions in Polynomials
When multiplying polynomials together, convolutions are equivalent to expanding the product and collecting like terms. The complexity comes from translating from one viewpoint to another. [![[/snapshots/KuXjwB4LzSA/00-18-55.png]]](<https://youtu.be/KuXjwB4LzSA?t=1133s>)

### Fast Fourier Transforms (FFT)
By selecting a specific set of complex numbers (roots of unity) as inputs for polynomial evaluation, the discrete Fourier transform can be computed more effectively. This allows for a faster algorithm to compute convolutions in O(n log n) operations. This benefits areas like probability distributions, image processing, and large integer multiplication. [![[/snapshots/KuXjwB4LzSA/00-20-15.png]]](<https://youtu.be/KuXjwB4LzSA?t=1213s>)

Source: [(167) But what is a convolution? - YouTube](https://www.youtube.com/watch?v=KuXjwB4LzSA&list=WL&index=17&t=301s)
