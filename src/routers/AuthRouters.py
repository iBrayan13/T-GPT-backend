from fastapi import APIRouter, HTTPException, status, Request
from decouple import config
from src.utils.security import Security

router = APIRouter()
security = Security()

@router.get("/get-access")
async def get_access_token(request: Request) -> dict:
    data = await request.json()

    conditions = [
        len(data) == 4,
        "key" in data,
        "engine" in data,
        "provideer" in data,
        "jwt_algorithm" in data,
    ]
    for condition in conditions:
        if not condition:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid request.",
                headers= {"content-type": "application/json"}
            )
    
    extra_conditions = [
        data["key"] == config("KEY"),
        data["engine"] == config("GPT_ENGINE"),
        data["provideer"] == config("PROVIDEER"),
        data["jwt_algorithm"] == config("JWT_ALGORITHM")
    ]
    for extra_condition in extra_conditions:
        if not extra_condition:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid request.",
                headers= {"content-type": "application/json"}
            )
    
    token = security.generate_token()
    if not len(token) > 1:
        raise HTTPException(
            status_code= status.HTTP_405_METHOD_NOT_ALLOWED,
            detail= "Got troubles during token generation.",
            headers= {"WWW-Authenticated":"Bearer"}
        )
    
    return {
        "access_token": token
    }