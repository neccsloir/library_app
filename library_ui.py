import tkinter as tk
from tkinter import messagebox


class LibraryApp:
    def __init__(self, root, library):
        self.library = library

        # Поля для ввода данных о книгах
        tk.Label(root, text="Название книги:").grid(row=0, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)

        tk.Label(root, text="Автор:").grid(row=1, column=0)
        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1)

        tk.Label(root, text="Год издания:").grid(row=2, column=0)
        self.year_entry = tk.Entry(root)
        self.year_entry.grid(row=2, column=1)

        tk.Label(root, text="Жанр:").grid(row=3, column=0)
        self.genre_entry = tk.Entry(root)
        self.genre_entry.grid(row=3, column=1)

        tk.Label(root, text="Количество экземпляров:").grid(row=4, column=0)
        self.copies_entry = tk.Entry(root)
        self.copies_entry.grid(row=4, column=1)

        # Поля для ввода данных о читателях
        tk.Label(root, text="Имя читателя:").grid(row=5, column=0)
        self.reader_name_entry = tk.Entry(root)
        self.reader_name_entry.grid(row=5, column=1)

        tk.Label(root, text="Фамилия читателя:").grid(row=6, column=0)
        self.reader_surname_entry = tk.Entry(root)
        self.reader_surname_entry.grid(row=6, column=1)

        tk.Label(root, text="Номер читательского билета:").grid(row=7, column=0)
        self.ticket_number_entry = tk.Entry(root)
        self.ticket_number_entry.grid(row=7, column=1)

        # Кнопки для взаимодействия
        tk.Button(root, text="Добавить книгу", command=self.add_book).grid(row=8, column=0)
        tk.Button(root, text="Удалить книгу", command=self.remove_book).grid(row=8, column=1)
        tk.Button(root, text="Добавить читателя", command=self.add_reader).grid(row=9, column=0)
        tk.Button(root, text="Удалить читателя", command=self.remove_reader).grid(row=9, column=1)
        tk.Button(root, text="Выдать книгу", command=self.issue_book).grid(row=10, column=0)
        tk.Button(root, text="Вернуть книгу", command=self.return_book).grid(row=10, column=1)
        tk.Button(root, text="Сохранить данные", command=self.save_data).grid(row=11, column=0)
        tk.Button(root, text="Загрузить данные", command=self.load_data).grid(row=11, column=1)

        # Поле для отображения информации
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=12, column=0, columnspan=2)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        genre = self.genre_entry.get()
        copies = self.copies_entry.get()
        if title and author and year and genre and copies.isdigit():
            self.library.add_book(title, author, year, genre, int(copies))
            self.output_text.insert(tk.END, f"Книга '{title}' добавлена в библиотеку.\n")
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля для книги корректно.")

    def remove_book(self):
        title = self.title_entry.get()
        if title:
            self.library.remove_book(title)
            self.output_text.insert(tk.END, f"Книга '{title}' удалена из библиотеки.\n")
        else:
            messagebox.showerror("Ошибка", "Введите название книги для удаления.")

    def add_reader(self):
        name = self.reader_name_entry.get()
        surname = self.reader_surname_entry.get()
        ticket_number = self.ticket_number_entry.get()
        if name and surname and ticket_number:
            self.library.add_reader(name, surname, ticket_number)
            self.output_text.insert(tk.END, f"Читатель '{name} {surname}' добавлен.\n")
        else:
            messagebox.showerror("Ошибка", "Заполните все поля для добавления читателя.")

    def remove_reader(self):
        ticket_number = self.ticket_number_entry.get()
        if ticket_number:
            self.library.remove_reader(ticket_number)
            self.output_text.insert(tk.END, f"Читатель с билетом №{ticket_number} удалён.\n")
        else:
            messagebox.showerror("Ошибка", "Введите номер читательского билета для удаления.")

    def issue_book(self):
        title = self.title_entry.get()
        ticket_number = self.ticket_number_entry.get()
        if title and ticket_number:
            if self.library.issue_book(title, ticket_number):
                self.output_text.insert(tk.END, f"Книга '{title}' выдана читателю с билетом №{ticket_number}.\n")
            else:
                messagebox.showerror("Ошибка", "Книга не найдена или нет в наличии.")
        else:
            messagebox.showerror("Ошибка", "Введите название книги и номер читательского билета.")

    def return_book(self):
        title = self.title_entry.get()
        ticket_number = self.ticket_number_entry.get()
        if title and ticket_number:
            if self.library.return_book(title, ticket_number):
                self.output_text.insert(tk.END, f"Книга '{title}' возвращена читателем с билетом №{ticket_number}.\n")
            else:
                messagebox.showerror("Ошибка", "Книга не найдена или не была выдана этому читателю.")
        else:
            messagebox.showerror("Ошибка", "Введите название книги и номер читательского билета.")

    def save_data(self):
        self.library.save_data("library_data.json")
        self.output_text.insert(tk.END, "Данные успешно сохранены в 'library_data.json'.\n")

    def load_data(self):
        self.library.load_data("library_data.json")
        self.output_text.insert(tk.END, "Данные успешно загружены из 'library_data.json'.\n")