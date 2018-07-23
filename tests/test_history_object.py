import pytest

from history_object import History


@History()
class T():
    def __init__(self, x):
        self.x = x


def test_init():
    test = T("lovely")
    assert test.x == "lovely"
    assert test.history['x'] == ["lovely"]


def test_one_change():
    test = T("hello world")
    test.x = "bye world"

    assert test.history['x'] == ["hello world", "bye world"]


def test_change_to_same_value():
    test = T("hi")
    test.x = "hi"  # Should not record a value getting set as the same thing.

    assert len(test.history['x']) == 1
