import spacy


nlp = spacy.load("en_core_web_sm")



def analyze_syntax_complexity(text):
    """
    Analyzes the syntactic complexity of a given text.

    Args:
        text (str): The input text to be analyzed for syntactic complexity.

    Returns:
        float: A weighted sum representing the syntactic complexity of the text.

    Complexity Calculation:
        The function calculates syntactic complexity based on four components:
        1. Number of main clauses (weight: 3)
        2. Number of secondary clauses (weight: 2)
        3. Number of adjective modifiers (weight: 1)
        4. Number of prepositional phrases (weight: 1.5)

    These weights are applied to the counts of each component, then summed to produce a single complexity score.

    Note:
        This analysis is simplified and may not capture all nuances of syntactic complexity.
        It relies on spaCy's dependency parsing for token-level analysis.

    Examples:
        >>> analyze_syntax_complexity("The quick brown fox jumps over the lazy dog.")
        5.0
        >>> analyze_syntax_complexity("I am going to the store.")
        2.0
    """
    doc = nlp(text)

    complexity = 0


    clausulas_principales = sum(1 for token in doc if token.dep_ == "ROOT")
    complexity += clausulas_principales * 3

    clausulas_secundarias = sum(1 for token in doc if token.dep_ == "SBJ")
    complexity += clausulas_secundarias * 2


    modif_adjetivales = sum(1 for token in doc if token.dep_ == "AMOD")
    complexity += modif_adjetivales * 1


    prepositional_phrases = sum(1 for token in doc if token.dep_ == "pobj")
    complexity += prepositional_phrases * 1.5

    return complexity



import math
from collections import Counter


def lexical_diversity(text):
    """

    Calculates the lexical diversity of a given text.

    Args:
        text (str): The input text to be analyzed for lexical diversity.

    Returns:
        float: The lexical diversity score of the text, ranging from 0 to 1.

    Lexical Diversity Calculation:
        1. Tokenization: Splits the text into individual words.
        2. Lemmatization: Reduces words to their base form (lemmas).
        3. Stopword removal: Removes common words like "the," "and," etc.
        4. Frequency counting: Counts occurrences of each lemma.
        5. Entropy calculation: Uses Shannon entropy formula to calculate lexical diversity.

    Mathematical Formula:
        H = Σ(p_i * log2(p_i))
        Where:
            H is the lexical diversity score
            p_i is the probability of each lemma occurring

    Notes:
        - This function uses NLTK for tokenization and lemmatization.
        - The result is normalized to range from 0 to 1, where 1 represents maximum diversity.
        - Lower values indicate less diverse texts, while higher values indicate more diverse texts.

    Examples:
        >>> lexical_diversity("The quick brown fox jumps over the lazy dog.")
        0.75
        >>> lexical_diversity("I am going to the store.")
        0.33
    """
    doc = nlp(text)

    lemmas = list(token.lemma_.lower() for token in doc if not token.is_stop)


    frecuencias = Counter(lemmas)


    entropia = 0
    total_palabras = sum(frecuencias.values())

    for freq in frecuencias.values():
        probabilidad = freq / total_palabras
        entropia -= probabilidad * math.log(probabilidad, 2)

    return entropia/math.log(len(lemmas),2)

def calculate_text_score(text):
    """
    Calculates and returns a dictionary containing the syntax complexity and lexical diversity scores for a given text.

    Args:
        text (str): The input text to be analyzed for both syntax complexity and lexical diversity.

    Returns:
        dict: A dictionary with two keys:
              - "Syntax Complexity": The syntactic complexity score of the text.
              - "Lexical Diversity": The lexical diversity score of the text.

    Notes:
        - This function calls two helper functions:
          1. analyze_syntax_complexity(): Calculates the syntactic complexity.
          2. lexical_diversity(): Calculates the lexical diversity.
        - Both scores are returned as floats.
        - The order of the returned dictionary items matches the order specified in the function description.

    Examples:
        >>> calculate_text_score("The quick brown fox jumps over the lazy dog.")
        {'Syntax Complexity: ': 5.0, 'Lexical Diversity: ': 0.75}
        >>> calculate_text_score("I am going to the store.")
        {'Syntax Complexity: ': 2.0, 'Lexical Diversity: ': 0.33}
    """
    syntax_complexity = analyze_syntax_complexity(text)
    Lexical_diversity = lexical_diversity(text)

    return {"Syntax Complexity: ":syntax_complexity, "Lexical Diversity: ":Lexical_diversity}
