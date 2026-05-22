import json

from models.book import Book
class Library:


    def __init__(self):
        self.books = []
        with open("config.json", "r") as file:
            self.config = json.load(file)
        print(self.config["library_name"])
        print(self.config["max_books"])

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.display_info()

    

    def lend_book(self, title, user):
        
        if len(user.borrowed_books) >= self.config["max_books"]:
            print(f"{user.name} can't lend books more than", self.config["max_books"])
            return
        
        for book in self.books:

            if book.title.lower() == title.lower():

                if book.is_available:
                    book.is_available = False
                    user.borrow_book(book)
                    with open("log.txt", "a") as file:
                        file.write(f"{user.name} borrowed {book.title}\n")
                    print(f"{user.name} book borrowed")
                    return
                else:
                    print("book is not available")
                    return
                

        print("book not found")

        
    def receive_book(self, title, user):
        try:

            for book in user.borrowed_books:
                if book.title.lower() == title.lower():
                    book.is_available = True
                    user.return_book(book)
                    with open("log.txt", "a") as file:
                        file.write(f"{user.name} returned {book.title}\n")
                    print(f"{user.name} book returned")
                    return
            raise ValueError("you did not borrow this book")
        except ValueError as e:
            print(e)        
            
    def available(self):
        print("\n AVAILABLE BOOKS")

        found = False
        for book in self.books:
            if book.is_available:
                book.display_info()
                found = True
        if not found:
            print(" no available books")

    def load_books(self):
        with open("books.json", "r") as file:
            data = json.load(file)
            for item in data:
                book = Book(item["title"], item["author"])
                book.is_available = item["available"]
                self.books.append(book)

            

    

    def save_book(self):
        with open("books.json", "w")as file:
            data = []

            for book in self.books:
                book_data = {
                    "title" : book.title,
                    "author" : book.author,
                    "available" : book.is_available
                }
                data.append(book_data)

            with open("books.json", "w") as file:
                json.dump(data, file, indent = 2)
                
            

