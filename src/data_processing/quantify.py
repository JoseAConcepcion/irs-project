from data_processing.analyze import calculate_text_score
from data_processing.feature_extraction import feature_extractor
class Quantify:
    def __init__(self, items):
        """
        Initializes the Quantify class with a list of objects.

        :param items: List of objects containing the necessary attributes for calculation.
        """
        self.items = items
        for asin, entries in self.items.items():
            for entry in entries:
                entry['comment_ranking_value'] = 0
        self.update_item_ranking_value()

    def rank_helpful_votes(self):
        max_helpful_vote = 0


        for key, reviews in self.items.items():
            for review in reviews:

                if 'helpful_vote' in review:

                    max_helpful_vote = max(max_helpful_vote, review['helpful_vote'])


        if max_helpful_vote == 0:
            return self.items

        for asin, entries in self.items.items():
            for entry in entries:

                if 'helpful_vote' in entry:
                    entry['comment_ranking_value'] += entry['helpful_vote'] / max_helpful_vote

        self.update_item_ranking_value()
        return self.items


    def calculate_features(self, item):
        """
        Logic to calculate the ranking based on features.

        :param item: Object from which features are extracted.
        :return: Number of features of the object.
        """
        return len(item.features)

    def calculate_text_analysis(self):
        """
                Logic to calculate the ranking based on text analysis.

                :return: Result of the text analysis of the object.
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
                entries[i]['comment_ranking_value'] += asign_scores[i]
        self.update_item_ranking_value()
        return self.items

    def calculate_length(self):
        """
        Logic to calculate the ranking based on length.

        :return: Length of the object.
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
        """
                        Updates the item ranking value for all items.

                        This method calculates the average comment ranking value for each item,
                        excluding the last review, and assigns it to the last review of each item.
        """
        for key, reviews in self.items.items():
            total_comment_ranking = 0
            count = 0
            

            for review in reviews[0:len(reviews)-1]:
                if 'comment_ranking_value' in review:
                    total_comment_ranking += review['comment_ranking_value']
                    count += 1
            

            if count > 0:
                item_ranking_value = total_comment_ranking / count
            else:
                item_ranking_value = 0

            if reviews:
                reviews[-1]['item_ranking_value'] = item_ranking_value

    def calculate_features_for_item(self, item):
        """
                        Extracts features for a given item and stores them in the corresponding reviews.

                        :param item: Object for which features are extracted.
                """
        ft = feature_extractor()
        features = ft.get_response(str(self.items[item]))

        for feat in features.items():
            item_id, reviews = feat
            data, positivity_value = self.parse_features(reviews)
            i = 1
            for review in self.items[item]:
                review_key = 'review' + str(i)
                if review_key in data:
                    review['features'] = data[review_key]
                    review['features_positivity'] = positivity_value
                else:
                    continue
                i += 1

    def parse_features(self, reviews):
        """
                        Parses the extracted features and calculates the overall positivity score.

                        :return: Dictionary of parsed features and the overall positivity score.
                """
        parsed_data = {}
        positivity = 0
        total_count = 0

        for review, features in reviews.items():
            parsed_data[review] = {}
            for feature, words in features.items():
                parsed_data[review][feature] = []
                if isinstance(words[0], list):
                    for word_info in words:
                        word, score = word_info
                        parsed_data[review][feature].append([word, score])
                        positivity += score 
                        total_count += 1  
                else:
                    word, score = words
                    parsed_data[review][feature].append([word, score])
                    positivity += score  # Sumar la puntuación a positivity
                    total_count += 1  # Incrementar el contador total

        # Calcular el promedio si hay puntuaciones
        if total_count > 0:
            positivity = positivity / total_count

        return parsed_data, positivity
