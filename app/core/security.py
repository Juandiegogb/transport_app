from bcrypt import checkpw, gensalt, hashpw
from jwt import decode, encode
from typing import Dict, Any
from datetime import datetime, timedelta, timezone
from .settings import JWT_KEY, JWT_ALGORITH, JWT_EXPIRE_TIME_IN_HOURS


def get_hash_password(password: str) -> str:
    salt = gensalt()
    bytes = password.encode()
    hashed_password = hashpw(bytes, salt)
    return hashed_password.decode()


def create_token(payload: Dict[str, Any]) -> str:
    expire = datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRE_TIME_IN_HOURS)
    payload["exp"] = expire
    token = encode(payload=payload, key=JWT_KEY, algorithm=JWT_ALGORITH)
    return token
