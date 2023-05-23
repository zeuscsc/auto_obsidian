## Cross Attention
### Introduction to Cross Attention
Cross attention is a technique that significantly improves the performance of many deep learning models by conditioning them on extra information, such as text. Models like Stable Diff, Image Gen, and Muse all utilize cross attention to achieve impressive results. [![[/snapshots/aw3H-wPuRcw/00-00-30.png]]](<https://youtu.be/aw3H-wPuRcw?t=28s>)

### Self-Attention Basics
Self-attention, also called standard attention, involves creating three matrices (Q, K, and V) from the input and performing several operations on them. These operations include calculating the dot product between Q and K to measure similarity, normalizing the resulting values with the softmax function, and multiplying the normalized values by the V matrix. [![[/snapshots/aw3H-wPuRcw/00-01-16.png]]](<https://youtu.be/aw3H-wPuRcw?t=74s>)

### Self-Attention on Images
When applying self-attention to images, we first flatten the image and then create our Q, K, and V matrices by projecting the flattened image into the latent space. We then perform the same operations as described earlier, ultimately enabling the model to route information between all pixels in a single layer. [![[/snapshots/aw3H-wPuRcw/00-01-51.png]]](<https://youtu.be/aw3H-wPuRcw?t=109s>)

### Cross Attention Concept
In cross attention, a major change occurs in the preparation of Q, K, and V matrices: Q is still a projection of the input features, but K and V are projections of the conditional information (e.g., the text). We perform the same operations with these new matrices, and the result is a model that can acquire information from the entire text conditioning and decide which parts to pay attention to the most. [![[/snapshots/aw3H-wPuRcw/00-00-38.png]]](<https://youtu.be/aw3H-wPuRcw?t=36s>)

### Cross Attention Application
Cross attention can be applied to many tasks by bringing the conditional data into a manageable dimensional space. Overall, cross attention enables global information routing and allows models to learn from additional conditioning, resulting in better performance and flexibility. 

Source: [(195) Cross Attention | Method Explanation | Math Explained - YouTube](https://www.youtube.com/watch?v=aw3H-wPuRcw)
