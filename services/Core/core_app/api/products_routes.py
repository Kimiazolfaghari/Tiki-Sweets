from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core_app.schemas.product_schemas import ProductCreate, ProductOut
from core_app.crud import products as crud_products
from iam_app.db.session import SessionLocal
from iam_app.core.dependencies import get_current_user

products_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@products_router.post("/", response_model=ProductOut)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return crud_products.create_product(db, product)

@products_router.get("/", response_model=list[ProductOut])
def read_all_products(db: Session = Depends(get_db)):
    return crud_products.get_all_products(db)

@products_router.get("/{product_id}", response_model=ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud_products.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@products_router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")

    product = crud_products.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
