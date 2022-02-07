# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:59:04 2022

@author: Claudio
"""

from icoscp.station import station as cpstation
import requests

METAURL = 'https://meta.icos-cp.eu/objects/'


def station(**kwargs):
    """
    Return a list of ICOS Stations

    Parameters
    ----------
    country : STR
        Two letter country code for countries (ISO 3166)
    theme : STR
        Filter station list by ICOS Theme:
            AS = Atmospher
            ES = Ecosystem
            OS = Ocean
    format : STR
        return list in format:
            csv, default
            jason

    Returns
    -------
    stations : STR
        returns the list of ICOS stations, in the format
        requested by the parameter format (see above)

    """
    # assert keywords not case sensitiv
    keys = __case(kwargs.keys())

    # get all stations and do some cleaning
    stations = cpstation.getIdList()
    stations = stations.drop(columns='project')

    # apply filters
    if 'country' in keys:
        stations = stations[stations.country == kwargs['country'].upper()]

    if 'theme' in keys:
        stations = stations[stations.theme == kwargs['theme'].upper()]

    # format output
    if 'format' in keys:

        if kwargs['format'] == 'csv':
            stations = stations.to_csv(index=False)

        if kwargs['format'] == 'json':
            stations.set_index('id', inplace=True)
            stations = stations.to_json()

    else:
        # by default return the csv format
        stations = stations.to_csv(index=False)

    return stations


def pid(**kwargs):
    """
    Return meta data about a digital object from ICOS Carbon Portal

    Parameters
    ----------
    pid : STR
        PJrovide a persistent identification obtained from
        the ICOS Carbn Portla in form of:
        pid = 11676/9GVNGXhqvmn7UUsxSWp-zLyR
        pid = 9GVNGXhqvmn7UUsxSWp-zLyR
        pid = https://meta.icos-cp.eu/objects/9GVNGXhqvmn7UUsxSWp-zLyR


    Returns
    -------
    meta : STR
        returns a json object containing all the meta data about the PID.

    """
    # assert keywords not case sensitiv
    keys = __case(kwargs.keys())

    meta = None

    if 'pid' in keys:
        url = METAURL
        pid_id = str(kwargs['pid'])
        if METAURL in pid_id:
            # we assume a full ICOS URI is provided
            url = pid_id + '/meta.json'

        pid_id = pid_id.split('/')
        if len(pid_id) == 2:
            # handle\pid is provided use pid only
            url = METAURL + pid_id[1] + '/meta.json'

        if len(pid_id) == 1:
            # we assume the pid only is provided
            url = METAURL + pid_id[0] + '/meta.json'

        req = requests.get(url)
        meta = req.text

    return meta


def __case(keys, case='l'):
    '''
    input keys = list
    convert to eiter all lower or uppercase
    case = l = lower
    case = u = upper
    default is lower
    return list of values
    '''
    ret = []
    if case == 'u':
        ret = [a.upper() for a in keys]
    else:
        ret = [a.lower() for a in keys]
    return ret
