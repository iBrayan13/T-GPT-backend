from fastapi import APIRouter, HTTPException, status, Request, Depends
from src.services.ChatServices import ChatService
from src.utils.security import Security

router = APIRouter()
service = ChatService()
security = Security()

@router.post("/get-answer", status_code= status.HTTP_200_OK)
async def get_answer(request: Request, has_access: bool = Depends(security.verify_token)) -> dict:
    # Verifying JWT
    if not has_access:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid credentials.",
            headers= {"WWW-Authenticated":"Bearer"}
        )

    # Getting and verifying data
    data = await request.json()
    if not len(data) == 1 or "question" not in data or not type(data["question"]) == str:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Invalid request.",
            headers= {"content-type": "application/json"}
        )
    
    # Asking to GPT
    ans = service.make_question(data["question"])
    if not len(ans) > 0:
        raise HTTPException(
            status_code= status.HTTP_204_NO_CONTENT,
            detail= "Something was wrong during communication with GPT.",
            headers= {"content-type": "applications/json"}
        )

    return {
        "answer": ans,
        "len": len(ans)
    }