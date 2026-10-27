from fastapi import FastAPI
from routers import books
from database import engine, Base
import models

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(books.router)