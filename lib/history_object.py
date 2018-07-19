
class HistoryObject():
    def __init__(self, history={}):
        self.history = history

    def __setattr__(self, name, value):
        if self.history.get(name, False):
            self.history[name].append(value)
        else:
            self.history[name] = [value]
        self.__dict__[name] = value
