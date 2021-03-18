import pyvo                                          # http://exoplanet.eu/API/
import numpy as np

class ExoplanetsDatabaseSaver:
    '''class save current exoplanets DB in XML ot Numpy array
       class able to return ADQL query result
       class return df of currently largest exoplanets'''

    def __init__(self, query=''):
        '''initializing function'''

        # connecting to the Exoplanets.eu Databases
        self.service = \
                pyvo.dal.TAPService('http://voparis-tap-planeto.obspm.fr/tap')

        # if query passed through class return results
        if query != '':
            self.query = query
            self.in_class_query_returner()


    def in_class_query_returner(self):
        '''return query given to class'''

        self.results = self.service.search(self.query)
        print(self.results)


    def largest_exoplanet(self, top_N):
        '''function return largest opened exoplanet by now'''

        self.query = f"SELECT TOP {top_N} radius, target_name \
                       FROM exoplanet.epn_core \
                       WHERE radius IS NOT NULL \
                       ORDER BY radius DESC"
        self.in_class_query_returner()


    def save_to_xml(self, name):
        '''saves result-set into XML (output file)'''

        vot = self.results.votable
        name = name + '.xml'
        vot.to_xml(name)
        print(f'\nResults successfully saved into {name}!')


    def save_to_numpy(self, name):
        '''saves result-set into numpy array (output file)'''

        np.save(name, self.results.table)
        results = np.load(name + '.npy', allow_pickle=True)
        print(results)



# query directly to class (schema query)
ExoplanetsDatabaseSaver("SELECT column_name \
                         FROM TAP_SCHEMA.columns \
                         WHERE table_name = 'exoplanet.epn_core'")
