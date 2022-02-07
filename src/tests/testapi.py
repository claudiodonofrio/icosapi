# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:14:49 2022
@author: Claudio
"""

import pytest
import requests

URL = 'http://127.0.0.1:8080/api/'


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
