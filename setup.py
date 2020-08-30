#!/usr/bin/env python

from setuptools import setup

setup(
    name='p1',
    version='0.1',
    description='Python Package 1',
    author='Adam Ta',
    author_email='notrelevant@mail.net',
    url='https://github.com/sababa11/p1.git',
    install_requires=['requests==2.24.0'],
    packages=['p1'],
    )

print("OK")
