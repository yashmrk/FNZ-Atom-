from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# Allow React frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# In-memory "chat context"
# -------------------------
current_project_context = None


# -------------------------
# Request models
# -------------------------
class ChatRequest(BaseModel):
    prompt: str


# -------------------------
# Start chat API
# -------------------------
@app.post("/api/chat/start")
def start_chat(request: ChatRequest):
    global current_project_context

    current_project_context = request.prompt

    return {
        "status": "ok",
        "message": "Chat context initialized"
    }


# -------------------------
# Chat prompt API
# -------------------------
@app.post("/api/chat")
def chat_prompt(request: ChatRequest):
    # Random mock replies
    replies = [
        "Sure, I can help you with that.",
        "Let me check that for you.",
        "That’s an interesting question!",
        "Here’s what I found regarding your request.",
        "Can you please clarify a bit more?"
    ]

    return "you selected start context as " + current_project_context + " and your current message prompt was " + request.prompt + " " + random.choice(replies)
