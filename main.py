import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

# Data distribution
x = np.random.uniform(0.0, 5.0, 250) # Low, High, Size
#print(x)

# Histogram
plt.hist(x , 5)
plt.show()

# Big Data Distribution
x = np.random.uniform(0.0, 5.0, 100000) # Low, High, Size
plt.hist(x, 100)
plt.show()
