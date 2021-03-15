import pyvo


class ExoplanetsBasicInfo:
    '''class returns basic information on exoplanets'''

    def __init__(self, query=''):

        # connecting to the Exoplanets.eu Databases
        self.service = \
                pyvo.dal.TAPService('http://voparis-tap-planeto.obspm.fr/tap')

        # if query passed through class return results
        if query != '':
            self.query = query
            self.in_class_query_returner()

        print(self.service.maxrec)


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
        '''saves result-set into XML'''
        vot = self.results.votable

        name = name + '.xml'
        vot.to_xml(name)
        print(f'\nResults successfully saved into {name}!')



# query directly to class
ExoplanetsBasicInfo("SELECT TOP 10 radius, target_name \
                     FROM exoplanet.epn_core\
                     WHERE radius IS NOT NULL \
                     ORDER BY radius DESC").save_to_xml('top 10 largest')



