from multiprocessing.dummy import connection
import os

from fastapi import WebSocket

from app.services.pubsub_service import subscribe_to_channel


class ConnectionManager:

    def __init__(self):

        self.active_connections = {}
        self.active_room_listeners = set()

    async def connect(self, room_id: str, websocket: WebSocket):

        await websocket.accept()
        print(f"PID {os.getpid()} accepted websocket")

        if room_id not in self.active_connections:
            self.active_connections[room_id] = []
        self.active_connections[room_id].append(websocket)

        print(
            f"Room {room_id}: "
            f"{len(self.active_connections[room_id])} "
            f"connections"
        )

    def disconnect(self, room_id: str, websocket: WebSocket):

        self.active_connections[room_id].remove(websocket)

        print(
            f"Room {room_id}: "
            f"{len(self.active_connections[room_id])} "
            f"connections"
        )

    async def send_personal_message(self, message: str, websocket: WebSocket):
        print(f"Sending to websocket : {message}")
        try:
            await websocket.send_text(message)
        except Exception as e:
            print(f"Send failed: {e}")

    async def broadcast(self, room_id: str, message: str):
        print(f"Broadcasting to room {room_id}")
        for websocket in self.active_connections.get(room_id, []):
            await self.send_personal_message(message, websocket)

    async def start_room_listener(self, room_id: str):
        if room_id in self.active_room_listeners:
            return

        self.active_room_listeners.add(room_id)

        pubsub = await subscribe_to_channel(room_id)

        async for message in pubsub.listen():
            if message["type"] != "message":
                continue
            print(f"PID {os.getpid()} raw Redis message: {message}")
            await self.broadcast(room_id, message["data"])
