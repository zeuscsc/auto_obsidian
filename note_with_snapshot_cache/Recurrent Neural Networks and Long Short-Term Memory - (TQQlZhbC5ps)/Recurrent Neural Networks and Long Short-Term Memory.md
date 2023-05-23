Recurrent Neural Networks and Long Short-Term Memory [![[/snapshots/TQQlZhbC5ps/00-01-40.png]]](<https://youtu.be/TQQlZhbC5ps?t=96s>)
### Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) [![[/snapshots/TQQlZhbC5ps/00-00-02.png]]](<https://youtu.be/TQQlZhbC5ps?t=0s>)
RNNs are feedforward neural networks rolled out over time, allowing for handling sequence data. There are three types of architectures: vector-to-sequence, sequence-to-vector, and sequence-to-sequence models. However, RNNs can be slow and struggle with long sequences. LSTM networks were introduced in 1991 to improve memory retention and deal with longer sequences. [![[/snapshots/TQQlZhbC5ps/00-12-09.png]]](<https://youtu.be/TQQlZhbC5ps?t=725s>)

### Transformer Architecture: High-Level Overview
Introduced in 2017, the transformer architecture employs an encoder-decoder design, allowing input sequences to be passed in parallel. It utilizes input embeddings, positional encoders, multiple encoder blocks, an attention mechanism, and feed-forward layers. [![[/snapshots/TQQlZhbC5ps/00-02-47.png]]](<https://youtu.be/TQQlZhbC5ps?t=165s>)

### Encoder and Decoder Components
The encoder maps words to vectors and positional encoders add context information. Encoders use multi-headed attention layers and feed-forward layers. The decoder focuses on predicting the next word using self-attention and encoder-decoder attention blocks. [![[/snapshots/TQQlZhbC5ps/00-06-47.png]]](<https://youtu.be/TQQlZhbC5ps?t=404s>)

### Multi-Headed Attention Networks
These networks have multiple weight matrices, resulting in multiple attention vectors per word. Attention vectors are generated, normalized, and passed through the encoder and decoder blocks. [![[/snapshots/TQQlZhbC5ps/00-11-09.png]]](<https://youtu.be/TQQlZhbC5ps?t=664s>)

### Transformers in Real-World Applications
Transformers have largely replaced LSTM networks for sequence data processing tasks. Google's BERT uses transformers for pre-training common NLP tasks. Other research, such as Pervasive Attention, may provide improvements over transformer models, but they remain a powerful tool in various contexts. [![[/snapshots/TQQlZhbC5ps/00-12-17.png]]](<https://youtu.be/TQQlZhbC5ps?t=733s>)

Source: [(167) Transformer Neural Networks - EXPLAINED! (Attention is all you need) - YouTube](https://www.youtube.com/watch?v=TQQlZhbC5ps)
