def search_book(title, books):
    
    for book in books:
        if book.title.lower() == title.lower():
            print(f"{book.title} by { book.author} here")
            return book
        
    print(f"{book.title} not found")
     

    

