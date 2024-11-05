import os

class Config:
    GEMINI_API_KEY = os.getenv("GENAI_API_KEY")
    FRONTEND_URL = os.getenv("FRONTEND_URL")

config = Config()