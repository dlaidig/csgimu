# SPDX-FileCopyrightText: 2021 Daniel Laidig <laidig@control.tu-berlin.de>
#
# SPDX-License-Identifier: MIT

# cf. https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

project = 'csgimu'
copyright = '2021, CSG'
author = 'CSG'

extensions = [
    'recommonmark',
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinxcontrib.matlab',
    'matplotlib.sphinxext.plot_directive',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

matlab_src_dir = os.path.abspath('../csgimu/matlab')
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
}
html_favicon = 'images/favicon.ico'
# html_static_path = ['_static']
plot_pre_code = '''
import numpy as np
import matplotlib.pyplot as plt
import csgimu
'''
autoclass_content = 'both'
