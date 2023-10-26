from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class User(BaseModel):
    user_id: str = Field(default_factory=uuid4)
    email: str
    password: str
    first_name: str
    last_name: str
    nickname: str | None = None