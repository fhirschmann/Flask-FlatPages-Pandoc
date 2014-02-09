from setuptools import setup


setup(
    name="Flask-FlatPages-Pandoc",
    version="0.1",
    description="Pandoc rendering for Flask-FlatPages",
    url="http://github.com/fhirschmann/Flask-FlatPages-Pandoc",
    author="Fabian Hirschmann",
    author_email="fabian@hirschm.net",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    platforms="any",
    install_requires=[
        "Flask",
        "Flask-FlatPages>=0.6"
    ],
    keywords="flask flatpages pandoc latex markdown",
    packages=["flask_flatpages_pandoc"],
)
