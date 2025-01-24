class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"You have borrowed '{self.title}'."
        return f"'{self.title}' is already borrowed."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"You have returned '{self.title}'."
        return f"'{self.title}' was not borrowed."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"{book.title} by {book.author} ({status})")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book.borrow())
                return
        print(f"'{title}' is not in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book.return_book())
                return
        print(f"'{title}' is not in the library.")

library = Library()
library.add_book(Book("Harry Potter", "J.K. Rowling"))

while True:
    print("\nMenu:")
    print("1. View books")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        library.list_books()
    elif choice == "2":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)
    elif choice == "3":
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
