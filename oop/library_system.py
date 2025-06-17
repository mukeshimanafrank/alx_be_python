class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


class EBook(Book):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def __str__(self):
        return f"EBook: {super().__str__()} - File Size: {self.file_size_mb}MB"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.year}, {self.file_size_mb})"


class PrintBook(Book):
    def __init__(self, title, author, year, page_count):
        super().__init__(title, author, year)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {super().__str__()} - Pages: {self.page_count}"

    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.year}, {self.page_count})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed: {book}")
        else:
            print("Book not found.")

    def list_books(self):
        print("Library Catalog:")
        for book in self.books:
            print(book)
