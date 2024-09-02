import tkinter as tk
from tkinter import filedialog
import os
from data_processing import load as ld

from vistas.vista2 import Vista2
from data_structure.trie import Trie 


class Vista1(tk.Frame):
    def __init__(self, parent):
        """
                Initializes the main window of the application.

                :param parent: Parent widget (usually the root window).
                """
        super().__init__(parent)
        
        self.lbl = tk.Label(self, text="Bienvenido, por favor cargue sus datos.", font=("Arial Bold", 30))
        self.lbl.grid(column=0, row=0)

        self.load_user_data_button = tk.Button(self, text="Cargar Datos de Usuario", command=self.load_user_data)
        self.load_user_data_button.grid(column=0, row=1)

        self.load_review_data_button = tk.Button(self, text="Cargar Datos de los Reviews", command=self.select_file)
        self.load_review_data_button.grid(column=0, row=2)

        self.calculate_ranking_button = tk.Button(self, text="Calcular el ranking", command=self.change_vist)
        self.calculate_ranking_button.grid(column=0, row=3)

        self.data = None

    def select_file(self):
        """
                Opens a file dialog to select a JSONL file and loads the review data.
                """
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON Lines files", "*.jsonl"), ("All files", "*.*")]
        )
        if file_path:
            self.selected_file = file_path
            self.lbl.configure(text=f"Archivo seleccionado: {file_path}")
            extractor = ld.ReviewExtractor(self.selected_file)
            self.data = extractor.extract_reviews()
            self.lbl.configure(text=f"Datos cargados!")

    def load_user_data(self):
        """
        Loads the user interests.
        """
        file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Text files", "*.txt")])
        
        if file_path:  
            with open(file_path, 'r') as file:
                self.user_data = file.readlines()  
            self.user_data = [line.strip() for line in self.user_data]

    def load_review_data(self):
        """
                Loads the review data (placeholder method, may need to be implemented).
                """
        self.lbl.configure(text="Reviews data loaded!!")

    def change_vist(self):
        """
                Switches to the second view after calculating the ranking.
                """
        self.pack_forget()

        self.trie = Trie()
        vista2 = Vista2(self.master, self.data, self.trie)

        vista2.pack(fill="both", expand=True)
