from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/books")
    assert response.status_code == 200

def test_create_book():
    response = client.post(
        "/books",
        json={"title": "Тест", "author": "Автор", "price": 100}
    )
    print(response.status_code)
    print(response.json())   # ← покажет, что реально возвращается
    assert response.status_code == 200
    assert "добавлена" in response.json()["message"]

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)