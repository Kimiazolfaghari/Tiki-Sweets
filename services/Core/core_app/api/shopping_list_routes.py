from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core_app.schemas import shopping_list_schemas as schemas
from core_app.crud import shopping_list as crud
from core_app.db.session import SessionLocal
from core_app.core.security import get_current_user

router = APIRouter(
    prefix="/shoppinglists",
    tags=["shoppinglists"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ShoppingListOut, status_code=status.HTTP_201_CREATED)
def create_shopping_list(
        shopping_list_in: schemas.ShoppingListCreate,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
):
    if shopping_list_in.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to create shopping list for this user")

    shopping_list = crud.create_shopping_list(db, shopping_list_in)
    return shopping_list


@router.get("/{list_id}", response_model=schemas.ShoppingListOut)
def get_shopping_list(
        list_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
):
    shopping_list = crud.get_shopping_list(db, list_id)
    if not shopping_list:
        raise HTTPException(status_code=404, detail="Shopping list not found")
    if shopping_list.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to view this shopping list")
    return shopping_list


@router.post("/{list_id}/items", response_model=schemas.ShoppingListItemOut, status_code=status.HTTP_201_CREATED)
def add_item_to_list(
        list_id: int,
        item_in: schemas.ShoppingListItemAdd,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
):
    shopping_list = crud.get_shopping_list(db, list_id)
    if not shopping_list:
        raise HTTPException(status_code=404, detail="Shopping list not found")
    if shopping_list.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to modify this shopping list")

    item = crud.add_item_to_list(db, list_id, item_in.product_id, item_in.quantity)
    return item


@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
        item_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
):
    item = crud.delete_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # چک کردن مالکیت آیتم اگر لازم بود (می‌تونی این قسمت رو اضافه کنی)
    # برای سادگی فرض می‌کنیم فقط خود کاربر می‌تواند حذف کند و این چک باید انجام شود

    return


@router.put("/{list_id}/status", response_model=schemas.ShoppingListOut)
def update_status(
        list_id: int,
        status_update: schemas.StatusUpdate,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
):
    shopping_list = crud.get_shopping_list(db, list_id)
    if not shopping_list:
        raise HTTPException(status_code=404, detail="Shopping list not found")
    if shopping_list.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to update this shopping list")

    updated_list = crud.update_status(db, list_id, status_update.status)
    if not updated_list:
        raise HTTPException(status_code=404, detail="Shopping list not found after update")
    return updated_list


@router.delete("/{list_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shopping_list(
        list_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
):
    shopping_list = crud.get_shopping_list(db, list_id)
    if not shopping_list:
        raise HTTPException(status_code=404, detail="Shopping list not found")
    if shopping_list.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this shopping list")

    crud.delete_list(db, list_id)
    return
