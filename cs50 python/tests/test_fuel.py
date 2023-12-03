from fuel import convert, gauge
import pytest


def test_cnvert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"

def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0") 