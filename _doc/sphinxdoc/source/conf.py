# -*- coding: utf-8 -*-
import sys
import os
import alabaster
from pyquickhelper.helpgen.default_conf import set_sphinx_variables


sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
local_template = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "phdoc_templates")

set_sphinx_variables(__file__, "wrapclib", "Xavier Dupré", 2023,
                     "alabaster", alabaster.get_path(),
                     locals(), extlinks=dict(issue=(
                         'https://github.com/sdpython/wrapclib/issues/%s',
                         'issue %s')),
                     title="wrapclib", book=True)

blog_root = "http://www.xavierdupre.fr/app/wrapclib/helpsphinx/"

html_css_files = ['my-styles.css']

html_logo = "phdoc_static/project_ico.png"
html_sidebars = {}
language = "en"

epkg_dictionary.update({
    'C': 'https://en.wikipedia.org/wiki/C_(programming_language)',
    'C++': 'https://en.wikipedia.org/wiki/C%2B%2B',
    're2': 'https://github.com/google/re2',
    'pyre2': 'https://github.com/facebook/pyre2',
})
