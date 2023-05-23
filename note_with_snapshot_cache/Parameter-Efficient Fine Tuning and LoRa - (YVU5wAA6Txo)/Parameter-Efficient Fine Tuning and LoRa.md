## Parameter-Efficient Fine Tuning and LoRa [![[/snapshots/YVU5wAA6Txo/00-00-09.png]]](<https://youtu.be/YVU5wAA6Txo?t=7s>)
### Introduction to Parameter-Efficient Fine Tuning and LoRa 
Parameter-efficient fine tuning is a way to adapt large models to specific tasks without updating all original weights. LoRa, or Low-Rank Adaptation, is a method used for this purpose by injecting trainable matrices into each layer of the transformer, using techniques from linear algebra. 

### Adapter Transformers and Adapter Hub [![[/snapshots/YVU5wAA6Txo/00-14-38.png]]](<https://youtu.be/YVU5wAA6Txo?t=872s>)
Adapter Transformers are an extension of Hugging Face transformers that include small amounts of new parameters, while the original pre-trained weights are frozen. Adapter Hub is a framework where adapters specific to different models and tasks are shared, allowing for minimalistic training and reduced memory requirements. [![[/snapshots/YVU5wAA6Txo/00-06-36.png]]](<https://youtu.be/YVU5wAA6Txo?t=393s>)

### Understanding LoRa
LoRa's main idea is to freeze the pre-trained model weights and inject trainable matrices into the transformer layers. The low-rank adaptation of weight matrix is achieved using matrix decomposition techniques like SVD, which enables the approximation of high-rank matrices with lower-rank matrices. [![[/snapshots/YVU5wAA6Txo/00-30-30.png]]](<https://youtu.be/YVU5wAA6Txo?t=1815s>)

### Applications and Performance
LoRa provides efficient fine-tuning for various tasks and model types, including language models, vision transformers, and diffusion models. The performance of LoRa-based methods is comparable to that of traditional fine-tuning based on benchmarks. 

### Hugging Face Path Library and LoRa Configurations [![[/snapshots/YVU5wAA6Txo/00-02-39.png]]](<https://youtu.be/YVU5wAA6Txo?t=157s>)
Hugging Face Path includes LoRa and other parameter-efficient fine-tuning techniques. To use LoRa effectively, identifying the optimal configuration for rank truncation and combining with other methods like prefix tuning or integer-8 quantization may be needed. [![[/snapshots/YVU5wAA6Txo/00-01-37.png]]](<https://youtu.be/YVU5wAA6Txo?t=91s>)

Source: [(188) PEFT LoRA Explained in Detail - Fine-Tune your LLM on your local GPU - YouTube](https://www.youtube.com/watch?v=YVU5wAA6Txo)
