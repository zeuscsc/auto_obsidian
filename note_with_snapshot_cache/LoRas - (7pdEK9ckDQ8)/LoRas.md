## LoRas
### Introduction to LoRas
LoRas are powerful tools for training and fine-tuning large language models. They use dimensionality reduction to efficiently update a lower-dimensional set of parameters during fine-tuning tasks. By applying linear algebra concepts like rank decomposition, they reduce the memory requirements during training. [![[/snapshots/7pdEK9ckDQ8/00-00-15.png]]](<https://youtu.be/7pdEK9ckDQ8?t=13s>)

### LoRas and Linear Algebra
LoRas employ rank decomposition, such as singular value decomposition, to represent matrices with lower-dimensional matrices that can be multiplied together. This results in memory savings, as the number of elements stored is significantly reduced. [![[/snapshots/7pdEK9ckDQ8/00-07-05.png]]](<https://youtu.be/7pdEK9ckDQ8?t=425s>)

### Implementing LoRas in Language Models 
LoRas are typically attached to the feedforward portion of the transformer model in large language models. The weights in the feedforward layer are fixed, and the weights in the LoRa matrices are updated. By applying dimensionality reduction techniques like principal component analysis, the memory requirements are further reduced. [![[/snapshots/7pdEK9ckDQ8/00-04-46.png]]](<https://youtu.be/7pdEK9ckDQ8?t=285s>)

### Fine-tuning Language Models with LoRas using Oogaboo's Web UI 
Oogaboo's text-generation web UI can be used for training and fine-tuning language models with LoRas. Users can import a raw text file or a formatted dataset, adjust hyperparameters like batch size, epoch, learning rate, LoRa rank, LoRa alpha, cutoff length, and dropout. After setting up the training and validation sets and choosing the appropriate format, users can start LoRa training. 

### Conclusion
LoRas provide an efficient way to fine-tune large language models with reduced memory requirements. By understanding the underlying linear algebra concepts and using tools like Oogaboo's text-generation web UI, researchers and developers can effectively train and customize their language models. 

Source: [(188) Fine-Tune Language Models with LoRA! OobaBooga Walkthrough and Explanation. - YouTube](https://www.youtube.com/watch?v=7pdEK9ckDQ8)
