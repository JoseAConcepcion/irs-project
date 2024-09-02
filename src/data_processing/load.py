import json

import demoji


class ReviewExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.asin_data = {}

    def extract_reviews(self):
        """Extrae comentarios, helpful votes y ratings por cada asin."""

        for_feature_extraction = {}

        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Parse each line as a JSON
                    review = json.loads(line.strip())

                    # Extract relevant data
                    asin = review.get('asin')

                    rating = review.get('rating') 
                    helpful_vote = review.get('helpful_vote')  
                    text = review.get('text')  


                    if asin not in self.asin_data:
                        self.asin_data[asin] = []

                        for_feature_extraction[asin] = []



                    self.asin_data[asin].append({
                        'text': text,
                        'helpful_vote': helpful_vote,

                        'rating': rating,
                        'comment_ranking_value': 0,
                        'features': '',
                        'features_positivity': 0
                    })

                    for_feature_extraction[asin].append({
                        'text': text

                    })

                except json.JSONDecodeError:

                    print(f"Error al procesar la línea: {line}")


        for key in self.asin_data.keys():
            self.asin_data[key].append({'item_ranking_value': 0})

        output_file = "data.json"  # You can change the file name here
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(for_feature_extraction, outfile, indent=4)

        return self.asin_data

