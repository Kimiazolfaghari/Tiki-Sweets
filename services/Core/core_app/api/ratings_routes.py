from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core_app.schemas.rating_schemas import RateCommentCreate, RateCommentOut
from core_app.crud import ratings as crud_rating
from core_app.db.session import SessionLocal
from core_app.core.security import get_current_user

router = APIRouter(
    prefix="/ratings",
    tags=["ratings"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RateCommentOut, status_code=status.HTTP_201_CREATED)
def create_rate_comment(
        rate_in: RateCommentCreate,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    if rate_in.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to rate as another user")

    rate = crud_rating.create_rate_comment(db, rate_in)
    return rate


@router.get("/product/{product_id}", response_model=List[RateCommentOut])
def get_comments_for_product(
        product_id: int,
        db: Session = Depends(get_db)
):
    comments = crud_rating.get_comments_by_product(db, product_id)
    return comments
