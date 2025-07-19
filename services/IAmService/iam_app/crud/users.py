from passlib.context import CryptContext
from iam_app.db import session as db_session
from iam_app.core.security import get_password_hash, verify_password
from iam_app.db.models import User
from iam_app.schemas.user_schemas import UserRegister
from iam_app.db.models import OTP
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = db_session.SessionLocal()
    try:
        yield db
    finally:
        db.close()
def store_otp(db: Session, email: str, otp: str):
    db_otp = OTP(email=email, otp=otp)
    db.add(db_otp)
    db.commit()
    db.refresh(db_otp)
    return db_otp
def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    return user


def create_user(db: Session, user_in: UserRegister):
    hashed_password = get_password_hash(user_in.password)
    new_user = User(
        full_name=user_in.full_name,
        email=user_in.email,
        phone=user_in.phone,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email=email)
    if not user:
        return None

    if not verify_password(password, str(user.password)):
        return None
    return user

