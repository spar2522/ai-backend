from sqlalchemy import Column, Integer, Text, Enum, TIMESTAMP
from sqlalchemy.sql import func
from app.core.db import Base

import enum


class MessageType(enum.Enum):

    USER = "USER"
    ASSISTANT = "ASSISTANT"
    SYSTEM = "SYSTEM"


class Chat(Base):

    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)

    message = Column(Text, nullable=False)

    message_type = Column(Enum(MessageType), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
