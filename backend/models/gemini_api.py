import google.generativeai as genai
# from backend.config import config

class GeminiAPI:
    def __init__(self):
        genai.configure(api_key="AIzaSyCGD4ozxanCzbpgZ6ejnV8bed-Ih9EtReU")
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def generate_text(self, prompt: str) -> str:
        response =self.model.generate_text(prompt)
        return response.text
