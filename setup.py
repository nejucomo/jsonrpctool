#!/usr/bin/env python

from setuptools import setup, find_packages


PACKAGE = 'jsonrpc'

setup(
    name=PACKAGE,
    description='Commandline JSON-RPC client tool.',
    version='0.1',
    author='Nathan Wilcox',
    author_email='nejucomo+dev@gmail.com',
    license='GPLv3',
    url='https://github.com/nejucomo/{}'.format(PACKAGE),
    install_requires=[
        'jsonrpcclient[requests]',
    ],

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            '{0} = {0}.main:main'.format(PACKAGE),
        ],
    }
)
