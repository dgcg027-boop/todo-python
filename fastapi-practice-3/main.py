from fastapi import FastAPI
from routers import books
from database import engine, Base
from models import Book, BookDB

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(books.router)