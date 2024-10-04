import pytest
from fuel import convert
from fuel import gauge

def test_notinteger():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_integer():
    assert convert("1/4") == 25

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_sameint():
    assert gauge(25) == "25%"
