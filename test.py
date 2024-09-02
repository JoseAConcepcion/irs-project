import data_processing.load as ld
import json
from data_processing.feature_extraction import feature_extractor as featex

data = ld.ReviewExtractor("/home/joseac/Carrera/3er Año/2do Semestre/SRI/Proyecto Final/GUI/data/Digital_Music.jsonl")
reviews = data.extract_reviews()

def print_reviews(self):
    """Imprime el texto de cada review."""
    for asin, reviews in self.asin_data.items():
        print(f"ASIN: {asin}")
        for review in reviews:
            print(f"- Review: {review['text']}")

# print(reviews["B004RQ2IRG"])

ft = featex()

comments = "B083QN4Y6H" 

for asin, info in reviews.items():
    if asin == "B083QN4Y6H":
        for texts in reviews["B083QN4Y6H"]:
            coment = texts["text"]
            comments += "\n" + coment
            print(coment)

print("respuesta del modelo \n")
response = ft.get_response("Jajajajaja que buen item crack")
print(response)

            # file_name = 'data.json'
            # # Abre el archivo en modo escritura
            # with open(file_name, 'w') as json_file:
            #     # Usa json.dump para escribir el objeto en el archivo
            #     json.dump(data, json_file, indent=4)
