#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals

import os
import sys
from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload -r internal')
    sys.exit()

requirements = [
]


setup(
    name='mymod',
    version="0.4",
    author='shenghuofei',
    packages=find_packages(),
    install_requires=requirements,
    download_url="http://pypi.douban.com/simple/",
    license="GPL",
)
