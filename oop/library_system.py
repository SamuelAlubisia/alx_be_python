class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} - {self.file_size}MB"


class Printbook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} - {self.page_count} pages"


class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Book added: {book}")
        else:
            print("Error: Only instances of Book, Ebook, or Printbook can be added.")

    def list_books(self):
        if not self.books:
            print("The library is currently empty.")
        else:
            print("Library Collection:")
            for book in self.books:
                print(f" - {book}")


