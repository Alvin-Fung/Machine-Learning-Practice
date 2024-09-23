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
