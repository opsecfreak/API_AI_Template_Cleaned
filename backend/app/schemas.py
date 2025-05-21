from pydantic import BaseModel

class Message(BaseModel):
    text: str

class Response(BaseModel):
    echo: str
