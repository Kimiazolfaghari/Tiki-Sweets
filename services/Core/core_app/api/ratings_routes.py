from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core_app.schemas.rating_schemas import RateCommentCreate, RateCommentOut
from core_app.crud.ratings import create_rate_comment, get_comments_by_product
from iam_app.db.session import SessionLocal

ratings_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@ratings_router.post("/", response_model=RateCommentOut)
def create_rating(rate: RateCommentCreate, db: Session = Depends(get_db)):
    return create_rate_comment(db, rate)

@ratings_router.get("/{product_id}", response_model=list[RateCommentOut])
def get_product_ratings(product_id: int, db: Session = Depends(get_db)):
    return get_comments_by_product(db, product_id)
