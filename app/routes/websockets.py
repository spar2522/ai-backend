from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.websocket.connection_manager import ConnectionManager

from app.services.ollama_async_service import stream_chat_async
import json
import asyncio
from app.services.pubsub_service import publish_message, subscribe_to_channel

router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):

    await manager.connect(room_id, websocket)
    # important to create a task for the room listener before entering the receive loop,
    # otherwise we might miss messages published to the channel while we're waiting for messages from the websocket
    asyncio.create_task(manager.start_room_listener(room_id))

    try:

        while True:

            message = await websocket.receive_text()
            print(f"Received message from websocket: {message}")

            event = {
                "type": "chat_message",
                "room_id": room_id,
                "data": {"message": message},
            }

            await publish_message(room_id, json.dumps(event))

    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
