from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core_app.schemas.product_schemas import ProductCreate, ProductOut
from core_app.crud import products as crud_product
from core_app.db.session import SessionLocal
from core_app.core.security import get_current_admin

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(
    product_in: ProductCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)
):
    product = crud_product.create_product(db, product_in)
    return product


@router.get("/", response_model=List[ProductOut])
def list_products(db: Session = Depends(get_db)):
    products = crud_product.get_all_products(db)
    return products


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud_product.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)
):
    product = crud_product.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return
