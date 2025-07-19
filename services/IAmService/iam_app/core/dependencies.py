from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from iam_app.core.security import SECRET_KEY, ALGORITHM
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


def get_current_user(token: str = Depends(api_key_header)):
    if token is None or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        token = token.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role = payload.get("role")
        if role != "user":
            raise HTTPException(status_code=403, detail="Not authorized as user")
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_admin(token: str = Depends(api_key_header)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role = payload.get("role")
        if role != "admin":
            raise HTTPException(status_code=403, detail="Not authorized as admin")
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_active_user_or_admin(token: str = Depends(api_key_header)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role = payload.get("role")
        if role not in ("user", "admin"):
            raise HTTPException(status_code=403, detail="Not authorized")
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
