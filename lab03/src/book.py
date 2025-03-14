class Book:

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def calculate_reading_time(self):
        return self.page_count // 2
