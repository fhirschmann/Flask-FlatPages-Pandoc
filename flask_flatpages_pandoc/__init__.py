"""
flask_flatpages_pandoc
~~~~~~~~~~~~~~~~~~~~~~

Flask-FlatPages-Pandoc is an HTML renderer for Flask-FlatPages that uses
pandoc as its backend.

:copyright: (c) 2014 Fabian Hirschmann <fabian@hirschm.net>
:license: MIT, see LICENSE.txt for more details.

"""
from __future__ import print_function
from subprocess import Popen, PIPE

__version__ = "0.1"


class FlatPagesPandoc(object):
    """
    Class that, when applied to a :class:`flask.Flask` instance,
    sets up an HTML renderer using pandoc.
    """
    def __init__(self, source_format, app=None, pandoc_args=[]):
        """
        Initializes Flask-FlatPages-KnitrPandoc

        :param source_format: the source file format; directly passed
                              to pandoc.
        :type source_format: string
        :param pandoc_args: extra arguments passed to pandoc
        :param app: your application. Can be omitted if you call
                    :meth:`init_app` later.
        :type app: :class:`flask.Flask`
        :type pandoc_args: sequence
        """
        self.source_format = source_format
        self.pandoc_args = pandoc_args

        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        Used to initialize an application. This is useful when passing
        an app later.

        :param app: your application
        :type app: :class:`flask.Flask`
        """
        self.app = app

        # The following lambda expression works around Flask-FlatPage's
        # reflection magic.
        self.app.config["FLATPAGES_HTML_RENDERER"] = lambda t, p, m: self.renderer(t, p, m)

    def renderer(self, text, flatpages, page):
        """
        Renders a flat page to HTML.

        :param text: the text of the flat page
        :type text: string
        :param flatpages: a list of flatpages
        :type flatpages: sequence
        :param page: a page instance
        :type page: :class:`flask_flatpages.Page`
        """
        args = ["pandoc", "-f", self.source_format, "-t", "html"]
        args.extend(self.pandoc_args)

        if self.app.debug:
            print("Executing:", *args, sep=" ")

        proc = Popen(args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        html, stderr = proc.communicate(text)

        if stderr:
            raise ValueError(stderr)

        return html.decode("utf-8")
