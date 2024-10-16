import tkinter as tk
from tkinter import simpledialog, messagebox

class Ksiegarnia:
    def __init__(self):
        self.ksiegarnia = []

    def add(self, ksionszka):
        self.ksiegarnia.append(ksionszka)

    def show(self):
        return self.ksiegarnia  

    def remove(self, index):
        if 0 <= index < len(self.ksiegarnia):  
            self.ksiegarnia.pop(index)

    def edit(self, index, tytul):
        if 0 <= index < len(self.ksiegarnia):  
            self.ksiegarnia[index] = tytul

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.title("Księgarnia")
        self.root.iconbitmap("ksionszka.ico")
        
        self.library1 = Ksiegarnia()
        self.library2 = Ksiegarnia()
        
        self.current_library = None

        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        self.pick_ksiegarnia1 = tk.Button(self.main_frame, text="Księgarnia 1", command=self.select_library1)
        self.pick_ksiegarnia1.pack(pady=10)

        self.pick_ksiegarnia2 = tk.Button(self.main_frame, text="Księgarnia 2", command=self.select_library2)
        self.pick_ksiegarnia2.pack(pady=10)

        self.action_frame = tk.Frame(root)
        self.action_frame.pack(pady=20)

        self.add_button = tk.Button(self.action_frame, text="Dodaj Książkę", command=self.add_book)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(self.action_frame, text="Usuń Książkę", command=self.remove_book)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(self.action_frame, text="Edytuj Książkę", command=self.edit_book)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.show_button = tk.Button(self.action_frame, text="Pokaż Książki", command=self.show_books)
        self.show_button.pack(side=tk.LEFT, padx=5)

        self.books_list = tk.Listbox(root, width=100)
        self.books_list.pack(pady=20)

    def select_library1(self):
        self.current_library = self.library1
        self.update_books_list()

    def select_library2(self):
        self.current_library = self.library2
        self.update_books_list()

    def add_book(self):
        if self.current_library is not None:
            tytul = simpledialog.askstring("Dodaj Książkę", "Podaj tytuł książki:")
            if tytul:
                self.current_library.add(tytul)
                self.update_books_list()

    def remove_book(self):
        if self.current_library is not None and self.books_list.curselection():
            index = self.books_list.curselection()[0]
            self.current_library.remove(index)
            self.update_books_list()

    def edit_book(self):
        if self.current_library is not None and self.books_list.curselection():
            index = self.books_list.curselection()[0]
            nowy_tytul = simpledialog.askstring("Edytuj Książkę", "Podaj nowy tytuł książki:")
            if nowy_tytul:
                self.current_library.edit(index, nowy_tytul)
                self.update_books_list()

    def show_books(self):
        if self.current_library is not None:
            books = self.current_library.show()
            messagebox.showinfo("Książki", "\n".join(books))

    def update_books_list(self):
        self.books_list.delete(0, tk.END)
        if self.current_library is not None:
            for book in self.current_library.show():
                self.books_list.insert(tk.END, book)

root = tk.Tk()
app = App(root)
root.mainloop()