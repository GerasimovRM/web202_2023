from typing import Optional

from pydantic import BaseModel


class UserIn(BaseModel):
    first_name: str
    middle_name: Optional[str]
    last_name: str
    login: str
    email: str

    class Config:
        orm_mode: True
