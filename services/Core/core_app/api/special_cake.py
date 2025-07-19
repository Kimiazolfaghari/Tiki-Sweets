from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from iam_app.db.session import SessionLocal
from core_app.schemas.special_cake import SpecialCakeCreate, SpecialCakeOut, SpecialCakeUpdateStatus
from core_app.crud import special_cake as crud_special
from iam_app.core.dependencies import get_current_user, get_current_admin

special_cake_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@special_cake_router.post("/", response_model=SpecialCakeOut)
def create_special_cake(
    special_cake_data: SpecialCakeCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return crud_special.create_special_cake(db, special_cake_data, user_id=current_user["user_id"])


@special_cake_router.get("/my", response_model=List[SpecialCakeOut])
def get_my_special_cakes(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return crud_special.get_user_special_cakes(db, user_id=current_user["user_id"])


@special_cake_router.get("/", response_model=List[SpecialCakeOut])
def get_all_special_cakes(
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin),
):
    return crud_special.get_all_special_cakes(db)


@special_cake_router.get("/{cake_id}", response_model=SpecialCakeOut)
def get_special_cake_by_id(
    cake_id: int,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin),
):
    special_cake = crud_special.get_special_cake_by_id(db, cake_id)
    if not special_cake:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Special cake not found")
    return special_cake


@special_cake_router.put("/{cake_id}/status", response_model=SpecialCakeOut)
def update_special_cake_status(
    cake_id: int,
    status_data: SpecialCakeUpdateStatus,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin),
):
    special_cake = crud_special.update_special_cake_status(db, cake_id, new_status=status_data.status)
    if not special_cake:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Special cake not found")
    return special_cake


@special_cake_router.delete("/{cake_id}")
def delete_special_cake(
    cake_id: int,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin),
):
    success = crud_special.delete_special_cake(db, cake_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Special cake not found")
    return {"detail": "Deleted successfully"}
