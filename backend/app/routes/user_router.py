from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth, UserOut, UserUpdate
from fastapi import Depends
from services.user_service import UserService
from tables.user_table import User

user_router = APIRouter()

@user_router.post("/create", summary="Create a new user", response_model=UserOut)
async def create_user(user: UserAuth) -> UserOut:
    try:
        new_user = await UserService.create_user(user)
        return new_user
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists"
        )

@user_router.get("/me", summary="Get current user", response_model=UserOut)
async def get_current_user(current_user: User = Depends(UserService.get_current_user)) -> UserOut:
    return current_user

@user_router.put("/update", summary="Update current user", response_model=UserOut)
async def update_current_user(data: UserUpdate, current_user: User = Depends(UserService.get_current_user)) -> UserOut:
    try:
        updated_user = await UserService.update_user(current_user.user_id, data)
        return updated_user
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found"
        )

## DELETE call here if we want it