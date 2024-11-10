from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


# Создаём движок для SQLite базы данных
DATABASE_URL = 'sqlite:///taskmanager.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создаём локальную сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
