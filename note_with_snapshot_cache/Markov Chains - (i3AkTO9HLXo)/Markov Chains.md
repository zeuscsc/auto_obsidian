## Markov Chains
### Introduction to Markov Chains
Markov Chains are used in various disciplines such as statistics, biology, economics, physics, and machine learning. This concept helps to predict future states based on current states. [![[/snapshots/i3AkTO9HLXo/00-00-14.png]]](<https://youtu.be/i3AkTO9HLXo?t=12s>)

### Restaurant Example
Consider a restaurant that serves three types of foods: hamburger, pizza, and hot dog. They serve only one item per day and follow rules based on the previous day's serving. A Markov Chain can be used to represent this scenario with weighted arrows indicating transition probabilities between different states. [![[/snapshots/i3AkTO9HLXo/00-00-41.png]]](<https://youtu.be/i3AkTO9HLXo?t=38s>)

### Markov Chain Properties
1. **Markov Property**: The future state depends only on the current state, not the steps before. [![[/snapshots/i3AkTO9HLXo/00-01-55.png]]](<https://youtu.be/i3AkTO9HLXo?t=112s>)
2. **Sum of Transition Probabilities**: The sum of the weights of the outgoing arrows from any state must be equal to 1, as they represent probabilities. [![[/snapshots/i3AkTO9HLXo/00-02-58.png]]](<https://youtu.be/i3AkTO9HLXo?t=174s>)

### Random Walk
By exploring the Markov chain through a random walk, one can find the probability distribution of different states. The stationary distribution or equilibrium state is the probability distribution that doesn't change with time for a given Markov chain. [![[/snapshots/i3AkTO9HLXo/00-04-55.png]]](<https://youtu.be/i3AkTO9HLXo?t=292s>)

### Linear Algebra Approach
The adjacency matrix (named the transition matrix) can be used to represent Markov chains efficiently. The equilibrium state can be given by the left eigenvector of the transition matrix with eigenvalue equal to 1. This technique also allows checking the existence of multiple stationary states. [![[/snapshots/i3AkTO9HLXo/00-08-44.png]]](<https://youtu.be/i3AkTO9HLXo?t=521s>)

### Conclusion
Markov chains provide a strong foundation for understanding various real-world problems. There's much more to learn about different types of Markov chains and their properties that cannot be covered in a single video. [![[/snapshots/i3AkTO9HLXo/00-00-25.png]]](<https://youtu.be/i3AkTO9HLXo?t=22s>)

Source: [(167) Markov Chains Clearly Explained! Part - 1 - YouTube](https://www.youtube.com/watch?v=i3AkTO9HLXo&t=332s)
