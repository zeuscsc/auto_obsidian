## Node2Vec
### Motivation: Graph Embeddings
Graph databases are used for analyzing interrelated data from various sources. To use machine learning algorithms, we need to map the graph structure to a vector form, which is called graph embeddings. The goal is to find a vector representation for the graph structure, not just the features of each node. [![[/snapshots/pS_POUVFXvk/00-00-18.png]]](<https://youtu.be/pS_POUVFXvk?t=12s>)

### Node2Vec Algorithm
Node2Vec is inspired by the Word2Vec algorithm and handles the mapping of nodes to vectors in a similar way. It explores the context of nodes in the graph and finds vector representations for them. Nodes with similar contexts should be mapped close in the embedding space. [![[/snapshots/pS_POUVFXvk/00-02-36.png]]](<https://youtu.be/pS_POUVFXvk?t=151s>)

### Context of Nodes: Homophily and Structural Equivalence [![[/snapshots/pS_POUVFXvk/00-12-20.png]]](<https://youtu.be/pS_POUVFXvk?t=737s>)
There are two ways to explore the context of nodes in graphs - homophily and structural equivalence - which are related to breadth-first and depth-first search. Homophily reveals that similar nodes have direct relationships, while structural equivalence detects the role of a node from a wider perspective. [![[/snapshots/pS_POUVFXvk/00-03-31.png]]](<https://youtu.be/pS_POUVFXvk?t=207s>)

### Context Approximation and Sampling Strategy [![[/snapshots/pS_POUVFXvk/00-07-20.png]]](<https://youtu.be/pS_POUVFXvk?t=439s>)
To avoid capturing the entire graph, we need to approximate the context of a node using a sampling strategy. Node2Vec employs a fixed number of random walks, parameterized by breadth-first and depth-first approaches. [![[/snapshots/pS_POUVFXvk/00-08-18.png]]](<https://youtu.be/pS_POUVFXvk?t=496s>)

### Using Similarity Scores and Softmax [![[/snapshots/pS_POUVFXvk/00-10-47.png]]](<https://youtu.be/pS_POUVFXvk?t=645s>)
To find the similarity between nodes, the dot product of their vectors is calculated, and a softmax function is applied to transform the similarity scores into probabilities. A function, f, is used to map nodes to vectors with probability maximization. [![[/snapshots/pS_POUVFXvk/00-11-41.png]]](<https://youtu.be/pS_POUVFXvk?t=697s>)

### Optimizing for Embeddings
The goal is to maximize the total probability score for finding the best graph embeddings. The process updates the function, f, and maximizes the probability using stochastic gradient descent. The simplicity and conciseness of Node2Vec make it ideal for many use cases. [![[/snapshots/pS_POUVFXvk/00-09-17.png]]](<https://youtu.be/pS_POUVFXvk?t=555s>)

Source: [(188) Graph Embeddings (node2vec) explained - How nodes get mapped to vectors - YouTube](https://www.youtube.com/watch?v=pS_POUVFXvk)
