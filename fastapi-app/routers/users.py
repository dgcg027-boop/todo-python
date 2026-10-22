from fastapi import APIRouter
from models import User

router = APIRouter()

@router.post("/users")
async def create_user(user: User):
    return {"message": f"Пользователь {user.name} создан"}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "status": "OK"}