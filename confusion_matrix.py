import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
# Used in classification problem to assess where errors in the model were made.

# Actual & predicted values
actual = np.random.binomial(1, 0.9, size=1000)
predicted = np.random.binomial(1, 0.9, size=1000)


confusion_matrix = metrics.confusion_matrix(actual, predicted)

# Visual display for converting the table into a confusion matrix display
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0,1])

cm_display.plot()
plt.show()

# Metrics

## Accuracy
# Formula: (True Positive + True Negative) / Total Predictions
Accuracy =  metrics.accuracy_score(actual, predicted)
print(Accuracy)

## Precision
# Formula: True Positive / (True Positive + False Positive)
Precision = metrics.precision_score(actual, predicted)

## Sensitivity(Recall)
# Formula: True Positive / (True Positive +  False Negative)
Sensitivity_recall = metrics.recall_score(actual, predicted)

## Specificity
# Formula: True Negative / (True Negative + False Positive)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)

## F-score
# Formula: 2 * ((Precision * Sensitivity) / (Precision + Sensitivity))

F1_score = metrics.f1_score(actual, predicted)

# All calculations in one:
print({"Accuracy": Accuracy, "Precision":Precision, "Sensivitiy_recall":Sensitivity_recall, "Specifity":Specificity, "F1_score":F1_score})
