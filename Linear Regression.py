# Task: Predict a student's grades based on the attributes presented in the data set.

import numpy as np
import pandas as pd
from sklearn import linear_model, sklearn
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from scipy import stats

# Data is being separated by semicolons
data = pd.read_csv("student_mat.csv", sep=";")

# print(data.head())

# Data Frame Filtering - we need to specifically filter the data set to predict their grades.
# G1 - G3 are the grades, G3 being the most recent grade that a student has acquired.
data = data[["absences", "studytime", "failures", "G1", "G2", "G3"]]
# print(data.head())

predict = "G3"
X = np.array(data.drop([predict], axis=1))  # New training data using G3
Y = np.array(data[predict])  # All of our labels

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, Y, test_size=0.1)  # Splits data up into 10% for test samples

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)  # Line of best fit
acc = linear.score(x_test, y_test)  # Represents accurracy of the model
print(acc)

print("Co: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
