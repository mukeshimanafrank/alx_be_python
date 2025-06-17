from library_system import Book, EBook, PrintBook, Library

def main():
    library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    ebook = EBook("Snow Crash", "Neal Stephenson", 1992, 500)
    print_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 234)

    library.add_book(classic_book)
    library.add_book(ebook)
    library.add_book(print_book)

    library.list_books()

if __name__ == "__main__":
    main()
