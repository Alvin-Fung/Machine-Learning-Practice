import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from scipy import stats

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
#plt.show()

# Scatter Plot

x = [5, 7, 8, 7, 12, 2, 4, 17, 18, 5, 6]
y = [52, 99, 87, 76, 54, 32, 101,87, 94, 78, 121]

plt.scatter(x,y)
#plt.show()

# Scatter plot with random data distribution

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
#plt.show()

# Linear Regression 

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Executes a method that returns important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x,y) # r for relationship, the coefficient of the correlation.
                                                        # - 1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.

def linear_equation(x): # Uses the slope and intercept values to return a new value. 
    # New value represents where on the y-axis the corresponding x value will be placed.
    return slope * x + intercept

# Runs every x value within the array through the function. Results in new array with new values for y-axis.
my_model =  list(map(linear_equation,x))

plt.scatter(x, y) # Draws the original scatter plot
plt.plot(x, my_model) # Draws the line of linear regression
#plt.show()

# Predicting Future Values

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def linear_equation(x):
    return slope * x + intercept

speed = linear_equation(10)
#print(speed) # Result = 85.59308314937454

# Linear Regression example where it would not be best used to predict future values.
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print(r) # Result = 0.01331814154297491, so no relation here.
