from sqlalchemy.orm import Session
from iam_app.db.models import SpecialCake
from core_app.schemas.special_cake import SpecialCakeCreate, SpecialCakeUpdateStatus
from typing import List, Optional


def create_special_cake(db: Session, special_cake_data: SpecialCakeCreate, user_id: int) -> SpecialCake:
    special_cake = SpecialCake(**special_cake_data.model_dump(), user_id=user_id, status="pending")
    db.add(special_cake)
    db.commit()
    db.refresh(special_cake)
    return special_cake


def get_user_special_cakes(db: Session, user_id: int) -> List[SpecialCake]:
    return db.query(SpecialCake).filter(SpecialCake.user_id == user_id).all()


def get_all_special_cakes(db: Session) -> List[SpecialCake]:
    return db.query(SpecialCake).all()


def get_special_cake_by_id(db: Session, cake_id: int) -> Optional[SpecialCake]:
    return db.query(SpecialCake).filter(SpecialCake.id == cake_id).first()


def update_special_cake_status(db: Session, cake_id: int, new_status: str) -> Optional[SpecialCake]:
    special_cake = db.query(SpecialCake).filter(SpecialCake.id == cake_id).first()
    if special_cake:
        special_cake.status = new_status
        db.commit()
        db.refresh(special_cake)
    return special_cake


def delete_special_cake(db: Session, cake_id: int) -> bool:
    special_cake = db.query(SpecialCake).filter(SpecialCake.id == cake_id).first()
    if special_cake:
        db.delete(special_cake)
        db.commit()
        return True
    return False
