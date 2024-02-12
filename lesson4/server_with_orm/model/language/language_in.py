from pydantic import BaseModel


class LanguageIn(BaseModel):
    lng: str

    class Config:
        orm_mode: True
