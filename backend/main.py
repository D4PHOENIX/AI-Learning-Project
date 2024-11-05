from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import api_endpoints
from utils import config
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL")], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router for API endpoints
app.include_router(api_endpoints.router)

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
