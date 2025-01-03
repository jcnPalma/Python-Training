class Stockbook:
    # Sets the title and author of the book on creation
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Converts the book object to a dictionary
    def get_book(self):
        booked = {
            "title": self.title,
            "author": self.author
        }

        return booked