# lib/book.py

class Book:
    """
    Book class to represent a book in the bookstore.
    """

    def __init__(self, title, page_count):
        # Initialize title and page_count
        self.title = title
        self._page_count = None
        self.page_count = page_count  # use the setter for validation

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Validate that page_count is an integer
        if isinstance(value, bool) or not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
