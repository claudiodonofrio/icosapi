# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 13:30:25 2022

@author: Claudio
"""

import pytest
import os 

absolut = os.path.dirname(os.path.realpath(__file__))
f = os.path.join(absolut, 'src/test/module_test.py')

modules = pytest.main(["-x", f])
#server = pytest.main(["-x", "src/test/api_test.py"])