from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Boolean
from database import Base

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: int = 1

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool
    priority: int
    class Config:
        from_attributes = True

class TaskDB(Base):
    __tablename__="tasks"
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_done = Column(Boolean, default = False)
    priority = Column(Integer, default = 1)
