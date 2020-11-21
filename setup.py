#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='wridgets',
    version='0.0.1',
    description='Wrapper around ipywidgets',
    author='Stelios Papadopoulos',
    author_email='stelios@spapa.us',
    packages=find_packages(exclude=[]),
    install_requires=['ipywidgets']
)
