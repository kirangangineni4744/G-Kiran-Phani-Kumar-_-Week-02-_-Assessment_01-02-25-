class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display(self):
        print(f"Details:\n Title:{self.title}\n Author:{self.author}\n Isbn:{self.isbn}")

print("Enter the book title:")
title=input()
print("Enter author name:")
author=input()
print("Enter book's isbn:")
isbn=int(input())

book=Book(title,author,isbn)
book.display()