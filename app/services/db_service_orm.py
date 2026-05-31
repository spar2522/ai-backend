from sqlalchemy import select

from app.db.chats import Chat, MessageType
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


async def save_chat(db: AsyncSession, message: str, message_type: MessageType):

    chat = Chat(message=message, message_type=message_type)

    db.add(chat)
    await db.commit()


def get_chats(db: Session):

    chats = db.query(Chat).order_by(Chat.id).all()

    return chats


async def async_get_chats(db: AsyncSession):

    result = await db.execute(select(Chat).order_by(Chat.id))

    chats = result.scalars().all()

    return chats
