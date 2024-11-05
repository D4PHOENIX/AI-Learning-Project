import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    BACKEND_URL = os.getenv("BACKEND_URL")
    FRONTEND_URL = os.getenv("FRONTEND_URL")
    GENAI_API_KEY = os.getenv("GEMINI_API_KEY")  # Access your API key here

config=Config()