# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:14:49 2022
@author: Claudio
"""

import pytest
import connexion
from icosapi import cp
from connexion import RestyResolver


flask_app = connexion.FlaskApp(__name__)
flask_app.add_api('../spec/cp_test_api.yaml', resolver=RestyResolver('api'))



@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200


"""



@pytest.fixture(scope='module')
def app():
    ''' this is supposed to mock the server ,but could not make it run..'''
    # with server.test_client() as client:
    #   yield client


@pytest.mark.parametrize('test_input,expected', [
   ('station?', 200),
   ('/pid?pid=9GVNGXhqvmn7UUsxSWp-zLyR', 200),
   ('/pid?', 400),
   ])
def test_api_response(test_input, expected):
    ''' test response of all root path '''
    response = requests.get(f"{URL}{test_input}")
    assert response.status_code == expected
"""