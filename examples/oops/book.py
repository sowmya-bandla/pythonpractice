#Create a Book class and allow the user to:
#Add book title and author
#Display book details
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(f"The title of book is {self.title} and author is {self.author}\n")

#taking user input
book_title=input("enter the book title:")
book_author=input("enter the author name:")
#creating book object
b1=book(book_title,book_author)

#displaying results
b1.display()

