from models import db, Task

def get_tasks():
    return Task.query.all()

def create_task(title, description, due_date):
    new_task = Task(title=title, description=description, due_date=due_date)
    db.session.add(new_task)
    db.session.commit()
    return new_task

def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return task
