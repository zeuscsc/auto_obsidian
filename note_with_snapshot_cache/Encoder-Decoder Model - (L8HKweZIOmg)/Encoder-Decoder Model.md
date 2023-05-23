## Encoder-Decoder Model
### Introduction: Sequence to Sequence (Seek to Seek) Problems [![[/snapshots/L8HKweZIOmg/00-02-26.png]]](<https://youtu.be/L8HKweZIOmg?t=143s>)
Both translation and 3D structure prediction are examples of sequence to sequence or seek to seek problems that could be solved using an Encoder-Decoder neural network model. 

### Encoder-Decoder Model
This model is used to handle variable input and output lengths. The main components of the model are: [![[/snapshots/L8HKweZIOmg/00-03-38.png]]](<https://youtu.be/L8HKweZIOmg?t=215s>)

1. Long short-term memory (LSTM) units for dealing with variable length inputs and outputs. [![[/snapshots/L8HKweZIOmg/00-03-45.png]]](<https://youtu.be/L8HKweZIOmg?t=222s>)
2. An embedding layer for converting words into numbers. [![[/snapshots/L8HKweZIOmg/00-04-21.png]]](<https://youtu.be/L8HKweZIOmg?t=257s>)

### Encoding
The encoder encodes the input sentence into a context vector, consisting of long and short-term memories (cell and hidden states) from LSTM cells. [![[/snapshots/L8HKweZIOmg/00-08-17.png]]](<https://youtu.be/L8HKweZIOmg?t=493s>)

### Decoding
The decoder initializes the long and short-term memories (cell and hidden states) in the LSTMs with the context vector, transforming it into the output sentence using additional weights and biases in a fully connected layer. The decoder repeats this process until an end-of-sentence token (EOS) is predicted or a maximum output length is reached. [![[/snapshots/L8HKweZIOmg/00-09-06.png]]](<https://youtu.be/L8HKweZIOmg?t=543s>)

### Training and Teacher Forcing
During training, instead of using the predicted token as input, the known correct token is used. This method is called teacher forcing. The process stops at the known phrase length rather than predicting additional tokens. [![[/snapshots/L8HKweZIOmg/00-14-28.png]]](<https://youtu.be/L8HKweZIOmg?t=865s>)

### Differences between the Basic Model and Original Manuscript [![[/snapshots/L8HKweZIOmg/00-14-47.png]]](<https://youtu.be/L8HKweZIOmg?t=883s>)
The basic model differs from the original manuscript in terms of vocabulary size, embedding values, LSTM layers and cells, and output layer inputs and outputs. The original manuscript used larger vocabularies and more layers and cells, resulting in more weights and biases to train. [![[/snapshots/L8HKweZIOmg/00-06-04.png]]](<https://youtu.be/L8HKweZIOmg?t=361s>)

Source: [Sequence-to-Sequence (seq2seq) Encoder-Decoder Neural Networks, Clearly Explained!!! - YouTube](https://www.youtube.com/watch?v=L8HKweZIOmg)
