import tkinter as tk
from vistas.vista1 import Vista1
from vistas.vista2 import Vista2
from data_processing import load as ld
from data_structure.trie import Trie

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reviews Ranking Analysis")
        self.geometry('1000x800')
        self.trie =  Trie()
        # Inicializar las vistas
        self.vista1 = Vista1(self)
        self.vista2 = Vista2(self, reviews=None, trie=self.trie)

        # Mostrar la vista 1 al inicio
        self.vista1.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
