from typing import Optional
from uuid import UUID
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError

from schemas.user_schema import UserAuth, UserUpdate
from tables.user_table import User
from schemas.auth_schema import TokenPayload

from .auth_service import get_hashed_password, verify_password
from config import settings

#TODO set up user service to work with dynamodb tables

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    scheme_name="JWT"
)

class UserService:
    @staticmethod
    async def create_user(user: UserAuth) -> User:
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_hashed_password(user.password),
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate_user(email: str, password: str) -> User | None:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hashed_password=user.hashed_password):
            return None

        return user

    @staticmethod
    async def get_user_by_email(email: str) -> User | None:
        # user = await User.find_one(User.email == email)  ####use dynamo db query here
        user = None
        return user

    @staticmethod
    async def get_user_by_id(user_id: UUID) -> User | None:
        # user = await User.find_one(User.user_id == user_id) ####use dynamo db query here
        user = None
        return user

    @staticmethod
    async def update_user(user_id: UUID, user: UserUpdate) -> User:
        # user = await User.find_one(User.user_id == user_id)  #### use dynamo db query here
        user = None
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # await user.update({"$set": user.model_dump(exclude_unset=True)}) ####use dynamo db update here
        return user

    @staticmethod
    async def get_current_user(token: str = Depends(reuseable_oauth)) -> User:
        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )

            token_data = TokenPayload(**payload)

            if datetime.fromtimestamp(token_data.exp) < datetime.now():
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired",
                    headers={"WWW-Authenticate": "Bearer"}
                )
        except(jwt.JWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"}
            )

        user = await UserService.get_user_by_id(token_data.sub)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        return user
