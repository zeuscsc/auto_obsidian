## Transformers in Natural Language Processing [![[/snapshots/4Bdc55j80l8/00-00-02.png]]](<https://youtu.be/4Bdc55j80l8?t=0s>)
### Introduction to Transformers in Natural Language Processing 

Transformers have revolutionized natural language processing, achieving various record-breaking results and pushing the state of the art. They have been used in machine translation, chatbots, and improving search engines. Transformers have outperformed RNNs, GRUs, and LSTMs in sequence problems. 

### Attention Mechanism

The attention mechanism allows the model to reference relevant words when generating text. Unlike RNNs, which only have a short window to reference from, the attention mechanism can use the entire context of input when generating text. [![[/snapshots/4Bdc55j80l8/00-01-54.png]]](<https://youtu.be/4Bdc55j80l8?t=110s>)

### Transformer Architecture

The transformer architecture is an attention-based encoder-decoder model. The encoder maps an input sequence into an abstract continuous representation, while the decoder generates a single output using the representation from the encoder. [![[/snapshots/4Bdc55j80l8/00-04-54.png]]](<https://youtu.be/4Bdc55j80l8?t=289s>)

### Positional Encoding

The inputs are fed into a word embedding layer, which maps words to a vector with continuous values representing each word. Positional information is injected into the embeddings using sine and cosine functions, giving the network information on the positions of each vector. [![[/snapshots/4Bdc55j80l8/00-10-44.png]]](<https://youtu.be/4Bdc55j80l8?t=641s>)

### Encoder Layer

The encoder layer's job is to map all input sequences into an abstract continuous representation. It contains two submodules: multi-headed attention and a fully connected network. Additionally, there are residual connections and layer normalization. 

### Multi-Headed Attention Module

Multi-headed attention uses self-attention, associating each word in the input with other words in the input. It computes the attention weights for the input and produces an output vector encoding information on how each word should attend to all other words in the sequence. [![[/snapshots/4Bdc55j80l8/00-08-12.png]]](<https://youtu.be/4Bdc55j80l8?t=489s>)

### Decoder Layer

The decoder layer generates text sequences. It has two multi-headed attention layers, a point-wise feedforward layer, residual connections, and layer normalizations, as well as a linear layer acting like a classifier and a softmax to get word probabilities. [![[/snapshots/4Bdc55j80l8/00-09-56.png]]](<https://youtu.be/4Bdc55j80l8?t=595s>)

The decoder is autoregressive, taking in previous outputs as inputs and the encoder outputs containing attention information from input. This continues until an end token is generated. [![[/snapshots/4Bdc55j80l8/00-13-55.png]]](<https://youtu.be/4Bdc55j80l8?t=831s>)

### Summary

Transformers leverage the power of attention mechanisms to make better predictions. They have outperformed RNNs in encoding or generating longer sequences, revolutionizing the natural language processing industry. [![[/snapshots/4Bdc55j80l8/00-14-31.png]]](<https://youtu.be/4Bdc55j80l8?t=869s>)

Source: [Illustrated Guide to Transformers Neural Network: A step by step explanation - YouTube](https://www.youtube.com/watch?v=4Bdc55j80l8&list=WL&index=20&t=1s)
