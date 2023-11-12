from fastapi import APIRouter

from backend.utility.utilities import get_dynamo_table
from backend.models.user_model import User
from backend.schemas.user_schema import UserLogin, UserOut, UserUpdate, UserCreate

user_router = APIRouter()

table = get_dynamo_table(table_name="users")

@user_router.get("/{user_id}", response_model=UserOut | None)
async def get_user(user_id: str):
    response = table.get_item(Key={"user_id": user_id})
    return response.get("Item")

@user_router.post("/", response_model=UserOut)
async def create_user(user: User):
    user_id = str(user.model_dump()["user_id"])
    user = user.model_dump() | {"user_id": user_id}
    table.put_item(Item=user)
    return user