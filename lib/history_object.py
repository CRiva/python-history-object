# Code derived from https://stackoverflow.com/questions/19121446/python-object-history/19124089#19124089
import datetime


class History():
    def __init__(self, *args):
        pass

    # def __setattr__(self, name, value):
    #     if self.history.get(name, False):
    #         self.history[name].append(value)
    #     else:
    #         self.history[name] = [value]
    #     self.__dict__[name] = value

    def __call__(self, cls):
        cls._history = {}
        this = self

        print(dir(cls))

        def getter(self, attr):
            if attr == 'history':
                return self._history
            if attr == 'historyTrace':
                return '\n'.join('%s: "%s" has changed to "%s"' % (t[0], t[1], t[2]) for t in self._history)
            return self.__dict__.get(attr)
        cls.__getattr__ = getter

        def setter(self, attr, value):
            if self._history.get(attr, False):
                self._history[attr].append(value)
            else:
                self._history[attr] = [value]
            self.__dict__[attr] = value
            # self._history[attr] = self._history.get(attr, []) + [(datetime.datetime.now(), attr, value)]
        cls.__setattr__ = setter

        return cls
