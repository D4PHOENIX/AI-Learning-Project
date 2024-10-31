# backend/main.py

from fastapi import FastAPI
from routers import chatbot  # Import your chatbot router

app = FastAPI()

# Include the chatbot router for handling chatbot-related routes
app.include_router(chatbot.router)

# Test endpoint
@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

# You can also create a health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}
