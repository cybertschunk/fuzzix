#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'dnspython',
    'beautifulsoup4',
    'colorama',
    'coloredlogger',
    'urllib3',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    author="David Leeuwestein",
    author_email='cybertschunk@mailbox.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description=
    "a python-driven url fuzzer and web-spiderer with the aim to give you a as detailed as possible insight of the websites' structure",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='fuzzix',
    name='fuzzix',
    packages=find_packages(include=['fuzzix']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/cybertschunk/fuzzix',
    version='0.0.1',
    scripts=[
        'bin/fuzzixscan',
    ],
    zip_safe=False,
)
