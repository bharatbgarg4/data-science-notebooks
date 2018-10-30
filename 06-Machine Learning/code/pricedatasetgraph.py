
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#==============================================================================
# imort the dataset of flat prices
#==============================================================================

flatdata = pd.read_csv ('Price.csv')
print(flatdata)

X = flatdata.iloc [:,:-1].values
y = flatdata.iloc [:,1].values
plt.plot(X,y)
plt.ylabel('price')
plt.xlabel('area')
plt.show()