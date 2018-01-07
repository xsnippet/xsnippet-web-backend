#!/usr/bin/env python
# coding: utf-8

import os
from setuptools import setup, find_packages as _find_packages

from xsnippet.web_backend import __version__ as version
from xsnippet.web_backend import __license__ as license


here = os.path.dirname(__file__)
with open(os.path.join(here, 'README.rst'), 'r', encoding='utf-8') as f:
    long_description = f.read()


# Unfortunately setuptools.find_packages() doesn't support PEP-420 namespace
# packages so we need our own implementation that does. All this shit happened
# due to desperate @ikalnytskyi's desire to use namespace packages.
def find_packages(namespace):
    return ['%s.%s' % (namespace, pkg) for pkg in _find_packages(namespace)]


setup(
    name='xsnippet-web-backend',
    version=version,
    description=(
        'XSnippet is a simple web-service for sharing code snippets on the '
        'Internet. Written for fun using bleeding edge technologies.'),
    long_description=long_description,
    license=license,
    url='https://github.com/xsnippet/xsnippet-web-backend/',
    keywords='web-service restful-api snippet storage',
    author='The XSnippet Team',
    author_email='dev@xsnippet.org',
    packages=find_packages('xsnippet'),
    zip_safe=False,
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'aiohttp >= 2.3.5',
    ],
    tests_require=[
        'pytest >= 2.8.7',
        'pytest-aiohttp >= 0.3.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
