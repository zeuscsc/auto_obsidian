## Langchain and Text Embeddings
### Introduction to Langchain and Text Embeddings [![[/snapshots/UO699Szp82M/00-00-03.png]]](<https://youtu.be/UO699Szp82M?t=0s>)
Langchain is a framework that utilizes a text embedding, which is a learned representation of text in the form of a vector of numbers. This allows for efficient context retrieval and enhances a language model's capabilities. This video demonstrates using Langchain with Amazon review data for customer experience analytics. 

### Importing and Preparing Data
The Amazon review dataset is loaded into Pandas dataframes, removing reviews without text and truncating long reviews. Hugging Face embeddings are used to create a new column in the dataframe with embedding vectors. Caution must be exercised when using OpenAI embeddings to avoid incurring high costs with large dataframes. [![[/snapshots/UO699Szp82M/00-03-24.png]]](<https://youtu.be/UO699Szp82M?t=203s>)

### Finding Signal in Review Data [![[/snapshots/UO699Szp82M/00-05-51.png]]](<https://youtu.be/UO699Szp82M?t=349s>)
The embedding vectors are used as features in a simple Random Forest regression model predicting overall ratings. With a mean absolute error of 0.53, the model shows promise if further optimized. The goal is not to predict the ratings but to use the signal in review data for value-generating machine learning models. [![[/snapshots/UO699Szp82M/00-04-38.png]]](<https://youtu.be/UO699Szp82M?t=276s>)

### Loading Review Embeddings into Vector Database [![[/snapshots/UO699Szp82M/00-06-08.png]]](<https://youtu.be/UO699Szp82M?t=366s>)
After loading the review embeddings into Pinecone, GPT-4 is used to access the data in the vector store, providing an overall impression of the reviews, examples of good and bad reviews, and suggestions for improvement. This information can be turned into a weekly digest sent to company email lists. [![[/snapshots/UO699Szp82M/00-06-55.png]]](<https://youtu.be/UO699Szp82M?t=413s>)

### Filtered Vector Similarity Search
Filtered vector similarity searches can be performed using Pinecone directly, as Langchain does not currently support this functionality. By creating an index with Pinecone, uploading data with metadata fields for filtering, and running filtered queries, top matching reviews for specific ratings can be retrieved. This allows users to divide reviews into themes for remarketing campaigns. 

### Conclusion
Using Langchain with text embeddings, review data can be analyzed for customer experience and valuable insights. Langchain's integration with Sepia allows for the creation of targeted campaigns and extraction of value from operational data. [![[/snapshots/UO699Szp82M/00-00-33.png]]](<https://youtu.be/UO699Szp82M?t=31s>)

Source: [LangChain In Action: Real-World Use Case With Step-by-Step Tutorial - YouTube](https://www.youtube.com/watch?v=UO699Szp82M)
