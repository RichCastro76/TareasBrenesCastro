# ERR8x3
from ejercicio1 import string_work


def test_one():
    assert string_work("VIVAsaprissa") is True


def test_two():
    assert string_work(123456789) is True


def test_three():
    assert string_work("VIVAsaprissa123#!$") is True
