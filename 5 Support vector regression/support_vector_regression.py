# -*- coding: utf-8 -*-
"""Support_vector_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G-jwL6FFYU20Ppdu2wRG-c4-UCQvHf4I

# Support Vector Regression (SVR)

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

data = pd.read_csv("Position_Salaries.csv")
X = data.iloc[:, 1:-1].values
Y = data.iloc[:, -1].values

print(X)

print(Y)

Y = Y.reshape(len(Y), 1)
print(Y)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X)
Y = sc_Y.fit_transform(Y)

print(X)

print(Y)

"""## Training the SVR model on the whole dataset"""

# By importing SVR from sklearn.svm, you gain access to the Support Vector 
# Regression (SVR) algorithm. SVR is a variant of Support Vector Machines (SVM) 
# used for regression tasks. It aims to find the best-fitting hyperplane that 
# maximizes the margin while still allowing for some tolerance (epsilon) for errors
from sklearn.svm import SVR
regressor = SVR()
regressor.fit(X, Y)

"""## Predicting a new result"""

# transform the input value using the sc_X scaler, make a prediction using the 
# SVR model (regressor), and then transform the predicted value back to its 
# original scale using the sc_Y scaler
sc_Y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])).reshape(-1, 1))

"""## Visualising the SVR results"""

plt.scatter(sc_X.inverse_transform(X), sc_Y.inverse_transform(Y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_Y.inverse_transform(regressor.predict(X).reshape(-1, 1)))
plt.title("Truth or Bluff (SVR)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()

"""## Visualising the SVR results (for higher resolution and smoother curve)"""

X_grid = np.arange(min(sc_X.inverse_transform(X)), max(sc_X.inverse_transform(X)), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(sc_X.inverse_transform(X), sc_Y.inverse_transform(Y), color = 'red')
plt.plot(X_grid, sc_Y.inverse_transform(regressor.predict(sc_X.transform(X_grid)).reshape(-1, 1)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()