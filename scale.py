import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pd.read_csv("data.csv")

# Mean value
v = df['Weight']

mean = np.mean(v)
print("This is the mean of the weight column:", mean)


# Standard deviation
std = np.std(v)
print("This is the standard deviation: ", std)

'''
Standardization method:
    z = (x - u) / s
    
z = New value
x = original value
u = is the mean
s = standard deviation
'''

#print ((790 - mean) / std) # Using first original value from weight column

# Example - scaling all values in the weight and volumn columns:
# X = df[['Weight', 'Volume']]
# scaledX = scale.fit_transform(X)
#print (scaledX)

# Predicting CO2 values using the scale to predict the values(Used when the weight and volume is known)
X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
