from pydantic import BaseModel, Field
from uuid import UUID


class UserAuth(BaseModel):
    email: str = Field(..., description="user email")
    username: str = Field(..., min_length=5, max_length=50, description="user username")
    password: str = Field(..., min_length=5, max_length=50, description="user password")

class UserOut(BaseModel):
    user_id: UUID
    email: str
    username: str
    first_name: str | None
    last_name: str | None

class UserUpdate(BaseModel):
    email: str | None
    first_name: str | None
    last_name: str | None