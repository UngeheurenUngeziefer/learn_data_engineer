# K-Nearest Neighbors

import numpy as np
import pandas as pd
from termcolor import colored as cl 				 # elegant printing of text
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.preprocessing import StandardScaler 	 # normalizing data
from sklearn.neighbors import KNeighborsClassifier   # KNN algorithm
from sklearn.metrics import accuracy_score 		  	 # algorithm accuracy
from sklearn.model_selection import train_test_split # splitting the data

style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (16, 7)


# Importing Data
class KNN:
	'''plotting KNN'''

	def __init__(self, df, *fields):
		'''initializing function'''
		self.df = df
		self.df = self.df[[*fields]]

		# print df
		self.df = self.df.dropna()
		print(self.df)

		print(self.df.nunique())

		self.scatter()
		
		

	def scatter(self):
		# 1. Sepal scatter visualization

		sb.scatterplot(self.df.columns[1], self.df.columns[2],
						 data=self.df, hue=self.df.columns[0], 
						 palette = 'Set2', edgecolor = 'b', 
						 s = 150, alpha = 0.7)
		plt.title('Star Mass / Semi Major Axis')
		plt.xlabel('Semi Major Axis')
		plt.ylabel('Star Mass')
		plt.legend(loc = 'upper right', fontsize = 12)
		plt.show()


	def scatter2(self):
		# 3. Data Heatmap

		sb.pairplot(data = self.df, hue='species', palette = ['Red', 'Blue', 'limegreen'])
		plt.show()


# load numpy exoplanets data
numpy_array = np.load('exoplanets_data.npy', allow_pickle=True)

# numpy array to pandas dataframe
df = pd.DataFrame.from_records(numpy_array)

# create normal number of groups by star spectre
df['spec_type_first_letter'] = df['star_spec_type'].astype(str).str[0]

KNN(df, 'spec_type_first_letter', 'semi_major_axis', 'star_mass')

