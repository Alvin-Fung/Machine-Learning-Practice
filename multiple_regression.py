import pandas
from sklearn import linear_model

# df = dataframe object
df = pandas.read_csv("data.csv")

# List of inpendent values, X
# List of dependent values, Y
X = df[['Weight', 'Volume']]
Y = df['CO2']

''' 
Can use the LinearRegression() method to create
a linear regression object.
fit() can be used the independent and dependent values as
parameters and fills the regression object with data that
describes the relationship.
'''

regr = linear_model.LinearRegression()
regr.fit(X, Y)

# Prediction with car weight of 2300KG & volume of 1300cm^3
predicatedCO2 = regr.predict([[2300, 1300]])
print(predicatedCO2)

# Coefficient
print(regr.coef_)
