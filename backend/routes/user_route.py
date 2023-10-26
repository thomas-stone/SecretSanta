from fastapi import APIRouter
import boto3

from backend.models.user_model import User
from backend.schemas.user_schema import UserLogin, UserOut, UserUpdate

user_router = APIRouter()

table = boto3.resource("dynamodb").Table("users")

@user_router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str):
    response = table.get_item(Key={"user_id": user_id})
    return response["Item"]
