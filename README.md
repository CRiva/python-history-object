[![Build Status](https://travis-ci.org/CRiva/python-history-object.svg?branch=master)](https://travis-ci.org/CRiva/python-history-object)

This repo lives both in [Github](https://github.com/CRiva/python-history-object) and [BitBucket](https://bitbucket.org/westmont/history_object/src/master/). 

# History Object #

An Object implementation that tracks added and changed elements.

## Usage ##

~~~python
>>> from history_object import History
>>> 
>>> @History()
>>> class T():
>>>     def __init__(self, x):
>>>        self.x = x
>>>
>>> test = T("Hello World")
>>> test.history['x']         # ["Hello World"]
>>> test.x = "Goodbye World"
>>> test.history['x']         # ["Hello World", "Goodbye World"]
~~~

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