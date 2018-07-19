import pytest

from history_object import History


@History()
class T():
    def __init__(self, x):
        self.x = x


def test_init():
    test = T("lovely")
    assert test.x == "lovely"
    print(test.history)
    assert test.history['x'] == ["lovely"]


def test_one_change():
    test = T("hello world")
    test.x = "bye world"
    print(test.history)

    assert test.history['x'] == ["hello world", "bye world"]
