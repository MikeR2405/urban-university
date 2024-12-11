from pydantic import BaseModel
from datetime import date
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
