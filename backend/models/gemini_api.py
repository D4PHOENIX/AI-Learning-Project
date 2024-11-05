import google.generativeai as genai
import os

class GeminiAPI:
    def __init__(self):
        genai.configure(api_key=os.getenv("GENAI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.chat = self.model.start_chat(
            history=[
                {"role": "user", "parts": "Hello"},
                {"role": "model", "parts": "Great to meet you. What would you like to know?"},
            ]
        )
    
    def send_message(self, message: str) -> str:
        response = self.chat.send_message(message)
        return response.text
    
    def generate_quiz(self, text: str, max_questions: int) -> list:
        prompt = f"Generate {max_questions} quiz questions with answers from the following text:\n\n{text}"
        response = self.model.generate_content(prompt)
        return response.text.splitlines()  # Parse lines as individual questions and answers
