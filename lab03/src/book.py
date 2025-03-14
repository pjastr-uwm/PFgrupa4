class Book:

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.authors = []

    def calculate_reading_time(self):
        return self.page_count // 2

    def add_author(self, param):
        if param == "":
            raise ValueError("Author name cannot be empty")

        self.authors.append(param)
