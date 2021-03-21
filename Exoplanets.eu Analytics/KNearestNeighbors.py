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


class KNN:
	'''plotting KNN'''

	def __init__(self, df, field1='', field2='', group_field=''):
		'''initializing function'''

		self.field1 = field1
		self.field2 = field2
		self.group_field = group_field
		self.title = f'{self.field1}/{self.field2} by {self.group_field}'

		self.df = df
		self.full_df = self.df
		if field1 != '' and field2 != '' and group_field != '':
			self.df = self.df[[self.group_field, self.field1, self.field2]]

			# print df
			self.df = self.df.dropna()
			print(self.df)

		self.column_names = self.df.columns.tolist()


	def sepal_scatter(self):
		'''returns plot of sepal scatter'''

		sb.scatterplot(self.df[self.field1], self.df[self.field2],
						 data = self.df, hue=self.df[self.group_field], 
						 palette = 'Set2', edgecolor = 'b', 
						 s = 150, alpha = 0.7)
		plt.title(self.title)
		plt.xlabel(self.field1)
		plt.ylabel(self.field2)
		plt.legend(loc = 'upper right', fontsize = 12)
		plt.show()


	def petal_scatter(self):
		'''return petal scatter'''

		sb.scatterplot(self.field1, self.field2,
					  data = df, hue = self.group_field, palette = 'magma',
					  edgecolor = 'b', s = 150, alpha = 0.7)
		plt.title(self.title)
		plt.xlabel(self.field1)
		plt.ylabel(self.field2)
		plt.legend(loc = 'upper left', fontsize = 12)
		plt.show()


	def heat_map(self):
		'''heat map plot'''
		
		df_corr = self.full_df.corr()
		sb.heatmap(df_corr, cmap = 'Blues', annot = True,
					 xticklabels = df_corr.columns.values,
					 yticklabels = df_corr.columns.values)
		plt.title('Dataframe Heat Map')
		plt.xticks(fontsize = 12)
		plt.yticks(fontsize = 12)
		plt.show()


	def scatter_matrix(self):
		'''scatter matrix'''

		sb.pairplot(data = self.full_df, hue = self.group_field)
		plt.show()

	def distribution_plot(self):
		'''distribution plot'''

		plt.subplot(211)
		sb.kdeplot(self.full_df[self.column_names[0]], color = 'r',
				   shade = True, label = self.column_names[0])
		sb.kdeplot(self.full_df[self.column_names[1]], color = 'b', 
				   shade = True, label = self.column_names[1])

		plt.subplot(212)
		sb.kdeplot(self.full_df[self.column_names[2]], color = 'coral',
				   shade = True, label = self.column_names[2])
		sb.kdeplot(self.full_df[self.column_names[3]], color = 'green',
				   shade = True, label = self.column_names[3])

		plt.show()

# load numpy exoplanets data
numpy_array = np.load('exoplanets_data.npy', allow_pickle=True)

# numpy array to pandas dataframe
df = pd.DataFrame.from_records(numpy_array)

# create normal number of groups by star spectre
# df['spec_type_short'] = df['star_spec_type'].astype(str).str[0]
df = df[['star_age', 'star_mass', 'star_metallicity',
		 'star_radius']]

KNN(df).distribution_plot()