#Library System (with Borrowing Logic)
class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print(f"Returned '{self.title}'")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Not Available"
            print(f"{book.title} - {status}")

# Example
lib = Library()
b1 = Book("Python Basics")
b2 = Book("OOP in Python")

lib.add_book(b1)
lib.add_book(b2)

lib.show_books()
b1.borrow()
lib.show_books()
b1.return_book()
lib.show_books()

print("=======================")

#Polymorphism with Duck Typing (Advanced)
class PDF:
    def read(self):
        print("Reading PDF content")

class Word:
    def read(self):
        print("Reading Word document")

def read_document(doc):
    doc.read()

read_document(PDF())
read_document(Word())

