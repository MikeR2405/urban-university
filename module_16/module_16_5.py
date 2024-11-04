from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="module_16/templates")

users_db = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.on_event("startup")
async def startup():
    users_db.append(User(id=0, username="UrbanUser", age=24))
    users_db.append(User(id=1, username="UrbanTest", age=22))
    users_db.append(User(id=2, username="Capybara", age=60))

@app.get("/", response_class=HTMLResponse)
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    if user_id < 0 or user_id >= len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    user = users_db[user_id]
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

@app.post("/user", response_model=User)
async def create_user(user: User) -> User:
    user.id = len(users_db)
    users_db.append(user)
    return user

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    if user_id < 0 or user_id >= len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    users_db.pop(user_id)
    return f"User {user_id} was deleted."

@app.delete("/")
async def delete_all_users() -> str:
    users_db.clear()
    return "All users deleted!"
