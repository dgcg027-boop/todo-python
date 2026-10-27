from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Book, BookDB
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/books")
async def create_book(book: Book, db: Session = Depends(get_db)):
    db_book = BookDB(title = book.title, author = book.author, price = book.price)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return {"message": f"книга '{book.title}' добавлена в БД", "id": db_book.id}

@router.get("/books")
async def get_book(db: Session = Depends(get_db)):
    books = db.query(BookDB).all()
    return [{"id": b.id, "title": b.title, "author": b.author, "price": b.price} for b in books]