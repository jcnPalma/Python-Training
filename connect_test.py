from modules import BookManager

book_manager = BookManager()

title = "The Great Gatsby"
author = "F. Scott Fitzgerald"
isbn = "9780743273565"

book_manager.save_book(title=title, author=author, isbn=isbn)
print(book_manager.books)