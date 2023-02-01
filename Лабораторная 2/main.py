class Book:

    def __init__(self, id_of_book: int, name: str, pages: int):
        self.id = id_of_book
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга '{self.name}'"

    def __repr__(self) -> str:
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"


class Library:

    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        return print((len(self.books) + 1))


    def get_index_by_book_id(self, id):
        return print(id - 1)


if __name__ == "__main__":
    book = Book(1, '1984', 200)

    list_1 = []
    book_list = ['1984', 'Gosudar', 'War and Peace']

    lib = Library(book_list)
    lib.get_next_book_id()
    lib.get_index_by_book_id(1)
    print(book)
    print(repr(book))
