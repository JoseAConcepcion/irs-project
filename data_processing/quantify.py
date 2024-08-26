class Quantify:
    def __init__(self, items):
        """
        Inicializa la clase Quantify con una lista de objetos.
        
        :param items: Lista de objetos que contienen los atributos necesarios para el cálculo.
        """
        self.items = items

    def rank_helpful_votes(self):
        for asin, entries in self.items.items():
            # Extraer todos los helpful_votes
            helpful_votes = [entry['helpful_vote'] for entry in entries]
            # for entry in entries:
            #     print(entry)
            # Verificar que hay votos útiles para evitar división por cero
            if helpful_votes:
                max_helpful_vote = max(helpful_votes)
                if max_helpful_vote == 0:
                    max_helpful_vote = 1
                
                # Calcular el ranking y actualizar ranking_value
                for entry in entries:
                    entry['ranking_value'] += entry['helpful_vote'] / max_helpful_vote


    def calculate_features(self, item):
        """
        Lógica para calcular el ranking basado en características.
        
        :param item: Objeto del cual se extraen las características.
        :return: Número de características del objeto.
        """
        return len(item.features)

    def calculate_text_analysis(self, item):
        """
        Lógica para calcular el ranking basado en análisis de texto.
        
        :param item: Objeto del cual se extrae el análisis de texto.
        :return: Resultado del análisis de texto del objeto.
        """
        return item.text_analysis

    def calculate_length(self, item):
        """
        Lógica para calcular el ranking basado en longitud.
        
        :param item: Objeto del cual se extrae la longitud.
        :return: Longitud del objeto.
        """
        return item.length
