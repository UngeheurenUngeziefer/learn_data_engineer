import pandas as pd
from sqlalchemy import create_engine
import pyodbc

# original csv to pandas dataframe
region = pd.read_csv('tpch_data/h_region.csv', delimiter=',')	

# pandas dataframe to sql database
engine = create_engine('mssql://sewer:@localhost/h_region', echo=False)

region.to_sql(name='h_region', con=engine, if_exists='replace')






# server = 'DESKTOP-SAACP1U/MSSQLSERVER01' 
# database = 'TestSQL' 
# username = 'DESKTOP-SAACP1U/sewer' 
# password = '' 
# PORT='1433'
# con = pyodbc.connect(r'DRIVER={SQL Server};SERVER='+server+'\\;DATABASE='+database+';UID='+username+';PWD='+ password+';PORT='+PORT)
# engine.execute("SELECT * FROM h_region").fetchall()
