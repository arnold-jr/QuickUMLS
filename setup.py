from setuptools import setup, find_packages

setup(
    name="QuickUMLS",
    version="0.1.dev.0",
    packages=find_packages(),
    scripts=["quickumls/install.py"],

    install_requires=[],

    package_data={},

    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
    license="PSF",
    keywords="quickumls umls",
    url="http://example.com/HelloWorld/",   
    project_urls={
      "Bug Tracker": "https://bugs.example.com/HelloWorld/",
      "Documentation": "https://docs.example.com/HelloWorld/",
      "Source Code": "https://code.example.com/HelloWorld/",
    },
    entry_points={
      'console_scripts': [
        'installdata = quickumls.install:main_func',
        ]
      }

    )
