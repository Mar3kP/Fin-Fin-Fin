import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("800x500")
root.title("Księgarnia")
root.iconbitmap("ksionszka.ico")


root.mainloop()



class Ksionszka():
    def __init__(self, tytul, strony):
        self.tytul = tytul
        self.strony = strony

Ksiega1 = Ksionszka("Hobbit", 390)



class Lista():
    def __init__(self):
        self.lista = []
    def add(self, ksionszka):
        (self.lista).append(ksionszka)
        



