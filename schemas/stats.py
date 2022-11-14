from pydantic import BaseModel
from datetime import datetime


class Statistics(BaseModel):
    visit_time: datetime