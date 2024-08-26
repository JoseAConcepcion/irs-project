import json

class ReviewExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.asin_data = {}

    def extract_reviews(self):
        """Extrae comentarios, helpful votes y ratings por cada asin."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Parsear cada línea como JSON
                    review = json.loads(line.strip())

                    # Extraer los datos relevantes
                    asin = review.get('asin')
                    rating = review.get('overall')  # Cambia 'rating' a 'overall' si es necesario
                    helpful_vote = review.get('helpful')  # Cambia 'helpful_vote' a 'helpful' si es necesario
                    text = review.get('reviewText')  # Cambia 'text' a 'reviewText' si es necesario

                    # Si el asin no está en el diccionario, inicialízalo
                    if asin not in self.asin_data:
                        self.asin_data[asin] = []

                    # Añadir el comentario, el helpful_vote y el rating a la lista del asin
                    self.asin_data[asin].append({
                        'text': text,
                        'helpful_vote': helpful_vote,
                        'rating': rating
                    })

                except json.JSONDecodeError:
                    # Manejo básico de errores si la línea no es un JSON válido
                    print(f"Error al procesar la línea: {line}")

        return self.asin_data

# Ejemplo de uso:
# extractor = ReviewExtractor('/ruta/al/archivo/Musical_instruments_reviews.csv')
# data = extractor.extract_reviews()
# print(data)
