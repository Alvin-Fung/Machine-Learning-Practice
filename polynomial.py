import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from scipy import stats

# Polynomial Regression

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

my_model = np.poly1d(np.polyfit(x, y, 3)) # The number is the degree of the fitting polynomial

my_line = np.linspace(1,22,100)

plt.scatter(x, y)
plt.plot(my_line,my_model(my_line))
plt.show()
