from fastapi import APIRouter, Depends, HTTPException, status, Body
from backend.schemas.token_schema import TokenSchema, TokenPayload
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
import boto3
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any
from pydantic import ValidationError

table = boto3.resource("dynamodb").Table("users")

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

JWT_SECRET_KEY = "secretkey"
JWT_REFRESH_SECRET_KEY = "refreshsecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

auth_router = APIRouter()

@auth_router.post("/login", response_model=TokenSchema)
async def login(login_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(username = login_data.username, password = login_data.password)
    if not user:
        raise HTTPException(status_code = 401, detail = "Invalid username or password")

    return {
        "access_token": create_access_token(user.username),
        "refresh_token": create_refresh_token(user.username)
    }

@auth_router.post("/refresh", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token, JWT_REFRESH_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await get_user(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid token for user",
        )
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
    }

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encodeed_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encodeed_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encodeed_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, algorithm=ALGORITHM)
    return encodeed_jwt

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

async def get_user(user_id: str):
    response = table.get_item(Key={"user_id": user_id})
    return response["Item"]