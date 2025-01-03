class Stockbook:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_book(self):
        booked = {
            "title": self.title,
            "author": self.author
        }

        return booked