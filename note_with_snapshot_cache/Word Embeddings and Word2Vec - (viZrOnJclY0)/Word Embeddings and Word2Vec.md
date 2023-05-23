## Word Embeddings and Word2Vec
### Introduction to Word Embeddings and Word2Vec [![[/snapshots/viZrOnJclY0/00-10-49.png]]](<https://youtu.be/viZrOnJclY0?t=645s>)
Word embeddings are a method for converting words into numbers that make sense, allowing algorithms like neural networks to work better with words. Similar words will have similar numbers which makes predicting words easier. [![[/snapshots/viZrOnJclY0/00-01-03.png]]](<https://youtu.be/viZrOnJclY0?t=61s>)

### Simple Neural Network for Word Embeddings [![[/snapshots/viZrOnJclY0/00-03-31.png]]](<https://youtu.be/viZrOnJclY0?t=209s>)
A simple neural network can be used to assign numbers to words, taking context into account. The weights on the connections become the word embeddings. This makes training a neural network easier like identifying sarcasm, as it can recognize and differentiate similar words used in different contexts. [![[/snapshots/viZrOnJclY0/00-11-03.png]]](<https://youtu.be/viZrOnJclY0?t=661s>)

### Two Strategies used by Word2Vec for Context [![[/snapshots/viZrOnJclY0/00-11-46.png]]](<https://youtu.be/viZrOnJclY0?t=702s>)
Word2Vecis a popular method for creating word embeddings which uses two strategies: Continuous Bag of Words (CBOW) and Skip-Gram. In CBOW, the surrounding words are used to predict the word in the middle. In Skip-Gram, the word in the middle is used to predict the surrounding words. 

### Training Word2Vec on Large Text Corpus 
In practice, instead of just having a small number of words and phrases like in the example, Word2Vec's vocabulary often consists of about three million words and phrases from Wikipedia. This increases the number of weights to optimize which makes training relatively slow. However, Word2Vec uses negative sampling to speed up the process and ignore some weights when optimizing. [![[/snapshots/viZrOnJclY0/00-13-04.png]]](<https://youtu.be/viZrOnJclY0?t=780s>)

### Summary
To summarize, word embeddings provide a useful way to represent words in numerical format which is great for machine learning algorithms. Word2Vec, a popular word embedding tool, helps to create accurate word embeddings by using two strategies: Continuous Bag of Words and Skip-Gram. Training Word2Vec on large text corpus can be slow but is made more efficient through negative sampling. 


Source: [(188) Word Embedding and Word2Vec, Clearly Explained!!! - YouTube](https://www.youtube.com/watch?v=viZrOnJclY0)
