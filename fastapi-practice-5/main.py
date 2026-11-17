from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import tasks
from database import engine, Base
import models

# Новый способ управления жизненным циклом приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код, который выполняется при запуске
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Код, который выполняется при остановке (если нужно)
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.include_router(tasks.router)