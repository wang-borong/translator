# -*- coding: utf-8 -*-

import re
import ast
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('translator/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='translator',
    version=version,
    description='translator for command line',
    long_description=readme,
    author='Jason Wang',
    author_email='1724555125@qq.com',
    url='https://github.com/stuha/translator',
    license=license,
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        translator=translator.translator:main
    '''
)
