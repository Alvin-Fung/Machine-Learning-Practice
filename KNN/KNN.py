import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")
# print(data.head())

le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))
# print(buying)

predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.1)  # Splits data up into 10% for test samples

model = KNeighborsClassifier(n_neighbors=8)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print("Accuracy: ", acc)

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    data_point = tuple(int(i) for i in x_test[x])
    print("Predicted:", names[predicted[x]], "Data:",
          data_point, "Actual:", names[y_test[x]])
    # Able to now see the neighbors of each point in testing data.
    n = model.kneighbors([x_test[x]], 9, True)
    print("N: ", n)
