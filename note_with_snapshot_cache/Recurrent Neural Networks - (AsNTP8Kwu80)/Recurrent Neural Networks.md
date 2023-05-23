## Recurrent Neural Networks
### Introduction to Recurrent Neural Networks (RNNs) [![[/snapshots/AsNTP8Kwu80/00-00-15.png]]](<https://youtu.be/AsNTP8Kwu80?t=10s>)
Recurrent neural networks (RNNs) are neural networks with feedback loops, allowing them to work with different amounts of sequential data to make predictions. They have weights, biases, layers, and activation functions, like other neural networks. [![[/snapshots/AsNTP8Kwu80/00-04-16.png]]](<https://youtu.be/AsNTP8Kwu80?t=255s>)

### RNNs for Predicting Stock Prices [![[/snapshots/AsNTP8Kwu80/00-01-55.png]]](<https://youtu.be/AsNTP8Kwu80?t=113s>)
To make predictions about stock prices or any other time-sequential data, we can use an RNN. A key feature of the RNN is its ability to adapt its input to the amount of data available. [![[/snapshots/AsNTP8Kwu80/00-02-35.png]]](<https://youtu.be/AsNTP8Kwu80?t=153s>)

### Unrolling the Feedback Loop in RNNs [![[/snapshots/AsNTP8Kwu80/00-07-55.png]]](<https://youtu.be/AsNTP8Kwu80?t=472s>)
The feedback loop in an RNN can be "unrolled" by creating a copy of the neural network for each input value. This makes it easier to understand how the network operates with sequential data. Regardless of how many times an RNN is unrolled, the weights and biases remain the same across all inputs. [![[/snapshots/AsNTP8Kwu80/00-10-35.png]]](<https://youtu.be/AsNTP8Kwu80?t=631s>)

### Vanishing/Exploding Gradient Problem in RNNs [![[/snapshots/AsNTP8Kwu80/00-11-32.png]]](<https://youtu.be/AsNTP8Kwu80?t=691s>)
The vanishing/exploding gradient problem is a significant difficulty when training RNNs, particularly when dealing with long sequences of data. Gradients can "explode" when some weights become too large, causing difficulty in finding optimal weights and biases. Conversely, gradients can "vanish" when some weights become too small, also making it difficult to find optimal parameters. [![[/snapshots/AsNTP8Kwu80/00-13-43.png]]](<https://youtu.be/AsNTP8Kwu80?t=820s>)

### Long Short-Term Memory (LSTM) Networks [![[/snapshots/AsNTP8Kwu80/00-15-48.png]]](<https://youtu.be/AsNTP8Kwu80?t=945s>)
Long short-term memory (LSTM) networks are a popular solution to the vanishing/exploding gradient problem, and will be discussed further in later StatQuests. 

### Conclusion
Recurrent neural networks allow for predictions based on sequential data, with the ability to adapt to different amounts of data. They can be used to predict stock prices when trained and optimized correctly. However, the vanishing/exploding gradient problem can create challenges when training RNNs, making LSTM networks an essential solution for such cases. [![[/snapshots/AsNTP8Kwu80/00-05-43.png]]](<https://youtu.be/AsNTP8Kwu80?t=340s>)

Source: [Recurrent Neural Networks (RNNs), Clearly Explained!!! - YouTube](https://www.youtube.com/watch?v=AsNTP8Kwu80)
