from fastapi import APIRouter, Depends, HTTPException, Request
from jose import jwt, JWTError

from iam_app.core.config import settings


router = APIRouter()


@router.post("/verify-token")
def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token missing")
    token = token[7:]  # remove "Bearer "

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return {"user": payload}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
