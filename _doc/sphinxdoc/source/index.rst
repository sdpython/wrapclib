
.. |gitlogo| image:: _static/git_logo.png
             :height: 20

wrapclib
========

.. image:: https://travis-ci.com/sdpython/wrapclib.svg?branch=master
    :target: https://app.travis-ci.com/github/sdpython/wrapclib
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/auonxiihm1eihv3t?svg=true
    :target: https://ci.appveyor.com/project/sdpython/wrapclib
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/wrapclib/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/wrapclib/tree/master

.. image:: https://badge.fury.io/py/wrapclib.svg
    :target: https://pypi.org/project/wrapclib/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://codecov.io/github/sdpython/wrapclib/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/wrapclib?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/wrapclib.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/wrapclib/issues

.. image:: nbcov.png
    :target: http://www.xavierdupre.fr/app/wrapclib/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

.. image:: https://img.shields.io/github/repo-size/sdpython/wrapclib
    :target: https://github.com/sdpython/wrapclib/
    :alt: size

**Links:** `github <https://github.com/sdpython/wrapclib/>`_,
`documentation <http://www.xavierdupre.fr/app/wrapclib/helpsphinx/index.html>`_,
:ref:`l-README`,
:ref:`blog <ap-main-0>`

*wrapclib* is a wrapper for some C libraries difficult to build
otherwise. The first one to be wrapped is :epkg:`re2` with some
code taken from :epkg:`pyre2`.

.. runpython::
    :showcode:

    from wrapclib import re2
    s = "<h1>mot</h1>"
    print(re2.compile("(<.*>)").match(s).groups())
    print(re2.findall("(<.*>)", s))

.. toctree::
    :maxdepth: 1

    api/index
    i_ex
    all_notebooks
    blog/blogindex
    i_index

+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`     |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`   | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`modindex`      |  :ref:`l-EX2`       | :ref:`search`       | :ref:`l-license`   | :ref:`l-changes`       | :ref:`l-README`                                |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`genindex`      |  :ref:`l-FAQ2`      | :ref:`l-notebooks`  | :ref:`l-HISTORY`   | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
