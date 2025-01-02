import json
import os

class BookManager:
    def __init__(self):
        # Initialize books by reading from the file
        self.books = self.read_from_file() or []

    def save_book(self, book):
        # Add a book to the list
        self.books.append(book)
        # Convert updated list to JSON and save to file
        self.write_to_file(self.convert_to_json(self.books))

    def convert_to_json(self, book):
        # Convert Python object to JSON string
        return json.dumps(book, indent=4)

    def convert_from_json(self, json_data):
        # Convert JSON string to Python object
        return json.loads(json_data)

    def write_to_file(self, data):
        # Ensure directory exists
        os.makedirs(os.path.dirname("./book data/books.json"), exist_ok=True)
        # Write data to file
        with open("./book data/books.json", "w") as file:
            file.write(data)

    def read_from_file(self):
        try:
            with open("./book data/books.json", "r") as file:
                return self.convert_from_json(file.read())
        except FileNotFoundError:
            # Create an empty file if not found
            self.write_to_file(self.convert_to_json([]))
            return []
        except json.JSONDecodeError:
            # Handle corrupted JSON file
            print("Error: Corrupted JSON file. Starting fresh.")
            self.write_to_file(self.convert_to_json([]))
            return []

# Runs this block if this file was executed
if __name__:
    test = BookManager()

    # Add and save a book
    test.save_book({"title": "1984", "author": "George Orwell"})
    print(test.books)