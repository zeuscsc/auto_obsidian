## Vector Databases
### Introduction to Vector Databases
Vector databases have gained popularity recently, with some companies raising significant funds to develop them for AI applications. In some cases, traditional databases or numpy nd arrays might be sufficient, but vector databases offer unique advantages, particularly for large language models like GPT-4. [![[/snapshots/dN0lsF2cvm4/00-00-24.png]]](<https://youtu.be/dN0lsF2cvm4?t=21s>)

### Unstructured Data and Vector Embeddings [![[/snapshots/dN0lsF2cvm4/00-01-28.png]]](<https://youtu.be/dN0lsF2cvm4?t=84s>)
More than 80% of existing data is unstructured, such as social media posts, images, videos, or audio data. These types of data are difficult to fit into a relational database. Using vector embeddings and vector databases, we can represent and store this data in a different way for fast retrieval and similarity search. 

### Calculating Vector Embeddings
Vector embeddings are calculated using machine learning models, and they represent data as a list of numbers. These embeddings can be calculated for words, sentences, or images, allowing computers to easily understand and process them. Calculating distances between vectors can identify similar items. [![[/snapshots/dN0lsF2cvm4/00-01-48.png]]](<https://youtu.be/dN0lsF2cvm4?t=106s>)

### Indexing Vectors in a Vector Database [![[/snapshots/dN0lsF2cvm4/00-02-30.png]]](<https://youtu.be/dN0lsF2cvm4?t=148s>)
To search efficiently across thousands of vectors, they need to be indexed. The indexing process maps vectors to a new data structure that enables faster searching. Different methods exist for calculating indexes, but the important thing is that they are needed for efficient search. [![[/snapshots/dN0lsF2cvm4/00-02-44.png]]](<https://youtu.be/dN0lsF2cvm4?t=160s>)

### Use Cases for Vector Databases 
- Long-term memory for large language models, like langchain [![[/snapshots/dN0lsF2cvm4/00-03-02.png]]](<https://youtu.be/dN0lsF2cvm4?t=179s>)
- Semantic search based on meaning or context, rather than string matches [![[/snapshots/dN0lsF2cvm4/00-03-11.png]]](<https://youtu.be/dN0lsF2cvm4?t=189s>)
- Similarity search for images, audio, or video data [![[/snapshots/dN0lsF2cvm4/00-03-19.png]]](<https://youtu.be/dN0lsF2cvm4?t=197s>)
- Ranking and recommendation engine for online retailers [![[/snapshots/dN0lsF2cvm4/00-03-31.png]]](<https://youtu.be/dN0lsF2cvm4?t=208s>)

### Vector Database Options
Several vector databases are available, such as Pinecone, Vivi, Chroma, Redis, Kudraint, Milvus, and Vespa AI. Comparisons of these options can be provided in a separate video.  [![[/snapshots/dN0lsF2cvm4/00-03-57.png]]](<https://youtu.be/dN0lsF2cvm4?t=236s>)

### Conclusion
Vector databases are a fascinating and powerful tool, particularly for AI applications handling unstructured data. Understanding their function and potential use cases can be helpful in determining whether they are the right choice for a project. 

Source: [(167) Vector Databases simply explained! (Embeddings & Indexes) - YouTube](https://www.youtube.com/watch?v=dN0lsF2cvm4)
