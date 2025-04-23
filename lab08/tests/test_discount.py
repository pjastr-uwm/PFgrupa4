import pytest
from src.discount import calculate_discounted_price


def test_calcaule_positive():
    assert calculate_discounted_price(100, 36) == 64


def test_calcaule_neg():
    assert calculate_discounted_price(100, 36) != 29


def test_invalid_price():
    with pytest.raises(ValueError):
        calculate_discounted_price("-4", 89)

def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discounted_price(100,-78)
