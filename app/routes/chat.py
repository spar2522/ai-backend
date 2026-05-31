from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from requests import Session
from sqlalchemy import select, text

from app.db.chats import Chat, MessageType
from app.models.chat_models import ChatRequest
from app.services.db_service_orm import async_get_chats, save_chat, get_chats

from app.services.ollama_async_service import stream_chat_async
from app.services.ollama_service import stream_chat

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_db

router = APIRouter()


@router.get("/chats")
async def chats(db: AsyncSession = Depends(get_async_db)):
    chats = await async_get_chats(db)
    response = []
    for chat in chats:

        response.append(
            {
                "id": chat.id,
                "message": chat.message,
                "message_type": chat.message_type.value,
                "created_at": str(chat.created_at),
            }
        )

    return response


@router.post("/chat")
async def chat(req: ChatRequest, db: AsyncSession = Depends(get_async_db)):
    await save_chat(db, req.message, MessageType.USER)

    async def generate():
        full_response = ""
        async for token in stream_chat_async(req.message):
            full_response += token
            yield token
        await save_chat(db, full_response, MessageType.ASSISTANT)

    return StreamingResponse(generate(), media_type="text/plain")


# usually used for entities {name}, example aitasks/flakedetection
@router.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name}"}


@router.get("/search")
def search(query: str):
    return {"query": query}
