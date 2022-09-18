from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item_by_id(item_id: int):
    return {"item_id": item_id}

@app.get("/items/name/{item_name}")
async def read_item_by_name(item_name: str):
    return {"item_name": item_name}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


