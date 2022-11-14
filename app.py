from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session

import models
from schemas import shorturl, stats
import db_worker


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/", response_model=shorturl.ShortURL)
def shorturl_create(shorturl: shorturl.ShortURLCreate, db: Session = Depends(get_db)):
    return db_worker.create_shorturl(db, shorturl)