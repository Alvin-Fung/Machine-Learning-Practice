import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

# Data distribution
#x = np.random.uniform(0.0, 5.0, 250) # Low, High, Size
#print(x)

# Histogram
#plt.hist(x , 5)
#plt.show()

# Big Data Distribution
x = np.random.uniform(0.0, 5.0, 100000) # Low, High, Size
#plt.hist(x, 100)
#plt.show()

# Normal Data Distribution / Gaussian data distribution
y = np.random.normal(5.0, 1.0, 100000) # Produces a bell curve in the graph - Mean value, standard deviation and size
plt.hist(y, 100)
plt.show()

# Scatter Plot

x = [5, 7, 8, 7, 12, 2, 4, 17, 18, 5, 6]
y = [52, 99, 87, 76, 54, 32, 101,87, 94, 78, 121]

plt.scatter(x,y)
plt.show()

# Scatter plot with random data distribution

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()
