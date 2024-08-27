from data_processing.analyze import calculate_text_score
class Quantify:
    def __init__(self, items):
        """
        Inicializa la clase Quantify con una lista de objetos.
        
        :param items: Lista de objetos que contienen los atributos necesarios para el cálculo.
        """
        self.items = items

    def rank_helpful_votes(self):
        # Inicializar una variable para almacenar el máximo
        max_helpful_vote = 0

        # Iterar sobre el diccionario de reseñas
        for key, reviews in self.items.items():
            for review in reviews:
                # Comprobar si 'helpful_vote' está en el diccionario
                if 'helpful_vote' in review:
                    # Actualizar el máximo si es necesario
                    max_helpful_vote = max(max_helpful_vote, review['helpful_vote'])

        # Si no hay votos útiles, establecer max_helpful_vote en 1 para evitar división por cero
        if max_helpful_vote == 0:
            return self.items
        # Calcular el ranking y actualizar ranking_value
        for asin, entries in self.items.items():
            for entry in entries:
                # Verificar que 'helpful_vote' está en el diccionario
                if 'helpful_vote' in entry:
                    entry['comment_ranking_value'] += entry['helpful_vote'] / max_helpful_vote

        self.update_item_ranking_value()
        return self.items


    def calculate_features(self, item):
        """
        Lógica para calcular el ranking basado en características.
        
        :param item: Objeto del cual se extraen las características.
        :return: Número de características del objeto.
        """
        return len(item.features)

    def calculate_text_analysis(self):
        """
        Lógica para calcular el ranking basado en análisis de texto.

        :return: Resultado del análisis de texto del objeto.
        """
        for asin, entries in self.items.items():
            texts = [entry['text'] for entry in entries[0:len(entries)-1]]
            scores = [calculate_text_score(item) for item in texts]
            max_syntax_complexity = 0
            for result in scores:
                if result['Syntax Complexity: ']>max_syntax_complexity:
                    max_syntax_complexity = result['Syntax Complexity: ']
            asign_scores = []
            for score in scores:
                asign_scores.append(((score['Syntax Complexity: ']/max_syntax_complexity)+score['Lexical Diversity: '])/2)
            for i in range(len(entries)-1):
                entries[i]['comment_ranking_value'] = asign_scores[i]
        self.update_item_ranking_value()
        return self.items

    def calculate_length(self):
        """
        Lógica para calcular el ranking basado en longitud.

        :return: Longitud del objeto.
        """
        max_length = 0
        for asin, entries in self.items.items():
            lengths = [len(entry['text']) for entry in entries[0:len(entries)-1]]
            max_length = max(lengths) if max(lengths) > max_length else max_length

        for asin, entries in self.items.items():
            for entry in entries[0:len(entries)-1]:
                entry['comment_ranking_value'] += len(entry['text'])/max_length

        self.update_item_ranking_value()
        return self.items
    
    def update_item_ranking_value(self):
        # Iterar sobre el diccionario de reseñas
        for key, reviews in self.items.items():
            total_comment_ranking = 0
            count = 0
            
            # Sumar los valores de comment_ranking y contar las reseñas válidas
            for review in reviews:
                if 'comment_ranking_value' in review:
                    total_comment_ranking += review['comment_ranking_value']
                    count += 1
            
            # Calcular el item_ranking_value
            if count > 0:
                item_ranking_value = total_comment_ranking / count
            else:
                item_ranking_value = 0  # O cualquier valor por defecto que desees

            # Actualizar el item_ranking_value en la última reseña o en un lugar específico
            # Aquí asumimos que quieres actualizar el último elemento de la lista de reseñas
            if reviews:
                reviews[-1]['item_ranking_value'] = item_ranking_value

