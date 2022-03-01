#!/usr/bin/env python3
"""
Created on Tue Jan 25 21:51:41 2022

@author: Claudio
"""

import connexion


def main():
    ''' start the webservice'''
    app = connexion.FlaskApp(__name__, specification_dir='./spec/',debug=True)
    app.add_api('cp_test_api.yaml',
                arguments={'title': 'cp_test_api'},
                pythonic_params=True)

    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
