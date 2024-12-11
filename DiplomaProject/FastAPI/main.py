from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from . import models, schemas, crud
from .database import SessionLocal, engine

# Создаем базу данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="C:/Users/SONY/PycharmProjects/URBAN/DiplomaProject/FastAPI/templates")


# Dependency для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})


@app.get("/tasks/new", response_class=HTMLResponse)
def create_task_form(request: Request):
    return templates.TemplateResponse("task_form.html", {"request": request})


@app.post("/tasks/", response_model=schemas.Task)
def create_task(title: str = Form(...), description: str = Form(...), due_date: str = Form(...),
                db: Session = Depends(get_db)):
    task_data = schemas.TaskCreate(title=title, description=description, due_date=due_date)
    return crud.create_task(db=db, task=task_data)


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return ({"detail": "Task deleted"})


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return ({"detail": "Task deleted"})
