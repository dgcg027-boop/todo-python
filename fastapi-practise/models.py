from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Book(BaseModel):
    title:str
    author:str
    price:float

class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    author = Column(String)
    price = Column(Float)
    
