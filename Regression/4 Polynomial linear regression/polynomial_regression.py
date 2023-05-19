# -*- coding: utf-8 -*-
"""Polynomial_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1byRbrhxijDPAWcqp9xpmPdXLMUlti8dx

# Polynomial Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

data = pd.read_csv('Position_Salaries.csv')
X = data.iloc[:, 1:-1].values
Y = data.iloc[:, -1].values

print(X)

print(Y)

"""## Training the Linear Regression model on the whole dataset"""

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, Y)

"""## Training the Polynomial Regression model on the whole dataset"""

# The PolynomialFeatures class is a transformer in scikit-learn, a popular 
# machine learning library in Python. It is used for generating polynomial 
# features from input data
from sklearn.preprocessing import PolynomialFeatures

# creates an instance of the PolynomialFeatures class named poly_reg with a 
# degree of 2. This means that the poly_reg object will be used to generate 
# polynomial features up to the second degree
poly_reg = PolynomialFeatures(degree = 4)

# applies the fit_transform method of the PolynomialFeatures object poly_reg to 
# the feature matrix X
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()

# 
lin_reg_2.fit(X_poly, Y)

"""## Visualising the Linear Regression results"""

plt.scatter(X, Y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title("Truth or Bluff (Linear regression)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()

"""## Visualising the Polynomial Regression results"""

plt.scatter(X, Y, color = 'red')
plt.plot(X, lin_reg_2.predict(X_poly), color = 'blue')
plt.title("Truth or Bluff (Polynomial regression)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()

"""## Visualising the Polynomial Regression results (for higher resolution and smoother curve)"""

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

"""## Predicting a new result with Linear Regression"""

lin_reg.predict([[6.5]])

"""## Predicting a new result with Polynomial Regression"""

lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))