## Decision Trees
### Decision Trees: Introduction and Classification [![[/snapshots/ZVR2Way4nwQ/00-00-08.png]]](<https://youtu.be/ZVR2Way4nwQ?t=5s>)

#### Dataset and Problem

We have a dataset with two features x0 and x1 and two classes (green and red). The dataset is not linearly separable. The goal is to use decision trees to classify data points based on these features. [![[/snapshots/ZVR2Way4nwQ/00-09-55.png]]](<https://youtu.be/ZVR2Way4nwQ?t=592s>)

#### Decision Tree

A decision tree is a binary tree that recursively splits the dataset into pure leaf nodes, that contain only one type of class. Decision tree has two kinds of nodes - decision nodes and leaf nodes. Decision nodes contain a condition to split the data, while leaf nodes help decide the class of a new data point. [![[/snapshots/ZVR2Way4nwQ/00-01-06.png]]](<https://youtu.be/ZVR2Way4nwQ?t=64s>)

#### Splitting Criteria

The model needs to learn the correct conditions for optimally splitting the data. This is done by information gain, which depends on entropy - a measure of information contained in a state. The model chooses the split that maximizes information gain by comparing every possible split. [![[/snapshots/ZVR2Way4nwQ/00-05-14.png]]](<https://youtu.be/ZVR2Way4nwQ?t=311s>)

#### Greedy Algorithm and Final Model [![[/snapshots/ZVR2Way4nwQ/00-09-24.png]]](<https://youtu.be/ZVR2Way4nwQ?t=561s>)

Decision tree is a greedy algorithm that selects the current best split that maximizes information gain without backtracking to change previous splits. This doesn't guarantee the most optimal set of splits but makes training faster and performs well despite its simplicity. 

In the next video, we will see how to code a decision tree from scratch and discuss Gini Index. 

Source: [Decision Tree Classification Clearly Explained! - YouTube](https://www.youtube.com/watch?v=ZVR2Way4nwQ)
