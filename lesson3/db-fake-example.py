from typing import Optional, List

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette import status


class ItemIn(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float | None = None


class ItemOut(ItemIn):
    id: int


current_count = 3


database = {
    "items": [ItemOut(id=1, name='Название1', description="Описание 1", price=12.6, tax=3.5),
              ItemOut(id=2, name='Название2', description="Описание 2", price=13.6)]
}

app = FastAPI()


@app.get("/items/{id}", response_model=Optional[ItemOut])
async def get_item(id: int):
    item = next(filter(lambda x: x.id == id, database["items"]), None)
    return item


@app.get("/items", response_model=List[ItemOut])
async def get_items():
    return database["items"]


@app.post("/items", response_model=ItemOut)
async def create_item(item: ItemIn):
    global current_count
    # здесь колхоз!
    # db_item = ItemOut(id=current_count,
    #                   tax=item.tax,
    #                   price=item.price,
    #                   description=item.description,
    #                   name=item.name)
    db_item = ItemOut(id=current_count,
                      **item.model_dump())
    current_count += 1
    database["items"].append(db_item)
    return db_item


@app.put("/items", response_model=ItemOut)
async def update_item(item: ItemOut):
    index, db_item = next(filter(lambda x: x[1].id == item.id, enumerate(database["items"])), (-1, None))
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    database["items"][index] = item
    return db_item


@app.delete("/items")
async def update_item(id: int):
    index, db_item = next(filter(lambda x: x[1].id == id, enumerate(database["items"])), (-1, None))
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    database["items"].pop(index)
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("db-fake-example:app", reload=True)
