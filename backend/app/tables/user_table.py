from pydantic import Field, BaseModel
from datetime import datetime
from uuid import UUID, uuid4

#### TODO: set up user model to work with dynamodb tables

class User(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    username: str
    email: str
    hashed_password: str
    first_name: str | None = None
    last_name: str | None = None

    def __repr__(self) -> str:
        return f"<User: {self.email}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False