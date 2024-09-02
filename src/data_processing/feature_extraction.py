import os
import google.generativeai as genai

import json

class feature_extractor():

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
    system_instruction="dado un comentario de un item debes extraer sus principales features con sus respectivos adjetivos, la clasificacion de positividad del adjetivo si existe un feature repetido por item debes agrupar sus adjetivos y sus positividades tu respuesta debe ser un json donde la llave sea el codigo del item o su nombre y los valores tus respuestas, si los features no se mencionan pero se habla del item extrae realiza el mismo proceso pero con la llave items\n\ndada una entrada de este tipo \n        \"A2NIT6BKW11XJQ \\nreview 1\\nIf you are not use to using a large sustaining pedal while playing the piano, it may appear little awkward.\\nreview 2\\nI like the size of the stand and the flexibility.  Easy to put together and holds my guitar very well.\\nreview 3\\nThe music stand is perfect for the keyboard I am playing.  It is strong, height flexible and hold the music sheets firmly\\n\\n\",\n\ntu salida debe ser la siguiente\n{\n    \"A2NIT6BKW11XJQ\": {\n        \"review1\": {\n            \"pedal\": [\"awkward\", 0.2]\n        },\n        \"review2\": {\n            \"stand\": [\n                [\"good size\", 0.8],\n                [\"flexible\", 0.8]\n            ],\n            \"assembly\": [\"easy\", 0.9],\n            \"hold\": [\"well\", 0.8]\n        },\n        \"review3\": {\n            \"stand\": [\n                [\"perfect\", 1.0],\n                [\"strong\", 0.9]\n            ],\n            \"height\": [\"flexible\", 0.8],\n            \"hold\": [\"firmly\", 0.9]\n        }\n    }\n}\n\n",
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
            "If i had a dollar for how many times I have played this cd and how many times I have asked Alexa to play it, I would be rich. Love this singer along with the Black Pumas. Finding a lot of new music that I like a lot on amazon. Try new things.\n\n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "This tweet expresses a **POSITIVE** sentiment. Here's why:\n\n* **\"Love this singer along with the Black Pumas\"**:  This clearly indicates a strong positive feeling towards the singer and the band.\n* **\"Finding a lot of new music that I like a lot on amazon\"**: This highlights a positive experience with Amazon's music recommendations.\n* **\"Try new things\"**: This suggests an open-minded and positive attitude towards exploring new music.\n\nEven though the tweet starts with a humorous observation about potentially being rich, the overall tone is one of enjoyment and positive discovery. \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "item B004RQ2IRG\n\nreview 1\nIf i had a dollar for how many times I have played this cd and how many times I have asked Alexa to play it, I would be rich. Love this singer along with the Black Pumas. Finding a lot of new music that I like a lot on amazon. Try new things.\n\nitem B083QN4Y6H\n\nreview1\nhis is without a doubt my favorite CD, and I may be close to wearing it out before the end of the month  LOL  Personally, I never looked at the song list, just popped it in the player and let 'er rip.  I sat back and was just amazed at the choices Ronnie made to put on this CD.  Highly recommend it to any fan of his.  And if you're not, try it, you will be !!!!!",
        ],
        },
        {
        "role": "model",
        "parts": [
            "```json\n{\n    \"B004RQ2IRG\": {\n        \"review1\": {\n            \"cd\": [\n                [\"great\", 1.0],\n                [\"love\", 1.0]\n            ],\n            \"singer\": [\"love\", 1.0],\n            \"music\": [\n                [\"like\", 0.9],\n                [\"good\", 0.8]\n            ],\n            \"amazon\": [\"good\", 0.8],\n            \"experience\": [\"good\", 0.8]\n        }\n    },\n    \"B083QN4Y6H\": {\n        \"review1\": {\n            \"cd\": [\n                [\"favorite\", 1.0],\n                [\"amazing\", 1.0],\n                [\"good\", 0.8]\n            ],\n            \"choices\": [\"good\", 0.8],\n            \"recommendation\": [\"highly recommend\", 1.0]\n        }\n    }\n}\n```",
        ],
        },
        {
        "role": "user",
        "parts": [
            "B083QN4345\n\nreview1\nMe encanto",
        ],
        },
        {
        "role": "model",
        "parts": [
            "```json\n{\n    \"B083QN4345\": {\n        \"review1\": {\n            \"items\": [\"great\", 1.0]\n        }\n    }\n}\n```",
        ],
        },
    ]
    )

    def get_response(self, user_input):
        response = self.chat_session.send_message(user_input)
        response_text = response.text
        cleaned_response = response_text.replace("```json\n", "").replace("\n```", "").strip()
        data = json.loads(cleaned_response)
        return data

