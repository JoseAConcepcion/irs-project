import os
import google.generativeai as genai


class feature_for_user():
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
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="Recibirás una lista con los intereses personales de un usuario y una lista de features de los items de un vendedor. Tu trabajo será realizar la inferencia de que features le puede intereasar más dados sus intereses. Si no existe features de interes tu respuesta debe ser \"None\".  Si existen features de interes tu respuesta deben ser los features.",
    )

    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "User:\nfan de futbol\nlector \ncorredor\n\nfeatures:\nropa deportiva\njuego de mesa\ncd \ntelefonos\ntecnologia\n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "ropa deportiva \n",
        ],
        },
    ]
    )


    def get_response(self, user_input):
        """
        Sends a query to the model and returns the processed response in text format.

        Args:
            user_input (str): The user input for the model.

        Returns:
            dict: Dictionary JSON with extracted features.
        """
        response = self.chat_session.send_message(user_input)
        return response.text

