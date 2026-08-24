from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from chatbot import chatbot_response


app = FastAPI(
    title="ForgeMint Chatbot API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
    show_agent: bool = False
    whatsapp_url: str | None = None
    social_media: dict | None = None


@app.get("/")
def home():
    return {
        "message": "ForgeMint Chatbot API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = chatbot_response(
        request.message
    )

    return result