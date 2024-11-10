from fastapi import FastAPI
from .routers.task import task_router
from .routers.user import user_router
from .backend.db import engine, Base

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)

# Создаём таблицы в базе данных
@app.on_event("startup")
async def startup_event():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
