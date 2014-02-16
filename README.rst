Flask-FlatPages-Pandoc
----------------------

.. image:: https://travis-ci.org/fhirschmann/Flask-FlatPages-Pandoc.png?branch=master
   :target: https://travis-ci.org/fhirschmann/Flask-FlatPages-Pandoc

Flask-FlatPages-Pandoc is an HTML renderer for
`Flask-FlatPages <https://github.com/SimonSapin/Flask-FlatPages/>`_
that uses `pandoc <http://johnmacfarlane.net/pandoc/>`_ as backend.

Quickstart
``````````

Flask-FlatPages-Pandoc is very easy to set up. First, install
it using pip:

.. code:: bash

    pip install Flask-FlatPages-Pandoc

Then, given that you already have a Flask application instance,
all you have to do is:

.. code:: python

    from flask_flatpages_pandoc import FlatPagesPandoc

    pages = FlatPages(app)
    FlatPagesPandoc("markdown", app, ["--mathjax"])


Links
`````

* `Demo Page <http://0x0b.de/sandbox/pandoc/>`_
* `GitHub Page <http://github.com/fhirschmann/Flask-FlatPages-Pandoc>`_
* `PyPI <http://pypi.python.org/pypi/Flask-FlatPages-Pandoc>`_
