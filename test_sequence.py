import pytest

from sequence import catalan


def test_base():
    assert catalan(0) == 1


def test_value():
    assert catalan(5) == 42


def test_invalid():
    with pytest.raises(ValueError):
        catalan(-10)

