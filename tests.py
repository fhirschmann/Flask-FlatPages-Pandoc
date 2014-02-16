# -*- coding: utf-8 -*-
import unittest
import os
from shutil import rmtree
from tempfile import mkdtemp
from codecs import open

from flask import Flask
from flask_flatpages import FlatPages
from flask_flatpages_pandoc import FlatPagesPandoc


class TestFlatPagesPandoc(unittest.TestCase):
    def setUp(self):
        self.tmp = mkdtemp()
        self.content = os.path.join(self.tmp, "content")
        os.makedirs(self.content)

        self.app = Flask(__name__)
        self.app.config.update(
            FLATPAGES_ROOT=self.content,
            FLATPAGES_AUTO_RELOAD=True,
        )
        self.pages = FlatPages(self.app)
        FlatPagesPandoc("markdown", self.app, pre_render=False)

    def tearDown(self):
        rmtree(self.tmp)

    def get(self, body, ext=".md"):
        self.app.config.update(FLATPAGES_EXTENSION=ext)
        with open(os.path.join(self.content, "test" + ext), "w", "utf-8") as f:
            f.write(u"title:test\n\n" + body)
        return self.pages.get("test").html

    def test_h1(self):
        self.assertEqual(self.get("# test"), '<h1 id="test">test</h1>\n')

    def test_unicode(self):
        self.assertEqual(self.get(u"萬大事都有得解決"), u"<p>萬大事都有得解決</p>\n")
