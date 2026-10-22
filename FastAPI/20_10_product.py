from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    title: str
    price: float
    quantity: int

@app.post("/products")
async def create_product(product: Product):
    return {"message": f"Товар {product.title} добавлен", "total": product.price * product.quantity}
