# app/routers/task.py
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ...backend.db_depends import get_db
from typing import Annotated, List
from ..models import Task, User
from ..schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete

task_router = APIRouter(prefix="/task", tags=["task"])


@task_router.get("/", response_model=List[Task])
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    """Получить все задачи из БД."""
    query = select(Task)
    tasks = db.execute(query).scalars().all()
    return tasks


@task_router.get("/{task_id}", response_model=Task)
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    """Получить задачу по task_id."""
    query = select(Task).where(Task.id == task_id)
    task = db.execute(query).scalars().first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


@task_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    """Создать новую задачу для пользователя."""
    # Проверяем, существует ли пользователь
    existing_user = db.execute(select(User).where(User.id == user_id)).scalars().first()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    task_data = task.dict()
    task_data['user_id'] = user_id

    stmt = insert(Task).values(**task_data)
    db.execute(stmt)
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@task_router.put("/update/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    """Обновить данные задачи."""
    stmt = update(Task).where(Task.id == task_id).values(**task.dict())
    result = db.execute(stmt)
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task was not found")

    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@task_router.delete("/delete/{task_id}", status_code=status.HTTP_200_OK)
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    """Удалить задачу."""
    stmt = delete(Task).where(Task.id == task_id)
    result = db.execute(stmt)
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task was not found")

    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task deleted successfully!'}
