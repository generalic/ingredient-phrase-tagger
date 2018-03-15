#!/usr/bin/env python
import sys

from setuptools import setup

requires, extra = ['Unidecode==1.0.22', 'pandas==0.22.0'], {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name='ingredient_phrase_tagger',
    version='0.0.0.dev0',
    description='Extract structured data from ingredient phrases using conditional random fields',
    author='The New York Times Company',
    author_email='',
    license='Apache 2.0',
    install_requires=requires,
    packages=['ingredient_parser'],
    package_data={'ingredient_parser': ['model_file']},
    include_package_data=True
)
