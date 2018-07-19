# History Object #

An Object implementation that tracks added and changed elements.

## Usage ##

## Test ##

You can run the tests using [tox](https://tox.readthedocs.io/en/latest/)

~~~shell
tox
~~~

## Publish ##

To publish a new version of this package your Pypi user needt to be added to the project. (Ask Connor to give you access)

~~~shell
# Update version number in setup.py

python setup.py sdist
twine upload dist/*
~~~