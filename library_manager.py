import json
from book import Book

class LibraryManager:
    def __init__(self, filename="books.json"):
        self.filename = filename

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_books(self, books):
        with open(self.filename, "w") as f:
            json.dump(books, f, indent=4)

    def add_book(self, book_id, title, author):
        books = self.load_books()

        new_book = Book(book_id, title, author)
        books.append(new_book.to_dict())

        self.save_books(books)
        print("Book added successfully!")

    def display_books(self):
        books = self.load_books()
        if not books:
            print("No books found!")
            return

        for b in books:
            print(f"ID: {b['id']}, Title: {b['title']}, Author: {b['author']}")

    def search_book(self, title):
        books = self.load_books()
        for b in books:
            if b["title"].lower() == title.lower():
                print("Book Found:")
                print(f"ID: {b['id']}  Title: {b['title']}  Author: {b['author']}")
                return
        print("Book not found!")