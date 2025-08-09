from typing import Annotated

from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlmodel import Session

from app.api.deps import SessionDep
from app.core.security import get_hash_password
from app.models import User, UserRegister


users_router = APIRouter(prefix="/users")


@users_router.post("/register", response_model=User)
def register(user: UserRegister, session: SessionDep):
    try:
        new_user = User.model_validate(
            user, update={"password": get_hash_password(user.password)}
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al registrar usuario: {str(e)}",
        )
