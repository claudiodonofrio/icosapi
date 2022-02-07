# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:51:41 2022

@author: Claudio
"""

import connexion

# app = connexion.FlaskApp(__name__, specification_dir='spec/')
# app.add_api('cp_test_api.yaml')
# app.run(host='127.0.0.1', port=8080)


def server_app():
    app = connexion.FlaskApp(__name__, specification_dir='./spec/')
    app.add_api('cp_test_api.yaml')
    return


if __name__ == '__main__':
    server_app().run(host='127.0.0.1', port=8080)
