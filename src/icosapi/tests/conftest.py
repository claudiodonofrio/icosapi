# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:44:08 2022

@author: Claudio
"""

import os
import pytest
from icosapi.run import create_app


@pytest.fixture(scope="session")
def app():
    abs_file_path = os.path.abspath(os.path.dirname(__file__))
    openapi_path = os.path.join(abs_file_path, "../", "icosapi", "spec")
    os.environ["SPEC_PATH"] = openapi_path

    app = create_app()
    return app
