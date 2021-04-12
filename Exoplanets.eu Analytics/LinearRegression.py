# test linear regression

# import frameworks
import numpy as np
from sklearn.linear_model import LinearRegression

# create x array with two dimensions
# create y array with one dimension
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# instance of regression model, calculate the optimal values of the weights x and y
model = LinearRegression().fit(x, y)

# model basic info
# print('Coefficient of determination:', model.score(x, y))
# print('Intercept - model predicts the response y =', model.intercept_, ' when 𝑥 is 0')
# print('Slope - predicted response rises by', model.coef_,  'when 𝑥 is increased by 1')
# print('-----------------------------------------------------------------------------')

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

# In this case, you multiply each element of x with model.coef_ and add model.intercept_ to the product.


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

ax.plot(y_pred, y_pred)

plt.show()