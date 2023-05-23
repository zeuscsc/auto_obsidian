## Hidden Markov Models
### Introduction to Hidden Markov Models [![[/snapshots/RWkHJnFj5rY/00-02-27.png]]](<https://youtu.be/RWkHJnFj5rY?t=144s>)
Hidden Markov Models (HMMs) are concepts derived from Markov chains and are useful in various domains such as bioinformatics, natural language processing, and speech recognition. This video discusses the intuition and mathematics behind HMMs and how Bayes theorem is utilized in the process. 

### Understanding Markov Chains and Hidden Markov Models 
To understand an HMM, one must first be familiar with Markov chains. A simple example involving weather transitions and a person's mood is used to illustrate the process. In an HMM, the states of the Markov chain are hidden or unknown, but certain variables dependent on those states can be observed. In this example, these observed variables are the person's mood. The HMM consists of an ordinary Markov chain and a set of observed variables. 

### Transition and Emission Matrices
The probabilities of state transitions and observed variables can be captured in two matrices: the transition matrix (green) and the emission matrix (red). The probabilities in the matrices can be used to calculate the joint probability of observed mood sequences and weather sequences. [![[/snapshots/RWkHJnFj5rY/00-03-47.png]]](<https://youtu.be/RWkHJnFj5rY?t=224s>)

### Stationary Distribution and Computing Probabilities [![[/snapshots/RWkHJnFj5rY/00-08-22.png]]](<https://youtu.be/RWkHJnFj5rY?t=498s>)
To find the probability of the first state, the stationary distribution of the Markov chain is needed. This can be computed using the normalized left eigenvectors or repeated matrix multiplication techniques as shown in previous videos. After finding the probability of the first state, the product of the probabilities can be calculated to determine the overall probability of a scenario occurring. [![[/snapshots/RWkHJnFj5rY/00-04-42.png]]](<https://youtu.be/RWkHJnFj5rY?t=278s>)

### Most Likely Weather Sequence
Given a sequence of observed moods, the most likely weather sequence can be found by calculating the probability of each possible permutation and selecting the one with the maximum probability using the same computation method as before. [![[/snapshots/RWkHJnFj5rY/00-05-31.png]]](<https://youtu.be/RWkHJnFj5rY?t=328s>)

### Formal Mathematics: Bayes Theorem and Joint Probability Distribution [![[/snapshots/RWkHJnFj5rY/00-00-25.png]]](<https://youtu.be/RWkHJnFj5rY?t=22s>)
The formal mathematics behind finding the most likely sequence of hidden states involves using Bayes theorem to rewrite the problem in terms of joint probability distribution. The numerator of the equation becomes a product of two sets of terms representing the probability of the observed variables given the hidden states and the probability of the hidden states themselves. By maximizing this expression, the most likely sequence of hidden states can be found. [![[/snapshots/RWkHJnFj5rY/00-05-55.png]]](<https://youtu.be/RWkHJnFj5rY?t=352s>)

### Conclusion and Next Steps
Hidden Markov Models are powerful tools for understanding underlying hidden states based on observed variables. The process can be complicated, but understanding the mathematics and using Bayes theorem helps in developing a clearer comprehension of the concept. [![[/snapshots/RWkHJnFj5rY/00-00-07.png]]](<https://youtu.be/RWkHJnFj5rY?t=4s>)

Source: [Hidden Markov Model Clearly Explained! Part - 5 - YouTube](https://www.youtube.com/watch?v=RWkHJnFj5rY)
