import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from database import engine, Base
import models

# Фикстура для создания таблиц перед тестами
@pytest.fixture(scope="session", autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # (опционально) удалить таблицы после тестов
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    
@pytest.mark.asyncio
async def test_create_task(client: AsyncClient):
    response = await client.post(
        "/tasks",
        json={"title": "Название", "description": "Описание", "priority": 1}
    )
    assert response.status_code == 200
    assert "id" in response.json()

@pytest.mark.asyncio
async def test_get_tasks(client: AsyncClient):
    response = await client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_update_task(client: AsyncClient):
    create_response = await client.post(
        "/tasks",
        json = {"title": "Для обновления", "description": "Тест", "priority": 1}
    )
    task_id = create_response.json()["id"]

    response = await client.put(
        f"/tasks/{task_id}",
        json = {"title": "Обновлено", "description": "Новое", "priority": 2}
    )
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_task(client: AsyncClient):
    create_response = await client.post(
        "/tasks",
        json = {"title": "Для удаления", "description": "Тест", "priority": 1}
    )
    task_id = create_response.json()["id"]

    response = await client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert "deleted" in response.json()["message"]

