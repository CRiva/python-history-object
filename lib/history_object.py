# Code derived in part from
# https://stackoverflow.com/questions/19121446/python-object-history/19124089#19124089

import datetime


class History():
    def __init__(self, *args):
        pass

    def start(self, obj):
        if '_history' not in obj.__dict__:
            obj.__dict__['_history'] = {}

    def __call__(self, cls):
        this = self

        def getter(self, attr):
            this.start(self)
            if attr == 'history':
                return self._history
            if attr == 'historyTrace':
                return '\n'.join('%s: "%s" has changed to "%s"' % (t[0], t[1], t[2]) for t in self._history)
            return self.__dict__.get(attr)
        cls.__getattr__ = getter

        def setter(self, attr, value):
            this.start(self)
            if self._history.get(attr, False):
                if self._history[attr][-1] == value:
                    pass
                else:
                    self._history[attr].append(value)
            else:
                self._history[attr] = [None, value] if value is not None else [None]
            self.__dict__[attr] = value
        cls.__setattr__ = setter

        return cls
