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

    def test_calculate_reading_time(self):
        book1 = Book("Pride and Prejudice", 432)
        self.assertEqual(book1.calculate_reading_time(), 216)
        book2 = Book("Animal Farm", 112)
        self.assertEqual(book2.calculate_reading_time(), 56)

    def test_add_author(self):
        book1 = Book("Pride and Prejudice", 432)
        book1.add_author("Jane Austen")
        self.assertIn("Jane Austen", book1.authors)
        book1.add_author("George Orwell")
        self.assertIn("George Orwell", book1.authors)
        book1.add_author("Aldous Huxley")
        self.assertIn("Aldous Huxley", book1.authors)
        book1.add_author("Ray Bradbury")
        self.assertIn("Ray Bradbury", book1.authors)

    def test_add_empty_author(self):
        book1 = Book("Pride and Prejudice", 432)
        with self.assertRaises(ValueError) as context:
            book1.add_author("")

        self.assertEqual(str(context.exception), "Author name cannot be empty")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
