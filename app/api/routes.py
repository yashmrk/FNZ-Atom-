from fastapi import APIRouter,WebSocket, WebSocketDisconnect
from google import genai
import os
from dotenv import load_dotenv
from app.services.llm import ChatGraph
from pydantic import BaseModel


load_dotenv()
router = APIRouter()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
projectPath = ''

class ProjectRequest(BaseModel):
    prompt: str

class ChatRequest(BaseModel):
    prompt: str

@router.get("/")
def read_root():
    return {"Hello": "World"}

# @router.get("/available_bsd")
# def get_available_bsd():
#     list_bsd = os.listdir("app/bsd")
#     return {"available_bsd": list_bsd}

# @router.get("/get_stories/{bsd_name}")
# def get_stories(bsd_name: str):
#     bsd_path = f"app/bsd/{bsd_name}"
#     if not os.path.exists(bsd_path):
#         return {"error": "BSD not found"}
#     stories = os.listdir(bsd_path)
#     return {"stories": stories}

@router.post("/api/chat/start")
def get_project_context_path(request: ProjectRequest):
    global projectPath
    projectPath =   f"app/bsd/{request.prompt}/NewProduct-JISA"
    return {
        "status": "ok",
        "message": "Chat context initialized",
        "project": projectPath
    }



def get_story_content():
    story_path = projectPath
    if not os.path.exists(story_path):
        return {"error": "Story not found"}
    with open(story_path, "r") as f:
        content = f.read()
        f.close()
    return {"content": content}

@router.post("/api/chat")
async def model_conversation(request: ChatRequest):
    pre_context_bsd = get_story_content()
    chat = ChatGraph(pre_context=pre_context_bsd["content"])
    try:
        
        user_text = request.prompt
        result = chat.invoke(user_text)
        message = result.get("messages", [])[-1]
        return message.content
    except Exception as e:
        return f"There was some error generating the response: {str(e)}"