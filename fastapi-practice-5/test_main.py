from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_tasks():
    response = client.post(
        "/tasks",
        json = {"title": "Название", "description": "Описание", "priority": 1}
    )
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(),list)

def test_update_task():
    client_response = client.post(
        "/tasks",
        json={"title": "Для обновления", "description": "Тест", "priority": 1}
    )
    task_id = client_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Обновлено", "description": "Новое", "priority": 2}
    )
    assert response.status_code == 200

def test_delete_task():
    client_response = client.post(
        "/tasks",
        json={"title": "Для удаления", "description": "Тест", "priority": 1}
    )
    task_id = client_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert "deleted" in response.json()["message"]