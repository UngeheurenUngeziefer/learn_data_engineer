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
		self.linear_regression()


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
		plt.text(75, 500000, coefficients_info, style='italic',
	        bbox={'facecolor': self.color, 'alpha': 0.5, 'pad': 10})
		plt.show()


class LogisticalRegression:
	'''returns number of 1 and 0 values by divider of column with values
	   		   percentage distribution on 1 and 0
	   		   model intercept and coefficient value
	   		   regression line values (x and y)
	   		   predicted Y list (0 and 1 sorted) - logistical regression
	   		   x values of predictor sorted
	   		   y values list 0 and 1
	   		   plot with Logistical Regression and labels
	   		   plot Confusion Matrix'''

	def __init__(self, field, divider, predictor, zeros, ones):
		'''initializing function'''

		self.field = field
		self.divider = divider
		self.predictor = predictor
		self.zeros = zeros
		self.ones = ones
		self.color = '#6495ED'
		self.title = f'Dependence of {self.ones}/{self.zeros} exoplanets ' + \
					 f'on the {self.predictor.capitalize()}'

		# load numpy exoplanets data
		numpy_array = np.load('exoplanets_data.npy', allow_pickle=True)

		# numpy array to pandas dataframe
		self.df = pd.DataFrame.from_records(numpy_array)

		# create new column populated with 0s and 1s
		self.to_one_zero_column()

		# save to df only needed columns
		self.df = self.df[['zero_one_field', self.predictor]]

		# drop all NULL's
		self.df = self.df.dropna()

		# sort values
		self.df = self.df.sort_values(by=self.predictor)

		# apply x and y values, reshape x, plot regression
		self.y = np.array(self.df['zero_one_field'])
		self.x = np.array(self.df[self.predictor])
		self.x = self.x.reshape(-1, 1)
		
		# evaluating model, plotting regression, plotting confusion matrix
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
		   					plot with logistical regression
		   					confusion matrix'''

		model = LogisticRegression(solver='liblinear', random_state=0)\
									.fit(self.x, self.y)

		regression_line = model.predict_proba(x)
		predicted_y = model.predict(x)
		print(f'\nRegression line values = {regression_line}')
		print(f'\nPredicted Y = {predicted_y}')


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

		labels = [f'0 ({self.zeros})', '0.5 (middle line)', f'1 ({self.ones})', '']
		plt.xticks(np.arange(min(self.x), max(self.x)+1, 1.0), rotation=45)
		plt.yticks(np.arange(min(self.y), max(self.y)+1, 0.5), labels)

		plt.grid(color = '.9', linestyle = '-.', linewidth = 0.5)
		plt.axhline(.5, color='.5')
		# limit of y axis
		plt.ylim([-0.1,1.1])
		
		plt.xlabel(f'x\n {self.predictor}')
		plt.ylabel(f'y, p(x)\n {self.field}')
		plt.locator_params(axis='x', nbins=50)
		plt.legend()

		plt.title(f'Logistical Regression: \n {self.title}')

		coefficients_info = f'Model intercept: {model.intercept_}' + \
							f'\nModel coef: {model.coef_}' + \
							f'\nModel accuracy: {model.score(x, y)}'

		plt.text(3, 0.75, coefficients_info, style='italic',
	        bbox={'facecolor': self.color, 'alpha': 0.5, 'pad': 10})
		plt.show()

		cm = confusion_matrix(y, model.predict(x))

		fig, ax = plt.subplots(figsize=(8, 8))
		ax.imshow(cm)
		ax.grid(False)
		ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
		ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
		ax.set_ylim(1.5, -0.5)
		plt.title('Confusion Matrix')
		for i in range(2):
		    for j in range(2):
		        ax.text(j, i, cm[i, j], ha='center', va='center', 
		        						color='white', fontsize='large')
		plt.show()




# Plot 1
# LinearRegression('radius', 'mass', 
# 				   'Planet Radius', 'Planet Mass',
# 				   '#6676bc')

# Plot 2
# LinearRegression('star_age', 'star_mass', 
# 				   'Star Age', 'Star Mass',
# 				   '#bca766')

# Plot 3
# LinearRegression('semi_major_axis', 'period', 
# 				   'Semi Major Axis', 'Orbital Period',
# 				   '#9f66bc')

# Plot 1
# LogisticalRegression('mass', 0.0315, 'radius',
# 					'Earth-like', 'Gigantic')
