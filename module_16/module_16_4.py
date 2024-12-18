from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users", response_model=List[User])
async def get_all_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int) -> User:
    if users:
        user_id = max(user.id for user in users) + 1
    else:
        user_id = 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, username: str, age: int) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/")
async def delete_all_users() -> str:
    users.clear()
    return "All users deleted!"
