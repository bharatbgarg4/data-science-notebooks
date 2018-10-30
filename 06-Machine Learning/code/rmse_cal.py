#RMSE measures the difference between the predictions of a model, and the corresponding ground truth. 
#A large RMSE is equivalent to a large average error, so smaller values of RMSE are better. 


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

flatdata = pd.read_csv ('//home//piford//Health.csv')


X = flatdata.iloc [:,:3].values
y = flatdata.iloc [:,:-1].values


from sklearn.preprocessing import Imputer
missingValueImputer = Imputer (missing_values = 'NaN', strategy = 'mean', 
                               axis = 0)
missingValueImputer = missingValueImputer.fit (X[:,1:3])
X[:,1:3] = missingValueImputer.transform(X[:,1:3])

#print("see imputation results")
#print(X[:,1:3])



from sklearn.preprocessing import LabelEncoder
X_labelencoder = LabelEncoder()
X[:, 0] = X_labelencoder.fit_transform(X[:, 0])
#print (X)

# for y
y_labelencoder = LabelEncoder ()
y = y_labelencoder.fit_transform (y)
#print (y)


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 1/4, 
                                                     random_state = 0)



from sklearn.linear_model import LinearRegression
regressoragent = LinearRegression()
regressoragent.fit (X_train, y_train )

predictValues = regressoragent.predict(X_test)
#print(predictValues)


m=regressoragent.coef_
c=regressoragent.intercept_
print(m)
print(c)




from sklearn import metrics
from sklearn.metrics import mean_squared_error
from math import sqrt
print("RMSE is:-")
print(np.sqrt(metrics.mean_squared_error(y_test, predictValues)))

