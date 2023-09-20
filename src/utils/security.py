from jose import jwt
from decouple import config
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

class Security:
    oauth = OAuth2PasswordBearer(tokenUrl= "token")
    JWT_ALGORITHM = config("JWT_ALGORITHM")
    JWT_SECRET_KEY = config("JWT_SECRET_KEY")
    JWT_MIN_DURATION = int(config("JWT_MIN_DURATION"))

    GPT_ENGINE = config("GPT_ENGINE")
    PROVIDEER = config("PROVIDEER")

    @classmethod
    def generate_token(cls) -> str:
        try:
            payload = {
                "engine": cls.GPT_ENGINE,
                "provideer": cls.PROVIDEER,
                "exp": datetime.utcnow() + timedelta(minutes= cls.JWT_MIN_DURATION)
            }

            return jwt.encode(
                payload,
                key= cls.JWT_SECRET_KEY,
                algorithm= cls.JWT_ALGORITHM
            )
        
        except Exception as ex:
            print(ex)
            return ""

    @classmethod
    def verify_token(cls, token:str = Depends(oauth)) -> bool:
        payload = jwt.decode(
            token,
            key= cls.JWT_SECRET_KEY,
            algorithms= [cls.JWT_ALGORITHM]
        )

        conditions = [
            len(payload) == 3,
            "engine" in payload,
            payload["engine"] == cls.GPT_ENGINE,
            "provideer" in payload,
            payload["provideer"] == cls.PROVIDEER,
            "exp" in payload,
        ]

        for condition in conditions:
            if not condition:
                return condition
        
        return True