import pyspark
from pyspark.sql import SQLContext, Row, SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql.types import *
from pyspark.sql.functions import col


class SparkSQLDataFrameCSVAnalysis:
	'''class analyze data from csv
	   return original datatypes and schema'''


	def __init__(self, csv, output_table_name, datatypes={}):
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
		self.df.registerTempTable(output_table_name)


	def __str__(self):
		'''print first rows and current schema'''

		self.df.show()
		return str(self.df.printSchema())


	def sparkSQLquery(self, sql_query, show_plan=False):
		'''process query to the table and print result'''
		
		df_selection = self.sqlContext.sql(sql_query)
		df_selection.show()
		
		if show_plan:
			df_selection.explain(extended = True)


	def correct_datatypes(self, datatypes):
		'''change datatypes to correct ones'''
		# key, mydictionary[key]
		for dtype in datatypes:
			self.df = \
			self.df.withColumn(dtype, col(dtype).cast(datatypes[dtype]))

	



# print first 20 rows and original CSV schema
# print(SparkSQLDataFrameCSVAnalysis('YndxMscFavTracks_Data.csv', 'FavoriteSongs'))


# Set table name and correct datatypes     # Querying CSV with PySpark
# SparkSQLDataFrameCSVAnalysis('YndxMscFavTracks_Data.csv', 'FavoriteSongs', \
# 							 datatypes={'song_id': IntegerType(), \
# 							  			'release_date': TimestampType(),
# 							  			'year': IntegerType(),
# 							  			'duration': DecimalType(3,2)}) \
# 							.sparkSQLquery('SELECT * \
# 										 	FROM FavoriteSongs \
# 										 	WHERE YEAR(release_date) = 2021\
# 										 	ORDER BY duration DESC', \
# 										 	show_plan = False)

SparkSQLDataFrameCSVAnalysis('YndxMscFavTracks_Data.csv', 'FavoriteSongs', \
							 datatypes={'song_id': IntegerType(), \
							  			'release_date': TimestampType(),
							  			'year': IntegerType(),
							  			'duration': DecimalType(3,2)})









