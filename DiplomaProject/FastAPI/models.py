from sqlalchemy import Column, Integer, String, Text, Boolean, Date
from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    due_date = Column(Date)
    completed = Column(Boolean, default=False)
