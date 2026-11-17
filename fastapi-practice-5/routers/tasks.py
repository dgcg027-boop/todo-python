from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import TaskDB, TaskCreate, TaskResponse
from database import get_db

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    db_task = TaskDB(title=task.title, priority = task.priority, description = task.description)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

@router.get("/tasks", response_model=list[TaskResponse])
async def get_task(is_done: bool | None = None, db: AsyncSession = Depends(get_db)):
    query = select(TaskDB)
    if is_done is not None:
        query = query.filter(TaskDB.is_done==is_done)
    result = await db.execute(query)
    return result.scalars().all()

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id:int, task: TaskCreate, db: AsyncSession = Depends(get_db)):
    query = select(TaskDB).filter(TaskDB.id == task_id)
    result = await db.execute(query)
    db_task = result.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code=404, detail = "Task not found")
    db_task.title = task.title
    db_task.priority = task.priority
    db_task.description = task.description
    await db.commit()
    await db.refresh(db_task)
    return db_task

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    query = select(TaskDB).filter(TaskDB.id == task_id)
    result = await db.execute(query)
    db_task = result.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code=404, detail = "Task not found")
    await db.delete(db_task)
    await db.commit()
    return {"message": "Task deleted"}