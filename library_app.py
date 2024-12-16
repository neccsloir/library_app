import tkinter as tk
from tkinter import messagebox
import json
import os

class Library:
    def __init__(self):
        self.books = []
        self.readers = []
        self.issued_books = {}

    def add_book(self, title, author, genre, copies):
        self.books.append({"title": title, "author": author, "genre": genre, "copies": int(copies)})

    def remove_book(self, title):
        self.books = [book for book in self.books if book["title"] != title]

    def edit_book(self, old_title, new_title, author, genre, copies):
        for book in self.books:
            if book["title"] == old_title:
                book["title"] = new_title
                book["author"] = author
                book["genre"] = genre
                book["copies"] = int(copies)
                break

    def add_reader(self, name, surname, ticket_number):
        self.readers.append({"name": name, "surname": surname, "ticket_number": ticket_number})

    def remove_reader(self, ticket_number):
        self.readers = [reader for reader in self.readers if reader["ticket_number"] != ticket_number]

    def edit_reader(self, ticket_number, new_name, new_surname):
        for reader in self.readers:
            if reader["ticket_number"] == ticket_number:
                reader["name"] = new_name
                reader["surname"] = new_surname
                break

    def issue_book(self, title, ticket_number):
        if title not in self.issued_books:
            self.issued_books[title] = []
        self.issued_books[title].append(ticket_number)

    def return_book(self, title, ticket_number):
        if title in self.issued_books:
            self.issued_books[title].remove(ticket_number)

    def search_books(self, query):
        return [book for book in self.books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower() or query.lower() in book["genre"].lower()]

    def search_reader(self, query):
        return [reader for reader in self.readers if query.lower() in reader["name"].lower() or query.lower() in reader["surname"].lower() or query.lower() in reader["ticket_number"]]

    def report_by_genre(self, genre):
        return len([book for book in self.books if book["genre"] == genre])

    def report_total_books(self):
        return len(self.books)

    def report_reader_books(self, ticket_number):
        return {title: readers for title, readers in self.issued_books.items() if ticket_number in readers}

    def report_reader_debts(self):
        return {title: readers for title, readers in self.issued_books.items()}

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

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.library = Library()

        # Загрузка данных
        self.library.load_data("library_data.json")

        # Метки и поля ввода
        self.title_label = tk.Label(root, text="Название книги")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)

        self.author_label = tk.Label(root, text="Автор")
        self.author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1)

        self.genre_label = tk.Label(root, text="Жанр")
        self.genre_label.grid(row=2, column=0)
        self.genre_entry = tk.Entry(root)
        self.genre_entry.grid(row=2, column=1)

        self.copies_label = tk.Label(root, text="Количество копий")
        self.copies_label.grid(row=3, column=0)
        self.copies_entry = tk.Entry(root)
        self.copies_entry.grid(row=3, column=1)

        self.reader_name_label = tk.Label(root, text="Имя читателя")
        self.reader_name_label.grid(row=4, column=0)
        self.reader_name_entry = tk.Entry(root)
        self.reader_name_entry.grid(row=4, column=1)

        self.reader_surname_label = tk.Label(root, text="Фамилия читателя")
        self.reader_surname_label.grid(row=5, column=0)
        self.reader_surname_entry = tk.Entry(root)
        self.reader_surname_entry.grid(row=5, column=1)

        self.ticket_label = tk.Label(root, text="Номер читательского билета")
        self.ticket_label.grid(row=6, column=0)
        self.ticket_entry = tk.Entry(root)
        self.ticket_entry.grid(row=6, column=1)

        # Кнопки управления
        self.add_book_button = tk.Button(root, text="Добавить книгу", command=self.add_book)
        self.add_book_button.grid(row=7, column=0)

        self.remove_book_button = tk.Button(root, text="Удалить книгу", command=self.remove_book)
        self.remove_book_button.grid(row=7, column=1)

        self.add_reader_button = tk.Button(root, text="Добавить читателя", command=self.add_reader)
        self.add_reader_button.grid(row=8, column=0)

        self.remove_reader_button = tk.Button(root, text="Удалить читателя", command=self.remove_reader)
        self.remove_reader_button.grid(row=8, column=1)

        self.issue_book_button = tk.Button(root, text="Выдать книгу", command=self.issue_book)
        self.issue_book_button.grid(row=9, column=0)

        self.return_book_button = tk.Button(root, text="Вернуть книгу", command=self.return_book)
        self.return_book_button.grid(row=9, column=1)

        self.save_data_button = tk.Button(root, text="Сохранить данные", command=self.save_data)
        self.save_data_button.grid(row=10, column=0)

        self.load_data_button = tk.Button(root, text="Загрузить данные", command=self.load_data)
        self.load_data_button.grid(row=10, column=1)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=11, column=0, columnspan=2)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        copies = self.copies_entry.get()
        self.library.add_book(title, author, genre, copies)
        self.update_output(f"Книга '{title}' добавлена.")

    def remove_book(self):
        title = self.title_entry.get()
        self.library.remove_book(title)
        self.update_output(f"Книга '{title}' удалена.")

    def add_reader(self):
        name = self.reader_name_entry.get()
        surname = self.reader_surname_entry.get()
        ticket = self.ticket_entry.get()
        self.library.add_reader(name, surname, ticket)
        self.update_output(f"Читатель {name} {surname} добавлен.")

    def remove_reader(self):
        ticket = self.ticket_entry.get()
        self.library.remove_reader(ticket)
        self.update_output(f"Читатель с билетом {ticket} удалён.")

    def issue_book(self):
        title = self.title_entry.get()
        ticket = self.ticket_entry.get()
        self.library.issue_book(title, ticket)
        self.update_output(f"Книга '{title}' выдана читателю с билетом {ticket}.")

    def return_book(self):
        title = self.title_entry.get()
        ticket = self.ticket_entry.get()
        self.library.return_book(title, ticket)
        self.update_output(f"Книга '{title}' возвращена читателем с билетом {ticket}.")

    def save_data(self):
        self.library.save_data("library_data.json")
        self.update_output("Данные сохранены.")

    def load_data(self):
        self.library.load_data("library_data.json")
        self.update_output("Данные загружены.")

    def update_output(self, message):
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()