# Task: Predict a student's grades based on the attributes presented in the data set.

import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("student_mat.csv", sep=";")
# Data is being separated by semicolons
print(data.head())

# Data Frame Filtering - we need to specifically filter the data set to predict their grades.
data = data[["absences", "studytime", "failures", "G1", "G2", "G3"]]
print(data.head())
