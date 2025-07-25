from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core_app.db.session import SessionLocal
from core_app.schemas import special_cake as schemas
from core_app.crud import special_cake as crud
from core_app.core.security import get_current_user, get_current_admin

router = APIRouter(
    prefix="/specialcakes",
    tags=["specialcakes"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.SpecialCakeOut, status_code=status.HTTP_201_CREATED)
def create_special_cake(
    cake_in: schemas.SpecialCakeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    special_cake = crud.create_special_cake(db, cake_in, user_id=current_user["id"])
    return special_cake


@router.get("/user", response_model=List[schemas.SpecialCakeOut])
def get_user_special_cakes(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    cakes = crud.get_user_special_cakes(db, current_user["id"])
    return cakes

@router.get("/", response_model=List[schemas.SpecialCakeOut])
def get_all_special_cakes(
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    return crud.get_all_special_cakes(db)

@router.get("/{cake_id}", response_model=schemas.SpecialCakeOut)
def get_special_cake_by_id(
    cake_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    cake = crud.get_special_cake_by_id(db, cake_id)
    if not cake:
        raise HTTPException(status_code=404, detail="Special cake not found")
    if ("id" in current_user and cake.user_id != current_user["id"]) and (not hasattr(current_user, "role") or current_user.get("role") != "admin"):
        raise HTTPException(status_code=403, detail="Not authorized to view this special cake")
    return cake


@router.patch("/{cake_id}/status", response_model=schemas.SpecialCakeOut)
def update_special_cake_status(
    cake_id: int,
    status_update: schemas.SpecialCakeUpdateStatus,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    updated_cake = crud.update_special_cake_status(db, cake_id, status_update.status)
    if not updated_cake:
        raise HTTPException(status_code=404, detail="Special cake not found")
    return updated_cake


@router.delete("/{cake_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_special_cake(
    cake_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    cake = crud.get_special_cake_by_id(db, cake_id)
    if not cake:
        raise HTTPException(status_code=404, detail="Special cake not found")
    if cake.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this special cake")
    success = crud.delete_special_cake(db, cake_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete special cake")
    return


