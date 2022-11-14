from database import Base

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime


class ShortURL(Base):
    __tablename__ = "shorturl"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(2083))
    shortcode = Column(String, unique=True)

    stats = relationship("Statistics", backref="shorturl")


class Statistics(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_url = Column(Integer, ForeignKey("shorturl.id"))
    visit_time = Column(DateTime)



