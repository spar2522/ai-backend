import os

from app.core.redis_client import redis_client


async def publish_message(channel: str, message: str):
    print(f"PID {os.getpid()} publishing message : {message} to channel {channel}")
    await redis_client.publish(channel, message)


async def subscribe_to_channel(channel: str):
    print(f"PID {os.getpid()} subscribing to channel {channel}")
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(channel)
    return pubsub
