import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load numpy exoplanets data
numpy_array = np.load('exoplanets_data.npy', allow_pickle=True)

# numpy array to pandas dataframe
df = pd.DataFrame.from_records(numpy_array)


# new df with planet name, radius and mass columns
rad_mass_df = df[['granule_uid', 'radius', 'mass']]

# drop NULL values
rad_mass_df = rad_mass_df.dropna()

# collecting X and Y
X = rad_mass_df['radius'].values
Y = rad_mass_df['mass'].values

# mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# total number of values
n = len(X)

# using the formula to calculate b1 and b2
numer = 0
denom = 0

for i in range(n):
	numer += (X[i] - mean_x) * (Y[i] - mean_y)
	denom += (X[i] - mean_x) ** 2

b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

# coefficients 
print(f'amount that Y will change for each 1 of X: {b1}',
	  f'\nvalue of Y if the X == 0: {b0}', '\n')

# plotting values and regression line
max_x = np.max(X) + 100
min_x = np.min(X) - 100

# calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

# plotting line
plt.plot(x, y, color='red', label='Regression Line')

# scatter points
plt.scatter(X, Y, color='blue', label='Scatter Plot')

plt.title('Exoplanets radius and mass correlation')
plt.xlabel('Planet Radius in Jupiters')
plt.ylabel('Planet Mass in Jupiters')
plt.legend()
# plt.show()

ss_t = 0
ss_r = 0
for i in range(n):
	y_pred = b0 + b1 * X[i]
	ss_t += (Y[i] - mean_y) ** 2
	ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(r2)


