from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from database import Base 

class Book(BaseModel):
    title: str
    author: str
    price: float

class User(BaseModel):
    name: str
    age: int

#SQLAlchemy-модели (для БД)
class BookDB(Base):
    __tablename__= "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index = True)
    author = Column(String)
    price = Column(Float)

