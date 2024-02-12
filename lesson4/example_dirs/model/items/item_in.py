from typing import Optional

from pydantic import BaseModel


class ItemIn(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float | None = None