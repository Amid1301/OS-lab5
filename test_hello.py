import pytest
from hello import greet, add


def test_greet_returns_correct_string():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_greet_empty_name_raises():
    with pytest.raises(ValueError):
        greet("")


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 5) == 5
