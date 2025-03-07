import unittest
from src.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.empty = ShoppingCart([])
        self.card = ShoppingCart(["Apple", "Bread"])

    def test_adding(self):
        self.empty.add_item("Apple")
        self.empty.add_item("Bread")
        # self.assertEqual(self.empty.items, self.card.items)
        self.assertEqual(self.empty, self.card)
        self.assertTrue(self.empty == self.card)

    def test_string_representation(self):
        s1 = str(self.card)
        s2 = "List: ['Apple', 'Bread']"
        self.assertEqual(s1, s2)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
