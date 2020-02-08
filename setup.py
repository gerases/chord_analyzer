# -*- coding: utf-8 -*-
"""Setup for chord_analyzer"""
from setuptools import setup, find_packages

DESC = "A set of tools related to music theory"
SHORT_DESC = DESC
LONG_DESC = DESC

setup(
    python_requires='>=3',
    description=SHORT_DESC,
    name='chord_finder',
    version='1.0.0',
    url='https://github.com/gerases/chord_analyzer.git',
    packages=find_packages(),
    license='Conversant',
    maintainer='Sergei Gerasenko',
    maintainer_email='gerases@gmail.com',
    long_description=LONG_DESC,
    install_requires=['termcolor'],
)
