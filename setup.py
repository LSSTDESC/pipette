#!/usr/bin/env python
"""
Lightweight pipeline engine for LSST DESC
Copyright (c) 2018-2020 LSST DESC
http://opensource.org/licenses/MIT
"""
from setuptools import setup
from io import open

version = open('./ceci/version.py').read().split('=')[1].strip().strip("'")

# read the contents of the README file
with open('README.md', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='ceci',
    version=version,
    description='Lightweight pipeline engine for LSST DESC',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LSSTDESC/ceci',
    maintainer='Joe Zuntz',
    license='BSD',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 3 - Alpha',
    ],
    packages=['ceci', 'ceci.sites'],
    entry_points={
        'console_scripts':['ceci=ceci.main:main']
    },
    install_requires=['pyyaml', 'psutil'],
    extras_require={
      'parsl': ['flask', 'parsl==0.8.0'],
      'cwl': ['cwlgen==0.4', 'cwltool==2.0.20200126090152'],
      'test': ['pytest', 'codecov', 'pytest-cov'],
      }
)
