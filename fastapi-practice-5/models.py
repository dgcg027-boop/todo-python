from pydantic import BaseModel
from sqlalchemy import Column, String, Boolean, Integer
from database import Base

class TaskCreate(BaseModel):
    title: str
    priority: int = 1
    description: str | None = None 

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_done: bool
    priority: int 

class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_done = Column(Boolean, default=False)
    priority = Column(Integer, default = 1)
    class Config:
            from_attributes = True

