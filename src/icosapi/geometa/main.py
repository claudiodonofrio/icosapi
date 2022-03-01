# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 22:25:45 2022

@author: Claudio
Within Lund Uni you can access the ISO standards at
https://libguides.lub.lu.se/c.php?g=297958&p=4654438

the geometa documetnation is at
https://geopython.github.io/pygeometa/
"""

import yaml
import requests


# choose ISO 19139 output schema
from pygeometa.schemas.iso19139 import ISO19139OutputSchema as iso
from pygeometa.schemas.iso19139_2 import ISO19139_2OutputSchema as iso2
from pygeometa.schemas.iso19139_icos import ISO19139ICOSOutputSchema as iso_icos

MCF = 'dobj.yml'

def pid_meta(pid):
    '''
    dowload meta data for the PID, return a dictionary

    Parameters
    ----------
    pid : STR
        provide the icos handle (pid) for a data object, allowd formats are:

            https://meta.icos-cp.eu/objects/M8STRfcQfU4Yj7Uy0snHvlve
            11676/M8STRfcQfU4Yj7Uy0snHvlve
            M8STRfcQfU4Yj7Uy0snHvlve
    Returns
    -------
    dict.

    '''
    pid = pid.split('/')[-1]
    url = f"https://meta.icos-cp.eu/objects/{pid}/meta.json"
    metadata = requests.get(url).json()
    metadata['self'] = url.rsplit('/',1)[0]
    return metadata


def meta_dobj(metaicos):
    '''
    replace information in dobj.yml with information from meta data
    collected from the PIDicos
    this is essentially the mapping from ICOS CP to the MCF file, which then
    can be trasformed into:
    iso19139,iso19139-2,iso19139-hnap,oarec-record,stac-item,dcat,wmo-cmp,wmo-wigos
    The mcf (.yaml) file has the following sections
    mcf
    metadata
    spatial
    identification
    content_info
    acquisition
    contact
    distribution
    dataquality

    Parameters
    ----------
    pid : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    # get metadata for the datastet


    # read the yaml template
    mcf ='dobj.yml'
    with open(mcf, 'r', encoding='utf8') as file:
        meta = yaml.load(file, Loader=yaml.FullLoader)

    # [metadata]
    meta['metadata']['identifier'] = metaicos['self']
    meta['metadata']['dataseturi'] = metaicos['specification']['self']['uri']

    # [spatial]
    # for ETC and ATC it is most likely to stay with the default values with
    # vector and point, but for OTC and Level3 Datasets this might change

    # [identification]
    meta['identification']['doi'] = metaicos['pid']
    meta['identification']['title']['en'] = metaicos['references']['title']
    # abstract is mandatory, but not available. duplicate title
    meta['identification']['abstract']['en'] = metaicos['references']['title']
    creation = metaicos['specificInfo']['productionInfo']['dateTime']
    meta['identification']['dates']['creation'] = creation


    #create bbox
    lat = float(metaicos['specificInfo']['acquisition']['station']['location']['lat'])
    lon = float(metaicos['specificInfo']['acquisition']['station']['location']['lon'])
    meta['identification']['extents']['spatial'][0]['bbox'] = [lon,lon,lat,lat]

    # CRS is by default set to WGS84 = 4326
    # meta['identification']['extents']['spatial']['crs'] = xxxx

    begin = metaicos['specificInfo']['acquisition']['interval']['start']
    end = metaicos['specificInfo']['acquisition']['interval']['stop']
    meta['identification']['extents']['temporal'][0]['begin'] = begin
    meta['identification']['extents']['temporal'][0]['end'] = end
    meta['identification']['url'] = metaicos['accessUrl']

    # [acquisition]
    stationid = metaicos['specificInfo']['acquisition']['station']['id']
    description = metaicos['specificInfo']['acquisition']['station']['org']['self']['uri']
    meta['acquisition']['platforms'][0]['identifier'] = stationid
    meta['acquisition']['platforms'][0]['description'] = description

    # [distribution]

    meta['distribution']['icos']['url'] = metaicos['specification']['self']['uri']
    meta['distribution']['icos']['description']['en'] = metaicos['references']['title']

    return meta

def main(pid, fmt='iso19139'):
    '''
    main function to create an xml metdata output for a given PID

    Parameters
    ----------
    pid : STR
        ICOS persistent identifier for a data object.
    fmt : STR, optional
        choose between iso19139 or iso19139. The default is 'iso19139'.

    Returns
    -------
    xml : STR
        Metadata for digital object conforming to ISO19139 standard.

    '''
    meta = meta_dobj(pid_meta(pid))
    if fmt.lower() == 'iso19139':
        xml = iso().write(meta)
    if fmt.lower() == 'iso19139_2':
        xml = iso2().write(meta)
    if fmt.lower() == 'iso_icos':
        xml = iso_icos().write(meta)
        
    return xml

if __name__ == '__main__':
    PID = 'M8STRfcQfU4Yj7Uy0snHvlve'
    
    #PID = '11676/WREaChiXhVOYRtgEvmayh6qy'
    icos = main(PID, fmt='iso_icos')
    ficos = f'icos_{PID}.xml'
    with open(ficos, 'w') as f:
        f.write(icos)
    '''
    iso19139 = main(PID)    
    file1 = f'icos_iso19139_{PID}.xml'
    with open(file1, 'w') as f:
        f.write(iso19139)
    
    iso19139_2 = main(PID, fmt='iso19139_2')
    file2 = f'icos_iso19139_2_{PID}.xml'
    with open(file2, 'w') as f:
        f.write(iso19139_2)
    '''