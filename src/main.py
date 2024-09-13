"""
Main application class for review ranking analysis.

This class represents the main application that uses Tkinter to create a graphical interface.
"""
import tkinter as tk
from vistas.vista1 import Vista1
from vistas.vista2 import Vista2
from data_processing import load as ld

from data_structure.trie import Trie


class Aplicacion(tk.Tk):
    """
        Main class that creates and manages the main window of the application.

        Attributes:
            title (str): The title of the window.
            geometry (str): The initial geometry of the window.
            trie (Trie): A Trie object for storing and processing data.
            vista1 (Vista1): An instance of the view 1.
            vista2 (Vista2): An instance of the view 2.

        Methods:
            __init__(self): Constructor of the class.
            pack(self, *args, **kwargs): Display the current view in the window.
        """
    def __init__(self):
        super().__init__()
        self.title("Reviews Ranking Analysis")
        self.geometry('1000x800')

        self.trie =  Trie()
        # Inicializar las vistas
        self.vista1 = Vista1(self)
        self.vista2 = Vista2(self, reviews=None, trie=self.trie, interests=[])


        # Mostrar la vista 1 al inicio
        self.vista1.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
