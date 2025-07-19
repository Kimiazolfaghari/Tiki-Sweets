from sqlalchemy.orm import Session
from iam_app.core.security import verify_password
from iam_app.db.models import Admin


def get_admin_by_email(db: Session, email: str):
    return db.query(Admin).filter(Admin.email == email).first()


def authenticate_admin(db: Session, email: str, password: str):
    admin = get_admin_by_email(db, email=email)
    if not admin:
        return None
    if not verify_password(password, str(admin.password)):
        return None
    return admin