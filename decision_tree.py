import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv("data2.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'Yes': 1, 'No': 0}
df['Go'] = df['Go'].map(d)


# Impute missing values in 'Go' column with the mean
df['Go'] = df['Go'].fillna(df['Go'].mean())  # Replace NaN with mean

features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

# Train the decision tree
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features)
plt.show()

# This doesn't work... why..?
