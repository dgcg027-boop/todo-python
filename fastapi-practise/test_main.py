from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_create_book():
    response = client.post(
        "/books",
        json={"title": "Тест", "author": "Автор", "price": 100}
    )
    assert response.status_code == 200
    assert "добавлена" in response.json()["message"]

def test_get_book():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)