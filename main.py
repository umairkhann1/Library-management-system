from models.book import Book
from models.user import User
from services.library import Library
from services.search import search_book

lib = Library()

b1 = Book("Python", "Ali")
b2 = Book("AI", "Sara")
b3 = Book("maths", "khan")
b4 = Book("physics", "jhon")
b5 = Book("programming", "david")


lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b5)
lib.add_book(b4)


u1 = User("Umair")
u2 = User("zara")

lib.lend_book("Python", u1)
lib.lend_book("AI", u1)
lib.lend_book("maths", u1)
lib.lend_book("maths", u2)
lib.receive_book("maths", u2)
lib.receive_book("maths", u1)
lib.available()
lib.show_books()
lib.load_books()
lib.save_book()
