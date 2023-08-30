class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed_by = None
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def __str__(self):
        return self.name
    
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            if book.borrowed_by:
                book.borrowed_by.borrowed_books.remove(book)
    
    def add_patron(self, patron):
        self.patrons.append(patron)
    
    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        return results
    
    def borrow_book(self, patron, book):
        if book in self.books and book.borrowed_by is None and patron in self.patrons:
            book.borrowed_by = patron
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed {book.title}.")
        else:
            print("Borrowing not possible.")
    
    def return_book(self, patron, book):
        if book in patron.borrowed_books and book in self.books:
            patron.borrowed_books.remove(book)
            book.borrowed_by = None
            print(f"{patron.name} returned {book.title}.")
        else:
            print("Returning not possible.")
    
    def list_borrowed_books(self):
        borrowed_books = [book for book in self.books if book.borrowed_by is not None]
        return borrowed_books

# Create a library
library = Library()

# Create and add books to the library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
library.add_book(book1)
library.add_book(book2)

# Create and add patrons to the library
patron1 = Patron("Alice")
patron2 = Patron("Bob")
library.add_patron(patron1)
library.add_patron(patron2)

print("Welcome to the Library Management System!")

while True:
    print("\nMenu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. List Borrowed Books")
    print("7. Add Patron")
    print("8. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        isbn = input("Enter the ISBN of the book: ")
        new_book = Book(title, author, isbn)
        library.add_book(new_book)
        print(f"Book '{title}' added to the library.")
    elif choice == '2':
        print("Available books:")
        for idx, book in enumerate(library.books, start=1):
            print(f"{idx}. {book}")
        book_idx = int(input("Enter the number of the book to remove: ")) - 1
        if 0 <= book_idx < len(library.books):
            removed_book = library.books[book_idx]
            library.remove_book(removed_book)
            print(f"Book '{removed_book.title}' removed from the library.")
        else:
            print("Invalid book number.")
    elif choice == '3':
        query = input("Enter the title or author to search for: ")
        results = library.search_books(query)
        print("Search results:")
        for idx, book in enumerate(results, start=1):
            print(f"{idx}. {book}")
    elif choice == '4':
        print("Available books:")
        for idx, book in enumerate(library.books, start=1):
            print(f"{idx}. {book}")
        book_idx = int(input("Enter the number of the book to borrow: ")) - 1
        if 0 <= book_idx < len(library.books):
            selected_book = library.books[book_idx]
            print("Available patrons:")
            for idx, patron in enumerate(library.patrons, start=1):
                print(f"{idx}. {patron}")
            patron_idx = int(input("Enter the number of the patron: ")) - 1
            if 0 <= patron_idx < len(library.patrons):
                selected_patron = library.patrons[patron_idx]
                library.borrow_book(selected_patron, selected_book)
            else:
                print("Invalid patron number.")
        else:
            print("Invalid book number.")
    elif choice == '5':
        print("Borrowed books:")
        for idx, book in enumerate(library.list_borrowed_books(), start=1):
            print(f"{idx}. {book}")
        book_idx = int(input("Enter the number of the book to return: ")) - 1
        if 0 <= book_idx < len(library.books):
            selected_book = library.books[book_idx]
            print("Borrowed by:")
            if selected_book.borrowed_by:
                print(selected_book.borrowed_by)
                patron_idx = int(input("Enter the number of the patron: ")) - 1
                if 0 <= patron_idx < len(library.patrons):
                    selected_patron = library.patrons[patron_idx]
                    library.return_book(selected_patron, selected_book)
                else:
                    print("Invalid patron number.")
            else:
                print("Not currently borrowed.")
        else:
            print("Invalid book number.")
    elif choice == '6':
        print("Borrowed books:")
        for idx, book in enumerate(library.list_borrowed_books(), start=1):
            print(f"{idx}. {book}")
    elif choice == '7':
        patron_name = input("Enter the name of the patron: ")
        new_patron = Patron(patron_name)
        library.add_patron(new_patron)
        print(f"Patron '{patron_name}' added to the library.")        
            
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
