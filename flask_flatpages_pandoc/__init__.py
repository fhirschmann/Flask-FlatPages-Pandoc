"""
flask_flatpages_pandoc
~~~~~~~~~~~~~~~~~~~~~~

Flask-FlatPages-Pandoc is an HTML renderer for Flask-FlatPages that uses
pandoc as backend.

:copyright: (c) 2014 Fabian Hirschmann <fabian@hirschm.net>
:license: MIT, see LICENSE.txt for more details.

"""
from __future__ import print_function
import pkg_resources
from subprocess import Popen, PIPE

from flask import render_template_string, Markup


try:
    __version__ = pkg_resources.require("Flask-FlatPages-Pandoc")[0]
except pkg_resources.DistributionNotFound:
    __version__ = "0.0-dev"


class FlatPagesPandoc(object):
    """
    Class that, when applied to a :class:`flask.Flask` instance,
    sets up an HTML renderer using pandoc.
    """
    def __init__(self, source_format, app=None, pandoc_args=[],
                 pre_render=False):
        """
        Initializes Flask-FlatPages-Pandoc.

        :param source_format: the source file format; directly passed
                              to pandoc.
        :type source_format: string
        :param app: your application. Can be omitted if you call
                    :meth:`init_app` later.
        :type app: :class:`flask.Flask`
        :param pandoc_args: extra arguments passed to pandoc
        :type pandoc_args: sequence
        :param pre_render: pre-render the page as :class:`flask.Markup`
        :type pre_render: boolean
        """
        self.source_format = source_format
        self.pandoc_args = pandoc_args
        self.pre_render = pre_render

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
        self.app.config["FLATPAGES_HTML_RENDERER"] = lambda t: self.renderer(t)

    def renderer(self, text):
        """
        Renders a flat page to HTML.

        :param text: the text of the flat page
        :type text: string
        """
        text = text.decode(self.app.config["FLATPAGES_ENCODING"])

        if self.pre_render:
            text = render_template_string(Markup(text))

        text = text.encode("utf-8")

        args = ["pandoc", "-f", self.source_format, "-t", "html"]
        args.extend(self.pandoc_args)

        if self.app.debug:
            print("Executing:", *args, sep=" ")

        proc = Popen(args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        html, stderr = proc.communicate(text)

        if stderr:
            raise ValueError(stderr)

        return html.decode("utf-8")
