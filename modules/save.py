import json

class BookSaver():
    def save_book(self, book):
        j_book = self.convert_to_json(book)

        # Save to file

    def convert_to_json(self, book):
        return json.dumps(book)
    
    def convert_from_json(self):
        return False
    
    def write_to_file(self, data):

        return False
    
    def read_from_file(self):

        return False