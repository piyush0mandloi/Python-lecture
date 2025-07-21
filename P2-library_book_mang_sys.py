class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author}-[{status}]"
    
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"\n✅ Book '{title}' added successfully" )
    
    def display_books(self):
        if not self.books:
            print("\nNo books in the library")
        else:
            print("\n List of Books:")
            for index,book in enumerate(self.books, start=1):
                print(f"{index}, {book}")
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower()==title.lower() and book.is_available:
                book.is_available=False
                print(f"\n You have borrowed '{book.title}'.")
                