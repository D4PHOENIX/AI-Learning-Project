from fastapi import APIRouter, HTTPException
from models.gemini_api import GeminiAPI
from models.chat_manager import ChatManager
from pydantic import BaseModel

router = APIRouter()
chat_manager = ChatManager()
gemini_api = GeminiAPI()

class ChatRequest(BaseModel):
    prompt: str
    
@router.post("/chat")
async def chat(request: ChatRequest):
    try: 
        context = chat_manager.get_context()
        prompt_with_context = f"Prompt_Context: {context} current_prompt: {request.prompt}"
        response_text = gemini_api.generate_text(prompt_with_context)
        chat_manager.add_message(request.prompt, response_text)
        return({"response": response_text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))