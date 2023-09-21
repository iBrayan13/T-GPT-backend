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
        """Generate a new token to get access for asking GPT.

        Returns:
            str: JSON Web Token.
        """
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
        """Verify JSON Web Token.

        Args:
            token (str, optional): token to verify. Defaults to Depends(oauth).

        Returns:
            bool: flag to continue.
        """
        try:
            payload = jwt.decode(
                token,
                key= cls.JWT_SECRET_KEY,
                algorithms= [cls.JWT_ALGORITHM]
            )

            conditions = [
                len(payload) == 3,
                "engine" in payload,
                "provideer" in payload,
                "exp" in payload
            ]
            for condition in conditions:
                if not condition:
                    return condition
                
            extra_conditions = [
                payload["engine"] == cls.GPT_ENGINE,
                payload["provideer"] == cls.PROVIDEER
            ]
            for extra_condition in extra_conditions:
                if not extra_condition:
                    return extra_condition
            
            return True
        except Exception as ex:
            print(ex)
            return False