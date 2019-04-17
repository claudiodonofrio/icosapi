# -*- coding: utf-8 -*-

"""
    This file contains an assembly of common sparql queries.
    Each function returns a valid sparql query as string.
    @param Input: you can provide a "limit" as how many 
    results are returned. By default it is set to 0 (zero)
    returning all results from the sparql endpoint
"""

__version__= "0.1.0"

# --------------------------------------------------------------------
# create helper functions
# --------------------------------------------------------------------


def _check_limit(limit):

    try:
        limit = int(limit)
        if limit > 0:
            return 'limit ' + str(limit)
        else:
            return ''
    except ValueError:
        return ''

# --------------------------------------------------------------------
# sparql query functions        
# -----------------------------------------------------------------------------


def etc_co2_level2(limit=0):

    """ ICOS Atmospheric CO2 level 2 data objects """

    query = """
        prefix cpmeta: <http://meta.icos-cp.eu/ontologies/cpmeta/>
        prefix prov: <http://www.w3.org/ns/prov#>
        select ?dobj ?spec ?fileName ?size ?submTime ?timeStart ?timeEnd
        FROM <http://meta.icos-cp.eu/resources/atmprodcsv/>
        where {
                BIND(<http://meta.icos-cp.eu/resources/cpmeta/atcCo2L2DataObject> AS ?spec)
                ?dobj cpmeta:hasObjectSpec ?spec .
                FILTER NOT EXISTS {[] cpmeta:isNextVersionOf ?dobj}
                ?dobj cpmeta:hasSizeInBytes ?size .
                ?dobj cpmeta:hasName ?fileName .
                ?dobj cpmeta:wasSubmittedBy [
                prov:endedAtTime ?submTime ;
                prov:wasAssociatedWith ?submitter
                ] .
                ?dobj cpmeta:hasStartTime | (cpmeta:wasAcquiredBy / prov:startedAtTime) ?timeStart .
                ?dobj cpmeta:hasEndTime | (cpmeta:wasAcquiredBy / prov:endedAtTime) ?timeEnd .
        }
        %s
        """ % _check_limit(limit)

    return query
# -----------------------------------------------------------------------------


def collections(limit=0):
    """ Return all known collections """

    query = """
            prefix cpmeta: <http://meta.icos-cp.eu/ontologies/cpmeta/>
            prefix dcterms: <http://purl.org/dc/terms/>
            select * where{
            ?coll a cpmeta:Collection .
            OPTIONAL{?coll cpmeta:hasDoi ?doi}
            ?coll dcterms:title ?title .
            }
            %s
            """ % _check_limit(limit)

    return query

# -----------------------------------------------------------------------------


def stations_with_pi(limit = 0):
    """
        Define SPARQL query to get a list of ICOS stations with PI and email.
        As per writing, (April 2019, the list is pulled from the provisional
        data, labeling process)
    """

    query = """
            prefix st: <http://meta.icos-cp.eu/ontologies/stationentry/>
            select distinct ?stationTheme ?stationId ?stationName ?firstName ?lastName ?email
            from <http://meta.icos-cp.eu/resources/stationentry/>
            where{
                ?s st:hasShortName ?stationId .
                ?s st:hasLongName ?stationName .
                ?s st:hasPi ?pi .
                ?pi st:hasFirstName ?firstName .
                ?pi st:hasLastName ?lastName .
                ?pi st:hasEmail ?email .
                ?s a ?stationClass .
                BIND (replace(str(?stationClass), "http://meta.icos-cp.eu/ontologies/stationentry/", "") AS ?stationTheme )
            }            
            %s
        """ % _check_limit(limit)

    return query
# -----------------------------------------------------------------------------
