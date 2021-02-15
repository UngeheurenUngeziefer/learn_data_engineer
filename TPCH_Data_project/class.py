import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import os


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

	def __init__(self, file_location, delimeter, server, database, driver):
		'''initializing method'''
		
		self.file_location = file_location
		self.delimeter = delimeter
		self.server = server
		self.database = database
		self.driver = driver
		self.as_list = []
		self.values = []
		
		self.file = pd.read_csv(self.file_location, delimiter=self.delimeter)
		self.file_to_list() 
		self.column_names()
		self.questions_generator()
		self.file_name()
		self.connection()


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


		# loop through each row in list of rows of our file
		for row in self.as_list:

			# adding every row to list
			self.values.append(row)


		for row in self.values:

			values = (tuple(row))
			
			# insert the data into db
			cursor.execute(insert_query, values)

		# commit the insertions
		conn.commit()
		

# instance of class
# file_location, delimeter, server, database, driver
input_file = \
 DCSV_file_to_MSSQL('tpch_data/h_region.csv', ',',
  'DESKTOP-SAACP1U\MSSQLSERVER01', 'TestSQL', 'ODBC Driver 17 for SQL Server')
