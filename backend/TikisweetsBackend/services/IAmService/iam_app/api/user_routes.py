from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from iam_app.core.security import create_access_token
from iam_app.crud import users as crud_users
from iam_app.db import session as db_session
from iam_app.db.models import OTP, User
from iam_app.schemas.user_schemas import UserLogin, UserOut, UserRegister
from iam_app.utils.email_utils import send_otp_email, generate_otp
from iam_app.crud.users import store_otp

router = APIRouter()


def get_db():
    db = db_session.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserOut)
def register(user: UserRegister, db: Session = Depends(get_db)):
    try:
        db_user = crud_users.get_user_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        new_user = crud_users.create_user(db, user)
        otp = generate_otp()
        store_otp(db, user.email, otp)
        send_otp_email(user.email, otp)

        return new_user
    except Exception as e:
        import traceback
        traceback.print_exc()  # یا لاگ کنید
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")




@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = crud_users.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )


    access_token = create_access_token(data={"sub": db_user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "message": "Login successful"
    }


@router.post("/verify-otp")
def verify_otp(email: str, otp: str, db: Session = Depends(get_db)):
    db_otp = db.query(OTP).filter(OTP.email == email).order_by(OTP.created_at.desc()).first()


    if not db_otp or db_otp.otp != otp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid OTP"
        )


    user = db.query(User).filter(User.email == email).first()
    if user:
        user.is_verified = True
        db.commit()
        db.refresh(user)
        return {"message": "User verified successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
