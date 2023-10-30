from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime
from pydantic import ValidationError
import boto3
from jose import jwt

from backend.models.user_model import User
from backend.schemas.user_schema import UserLogin, UserOut, UserUpdate, UserCreate
from backend.routes.auth_route import get_hashed_password, verify_password, JWT_SECRET_KEY, ALGORITHM, get_user_by_id
from backend.schemas.token_schema import TokenPayload

user_router = APIRouter()

table = boto3.resource("dynamodb").Table("users")

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl=f"/auth/login",
    scheme_name="JWT"
)

async def get_current_user(token: str = Depends(reuseable_oauth)) -> User:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = await get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user

@user_router.get("/me", response_model=UserOut, operation_id="getCurrentUser")
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@user_router.get("/{user_id}", response_model=UserOut, operation_id="getUser")
async def get_user(user_id: str):
    response = table.get_item(Key={"user_id": user_id})
    return response["Item"]

@user_router.post("/", response_model=UserOut, operation_id="createUser")
async def create_user(user: User):
    user_id = str(user.model_dump()["user_id"])
    hashed_password = get_hashed_password(user.model_dump()["password"])
    email = user.model_dump()["email"]
    first_name = user.model_dump()["first_name"]
    last_name = user.model_dump()["last_name"]
    nickname = user.model_dump()["nickname"]
    user = {"user_id": user_id, "password": hashed_password, "email": email, "first_name": first_name, "last_name": last_name, "nickname": nickname}
    table.put_item(Item=user)
    return user

@user_router.put("/{user_id}", response_model=UserOut, operation_id="updateUser")
async def update_user(user_id: str, user: UserUpdate):
    user = user.model_dump()

    update_expression = "SET "
    expression_attribute_values = {}

    for key, value in user.items():
        if value is not None and value != "":  # only update fields that are not None and not empty
            update_expression += f"{key} = :{key}, "
            expression_attribute_values[f":{key}"] = value

    update_expression = update_expression.rstrip(', ')  # remove trailing comma and space

    table.update_item(
        Key={"user_id": user_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )

    user["user_id"] = user_id  # add user_id to the returned dictionary
    return user

@user_router.delete("/{user_id}", operation_id="deleteUser")
async def delete_user(user_id: str):
    table.delete_item(Key={"user_id": user_id})
    return {"message": "User successfully deleted"}