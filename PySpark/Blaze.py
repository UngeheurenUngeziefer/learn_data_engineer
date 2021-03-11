import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from blaze import Data, by, join, merge
from odo import odo


### Pandas DF ##################################################################
favSongs_pd_df = pd.read_csv('YndxMscFavTracks_Data.csv', delimiter=',')

# first rows of df
favSongs_pd_df.head()

# # show datatypes and stuff
favSongs_pd_df.describe()

# ### Exploring data using Blaze #################################################

# convert Pandas df to Blaze
favSongs_bz_df = Data(favSongs_pd_df)

# retrieve the schema
favSongs_bz_df.schema

# record count and schema
favSongs_bz_df.dshape

# print Blaze content
favSongs_bz_df.data

# extract multiple columns and take the unqiue records
favSongs_bz_df[['album', 'title', 'artist']].distinct

## Transfering data using Odo ##################################################
filepath = ''
filename = 'YndxMscFavTracks_Data'
filesuffix = 'csv'
favSongs_odo_df = Data(f'{filepath}{filename}.{filesuffix}')

print(favSongs_odo_df.count())


