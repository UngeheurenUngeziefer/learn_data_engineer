import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class RegressionPlotting:
	'''return plot and coefficients of regression'''

	def __init__(self, field1, field2, field1_label, field2_label, color):
		'''initializing function'''

		self.field1 = field1
		self.field2 = field2
		self.field1_label = field1_label
		self.field2_label = field2_label
		self.color = color

		# load numpy exoplanets data
		numpy_array = np.load('exoplanets_data.npy', allow_pickle=True)

		# numpy array to pandas dataframe
		self.df = pd.DataFrame.from_records(numpy_array)


	def linear_regression(self):
		'''function returns pandas df with planet name and two fields 
		   (NULL values dropped)
		   return linear regression coefficients
		   return plot with regression'''

		# new df with planet name, and two given columns
		cleared_df = self.df[['granule_uid', self.field1, self.field2]]

		# drop NULL values
		cleared_df = cleared_df.dropna()

		# printing clear df
		print(cleared_df)

		# collecting X and Y values
		X = cleared_df[self.field1].values
		Y = cleared_df[self.field2].values

		# mean for X and Y
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

		# coefficients 
		b1 = numer / denom
		b0 = mean_y - (b1 * mean_x)

		# plotting values and regression line
		max_x = np.max(X) + 100
		min_x = np.min(X) - 100

		# calculating line values x and y
		x = np.linspace(min_x, max_x, 1000)
		y = b0 + b1 * x

		ss_t = 0
		ss_r = 0

		for i in range(n):
			y_pred = b0 + b1 * X[i]
			ss_t += (Y[i] - mean_y) ** 2
			ss_r += (Y[i] - y_pred) ** 2
		r2 = 1 - (ss_r/ss_t)
		
		coefficients_info = \
			f'r² = {r2}\n' + \
			f'amount that Y ({self.field2_label}) will change ' + \
			f'for each 1 of X ({self.field1_label}): {b1}\n' + \
			f'value of Y ({self.field2_label}) ' + \
			f'if the X ({self.field1_label}) == 0: {b0}'

		# plotting line
		plt.plot(x, y, color='red', label='Regression Line')

		# scatter points
		plt.scatter(X, Y, color=self.color, label='Scatter Plot')

		plt.title(f'{self.field1_label} and {self.field2_label} correlation')
		plt.xlabel(self.field1_label)
		plt.ylabel(self.field2_label)
		plt.legend()

		# text position is not scalable! you need to change it for each plot!
		plt.text(10, 2.5, coefficients_info, style='italic',
	        bbox={'facecolor': self.color, 'alpha': 0.5, 'pad': 10})
		plt.show()


# Plot 1
# RegressionPlotting('radius', 'mass', 
# 					'Planet Radius', 'Planet Mass',
# 					'#6676bc').linear_regression()

# Plot 2
# RegressionPlotting('star_age', 'star_mass', 
# 					'Star Age', 'Star Mass',
# 					'#bca766').linear_regression()

# Plot 3
# RegressionPlotting('period', 'semi_major_axis', 
# 					'Orbital Period', 'Semi Major Axis',
# 					'#9f66bc').linear_regression()
