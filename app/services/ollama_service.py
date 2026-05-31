import json
import requests

def stream_chat(message: str):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:14b",
            "prompt": message,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():

        if line:
            chunk = json.loads(line.decode("utf-8"))
            token = chunk.get("response", "")
            yield token