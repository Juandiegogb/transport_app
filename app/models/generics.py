from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from uuid import uuid4, UUID
from pydantic import AfterValidator, BeforeValidator


class UserBase(SQLModel):
    full_name: str = Field(nullable=False)
    username: EmailStr = Field(
        BeforeValidator(lambda x: x.lower()), nullable=False, unique=True
    )


class UserRegister(UserBase):
    password: str = Field(nullable=False)


class User(UserBase, table=True):
    id: UUID = Field(primary_key=True, nullable=False, default_factory=uuid4)
    password: str = Field(nullable=False)


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"
