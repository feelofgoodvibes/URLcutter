from pydantic import BaseModel
from .stats import Statistics


class ShortURL(BaseModel):
    url: str
    shortcode: str

    class Config:
        orm_mode = True


class ShortURLCreate(BaseModel):
    url: str


class ShortURLFull(ShortURL):
    statistics: list[Statistics]