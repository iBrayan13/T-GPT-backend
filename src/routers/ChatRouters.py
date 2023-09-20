from fastapi import APIRouter, HTTPException, status, Request, Depends
from src.services.ChatServices import ChatService
from src.utils.security import Security

router = APIRouter()
service = ChatService()
security = Security()

@router.get("/get-answer")
async def get_answer(request: Request) -> dict:
    data = await request.json()
    if not len(data) == 1 or "question" not in data or not type(data["question"]) == str:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Invalid request",
            headers= {"content-type": "application/json"}
        )
    
    ans = service.make_question(data["question"])
    if not len(ans) > 0:
        raise HTTPException(
            status_code= status.HTTP_204_NO_CONTENT,
            detail= "Something was wrong during communication with GPT",
            headers= {"content-type": "applications/json"}
        )

    return {
        "answer": ans,
        "len": len(ans)
    }