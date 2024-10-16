import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("800x500")
root.title("Księgarnia")
root.iconbitmap("ksionszka.ico")

class Ksiegarnia1():
    def __init__(self):
        self.ksiegarnia = []

    def add(self, ksionszka):
        self.ksiegarnia.append(ksionszka)

    def show(self):
        print(self.ksiegarnia)

    def remove(self, miejsce):
        self.ksiegarnia.remove(miejsce)

    def edit(self, miejsce, tytul):
        self.ksiegarnia[miejsce] = tytul

root.mainloop()