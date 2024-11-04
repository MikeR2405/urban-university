from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    user_id: str = str(int(max(users, key=int)) + 1)
    users[user_id] = {"username": username, "age": age}
    return "User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int) -> str:
    users[user_id] = {f"Имя: {username}, возраст: {age}"}
    return f"User {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_message(user_id: str) -> str:
    users.pop(user_id)
    return f"Message {user_id} was  deleted."