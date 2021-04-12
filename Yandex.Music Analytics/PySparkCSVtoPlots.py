import pyspark
import pandas as pd
from datetime import datetime, date
from pyspark.sql import SQLContext, Row, SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, count, countDistinct 
import plotly.express as px


class PySparkCSVtoPlots:
	'''class import data from csv
	   return original datatypes and schema
	   apply correct datatypes for Spark table
	   show unqiue values of every given column
	   visualize Spark DataFrame'''


	def __init__(self, csv, table_name, datatypes={}, sql_query=''):
		'''initialize Spark Session'''
		
		# spark session
		spark = SparkSession.builder.getOrCreate()
		sc = spark.sparkContext
		self.sqlContext = SQLContext(sc)

		# use df from csv, use 1st line as headers
		self.df = self.sqlContext.read.csv(csv, header=True)

		# correct datatypes if given
		self.datatypes = datatypes
		self.correct_datatypes(self.datatypes)
		
		# register our df as table
		self.table_name = table_name
		self.df.registerTempTable(self.table_name)
		self.sql_query = sql_query
		if sql_query != '':
			self.sparkSQLquery(self.sql_query)


	def __str__(self):
		'''print first rows and current schema'''

		self.df.show()
		return str(self.df.printSchema())


	def sparkSQLquery(self, sql_query, show_plan=False):
		'''process query to the table and print result'''
		
		self.df_selection = self.sqlContext.sql(sql_query)
		self.df_selection.show()
		
		if show_plan:
			df_selection.explain(extended = True)


	def correct_datatypes(self, datatypes):
		'''change datatypes to correct ones
		   datatypes - dictationary'''

		# key, mydictionary[key]
		for dtype in datatypes:
			self.df = \
			self.df.withColumn(dtype, col(dtype).cast(datatypes[dtype]))


	def number_of_unique_values(self, columns):
		'''return number of unqiue values in every column
		   columns - list'''
		expression = [countDistinct(c).alias(c) for c in self.df.columns]
		self.df.select(*expression).show()


	def scatter_plot(self, title, x_series, y_series):
		'''create scatter plot
		   title - string
		   x_series - spark df column
		   y_series - spark df column'''

		fig = px.scatter(self.df_selection.toPandas(), x=x_series, y=y_series, 
			color=x_series, title=title)
		fig.show()
	

	def bar_chart(self, title, x_series, y_series):
		'''create bar chart
		   title - string
		   x_series - spark df column
		   y_series - spark df column'''

		fig = px.bar(self.df_selection.toPandas().dropna(), title=title, \
					 color=y_series, y=y_series, x=x_series, text=y_series)
		fig.show()

	
	def pie_chart(self, title, x_series, y_series):
		'''create pie chart
		   title - string
		   x_series - spark df column
		   y_series - spark df column'''

		fig = px.pie(self.df_selection.toPandas(), values=x_series, \
					names=y_series, title=title)
		fig.show()


	def line_chart(self, title, x_series, y_series):
		'''create line chart
		   title - string
		   x_series - spark df column
		   y_series - spark df column'''

		fig = px.line(self.df_selection.toPandas(), x=x_series, \
						 y=y_series, title=title)
		fig.show()


# print first 20 rows and original CSV schema
# print(SparkSQLDataFrameCSVAnalysis('YndxMscFavTracks_Data.csv', 'FavoriteSongs'))

fav_songs_datatypes = {'song_id': IntegerType(), \
			  		   'release_date': TimestampType(),
			  		   'year': IntegerType(),
			  		   'duration': DecimalType(3,2)}

sql_query = 'SELECT COUNT(song_id) as song_id, duration \
		 	 FROM FavoriteSongs \
		 	 GROUP BY duration \
		 	 ORDER BY COUNT(song_id) DESC'

columns_list = ['song_id', 'artist', 'title', 'album', 'major', 'label',\
				'genre', 'release_date', 'year', 'duration', \
				'content_warning', 'song_type']

# Set table name and correct datatypes
# Querying CSV with PySpark
# SparkSQLDataFrameCSVAnalysis('YndxMscFavTracks_Data.csv', 'FavoriteSongs', \
# 							 datatypes = fav_songs_datatypes) \
# 							.sparkSQLquery(sql_query, \
# 										 	show_plan = False)

# Unique values of every column
# SparkSQLDataFrameCSVAnalysis('YndxMscFavTracks_Data.csv', 'FavoriteSongs', \
# 							 datatypes=fav_songs_datatypes)
# 							.number_of_unique_values(columns_list)

# # Plot #1
# SparkSQLDataFrameCSVAnalysis('YndxMscFavTracks_Data.csv', 'FavoriteSongs', \
#  							 datatypes=fav_songs_datatypes).scatter_plot(
#  							 'Distribution of Favorite Songs by Release Date',\
#  							 'release_date', 'title')
