class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = page_count

    @property
    def title(self):
        return self._title

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# Example usage
if __name__ == "__main__":

    book1 = Book("And Then There Were None", 272)
    assert book1.page_count == 272
    assert book1.title == "And Then There Were None"

    book2 = Book("The World According to Garp", 69)
    book2.turn_page()

    book3 = Book("The Catcher in the Rye", 200)
    book3.page_count = "not an integer"
