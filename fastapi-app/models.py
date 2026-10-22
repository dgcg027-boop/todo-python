from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    price: float

class User(BaseModel):
    name: str
    age: int