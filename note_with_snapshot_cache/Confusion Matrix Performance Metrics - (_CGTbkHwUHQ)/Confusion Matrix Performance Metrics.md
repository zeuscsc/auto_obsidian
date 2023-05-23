## Confusion Matrix Performance Metrics
### Performance Metrics for Confusion Matrix [![[/snapshots/_CGTbkHwUHQ/00-00-09.png]]](<https://youtu.be/_CGTbkHwUHQ?t=5s>)

#### Given Confusion Matrix
A given confusion matrix has 150 predictions with 100 examples predicted as 'yes' and 50 examples predicted as 'no'. There are 50 'no' type examples and 100 'yes' type examples. [![[/snapshots/_CGTbkHwUHQ/00-00-15.png]]](<https://youtu.be/_CGTbkHwUHQ?t=12s>)

#### Definitions
- True Negative: 45, actual type is 'no' and predicted as 'no' [![[/snapshots/_CGTbkHwUHQ/00-01-24.png]]](<https://youtu.be/_CGTbkHwUHQ?t=80s>)
- False Positive: 5, actual type is 'no' but predicted as 'yes' 
- False Negative: 5, actual type is 'yes' but predicted as 'no' 
- True Positive: 95, actual type is 'yes' and predicted as 'yes' 

#### Performance Metrics Calculation
1. Accuracy: (TN + TP) / Total predictions = (45 + 95) / 150 = 93.33% [![[/snapshots/_CGTbkHwUHQ/00-04-52.png]]](<https://youtu.be/_CGTbkHwUHQ?t=290s>)
2. Misclassification Rate: (FN + FP) / Total predictions = 10 / 150 = 6.67% [![[/snapshots/_CGTbkHwUHQ/00-02-15.png]]](<https://youtu.be/_CGTbkHwUHQ?t=132s>)
3. True Positive Rate (Sensitivity or Recall): TP / Actual Yes = 95 / 100 = 95% [![[/snapshots/_CGTbkHwUHQ/00-03-25.png]]](<https://youtu.be/_CGTbkHwUHQ?t=202s>)
4. False Positive Rate: FP / Actual No = 5 / 50 = 10% [![[/snapshots/_CGTbkHwUHQ/00-03-32.png]]](<https://youtu.be/_CGTbkHwUHQ?t=208s>)
5. True Negative Rate (Specificity): TN / Actual No = 45 / 50 = 90% [![[/snapshots/_CGTbkHwUHQ/00-04-14.png]]](<https://youtu.be/_CGTbkHwUHQ?t=252s>)
6. Precision: TP / Predicted Yes = 95 / 100 = 95% [![[/snapshots/_CGTbkHwUHQ/00-03-08.png]]](<https://youtu.be/_CGTbkHwUHQ?t=185s>)
7. Prevalence: Actual Yes / Total predictions = 100 / 150 = 66.67% [![[/snapshots/_CGTbkHwUHQ/00-05-05.png]]](<https://youtu.be/_CGTbkHwUHQ?t=301s>)

These different performance metrics are used to evaluate machine learning model performance. [![[/snapshots/_CGTbkHwUHQ/00-01-34.png]]](<https://youtu.be/_CGTbkHwUHQ?t=92s>)

Source: [Confusion Matrix Solved Example Accuracy Precision Recall F1 Score Prevalence by Mahesh Huddar - YouTube](https://www.youtube.com/watch?v=_CGTbkHwUHQ)
