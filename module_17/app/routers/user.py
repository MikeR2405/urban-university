# app/routers/user.py
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..backend.db_depends import get_db
from typing import Annotated, List
from ..models import User
from ..schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/", response_model=List[User])
async def all_users(db: Annotated[Session, Depends(get_db)]):
    """Получить всех пользователей из БД."""
    query = select(User)
    users = db.execute(query).scalars().all()
    return users


@user_router.get("/{user_id}", response_model=User)
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    """Получить пользователя по user_id."""
    query = select(User).where(User.id == user_id)
    user = db.execute(query).scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


@user_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    """Создать нового пользователя."""
    user_data = user.dict()
    user_data['slug'] = slugify(user.username)

    # Проверяем, существует ли пользователь с таким именем или id
    existing_user = db.execute(select(User).where(User.username == user.username)).scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    stmt = insert(User).values(**user_data)
    db.execute(stmt)
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction
