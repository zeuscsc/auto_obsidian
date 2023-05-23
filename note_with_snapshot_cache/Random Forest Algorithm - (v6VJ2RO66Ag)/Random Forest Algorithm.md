## Random Forest Algorithm
### Random Forest Algorithm Introduction
Random Forest Algorithm is a collection of multiple random decision trees, which is less sensitive to training data and is more effective in generalization. In this discussion, a simple binary classification problem dataset is used to compare Random Forest with Decision Trees. [![[/snapshots/v6VJ2RO66Ag/00-00-09.png]]](<https://youtu.be/v6VJ2RO66Ag?t=6s>)

### Issue with Decision Trees
Decision trees are highly sensitive to the training data, which can result in high variance and failure to generalize. To overcome this, the Random Forest algorithm is introduced. [![[/snapshots/v6VJ2RO66Ag/00-02-05.png]]](<https://youtu.be/v6VJ2RO66Ag?t=123s>)

### Bootstrapping in Random Forest
The first step in creating a Random Forest is building new datasets from the original data by randomly selecting rows with replacement. This process is called bootstrapping. [![[/snapshots/v6VJ2RO66Ag/00-02-35.png]]](<https://youtu.be/v6VJ2RO66Ag?t=152s>)

### Feature Selection in Random Forest [![[/snapshots/v6VJ2RO66Ag/00-06-25.png]]](<https://youtu.be/v6VJ2RO66Ag?t=383s>)
When training a decision tree on each bootstrap dataset, a subset of features is randomly selected for training. This reduces the correlation between trees and helps the model be less sensitive to the original training data. [![[/snapshots/v6VJ2RO66Ag/00-03-33.png]]](<https://youtu.be/v6VJ2RO66Ag?t=210s>)

### Building Random Forest Trees
Random Forest builds trees using bootstrapping and random feature selection processes which leads to different trees in the forest. The trees are then combined to make predictions using majority voting for classification problems and averaging for regression problems. 

### Key Points about Random Forest Algorithm 
- It is called "random" due to the bootstrapping and random feature selection processes. [![[/snapshots/v6VJ2RO66Ag/00-06-02.png]]](<https://youtu.be/v6VJ2RO66Ag?t=359s>)
- Bootstrapping helps the model be less sensitive to the original training data. [![[/snapshots/v6VJ2RO66Ag/00-06-20.png]]](<https://youtu.be/v6VJ2RO66Ag?t=377s>)
- Random feature selection reduces correlation between trees and helps to lower variance. 
- Ideal feature subset size is usually close to the square root of the total number of features. [![[/snapshots/v6VJ2RO66Ag/00-06-59.png]]](<https://youtu.be/v6VJ2RO66Ag?t=417s>)
- For regression problems, predictions are combined using averaging instead of majority voting. [![[/snapshots/v6VJ2RO66Ag/00-07-25.png]]](<https://youtu.be/v6VJ2RO66Ag?t=442s>)

Source: [(188) Random Forest Algorithm Clearly Explained! - YouTube](https://www.youtube.com/watch?v=v6VJ2RO66Ag)
