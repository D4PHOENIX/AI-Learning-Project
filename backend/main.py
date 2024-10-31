from fastapi import FastAPI
from backend.routers import chatbot

app = FastAPI()

# Include chat API router
app.include_router(chatbot.router)
