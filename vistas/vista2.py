import tkinter as tk
import random
import speedtest
from data_processing.quantify import Quantify
from data_structure.trie import Trie

class Vista2(tk.Frame):
    def __init__(self, parent, reviews, trie):
        super().__init__(parent)
        self.trie = trie
        
        # Título
        self.titulo = tk.Label(self, text="Ranking de Reviews", font=("Arial Bold", 30))
        self.titulo.grid(column=0, row=0, pady=20)

        # Barra de búsqueda con autocompletado
        self.entry_var = tk.StringVar()
        self.entry_var.trace("w", self.update_suggestions)

        self.query_entry = tk.Entry(self, textvariable=self.entry_var, width=50)
        self.query_entry.grid(column=0, row=1, padx=10, pady=10)

        self.suggestion_listbox = tk.Listbox(self, height=5)
        self.suggestion_listbox.grid(column=0, row=2, padx=10, pady=10)
        self.suggestion_listbox.bind("<<ListboxSelect>>", self.autocomplete)

        # Botón de búsqueda
        self.buscar_button = tk.Button(self, text="Buscar", command=self.update_ranking)
        self.buscar_button.grid(column=1, row=1, padx=10)

        # Listbox para mostrar reviews
        self.review_listbox = tk.Listbox(self, height=10, width=40)
        self.review_listbox.grid(column=0, row=3, padx=10, pady=10)
        self.review_listbox.bind('<<ListboxSelect>>', self.mostrar_comentario)

        # Cajas de texto para mostrar comentarios
        self.comentario_text = tk.Text(self, height=20, width=80)
        self.comentario_text.grid(column=1, row=3, padx=10, pady=10)

        # Checkboxes
        self.checkbox_var1 = tk.BooleanVar()
        self.checkbox_var2 = tk.BooleanVar()
        self.checkbox_var3 = tk.BooleanVar()
        self.checkbox_var4 = tk.BooleanVar()

        self.checkbox1 = tk.Checkbutton(self, text="Incluir Votos de Utilidad", variable=self.checkbox_var1)
        self.checkbox1.grid(column=0, row=4, sticky='w', padx=10)

        self.checkbox2 = tk.Checkbutton(self, text="Inlcuir Análisis de Features", variable=self.checkbox_var2)
        self.checkbox2.grid(column=0, row=5, sticky='w', padx=10)

        self.checkbox3 = tk.Checkbutton(self, text="Inlcuir Análisis de estructura de texto", variable=self.checkbox_var3)
        self.checkbox3.grid(column=1, row=4, sticky='w', padx=10)

        self.checkbox4 = tk.Checkbutton(self, text="Incluir Longitud", variable=self.checkbox_var4)
        self.checkbox4.grid(column=1, row=5, sticky='w', padx=10)

        self.volver_button = tk.Button(self, text="Volver", command=self.volver_a_vista1)
        self.volver_button.grid(column=0, row=6, pady=10)

        self.update_button = tk.Button(self, text="Recalcular", command=self.update_ranking)
        self.update_button.grid(column=1, row=6, pady=11)
        
        self.feature_button = tk.Button(self, text="Analizar Features de este item", command=self.analyze_features)
        self.feature_button.grid(column=0, row=7, sticky='w', padx=10)

        if reviews is None:

        # Datos de ejemplo
            self.reviews = {
                "Review 1": "Excelente producto, superó mis expectativas.",
                "Review 2": "No estoy satisfecho con la calidad, esperaba más.",
                "Review 3": "Gran servicio al cliente, muy atentos y rápidos.",
                "Review 4": "El envío fue rápido, pero el paquete llegó dañado.",
                "Review 5": "Me encanta este producto, lo recomiendo al 100%.",
                "Review 6": "No funcionó como esperaba, decepcionado.",
                "Review 7": "Buena relación calidad-precio, volveré a comprar.",
                "Review 8": "El diseño es muy atractivo, me gusta mucho.",
                "Review 9": "Tardó un poco en llegar, pero valió la pena.",
                "Review 10": "Mal servicio, no respondieron a mis consultas.",
                "Review 11": "Producto de alta calidad, definitivamente lo volveré a comprar.",
                "Review 12": "No cumplió con lo prometido, muy insatisfecho.",
                "Review 13": "Excelente atención al cliente, muy amables.",
                "Review 14": "El producto llegó a tiempo y en perfectas condiciones.",
                "Review 15": "Me sorprendió lo bien que funciona, muy recomendable.",
                "Review 16": "No me gustó el color, pero la calidad es buena.",
                "Review 17": "Gran experiencia de compra, fácil y rápida.",
                "Review 18": "El producto es justo lo que necesitaba, gracias.",
                "Review 19": "No volveré a comprar, muy mala experiencia.",
                "Review 20": "El mejor producto que he comprado en mucho tiempo.",
                "Review 21": "El envío fue lento, pero el producto es bueno.",
                "Review 22": "Me encanta, lo uso todos los días.",
                "Review 23": "No es lo que esperaba, me decepcionó.",
                "Review 24": "Excelente calidad, lo recomiendo sin dudar.",
                "Review 25": "El servicio fue muy malo, no volveré a comprar aquí.",
                "Review 26": "Producto muy útil, estoy muy satisfecho.",
                "Review 27": "El diseño es bonito, pero no es muy funcional.",
                "Review 28": "Gran compra, lo volvería a hacer.",
                "Review 29": "No me gustó, no cumplió con mis expectativas.",
                "Review 30": "El mejor servicio al cliente que he tenido.",
                "Review 31": "El producto llegó rápido y en perfectas condiciones.",
                "Review 32": "Me encanta, es justo lo que buscaba.",
                "Review 33": "No lo recomendaría, no es de buena calidad.",
                "Review 34": "Excelente relación calidad-precio, muy satisfecho.",
                "Review 35": "El producto es bueno, pero el envío fue lento.",
                "Review 36": "Gran calidad, definitivamente lo volveré a comprar.",
                "Review 37": "No estoy contento con mi compra, esperaba más.",
                "Review 38": "El servicio fue excepcional, muy recomendables.",
                "Review 39": "El producto es increíble, lo uso todos los días.",
                "Review 40": "No cumplió con lo que prometía, decepcionante.",
                "Review 41": "Me encanta, es de muy buena calidad.",
                "Review 42": "El envío fue rápido, pero el producto no es bueno.",
                "Review 43": "Gran experiencia de compra, todo perfecto.",
                "Review 44": "No lo volvería a comprar, no me gustó.",
                "Review 45": "Excelente producto, lo recomiendo a todos.",
                "Review 46": "El servicio al cliente fue muy útil y amable.",
                "Review 47": "El producto llegó a tiempo y en perfectas condiciones.",
                "Review 48": "Me sorprendió lo bien que funciona, muy recomendable.",
                "Review 49": "No estoy satisfecho, no cumplió con mis expectativas.",
                "Review 50": "Gran calidad y buen precio, estoy muy contento."
            }
        else:
            self.reviews = reviews

        for key in self.reviews.keys():
            self.trie.insert(str(key))

        self.show_ranking()

    def show_ranking(self):
        # Limpiar el Listbox antes de cargar las reseñas
        self.review_listbox.delete(0, tk.END)
        # Cargar reviews en el Listbox
        for review in self.reviews.keys():
            self.review_listbox.insert(tk.END, review)

    def mostrar_comentario(self, event):
        # Obtener el índice del elemento seleccionado
        seleccion = self.review_listbox.curselection()
        if seleccion:
            index = seleccion[0]
            review_seleccionado = self.review_listbox.get(index)
            comentarios = self.reviews[review_seleccionado]
            ranking = str(self.reviews[review_seleccionado][-1]["item_ranking_value"])
            # Mostrar el comentario en la caja de texto
            self.comentario_text.delete(1.0, tk.END) 
            self.comentario_text.insert(tk.END, "el ranking general del item aqui aqui " + ranking + " \n\n ")
            
            for item in comentarios[:-1]:
                texto = item["text"]
                votos_útiles = str(item["helpful_vote"])
                ranking_comentario = str(item["comment_ranking_value"])
                features = str(item["features"])
                features_value = str(item['features_positivity'])

                # Construir la cadena a insertar en el widget de texto
                comentario_str = (
                    f"{texto}\n\n"
                    f"votes {votos_útiles}\n"
                    f"comment ranking {ranking_comentario}\n"
                    f"features {features}\n"
                    f"features positivity {features_value}\n\n"
                )

            # Insertar el texto en el widget
            self.comentario_text.insert(tk.END, comentario_str)

    def sort_reviews_by_ranking(self):
        # Obtener las claves del diccionario
        keys = list(self.reviews.keys())
        
        # Ordenar las claves según el item_ranking_value del último diccionario en la lista de reseñas
        sorted_keys = sorted(keys, key=lambda k: self.reviews[k][-1].get('item_ranking_value', 0), reverse=True)
        
        # Crear un nuevo diccionario con el orden basado en item_ranking_value
        sorted_reviews = {key: self.reviews[key] for key in sorted_keys}
        
        # Actualizar self.reviews con las reseñas ordenadas
        self.reviews = sorted_reviews

    def analyze_features(self):
        seleccion = self.review_listbox.curselection()
        if seleccion:
            index = seleccion[0]
            review_seleccionado = self.review_listbox.get(index)
            qt = Quantify(self.reviews)
            qt.calculate_features_for_item(review_seleccionado)
            self.mostrar_comentario(None)

    def update_suggestions(self, *args):
        prefix = self.entry_var.get()
        suggestions = self.trie.search(prefix)
        self.suggestion_listbox.delete(0, tk.END)
        for suggestion in suggestions:
            self.suggestion_listbox.insert(tk.END, suggestion)

    def autocomplete(self, event):
        selected_index = self.suggestion_listbox.curselection()
        if selected_index:
            selected_text = self.suggestion_listbox.get(selected_index)
            self.entry_var.set(selected_text)
            self.suggestion_listbox.delete(0, tk.END)
    

    def update_ranking(self):
        query = self.query_entry.get()
        opciones_seleccionadas = []
        qt = Quantify(self.reviews)
        

        if self.checkbox_var1.get():
            opciones_seleccionadas.append("Incluir Votos de Utilidad")
            self.reviews = qt.rank_helpful_votes()
        if self.checkbox_var2.get():
            opciones_seleccionadas.append("Incluir Análisis de Features")
        if self.checkbox_var3.get():
            opciones_seleccionadas.append("Incluir Análisis de estructura de texto")
            self.reviews = qt.calculate_text_analysis()
        if self.checkbox_var4.get():
            opciones_seleccionadas.append("Incluir Longitud")
            self.reviews = qt.calculate_length()

        # Limpiar el contenido anterior
        self.comentario_text.delete(1.0, tk.END)

        # Mostrar resultados en función de la búsqueda y las opciones seleccionadas
        self.comentario_text.insert(tk.END, f"Consulta: {query}\nOpciones seleccionadas: {', '.join(opciones_seleccionadas)}")
        
        # Mezclar las reseñas y mostrar el ranking
        self.sort_reviews_by_ranking()
        self.show_ranking()

    def volver_a_vista1(self):
        self.pack_forget()  # Ocultar la vista actual
        self.master.vista1.pack(fill="both", expand=True)  # Mostrar la vista 1
