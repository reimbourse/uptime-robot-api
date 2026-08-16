from datetime import datetime, timedelta, timezone
from bcrypt import hashpw, checkpw, gensalt
import jwt

from src.core.config import settings


class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    @staticmethod
    def create_access_token(user_id: int) -> str:
        exp = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {
            'sub': user_id,
            'exp': exp
        }
        return jwt.encode(payload=payload, key=settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)