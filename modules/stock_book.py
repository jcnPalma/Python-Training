class Stockbook:
    # Sets the title, author, publication year, and ISBN of the book on creation
    def __init__(self, title, author, publication_year='', isbn=''):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn

    # Converts the book object to a dictionary
    def get_book(self):
        booked = {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "isbn": self.isbn
        }
        return booked
