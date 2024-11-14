# SVM works well for high dimensional data and allows for clarrifying data that
# does not have a linear correspondence.

import sklearn
from sklearn import datasets
from sklearn import svm

cancer = datasets.load_breast_cancer()

print("Features:", cancer.feature_names)
print("Labels: ", cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x, y, test_size=0.1)  # Splits data up into 10% for test samples

print(x_train, y_train)
