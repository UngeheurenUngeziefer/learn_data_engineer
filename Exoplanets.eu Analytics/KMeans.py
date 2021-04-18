import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numpy_array = np.load('Data_Engineer\Exoplanets.eu Analytics' + \
                                    '\exoplanets_data.npy', allow_pickle=True)
df = pd.DataFrame.from_records(numpy_array)

pd.set_option('display.max_columns', None)
df.head()

columns = ['granule_uid', 'mass', 'semi_major_axis']

mass_sma_df = df[['mass', 'semi_major_axis']]
mass_sma_df.dropna()

x = mass_sma_df['mass']
y = mass_sma_df['semi_major_axis']
s = mass_sma_df['mass']

plt.xlabel('Mass')
plt.ylabel('Semi Major Axis')

# plt.scatter(x, y, s=s)
# plt.show()

