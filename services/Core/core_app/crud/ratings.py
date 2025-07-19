from sqlalchemy import func
from sqlalchemy.orm import Session
from iam_app.db.models import RateComment,Product
from core_app.schemas.rating_schemas import RateCommentCreate

def create_rate_comment(db: Session, rate: RateCommentCreate):
    db_rate = RateComment(**rate.dict())
    db.add(db_rate)
    db.commit()
    db.refresh(db_rate)

    avg = db.query(func.avg(RateComment.rate_number)).filter(RateComment.product_id == db_rate.product_id).scalar()

    product = db.query(Product).filter(Product.id == db_rate.product_id).first()
    if product:
        product.avg_rating = avg
        db.commit()
        db.refresh(product)

    return db_rate

def get_comments_by_product(db: Session, product_id: int):
    return db.query(RateComment).filter(RateComment.product_id == product_id).all()
