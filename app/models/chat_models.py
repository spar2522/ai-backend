from pydantic import BaseModel

#Coming from pydantic, which is used for data validation and settings management using Python type annotations. It allows us to define data models with type annotations, and it will automatically validate the data against those types when we receive requests.
class ChatRequest(BaseModel):
    message: str