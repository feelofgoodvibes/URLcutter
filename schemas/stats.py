from pydantic import BaseModel
from datetime import datetime


class Statistics(BaseModel):
    visit_time: datetime

    class Config:
        orm_mode = True