from fastapi import APIRouter, HTTPException, status, Request
from src.services.ChatServices import ChatService

router = APIRouter()
service = ChatService()

@router.get("/get-answer")
async def get_answer(request: Request) -> dict:
    data = await request.json()
    if not len(data) == 1 or "question" not in data or data["question"] != str:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Invalid request",
            headers= {"content-type": "application/json"}
        )
    
    ans = await service.make_question(data["question"])

    return {
        "data": ans
    }