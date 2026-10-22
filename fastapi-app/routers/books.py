from fastapi import APIRouter
from models import Book

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Книжный магазин"}

@router.post("/books")
async def create_book(book: Book):
    return {"message": f"Книга '{book.title}' добавлена", "price": book.price}

@router.get("/books/{books_id}")
async def get_book(book_id: int):
    return  {"book_id": book_id, "status": "OK"}
