# -*- coding: utf-8 -*-
"""Salary_Estimation_using_KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fUsuRAE2REf83O1CIbvGI_mrf-SPE5kM
"""

import pandas as pd #used for loading dataset
import numpy as np #used to perform array array

from google.colab import files
uploaded = files.upload()

dataset = pd.read_csv("salary.csv")

print(dataset.shape)
print(dataset.head(5))

income_set = set(dataset['income'])
dataset['income'] = dataset['income'].map({'<=50K': 0, '>50K': 1}).astype(int)
print(dataset.head)

x = dataset.iloc[:, :-1].values
x

y = dataset.iloc[:, -1].values
y

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train) 
x_test = sc.transform(x_test)

error = []
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

#calculating error for k values between 0 to 40
for i in range(1, 40):
  model = KNeighborsClassifier(n_neighbors = i)
  model.fit(x_train, y_train)
  pred_i = model.predict(x_test)
  error.append(np.mean(pred_i != y_test))

plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color ='black', linestyle = 'dashed', marker = 'o', markerfacecolor='yellow', markersize = 10)
plt.title("Error rate of k value")
plt.xlabel('K Value')
plt.ylabel('Mean Error')

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 2, metric = 'minkowski', p = 2)
model.fit(x_train, y_train)

age = int(input("Enter New Employee's Age: "))
edu = int(input("Enter New Employee's Education: "))
cg = int(input("Enter New Employee's Central gain: "))
wh = int(input("Enter New Employee's Hour's per week: "))
newEmp = [[age, edu, cg, wh]]
result = model.predict(sc.transform(newEmp))
print(result)

if result == 1:
  print("Employee might get salary above 50k")
else:
  print("Employee might not get salary above 50k")

y_pred = model.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix: ")
print(cm)

print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, y_pred)*100))

