import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Analyze the sentiment of the following Tweets and classify them as POSITIVE, NEGATIVE, or NEUTRAL. \"It's so beautiful today!\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "POSITIVE",
      ],
    },
    {
      "role": "user",
      "parts": [
        "\"It's so cold today I can't feel my feet...\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "NEGATIVE",
      ],
    },
    {
      "role": "user",
      "parts": [
        "\"The weather today is perfectly adequate.\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "NEUTRAL",
      ],
    },
    {
      "role": "user",
      "parts": [
        "The hotel was nice. The service was excellent but the food was terrible.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "NEGATIVE \n\nWhile the hotel and service were positive, the negative experience with the food outweighs the positives, making the overall sentiment negative. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "The hotel was nice. The service was excellent but the food was terrible.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here's how we can break down the sentiment and extract features:\n\n**Sentiment:**  NEGATIVE\n\n**Reasoning:** While the hotel and service receive positive mentions (\"nice\" and \"excellent\"), the negative experience with the food (\"terrible\") carries more weight, leading to an overall negative sentiment.\n\n**Feature Extraction:**\n\nWe can represent the features and their associated sentiment scores using a dictionary:\n\n```python\nfeatures = {\n    \"hotel\": (\"nice\", 0.6),  # Assuming \"nice\" has a moderate positivity score\n    \"service\": (\"excellent\", 0.9), # Assuming \"excellent\" has a high positivity score\n    \"food\": (\"terrible\", 0.1) # Assuming \"terrible\" has a very low (close to negative) score\n}\n```\n\n**Explanation:**\n\n* **Key:** The key represents the feature being reviewed (e.g., \"hotel\", \"service\", \"food\").\n* **Value:** The value is a tuple containing:\n    * **Adjective:** The adjective used to describe the feature.\n    * **Sentiment Score:** A numerical representation of the sentiment associated with the adjective (from 0.0 to 1.0, with 0.0 being extremely negative and 1.0 being extremely positive).\n\n**Important Note:** The sentiment scores are subjective and can vary based on how you define your scale. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Hotel Villanueva \nReview 1\nThe hotel was nice. The service was excellent but the food was terrible.\nReview 2 \nI did not like at all the service.\nReview 3\nThe rooms were dirty.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here's the breakdown of the sentiment and feature extraction for Hotel Villanueva:\n\n**Sentiment:** NEGATIVE\n\n**Reasoning:**  While there is one positive mention (\"nice\" for the hotel), the negative experiences with the service (\"terrible\" and \"did not like at all\") and the rooms (\"dirty\") outweigh the positive, resulting in an overall negative sentiment.\n\n**Feature Extraction:**\n\n```python\nHotelVillanueva = {\n    \"review1\": {\n        \"hotel\": (\"nice\", 0.6),  \n        \"service\": (\"excellent\", 0.9), \n        \"food\": (\"terrible\", 0.1) \n    },\n    \"review2\": {\n        \"service\": (\"did not like at all\", 0.1) \n    },\n    \"review3\": {\n        \"rooms\": (\"dirty\", 0.1)\n    }\n}\n```\n\n**Explanation:**\n\n* **Structure:** The output is organized as a dictionary with the hotel name as the key. Inside, each review is a key, and its features and sentiment scores are stored in nested dictionaries.\n* **Features:** The features represent the aspects of the hotel being reviewed.\n* **Adjectives:**  The adjectives used to describe the features are included.\n* **Sentiment Scores:** The scores are assigned based on the negativity or positivity of the adjectives, using a scale from 0.0 (extremely negative) to 1.0 (extremely positive). You can adjust these scores based on your specific needs. \n\n**Important Considerations:**\n\n* **Context:**  Remember that sentiment analysis can be subjective.  Consider the context of the reviews and how the adjectives are used. \n* **Scale:** Choose a consistent scale for your sentiment scores to ensure meaningful comparison. \n* **Polarity:** You can further refine this analysis by incorporating polarity (positive, negative, neutral) for each feature. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "A2NIT6BKW11XJQ \nreview 1\nIf you are not use to using a large sustaining pedal while playing the piano, it may appear little awkward.\nreview 2\nI like the size of the stand and the flexibility.  Easy to put together and holds my guitar very well.\nreview 3\nThe music stand is perfect for the keyboard I am playing.  It is strong, height flexible and hold the music sheets firmly\n\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nA2NIT6BKW11XJQ = {\n    \"review1\": {\n        \"pedal\": (\"awkward\", 0.2) \n    },\n    \"review2\": {\n        \"stand\": (\"good size\", 0.8),\n        \"stand\": (\"flexible\", 0.8),\n        \"assembly\": (\"easy\", 0.9), \n        \"hold\": (\"well\", 0.8)\n    },\n    \"review3\": {\n        \"stand\": (\"perfect\", 1.0),\n        \"stand\": (\"strong\", 0.9),\n        \"height\": (\"flexible\", 0.8),\n        \"hold\": (\"firmly\", 0.9)\n    }\n}\n```\n",
      ],
    },
  ]
)



response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)