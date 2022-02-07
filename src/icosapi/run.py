# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:45:59 2022

@author: Claudio
"""

import os
import connexion


def create_app():
    if "API_PATH" in os.environ:
        openapi_path = os.environ["API_PATH"]
    else:
        abs_file_path = os.path.abspath(os.path.dirname(__file__))
        openapi_path = os.path.join(abs_file_path, "spec")
    app = connexion.FlaskApp(
        __name__,
        specification_dir=openapi_path,
        options={"swagger_ui": False, "serve_spec": False},
    )
    app.add_api("cp_test_api.yaml", strict_validation=True)
    flask_app = app.app

    return flask_app
