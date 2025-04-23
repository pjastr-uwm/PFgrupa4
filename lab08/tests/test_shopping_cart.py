import pytest
from src.shopping_cart import Product, ShoppingCart

@pytest.fixture
def sample_product1():
    return Product(567, "Apple", 6.34)

@pytest.fixture
def sample_product2():
    return Product(34, "Milk", 5.99)

@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.fixture
def filled_cart(sample_product1, empty_cart):
    empty_cart.add_product(sample_product1, 5)
    return empty_cart


def test_adding_positive(empty_cart, sample_product1):
    empty_cart.add_product(sample_product1)
    assert empty_cart.get_product_count() == 1

def test_adding_positive2(empty_cart, sample_product2):
    empty_cart.add_product(sample_product2, 5)
    assert empty_cart.get_product_count() == 5
    assert empty_cart.get_total_price() == 29.95

@pytest.mark.parametrize("quantity",[1, 5, 10])
def test_multiple_adding(empty_cart, sample_product1, quantity):
    empty_cart.add_product(sample_product1, quantity)
    assert empty_cart.get_product_count() == quantity

def test_removing_positive(filled_cart,sample_product1):
    filled_cart.remove_product(sample_product1.id)
    assert filled_cart.get_product_count() == 4

def test_removing_neg(filled_cart,sample_product2):
    with pytest.raises(ValueError):
        filled_cart.remove_product(sample_product2.id)

def test_clear_cart(filled_cart, sample_product1):
    filled_cart.remove_product(sample_product1.id, 5)
    assert filled_cart.get_product_count() == 0
    assert sample_product1.id not in filled_cart.products.keys()
