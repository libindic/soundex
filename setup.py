#!/usr/bin/env python

from setuptools import setup

setup (
    name = "soundex",
    version = "0.3",
    url = "http://silpa.org.in/Soundex",
    license = "LGPL-3.0",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    description = "Soundex Phonetic Code Algorithm for Indian Languages",
    long_description ="""Soundex Phonetic Code Algorithm Demo for Indian Languages.
 Supports all indian languages and English. Provides intra-indic string comparison""",
    packages = ['soundex'],
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools'],
    zip_safe = False,
    )
