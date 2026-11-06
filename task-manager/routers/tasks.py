from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import TaskDB, TaskResponse, TaskCreate
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tasks", response_model = TaskResponse)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = TaskDB(title = task.title, description = task.description, priority = task.priority)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/tasks", response_model = list[TaskResponse])
async def get_task(is_done: bool | None = None, db: Session = Depends(get_db)):
    query = db.query(TaskDB)
    if is_done is not None:
        query = query.filter(TaskDB.is_done==is_done)
    return query.all()

@router.put("/tasks/{task_id}", response_model = TaskResponse)
async def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(TaskDB).filter(TaskDB.id==task_id).first()
    if not db_task: raise HTTPException(status_code=404, detail = "Task not found")
    db_task.title = task.title
    db_task.description = task.description
    db_task.priority = task.priority
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(TaskDB).filter(TaskDB.id==task_id).first()
    if not db_task: raise HTTPException(status_code=404, detail = "Task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted"}