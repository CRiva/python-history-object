import pytest

from history_object import HistoryObject


@HistoryObject()
class Test():
    def __init__(self, x):
        self.x = x


def test_init():
    test = Test("lovely")
    assert test.x == "lovely"
    print(test.history)
    assert test.history['x'] == ["lovely"]


def test_one_change():
    test = Test("hello world")
    test.x = "bye world"
    print(test.history)

    assert test.history['x'] == ["hello world", "bye world"]
