from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import TaskCreate, TaskDB, TaskResponse


async def create_task_service(task: TaskCreate, db: AsyncSession):
    db_task = TaskDB(title=task.title, priority=task.priority, description=task.description)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_tasks_service(db: AsyncSession, is_done: bool | None = None):
    query = select(TaskDB)
    if is_done is not None:
        query = query.filter(TaskDB.is_done == is_done)
    result = await db.execute(query)
    return result.scalars().all()

async def get_task_service(task_id: int, db: AsyncSession):
    query = select(TaskDB).filter(TaskDB.id == task_id)
    result = await db.execute(query)
    db_task = result.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code=404, detail = "Task not found")
    return db_task

async def update_task_service(task_id: int, task: TaskCreate, db: AsyncSession):
    query = select(TaskDB).filter(TaskDB.id == task_id)
    result = await db.execute(query)
    db_task = result.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code=404, detail = "Task not found")
    db_task.title = task.title
    db_task.description = task.description
    db_task.priority = task.priority
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def delete_task_service(task_id: int, db: AsyncSession):
    query = select(TaskDB).filter(TaskDB.id == task_id)
    result = await db.execute(query)
    db_task = result.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code = 404, detail = "Task not found")
    await db.delete(db_task)
    await db.commit()
    return {"message": "Task deleted"}