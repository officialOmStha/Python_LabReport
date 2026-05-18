# Lab 2:

class Library:
    # Class variable
    total_books = 0

    # Constructor
    def __init__(self):
        self.books = []

    # Static method
    @staticmethod
    def is_valid_book(book_name):
        return len(book_name) > 0

    # Method to add a book
    def add_book(self, book_name):
        if Library.is_valid_book(book_name):
            self.books.append(book_name)
            Library.total_books += 1
            print(f'"{book_name}" added successfully.')
        else:
            print("Invalid book name.")

    # Method to remove a book
    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            Library.total_books -= 1
            print(f'"{book_name}" removed successfully.')
        else:
            print(f'"{book_name}" not found.')

    # Method to display books
    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("Books in library:")
            for book in self.books:
                print(book)

    # Class method
    @classmethod
    def display_total_books(cls):
        print("Total books across all libraries:", cls.total_books)


# Separate function using list comprehension
def uppercase_books(book_list):
    return [book.upper() for book in book_list]


# Creating library objects
library1 = Library()
library2 = Library()

# Adding books
library1.add_book("Python Basics")
library1.add_book("Artificial Intelligence")
library2.add_book("Data Science")

# Display books
library1.display_books()
library2.display_books()

# Remove a book
library1.remove_book("Python Basics")

# Display total books
Library.display_total_books()

# Convert books to uppercase
upper_books = uppercase_books(library1.books)

print("Books in uppercase:", upper_books)