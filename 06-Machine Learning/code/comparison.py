import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

flatdata = pd.read_csv ('Price.csv')
X = flatdata.iloc [:,0].values
y = flatdata.iloc [:,1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = .20)

# Fitting DecisionTree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(max_depth=2)
dt_reg.fit(X_train, y_train)
y_1 = dt_reg.predict()

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_2 = lin_reg.predict()

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y_train)
y_3 = lin_reg_2.predict(poly_reg.fit_transform(X_test))

# Visualising the DecisionTree Regression results
plt.scatter(X_train, y_train, color = 'green')
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, y_1, color="black")
plt.xlabel("Area of Flat")
plt.ylabel("Price")
plt.title("compare Training result Decision Tree - Area/Price")
plt.legend()
plt.show()

# Visualising the Linear Regression results
plt.scatter(X_train, y_train, color = 'green')
plt.scatter(X_test, y_test, color = 'red')
plt.plot (X_test, y_2, color = 'black')
plt.title ('compare Training result Linear - Area/Price')
plt.xlabel('Area of Flat')
plt.ylabel('Price')
plt.show()

# Visualising the Polynomial Regression results
plt.scatter(X_train, y_train, color = 'green')
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, y_3, color = 'black')
plt.title ('compare Training result Polynomial - Area/Price')
plt.xlabel('Area of Flat')
plt.ylabel('Price')
plt.show()