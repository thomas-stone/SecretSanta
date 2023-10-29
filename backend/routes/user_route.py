from fastapi import APIRouter
import boto3

from backend.models.user_model import User
from backend.schemas.user_schema import UserLogin, UserOut, UserUpdate, UserCreate
from backend.routes.auth_route import get_hashed_password

user_router = APIRouter()

table = boto3.resource("dynamodb").Table("users")

@user_router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str):
    response = table.get_item(Key={"user_id": user_id})
    return response["Item"]

@user_router.post("/", response_model=UserOut)
async def create_user(user: User):
    user_id = str(user.model_dump()["user_id"])
    hashed_password = get_hashed_password(user.model_dump()["password"])
    email = user.model_dump()["email"]
    first_name = user.model_dump()["first_name"]
    last_name = user.model_dump()["last_name"]
    nickname = user.model_dump()["nickname"]
    print(hashed_password)
    user = {"user_id": user_id, "password": hashed_password, "email": email, "first_name": first_name, "last_name": last_name, "nickname": nickname}
    table.put_item(Item=user)
    return user