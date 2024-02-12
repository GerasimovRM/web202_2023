from typing import Optional, List

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette import status




current_count = 3


database = {
    "items": [ItemOut(id=1, name='Название1', description="Описание 1", price=12.6, tax=3.5),
              ItemOut(id=2, name='Название2', description="Описание 2", price=13.6)]
}

app = FastAPI()




if __name__ == "__main__":
    uvicorn.run("db-fake-example:app", reload=True)
