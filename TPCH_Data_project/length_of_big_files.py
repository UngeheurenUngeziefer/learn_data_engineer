import pandas as pd

chunksize = 1000000
length_of_file = 0
for chunk in pd.read_csv('tpch_data/h_lineitem.dsv', delimiter='|', chunksize=chunksize):
	length_of_file += len(chunk)

print(length_of_file)