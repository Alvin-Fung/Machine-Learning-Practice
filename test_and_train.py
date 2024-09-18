import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
np.random.seed(2)


# Example - Shows 100 customers in a shop, and their habits
x = np.random.normal(3, 1, 100) # Represents number of minutes before making a purhcase
y = np.random.normal(150, 40, 100) / x # Represents amount of money spent on the purchase

plt.scatter(x, y)
plt.show()

# Training
# Random Selection of 80% of the original data
train_x = x[:80]
train_y = y[:80]

# Remaining 20%
test_x = x[80:]
test_y = y[80:]

model = np.poly1d(np.polyfit(train_x, train_y,4))

r2 = r2_score(train_y, model(train_x))
print(r2) # 0.7988645544629797

myline = np.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, model(myline))
plt.show()
print(model(5)) # 22.87962591811811
