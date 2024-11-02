from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

@app.get("/main")
async def welcome() -> dict:
    return {"message": "Main page"}

@app.get("/user/A/B")
async def news() -> dict:
    return {"message": f"Hello, Tester!"}

@app.get("/id")
async def id_paginator(username: str = "Mike", age: int = 37) -> dict:
    return {"User": username, "Age": age}

@app.get("/user/{first_name}/{last_name}")
async def news(first_name: str, last_name: str) -> dict:
    return {"message": f"Hello, {first_name} {last_name}"}