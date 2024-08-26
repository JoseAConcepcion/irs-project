import spacy

# Cargar el modelo de SpaCy para ingles
nlp = spacy.load("en_core_web_sm")


# Función para analizar la complejidad sintáctica
def analyze_syntax_complexity(text):
    doc = nlp(text)

    complexity = 0

    # Count main clauses
    clausulas_principales = sum(1 for token in doc if token.dep_ == "ROOT")
    complexity += clausulas_principales * 3
    # Count subordinate clauses
    clausulas_secundarias = sum(1 for token in doc if token.dep_ == "SBJ")
    complexity += clausulas_secundarias * 2

    # Count adjectival modifiers
    modif_adjetivales = sum(1 for token in doc if token.dep_ == "AMOD")
    complexity += modif_adjetivales * 1

    # Count prepositional phrases
    prepositional_phrases = sum(1 for token in doc if token.dep_ == "pobj")
    complexity += prepositional_phrases * 1.5

    return complexity



import math
from collections import Counter


def lexical_diversity(text):
    doc = nlp(text)
    # Obtener todas las formas léxicas únicas
    lemmas = list(token.lemma_.lower() for token in doc if not token.is_stop)

    # Contar frecuencia de cada forma léxica
    frecuencias = Counter(lemmas)

    # Calcular entropía de Shannon
    entropia = 0
    total_palabras = sum(frecuencias.values())

    for freq in frecuencias.values():
        probabilidad = freq / total_palabras
        entropia -= probabilidad * math.log(probabilidad, 2)

    return entropia/math.log(len(lemmas),2)

def calculate_text_score(text):

    syntax_complexity = analyze_syntax_complexity(text)
    Lexical_diversity = lexical_diversity(text)

    return {"Syntax Complexity: ":syntax_complexity, "Lexical Diversity: ":Lexical_diversity}

# if __name__ == '__main__':
#     freeze_support()
#
#     texts = ["The sun rises in the east and sets in the west. It is a beautiful day today."
#
#     ,"Although the weather forecast predicted rain, the sun unexpectedly emerged from behind the clouds, casting a warm glow over the bustling city streets, much to the delight of the locals who had been eagerly awaiting the arrival of spring."
#
#     ,"The cat chased the mouse. The dog barked at the cat. The bird sang in the tree. The flower bloomed in the garden."
#
#     ,"The dog run fast. They're going to the park. Its a beautiful day outside."
#
#     ,"The cat meowed. The dog barked loudly. The bird sang a beautiful melody. The butterfly fluttered gracefully among the flowers in the garden."
#
#     ,"It was a sunny day, but it was raining at the same time. The cat chased the dog, but the dog was bigger than the cat."
#
#     ,"The incredibly huge, gigantic, massive, colossal mountain towered majestically over the tiny, minuscule, diminutive village nestled snugly at its base."
#
#     ,"The quick brown fox jumps over the lazy dog. It is a sunny day. Let's go to the park!"
#
#     ,"The quick brown fox jumps over the lazy dog! It is a sunny day? Let's go to the park."
#
#     ,"The cat chased the mouse. Although the weather forecast predicted rain, the sun unexpectedly emerged from behind the clouds, casting a warm glow over the bustling city streets, much to the delight of the locals who had been eagerly awaiting the arrival of spring. The dog barked loudly. Its a beautiful day outside."]
#
#     for text in texts:
#         print(calculate_text_score(text))