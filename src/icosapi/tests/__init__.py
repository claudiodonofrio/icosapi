"""
import logging

import connexion
from flask_testing import TestCase


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../icosapi/spec/')        
        app.add_api('cp_test_api.yaml', pythonic_params=True)
        return app.app
"""