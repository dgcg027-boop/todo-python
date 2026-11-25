from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models import TaskCreate, TaskResponse
from database import get_db
from services.task_service import (
    create_task_service,
    get_tasks_service,
    get_task_service,
    update_task_service,
    delete_task_service, 
)

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await create_task_service(task, db)

@router.get("/tasks", response_model=list[TaskResponse])
async def get_tasks(is_done: bool | None = None, db: AsyncSession = Depends(get_db)):
    return await get_tasks_service(db, is_done)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
      return await get_task_service(task_id, db)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id:int, task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await update_task_service(task_id, task, db)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_task_service(task_id, db)
