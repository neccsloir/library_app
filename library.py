from library_logic import Library
from library_ui import LibraryApp
import tkinter as tk

if __name__ == "__main__":
    library = Library()
    root = tk.Tk()
    root.title("Библиотека")
    app = LibraryApp(root, library)
    root.mainloop()

# library.py - основной файл, который соединяет все части
# library_logic.py - логика библиотеки (работа с книгами, читателями и т д)
# library_ui.py - интерфейс
#
#
#
#
