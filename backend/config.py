import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("AIzaSyCGD4ozxanCzbpgZ6ejnV8bed-Ih9EtReU")
    
config = Config()