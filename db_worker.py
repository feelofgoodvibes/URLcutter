import hashlib
from sqlalchemy.orm import Session
from schemas import shorturl
from models import ShortURL, Statistics, SHORT_URL_LENGTH
from os import urandom


def generate_url_hash(url: bytes) -> str:
    return hashlib.sha256(url).hexdigest()[:SHORT_URL_LENGTH]


def create_shorturl(db: Session, shorturl: shorturl.ShortURLCreate):
    hash = generate_url_hash(shorturl.url.encode("utf-8"))

    while db.query(ShortURL).filter(ShortURL.shortcode==hash).first() is not None:
        hash = generate_url_hash(shorturl.url.encode("utf-8")+urandom(5))

    db_shorturl = ShortURL(url=shorturl.url, shortcode=hash)
    
    db.add(db_shorturl)
    db.commit()
    db.refresh(db_shorturl)

    return db_shorturl