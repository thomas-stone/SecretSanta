from pydantic import BaseModel, Field
from uuid import UUID

class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    nickname: str | None = None
class UserUpdate(BaseModel):
    email: str | None
    password: str | None
    first_name: str | None
    last_name: str | None
    nickname: str | None

class UserOut(BaseModel):
    user_id: str
    email: str
    first_name: str
    last_name: str
    nickname: str | None