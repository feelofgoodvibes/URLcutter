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


@app.get("/{shortcode}", response_model=shorturl.ShortURL)
def shorturl_view(shortcode: str, db: Session = Depends(get_db)):
    shorturl = db_worker.get_shorturl_by_shortcode(db, shortcode)

    # Add +1 view for shortURL
    db.add(models.Statistics(short_url=shorturl.id))
    db.commit()

    if shorturl is None:
        raise HTTPException(status_code=404, detail="ShortURL not found")

    return shorturl


# TODO: Change to schema with stats
@app.get("/full/{shorturl_id}", response_model=shorturl.ShortURLFull)
def shorturl_view_full(shorturl_id: int, db: Session = Depends(get_db)):
    short_url = db_worker.get_shorturl_by_id(db, shorturl_id)

    if short_url is None:
        raise HTTPException(status_code=404, detail="ShortURL not found")

    return shorturl.ShortURLFull.parse_obj(short_url)
