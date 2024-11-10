from sqlalchemy.orm import Session
from fastapi import Depends
from .db import SessionLocal

# Создаем функцию для получения сессии базы данных
def get_db() -> Session:
    db = SessionLocal()  # Создаем новую сессию
    try:
        yield db  # Возвращаем сессию в качестве зависимости
    finally:
        db.close()  # Закрываем сессию после завершения запроса
