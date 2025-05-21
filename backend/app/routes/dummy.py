from fastapi import APIRouter, HTTPException
from ..schemas import Message, Response

router = APIRouter()

@router.post("/echo", response_model=Response)
async def echo_message(msg: Message):
    # Just echoes back what you send
    return Response(echo=f"You said: {msg.text}")
