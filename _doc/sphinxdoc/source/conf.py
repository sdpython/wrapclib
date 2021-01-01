# -*- coding: utf-8 -*-
import sys
import os
import alabaster


sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
local_template = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "phdoc_templates")

from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet
set_sphinx_variables(__file__, "wrapclib", "Xavier Dupré", 2021,
                     "alabaster", alabaster.get_path(),
                     locals(), extlinks=dict(
                         issue=('https://github.com/sdpython/wrapclib/issues/%s', 'issue')),
                     title="wrapclib", book=True)

blog_root = "http://www.xavierdupre.fr/app/wrapclib/helpsphinx/"

html_context = {
    'css_files': get_default_stylesheet() + ['_static/my-styles.css'],
}

html_logo = "phdoc_static/project_ico.png"
html_sidebars = {}
language = "en"

epkg_dictionary.update({
    'C': 'https://en.wikipedia.org/wiki/C_(programming_language)',
    'C++': 'https://en.wikipedia.org/wiki/C%2B%2B',
    're2': 'https://github.com/google/re2',
    'pyre2': 'https://github.com/facebook/pyre2',
})
