from fastapi import FastAPI
from routers import books, users
from database import engine, Base
import models

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(books.router)
app.include_router(users.router)
