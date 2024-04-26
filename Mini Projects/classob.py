class Book:
    def __init__(self, book_id, title, price):
        self.book_id = book_id
        self.title = title
        self.price = price
# new books add

def add_book_to_stock(stock, book_id, title, price):
    new_book = Book(book_id, title, price)
    stock.append(new_book)
    print(f"Book '{title}' added to the stock.")

# Example usage

stock = []
add_book_to_stock(stock, 1, "Harry Potter and the Philosopher's Stone", 80.0)

# book id

class Book:
    def __init__(self, book_id,):
        self.book_id = book_id

        # Show all books
        print("All Books in the Shop:")
        show_all_books(stock)

 # delete book from stock

def delete_book(stock, identifier):
    # Iterate through the stock and find the book to delete
    for book in stock:
        if identifier == book.book_id or identifier == book.title or identifier == book.price:
            stock.remove(book)
            print(f"Book with ID {book.book_id}, Title '{book.title}', and Price ${book.price} deleted successfully.")
            return
    print("Book not found.")

# Example usage

stock = [
    Book(1, "Harry Potter and the Philosopher's Stone", 20.0),
    Book(2, "The Hobbit", 15.0),
    Book(3, "To Kill a Mockingbird", 18.0)
]

# Delete a book by ID
delete_book(stock, 2)




