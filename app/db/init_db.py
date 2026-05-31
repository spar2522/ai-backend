from app.core.db import engine
from app.core.db import Base
from app.db.chats import Chat
import asyncio


async def init_db():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Database initialized successfully.")


asyncio.run(init_db())
