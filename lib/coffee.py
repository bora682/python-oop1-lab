# lib/coffee.py

class Coffee:
    """
    Coffee model for the bookstore cafe.
    """

    _VALID_SIZES = {"Small", "Medium", "Large"}

    def __init__(self, size, price):
        self._size = None
        self.size = size      # validate via setter
        self.price = price    # numeric (int/float)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # accept case-insensitive inputs like "small"
        if isinstance(value, str):
            normalized = value.strip().capitalize()
        else:
            normalized = value

        if normalized not in self._VALID_SIZES:
            print("size must be Small, Medium, or Large")
            return

        self._size = normalized

    def tip(self):
        print("This coffee is great, here’s a tip!")
        try:
            self.price = self.price + 1
        except TypeError:
            pass
