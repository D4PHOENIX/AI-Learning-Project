from fastapi import APIRouter, HTTPException
from models.gemini_api import GeminiAPI
from models.chat_manager import ChatManager
from models.summarizer import Summarizer
from pydantic import BaseModel

router = APIRouter()
chat_manager = ChatManager()
gemini_api = GeminiAPI()
summarizer = Summarizer()

class ChatRequest(BaseModel):
    message: str

class QuizRequest(BaseModel):
    text: str
    max_questions: int

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 150
    min_length: int = 40

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        response_text = gemini_api.send_message(request.message)
        chat_manager.add_message(request.message, response_text)
        return {"response": response_text}
    except HTTPException as e:
        raise e  # Re-raise known HTTP exceptions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.post("/quiz")
async def generate_quiz(request: QuizRequest):
    try:
        if request.max_questions <= 0:
            raise HTTPException(status_code=400, detail="max_questions must be greater than 0.")
        
        quiz = gemini_api.generate_quiz(request.text, request.max_questions)

        if not quiz:
            raise HTTPException(status_code=500, detail="Failed to generate quiz questions.")

        return {"questions": quiz}
    except HTTPException as e:
        raise e  # Re-raise known HTTP exceptions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.post("/summarize")
async def summarize(request: SummarizeRequest):
    try:
        summary = summarizer.summarize(
            text=request.text, 
            max_length=request.max_length, 
            min_length=request.min_length
        )
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.get("/chat/history")
async def get_chat_history():
    try:
        history = chat_manager.get_context()  # Fetch the formatted chat history
        return {"history": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat/clear")
async def clear_chat():
    try:
        chat_manager.clear_history()  # Clear the history
        return {"message": "Chat history cleared!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

