from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from iam_app.core.dependencies import get_current_admin
from iam_app.core.security import create_access_token
from iam_app.crud import admin as crud_admin
from iam_app.db.session import SessionLocal
from iam_app.schemas.admin_schemas import AdminLogin, AdminOut

admin_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@admin_router.post("/admin/login")
def login_admin(admin: AdminLogin, db: Session = Depends(get_db)):
    db_admin = crud_admin.authenticate_admin(db, admin.email, admin.password)
    if not db_admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token(data={"sub": db_admin.email, "role": "admin"})
    return {"access_token": token, "token_type": "bearer"}

@admin_router.get("/profile")
def get_profile(current_admin_email: str = Depends(get_current_admin), db: Session = Depends(get_db)):
    admin= crud_admin.get_admin_by_email((db, current_admin_email))
    if not admin:
        raise HTTPException(status_code=404, detail="admin not found")
    return admin