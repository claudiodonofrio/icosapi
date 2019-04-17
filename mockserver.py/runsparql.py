# -*- coding: utf-8 -*-

"""
    This file contains a class RunSparql()
    which handles the communication with the ICOS Sparql Endpoint.
"""

# import modules
# ----------------------------------------------------------
import requests
import pandas as pd
import textile


__credit__ = ['Claudio DOnofrio', '']
__author__ = 'ICOS Carbon Portal'
__contact__ = 'https://www.icos-cp.eu'
__email__ = 'info at icos-cp.eu'
__license__ = 'CCBY 4.0'
__version__ = '0.1.0'
__status__ = 'development'


class RunSparql():
    """
        Class to send a sparql query to the icos endpoint and get
        formated output back.
        :param sparql_query, string, valid query
        :param output_format, define format of returned object ['json', 'csv', 'array', 'dict', 'pandas']
        :return False, if query is not successful otherwise output_format(results)
    """

    def __init__(self, sparql_query='', output_format='txt'):

        self.format = output_format
        self.query = sparql_query
        self.__result = False

    @property
    def format(self):
        """ contains the output format for the results from the ICOS sqparql endpoint"""
        return self.__format

    @format.setter
    def format(self, fmt):
        """
            You can set the format of the results returned after running the query.
            Allowed formats are:
            - 'json' (default), string
            - 'csv' a string object with comma separated values, where the the first row contains the column names
            Python specific formats:
            - 'dict' a python dict representing the json object
            - 'pandas' a pandas table with column names
            - 'list'
            - 'array' returns TWO python arrays, the first with the headers, the second with the values.
        """
        allowed = ['json', 'csv', 'dict', 'pandas', 'array', 'html']
        try:
            fmt = str(fmt)
        except TypeError:
            return 0

        if fmt.lower() in allowed:
            self.__format = fmt.lower()
        else:
            self.__format = 'json'

    @property
    def query(self):
        """ Import a sparql query. No validation is performed. """
        return self.__query

    @query.setter
    def query(self, query):

        try:
            query = str(query)
        except TypeError:
            return 0
        self.__query = str(query)

    # ------------------------------------------------------------------------
    def data(self):
        return self.__result

    # ------------------------------------------------------------------------
    def run(self):
        """
            This functions queries the ICOS sparql endpoint queryString.
            By default the returned object is the raw "json" object.
        """
        # check if query is set
        if not len(self.__query):
            print('no query found')
            return

        url = 'https://meta.icos-cp.eu/sparql'

        r = requests.get(url, params={'query': self.__query})
        if not r.ok:
            return r.ok, r.reason

        # now check what format we should return.
        # either set the __result directly, or call a transform
        # function which sets the __result.

        if self.format == 'json':
            self.__result = r.text
        if self.__format == 'dict':
            self.__result = r.json()
        if self.__format == 'csv':
            self.__result = self.__to_csv(r.json())
        if self.__format == 'pandas':
            self.__result = self.__to_pandas(r.json())
        if self.__format == 'array':
            self.__result = self.__to_array(r.json())
        if self.__format == 'html':
            self.__result = self.__to_html(r.json())

        return self.__result

    # ------------------------------------------------------------------------
    def __to_array(self, data):

        # convert the the result into two arrays
        # colName, colData
        colname = data['head']['vars']
        coldata = []

        for row in data['results']['bindings']:
            item = []
            for c in colname:
                item.append(row.get(c, {}).get('value'))
            coldata.append(item)
        return colname, coldata

    # ------------------------------------------------------------------------
    def __to_csv(self, data):
        colname, coldata = self.__to_array(data)

        # add the header line
        csvstring = ','.join(colname) + '\n'
        for row in coldata:
            csvstring += ','.join(row) + '\n'

        return csvstring

    # ------------------------------------------------------------------------
    def __to_pandas(self, data):

        colname, coldata = self.__to_array(data)

        return pd.DataFrame(coldata, columns=colname)

        # ------------------------------------------------------------------------
    def __to_html(self, data):
        colname, coldata = self.__to_array(data)
        out = pd.DataFrame(coldata, columns=colname).to_html()
        return textile.textile(out)













