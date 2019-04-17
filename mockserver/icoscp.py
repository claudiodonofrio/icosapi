import connexion
import sparqls
import runsparql


def get_data(**param):

    out = 'not implemented yet, get the data'
    out += str(param)
    return out


def get_download(**param):

    out = 'not implemented yet, get the data'
    out += str(param)
    return out


def get_stations(**param):
    # return a list of known collections
    c = runsparql.RunSparql()
    c.format = 'csv'
    if not (len(param)):
        c.query = sparqls.stations_with_pi()
    return c.run()


def get_collections(**param):
    if not (len(param)):
        # return a list of known collections
        c = runsparql.RunSparql()
        c.query = sparqls.collections()
        c.format = 'csv'
        return c.run()
    else:
        return(param)


def get_provisional_stations(**param):
    # return a list of known collections
    c = runsparql.RunSparql()
    c.query = sparqls.stations_with_pi()
    c.format = 'csv'
    return c.run()


if __name__ == '__main__':
    # create the flask web app
    app = connexion.FlaskApp(__name__, host='127.0.0.1', port=9090, specification_dir='../')
    app.add_api('icos-cp-api.yaml', arguments={'title': 'Carbon Portal API example'})
    app.run()
