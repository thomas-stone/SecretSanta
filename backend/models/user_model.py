from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class User(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    email: str
    hashed_password: str
    first_name: str
    last_name: str
    nickname: str | None = None