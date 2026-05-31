import asyncio
import json
from urllib import response
from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes import websockets
app = FastAPI()
app.include_router(chat_router)
app.include_router(websockets.router)

@app.get("/")
def root():
    return {"message": "AI Backend Running"}


