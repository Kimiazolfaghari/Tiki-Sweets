from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core_app.schemas.shopping_list_schemas import (
    ShoppingListCreate, ShoppingListOut, ShoppingListItemAdd, StatusUpdate
)
from core_app.crud import shopping_list as crud
from iam_app.db.session import SessionLocal
from iam_app.core.dependencies import get_current_user

shopping_list_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@shopping_list_router.post("/", response_model=ShoppingListOut)
def create_list(
        shopping_list: ShoppingListCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user),
):
    return crud.create_shopping_list(db, shopping_list, user_id=current_user["user_id"])


@shopping_list_router.get("/{list_id}", response_model=ShoppingListOut)
def get_list(
        list_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user),
):
    shopping_list = crud.get_shopping_list(db, list_id)
    if not shopping_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shopping list not found")

    if shopping_list.user_id != current_user["user_id"] and current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    return shopping_list


@shopping_list_router.post("/{list_id}/add-item")
def add_item(
        list_id: int,
        item: ShoppingListItemAdd,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user),
):
    shopping_list = crud.get_shopping_list(db, list_id)
    if not shopping_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shopping list not found")

    if shopping_list.user_id != current_user["user_id"] and current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    return crud.add_item_to_list(db, list_id, item.product_id, item.quantity)


@shopping_list_router.delete("/item/{item_id}")
def delete_item(
        item_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user),
):
    item = crud.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    if item.shopping_list.user_id != current_user["user_id"] and current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    crud.delete_item(db, item_id)
    return {"detail": "Item deleted"}


@shopping_list_router.patch("/{list_id}/status")
def update_list_status(
        list_id: int,
        status_data: StatusUpdate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user),
):
    shopping_list = crud.get_shopping_list(db, list_id)
    if not shopping_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="List not found")

    if shopping_list.user_id != current_user["user_id"] and current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    result = crud.update_status(db, list_id, status_data.status)
    return result


@shopping_list_router.delete("/{list_id}")
def delete_list(
        list_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user),
):
    shopping_list = crud.get_shopping_list(db, list_id)
    if not shopping_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shopping list not found")

    if shopping_list.user_id != current_user["user_id"] and current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    crud.delete_list(db, list_id)
    return {"detail": "List deleted"}
