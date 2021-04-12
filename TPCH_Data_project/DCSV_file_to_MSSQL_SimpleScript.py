import pandas as pd
from sqlalchemy import create_engine
import pyodbc

# original csv to pandas dataframe
region = pd.read_csv('tpch_data/h_region.csv', delimiter=',')
print(region)
# to list
region_list = region.values.tolist()
print(region_list)
# without headers
region_list = region_list[0::]


# list of drivers, we need - ODBC Driver 17 for SQL Server
# for driver in pyodbc.drivers():
# 	print(driver)


# define server name and db name
server = 'DESKTOP-SAACP1U\MSSQLSERVER01'
database = 'StagingDB'

# define our connection
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
					   SERVER=' + server + '; \
					   DATABASE=' + database + '; \
					   Trusted_Connection=yes;')

# create connetion cursor
cursor = conn.cursor()


# INSERT query
insert_query = '''INSERT INTO h_region (R_REGIONKEY, R_NAME, R_COMMENT)
				  VALUES(?,?,?)'''

# loop through each row in df
print(region_list)

for row in region_list:
	# values to insert
	
 	values = (tuple(row))
 	print(values)

 	# insert the data into db
 	cursor.execute(insert_query, values)

# commit the insertions
conn.commit()


