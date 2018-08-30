#!/usr/bin/env python3
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

setup(name='history-object',
      version="0.2.2",
      description='A python decorator that tracks added and changed elements of the decorated object.',
      packages=find_packages('lib'),
      package_dir={'': 'lib'},
      author='Connor Riva, Dave Lundgren',
      author_email='criva@westmont.edu, dlungren@outsideopen.com',
      url='https://bitbucket.org/westmont/history_object',
      py_modules=[splitext(basename(path))[0] for path in glob('lib/*.py')],
      keywords=['history', 'attributes', 'tracking', 'object', 'decorator'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      setup_requires=['setuptools-markdown'],
      long_description_markdown_filename='README.md'
      )
