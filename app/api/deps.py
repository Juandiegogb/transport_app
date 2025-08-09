from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.engine.base import Engine
from sqlmodel import Session
from fastapi.security import OAuth2PasswordBearer
from app.models import Token
from ..core.database import engine


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


oauth2_scheme = OAuth2PasswordBearer("/api/auth/login")

SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(oauth2_scheme)]
