#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for
from flask_flatpages import FlatPages
from flask_flatpages_pandoc import FlatPagesPandoc


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_ROOT = "content"
FLATPAGES_EXTENSION = ".md"
FLATPAGES_ENCODING = "utf-8"

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
FlatPagesPandoc("markdown", app,
                ["--mathjax", "--bibliography", "bibliography.bib"],
                pre_render=True)


@app.route("/")
def home():
    return redirect(url_for("page", path="test"))


@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)


if __name__ == "__main__":
    app.run(port=8001)
