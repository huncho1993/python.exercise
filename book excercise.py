class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"You have successfully borrowed '{self.title}'."
        return f"Sorry, '{self.title}' is already borrowed."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"You have successfully returned '{self.title}'."
        return f"The book '{self.title}' was not borrowed."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"- {book.title} by {book.author} ({status})")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            print(book.borrow())
        else:
            print(f"Sorry, the book '{title}' is not in the library.")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            print(book.return_book())
        else:
            print(f"Sorry, the book '{title}' is not in the library.")

if __name__ == "__main__":
    library = Library()

    # Adding books to the library
    library.add_book(Book("Harry Potter", "J.K. Rowling"))
    library.add_book(Book("The Witcher", "Andrzej Sapkowski"))
    library.add_book(Book("Atomic Habits", "James Clear"))
    library.add_book(Book("The Psychology of Money", "Morgan Housel"))
    library.add_book(Book("Rich Dad Poor Dad", "Robert Kiyosaki"))

    # Menu-driven system
    while True:
        print("Library Menu:")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice : "))

            if choice == 1:
                library.list_books()
            elif choice == 2:
                title = input("Enter the title of the book to borrow: ")
                library.borrow_book(title)
            elif choice == 3:
                title = input("Enter the title of the book to return: ")
                library.return_book(title)
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")      