from fastapi import HTTPException
from sqlalchemy.orm import Session
from iam_app.db.models import ShoppingList, ShoppingListItem, Product
from core_app.schemas.shopping_list_schemas import ShoppingListCreate

def create_shopping_list(db: Session, shopping_list_data: ShoppingListCreate):
    shopping_list = ShoppingList(
        user_id=shopping_list_data.user_id,
        status="created",
    )
    db.add(shopping_list)
    db.flush()

    for item in shopping_list_data.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=400, detail=f"Product with id {item.product_id} not found")

        db_item = ShoppingListItem(
            shopping_list_id=shopping_list.id,
            product_id=item.product_id,
            quantity=item.quantity,
        )
        db.add(db_item)

    db.commit()
    db.refresh(shopping_list)
    return shopping_list

def get_shopping_list(db: Session, shopping_list_id: int):
    return db.query(ShoppingList).filter(ShoppingList.id == shopping_list_id).first()

def add_item_to_list(db: Session, shopping_list_id: int, product_id: int, quantity: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=400, detail="Product not found")

    item = ShoppingListItem(
        shopping_list_id=shopping_list_id,
        product_id=product_id,
        quantity=quantity,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item_id: int):
    item = db.query(ShoppingListItem).filter(ShoppingListItem.id == item_id).first()
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item

def update_status(db: Session, list_id: int, status: str):
    shopping_list = db.query(ShoppingList).filter(ShoppingList.id == list_id).first()
    if not shopping_list:
        return None
    shopping_list.status = status
    db.commit()
    db.refresh(shopping_list)
    return shopping_list

def delete_list(db: Session, list_id: int):
    shopping_list = db.query(ShoppingList).filter(ShoppingList.id == list_id).first()
    if not shopping_list:
        return None
    db.delete(shopping_list)
    db.commit()
    return True
