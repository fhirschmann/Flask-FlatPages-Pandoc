import unittest
import os
from shutil import rmtree
from tempfile import mkdtemp


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
            FLATPAGES_EXTENSION=".md",
        )
        self.pages = FlatPages(self.app)
        FlatPagesPandoc("markdown", self.app, pre_render=False)

    def tearDown(self):
        rmtree(self.tmp)

    def write(self, body, ext="md"):
        with open(os.path.join(self.content, "test." + ext), "w") as f:
            f.write(body)

    def html(self):
        return self.pages.get("test").html

    def test1(self):
        self.write("title:test\n\n# test")
        self.assertEqual(self.html(), '<h1 id="test">test</h1>\n')
