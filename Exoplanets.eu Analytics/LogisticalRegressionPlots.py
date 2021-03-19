import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


numpy_array = np.load('exoplanets_data.npy', allow_pickle=True)
df = pd.DataFrame.from_records(numpy_array)

# mass greater than Mercury (tiniest) and greater than 10 Earthes
# create a list of our conditions
conditions = [
    (df['mass'] >= 0.00017325) & (df['mass'] <= 0.0315),	# Earth like
    (df['mass'] > 0.0315),									# gigantic
    (df['mass'] < 0.00017325)								# less than Mercury
    ]

# create a list of the values we want to assign for each condition
values = [0, 1, 2]

# create a new column and use np.select to assign values to it using our lists as arguments
df['planet_type'] = np.select(conditions, values)

# where mass exist
df = df[df['mass'].notna()]

# display updated DataFrame
# print(df[['planet_type', 'target_name']].head(50))

# drop 2 values = where mass less than tiniest planet (Mercury)
df = df[df['planet_type'] != 2]
# statistical distribution
print(df['planet_type'].value_counts())

# sns.countplot(x='planet_type', data=df, palette='hls')
# plt.ylabel('Number of exoplanets')
# plt.xlabel('Exoplanet type')
# plt.title('Distribution of exoplanets by planet type')
# plt.show()

# percentage distribution
count_gigantic = len(df[df['planet_type']==1])
count_earthlike = len(df[df['planet_type']==0])
percentage_of_gig = count_gigantic/(count_gigantic + count_earthlike) * 100
percentage_of_erl = count_earthlike/(count_gigantic + count_earthlike) * 100
print("percentage of Giant is", percentage_of_gig)
print("percentage of Earth-like is", percentage_of_erl)

# observation
pd.options.display.max_columns = None
# print(df.groupby('planet_type').mean())

# The average semi major axis of Gigantic planets is higher than that of the Earth like planets
# Earth like planets have greater albedo than Giant planets
# Distance to stars with Giant planets greater than with Earth planets
# Star age greater for Earth like planets and less for Giant planets

# print(df.groupby('star_mass').mean())

# pd.crosstab(df.star_age.round(0),df.planet_type).plot(kind='bar')
# plt.title('Planet type per Star Age')
# plt.xlabel('Star Age')
# plt.ylabel('Planet Type')
# plt.show()


# table = pd.crosstab(df.albedo, df.planet_type)
# table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
# plt.title('Stacked Bar Chart of Albedo vs Planet Type')
# plt.xlabel('Albedo')
# plt.ylabel('Planet Type')
# plt.show()


# pd.crosstab(df.radius.round(0), df.planet_type).plot(kind='bar')
# plt.title('Radius and Planet Type')
# plt.xlabel('Radius')
# plt.ylabel('Planet Type')
# plt.show()


# df.star_age.hist()
# plt.title('Histogram of Star Age')
# plt.xlabel('Star Age')
# plt.ylabel('Frequency')
# plt.show()