from typing import Optional

from pydantic import BaseModel


class PhoneIn(BaseModel):
    phone_number: str

    class Config:
        orm_mode: True
