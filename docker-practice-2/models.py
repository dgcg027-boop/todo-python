from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Float
from database import Base

class Book(BaseModel):
    title: str
    author: str
    price: float

class BookDB(Base):
    __tablename__="books"
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String, index = True)
    author = Column(String)
    price = Column(Float)


