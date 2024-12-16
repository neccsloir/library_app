import json
import os


class Library:
    def __init__(self):
        self.books = []
        self.readers = []
        self.issued_books = {}

    def add_book(self, title, author, year, genre, copies):
        self.books.append({
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "copies": int(copies)
        })

    def remove_book(self, title):
        self.books = [book for book in self.books if book["title"] != title]

    def add_reader(self, name, surname, ticket_number):
        self.readers.append({
            "name": name,
            "surname": surname,
            "ticket_number": ticket_number
        })

    def remove_reader(self, ticket_number):
        self.readers = [reader for reader in self.readers if reader["ticket_number"] != ticket_number]

    def issue_book(self, title, ticket_number):
        for book in self.books:
            if book["title"] == title and book["copies"] > 0:
                if title not in self.issued_books:
                    self.issued_books[title] = []
                self.issued_books[title].append(ticket_number)
                book["copies"] -= 1
                return True
        return False

    def return_book(self, title, ticket_number):
        if title in self.issued_books and ticket_number in self.issued_books[title]:
            self.issued_books[title].remove(ticket_number)
            for book in self.books:
                if book["title"] == title:
                    book["copies"] += 1
                    break
            return True
        return False

    def save_data(self, filename):
        data = {
            "books": self.books,
            "readers": self.readers,
            "issued_books": self.issued_books
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_data(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
                self.books = data.get("books", [])
                self.readers = data.get("readers", [])
                self.issued_books = data.get("issued_books", {})
        else:
            self.books = []
            self.readers = []
            self.issued_books = {}