import httpx
import json


async def stream_chat_async(
    message: str
):

    async with httpx.AsyncClient(
        timeout=None
    ) as client:

        async with client.stream(
            "POST",
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen3:14b",
                "prompt": message,
                "stream": True
            }
        ) as response:

            async for line in response.aiter_lines():

                if line:

                    chunk = json.loads(line)

                    token = chunk.get(
                        "response",
                        ""
                    )

                    yield token