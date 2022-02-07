# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:14:49 2022
@author: Claudio
"""


import csv
import json
import pytest
import pandas as pd
import icosapi.cp


@pytest.mark.parametrize('test_input,expected', [
    ('gibberish', 'The requested resource could not be found.'),
    (123456, 'The requested resource could not be found.'),
    ('9GVNGXhqvmn7UUsxSWp-zLyR', '9GVNGXhqvmn7UUsxSWp-zLyR'),
    ('11676/9GVNGXhqvmn7UUsxSWp-zLyR', '9GVNGXhqvmn7UUsxSWp-zLyR'),
    ('https://meta.icos-cp.eu/objects/9GVNGXhqvmn7UUsxSWp-zLyR', '9GVNGXhqvmn7UUsxSWp-zLyR')
    ])
def test_pidinput(test_input, expected):
    ''' test different formats of pid. We accept PID, HANDLE/PID, URI '''
    meta = icosapi.cp.pid(pid=test_input)
    assert expected in meta


def test_station_csv():
    ''' test different station parameters '''
    stn = icosapi.cp.station()
    assert isinstance(stn, str)

    lines = stn.splitlines()
    lines = list(csv.reader(lines))
    try:
        # convert csv to pandas dataframe,
        # and let pandas do all the work
        dataframe = pd.DataFrame(lines[1:], columns=lines[0])
    except Exception as e_info:
        assert False, f"convert csv raised an exception {e_info}"
    assert len(dataframe.columns) == 8


def test_station_json():
    ''' test different station parameters '''
    stn = icosapi.cp.station(format='json')
    assert isinstance(stn, str)
    try:
        # convert string to json object (dict)
        stn = json.loads(stn)
    except Exception as e_info:
        assert False, f"convert json raised an exception {e_info}"

    # 7 columns/keys should be present
    assert len(stn) == 7


def test_station_country():
    ''' check country parameter'''
    stn = icosapi.cp.station(country='ch')
    assert isinstance(stn, str)
    lines = stn.splitlines()
    assert len(lines) >= 3


@pytest.mark.parametrize('test_input,expected', [
    ('es', 3),
    ('os', 3),
    ('as', 3),
    ])
def test_station_theme(test_input, expected):
    ''' check theme parameter'''
    stn = icosapi.cp.station(theme=test_input)
    assert isinstance(stn, str)
    lines = stn.splitlines()
    assert len(lines) >= expected
