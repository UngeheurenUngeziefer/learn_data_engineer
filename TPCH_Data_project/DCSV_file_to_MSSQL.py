import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import os
import sys

def list_of_drivers():
	''' check available drivers on current machine '''
	
	# we need 'ODBC Driver 17 for SQL Server' for SSMS	
	for driver in pyodbc.drivers():
		print(driver)		

# list_of_drivers()


# Before inserting we need to create table in SSMS with name of filename!!!
# Column names function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class DCSV_file_to_MSSQL:
	'''class open dcv/csv file and send it raw to MSSQL Server'''

	def __init__(self, file_location, delimiter, server, database, driver):
		'''initializing method'''
		
		self.file_location = file_location
		self.delimiter = delimiter
		self.server = server
		self.database = database
		self.driver = driver
		self.values = []
		
		try:
			self.file = pd.read_csv(self.file_location, delimiter=self.delimiter)

		# if there no memory split file
		except MemoryError as original_error: 
			print(f'Out of memory: {original_error}\n' + \
				   'Splitting dataframe into 5 parts...\n')
			
			count = 0	 				# keep track of chunks
			chunk_rows = 100000		 	# read 100k rows at a time
			self.file = pd.read_csv(self.file_location, delimiter=self.delimiter,
									 iterator=True, chunksize=chunk_rows)

			for chunk in self.file: 			# for each 100k rows
				if count <= 30:
					outname = 'csv_big_file_1.csv'
				elif count <= 60:
					outname = 'csv_big_file_2.csv'
				elif count <= 90:
					outname = 'csv_big_file_3.csv'
				elif count <= 120:
					outname = 'csv_big_file_4.csv'
				else:
					outname = 'csv_big_file_5.csv'

				# append each output to same csv
				chunk.to_csv(outname, mode='a', index=None, header=None)
				count += 1

			sys.exit(f'Big file splitted!\n' + \
				  	 f'Now add all files (from "csv_big_file_1.csv" to ' + \
				  	 f'"{outname}") to class separately!\n')

		self.file_to_list() 
		self.file_name()
		self.column_names()
		self.questions_generator()
		

		try:
			self.connection()
			print('Successfully INSERTED into DB!')
		except pyodbc.InterfaceError:
			print('You need to create DB!')
		except pyodbc.ProgrammingError:
			print(f'You need to create Table "{self.table_name}" in {self.database}:\n\n')
			print(f'-- {self.table_name}\n' +
				  f'USE {self.database}\n' +
				  f'CREATE TABLE {self.table_name} (\n')
			print(self.columns_datatypes())
			print(')')
			print(f'SELECT * FROM {self.table_name} ')
			print(f'DROP TABLE {self.table_name}')
		
			
	def columns_datatypes(self):
		'''convert pandas datatype to TSQL datatype
		   prints column name and TSQL datatype'''

		for name, dtype in self.file.dtypes.iteritems():
			if dtype == 'int64':
				dtype = 'INT'
			else:
				dtype = 'VARCHAR(255)'
			print(name, dtype, ',')
		return ''
		

	def file_to_list(self):
		'''convert pandas df to list without headers'''
		
		# pandas df to list
		self.as_list = self.file.values.tolist()

		# without headers
		self.as_list = self.as_list[0::]
		return self.as_list


	def column_names(self):
		'''return column names and num of columns of raw file'''
		# df to list

		if 'csv_big_file_' in self.table_name: 
			self.table_column_names = 'L_ORDERKEY, L_PARTKEY, L_SUPPKEY, L_LINENUMBER, L_QUANTITY, L_EXTENDEDPRICE, L_DISCOUNT, L_TAX, L_RETURNFLAG, L_LINESTATUS, L_SHIPDATE, L_COMMITDATE, L_RECEIPTDATE, L_SHIPINSTRUCT, L_SHIPMODE, L_COMMENT'
			self.num_of_columns = 16
		else:
			self.column_names = list(self.file.columns)

			# list to comma-separated string
			self.column_names = ','.join(self.column_names)

			# number of columns in table
			self.num_of_columns = len(self.file.columns)

		# return column names and number of names
		return self.column_names, self.num_of_columns


	def questions_generator(self):
		'''generate question marks for VALUES for every column'''

		rawlist = []

		for i in range(self.num_of_columns):
			rawlist.append('?')

		self.questions = ','.join(rawlist)
		return self.questions


	def file_name(self):
		'''return filename from path, and tablename'''

		self.filename = os.path.basename(self.file_location)
		self.table_name = self.filename[0:-4]
		
		if 'csv_big_file_' in self.table_name: 
			self.table_name = 'h_lineitem'
		else:
			pass
		return self.filename, self.table_name

	
	def connection(self):
		'''establish connection to MSSQL and INSERT values from D/CSV'''
		
		# define connection to MSSQL
		conn = pyodbc.connect('DRIVER={' + self.driver + '}; \
							   SERVER=' + self.server + '; \
							   DATABASE=' + self.database + '; \
							   Trusted_Connection=yes;')

		# create connetion cursor
		cursor = conn.cursor()

		# INSERT query
		insert_query = f'INSERT INTO {self.table_name} ({self.column_names}) VALUES({self.questions})'


		# convert list of lists to list of tuples
		nested_lst_of_tuples = [tuple(row) for row in self.as_list]
		
		for row in nested_lst_of_tuples:

			# insert the data into db
			cursor.execute(insert_query, row)

		# # commit the insertions
		conn.commit()

# file_location, delimiter, server, database, driver
input_file = \
 DCSV_file_to_MSSQL('tpch_data/h_region.csv', ',',
  'DESKTOP-SAACP1U\MSSQLSERVER01', 'StagingDB', 'ODBC Driver 17 for SQL Server')

# tpch_data/
# File Name 		 | Size	   | Rows	| Execution Time	|
#############################################################
# h_region.csv 		 | 1 KB	   | 		| fast				|
# h_nation.dsv 		 | 3 KB    |		| fast				|
# h_supplier.dsv  	 | 3 MB    | 20k 	| 10 sec 			|
# h_customer.dsv 	 | 43 MB   | 300k	| 1 min 16 sec 		|
# h_part.dsv 		 | 57 MB   | 400k	| 1 min 17 sec 		|
# h_partsupp.dsv 	 | 114 MB  | 1.6M	| 9 min 50 sec 		|
# h_order.dsv 		 | 360 MB  | 3.0M 	| 11 min 			|
# h_lineitem.dsv 	 | 1.7 GB  |

# /
# Splitted 			 | Size	   | Rows	| Execution Time	|
#############################################################
# csv_big_file_1.csv | 440 MB  | 3.2M   | 18 min 			|
# csv_big_file_2.csv | 425 MB  | 3.0M   | 18 min 			|
# csv_big_file_3.csv | 425 MB  | 3.0M   | 11 min 			|
# csv_big_file_4.csv | 410 MB  | 2.9M   | 11 min 			|

# 11 996 782 - overall rows
