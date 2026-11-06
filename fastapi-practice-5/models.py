from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class TaskDB(Base):
    __tablename__="tasks"
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)
    priority = Column(Integer, default=1)

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: int = 1

class TaskResponse(BaseModel):
    id: int
    title: str
    discription: str | None = None
    is_done: bool
    priority: int

    class Config:
        from_atributes = True
