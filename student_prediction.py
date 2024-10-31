import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("student_mat.csv", sep=";")
# Data is being separated by semicolons
print(data.head())
