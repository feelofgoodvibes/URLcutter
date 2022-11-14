from pydantic import BaseModel
from .stats import Statistics
from datetime import datetime


class ShortURL(BaseModel):
    url: str
    shortcode: str

    class Config:
        orm_mode = True


class ShortURLCreate(BaseModel):
    url: str


class ShortURLFull(ShortURL):
    views: int
    stats: list[datetime]