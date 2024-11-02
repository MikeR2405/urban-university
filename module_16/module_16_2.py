from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def greeting() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user_number(
    user_id: int = Path(ge=1, le=100, description="Введите идентификатор пользователя", example="77")
) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Введите имя пользователя", example="UrbanUser")],
    age: int = Path(ge=18, le=120, description="Введите возраст", example="24")
) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
