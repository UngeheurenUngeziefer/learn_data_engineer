import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import preprocessing, linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


class LinearRegression:
	'''returns plot and coefficients of regression'''

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



class LogisticalRegression:
	'''returns logistical regression, coefficients, 
	   plot, and confusion matrix'''

	def __init__(self, field, divider, title):
		'''initializing function'''

		self.field = field
		self.divider = divider
		self.title = title

		# load numpy exoplanets data
		numpy_array = np.load('exoplanets_data.npy', allow_pickle=True)

		# numpy array to pandas dataframe
		self.df = pd.DataFrame.from_records(numpy_array)

		# create new column populated with 0s and 1s
		self.to_one_zero_column()

		# evaluating model, plotting regression, plotting confusion matrix
		self.x = np.arange(len(self.df['zero_one_field'])).reshape(-1, 1)
		self.y = np.array(self.df['zero_one_field'].sort_values())
		self.logistical_regression(self.x, self.y, self.title)


	def to_one_zero_column(self):
		'''function create new column populated with only 0 and 1
	   	   divider value split column values into two categories 0 and 1
		   also function returns percentage of distribution of 0 and 1'''

		# create a list of our conditions
		conditions = [
		    (self.df[self.field] >= self.divider),								   
		    (self.df[self.field] < self.divider)							
		    ]

		# create a list of the values we want to assign for each condition
		values = [1, 0]

		# create a new column and use np.select to assign values 
		# to it using our lists as arguments
		self.df['zero_one_field'] = np.select(conditions, values)

		# where field values exist
		self.df = self.df[self.df[self.field].notna()]

		# statistical distribution
		print(self.df['zero_one_field'].value_counts())

		# percentage distribution
		greater_than_divider = len(self.df[self.df['zero_one_field']==1])
		lesser_than_divider = len(self.df[self.df['zero_one_field']==0])
		percentage_of_great = \
			greater_than_divider/(greater_than_divider + lesser_than_divider) \
			* 100
		percentage_of_lessr = \
			lesser_than_divider/(greater_than_divider + lesser_than_divider) \
			* 100
		print("Percentage of values greater than divider is", \
			percentage_of_great)
		print("Percentage of values lesser than divider is", \
			percentage_of_lessr)


	def logistical_regression(self, x, y, title):
		'''function returns logistical regression coefficients 
		   returns plot with logistical regression
		   returns confusion matrix'''

		model = LogisticRegression(solver='liblinear', random_state=0)\
									.fit(self.x, self.y)

		print(f'Model intercept: {model.intercept_}')
		print(f'Model coef: {model.coef_}')

		regression_line = model.predict_proba(x)
		predicted_y = model.predict(x)
		print(f'\nRegression line values = {regression_line}')
		print(f'\nPredicted Y = {predicted_y}')
		print(f'\nx = {self.x}')
		print(f'\ny = {self.y}')

		reg_line_y = []
		for i in regression_line:
			reg_line_y.append(i[1])

		plt.scatter(self.x, predicted_y, color='red', \
		 							label='Incorrect predictions', marker='x')
		
		plt.scatter(self.x, self.y, color='green', label='Actual responses')

		plt.plot(self.x, reg_line_y, color='grey', \
								label='Logistical regression line')

		plt.scatter(self.x, reg_line_y, color='grey',\
								   label='Predicted probability', marker='s')

		plt.xticks(np.arange(min(self.x), max(self.x)+1, 1.0), rotation=45)
		plt.yticks(np.arange(min(self.y), max(self.y)+1, 0.5))
		plt.grid(color = '.9', linestyle = '-.', linewidth = 0.5)
		plt.axhline(.5, color='.5')
		plt.xlabel('x')
		plt.ylabel('y, p(x)')
		plt.locator_params(axis='x', nbins=50)
		plt.legend()
		plt.title(self.title)
		plt.show()

		print(model.score(x, y))
		cm = confusion_matrix(y, model.predict(x))

		fig, ax = plt.subplots(figsize=(8, 8))
		ax.imshow(cm)
		ax.grid(False)
		ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
		ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
		ax.set_ylim(1.5, -0.5)
		plt.title('Test Confusion Matrix')
		for i in range(2):
		    for j in range(2):
		        ax.text(j, i, cm[i, j], ha='center', va='center', 
		        						color='white', fontsize='large')
		plt.show()




# Plot 1
# LinearRegression('radius', 'mass', 
# 					'Planet Radius', 'Planet Mass',
# 					'#6676bc').linear_regression()

# Plot 2
# LinearRegression('star_age', 'star_mass', 
# 					'Star Age', 'Star Mass',
# 					'#bca766').linear_regression()

# Plot 3
# LinearRegression('period', 'semi_major_axis', 
# 					'Orbital Period', 'Semi Major Axis',
# 					'#9f66bc').linear_regression()

# Plot 4 and Plot 5
# LogisticalRegression('mass', 0.0315, 'Gigantic (1) vs Earth-like (0) exoplanets')