import unittest
from src.book import Book

class TestBookInitialization(unittest.TestCase):

    def setUp(self):
        pass

    def test_creation(self):
        book1 = Book("Pride and Prejudice", 432)
        self.assertIsInstance(book1, Book)

    def test_arguments(self):
        book1 = Book("Pride and Prejudice", 432)
        self.assertEqual(book1.title, "Pride and Prejudice")
        self.assertEqual(book1.page_count, 432)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()