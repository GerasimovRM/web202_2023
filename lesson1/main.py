import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hehe")
async def root():
    return {"message": "Hello World", "a": 123}


@app.get("/items/{item_id}/{text}")
async def read_item(item_id: int, text: str):
    """
    Пример описания

    """
    return {"item_id": item_id, "text": text}


@app.get("/items")
async def read_item(item_id: int, text: str):
    return {"item_id": item_id, "text": text}


@app.get("/users/{user_id}")
async def read_item(user_id: int, msg_text: str):
    return {"user_id": user_id, "msg": msg_text}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
